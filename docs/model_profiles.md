# 模型设置

**简体中文** · [English](en/model_profiles.md) · [文档首页](../README.zh-CN.md#指南导航)

## 默认模型选择

以下是待任务验证的选择建议，不是能力排名或可用性证明；启用项和允许发送的资料范围写本机入口。当前 Root 保持用户模型与推理设置，架构、拆分和最终验收仍由它负责；表中建议不自动切换 Root。

| 工作 | 建议执行者与设置 |
| --- | --- |
| 架构、复杂理解、核心实现、根因定位 | Astra / `gpt-6-astra` / `high`；架构决定留当前 Root |
| 难解竞态、生命周期、重大方案取舍 | Astra / `xhigh`；重大取舍留当前 Root |
| 契约明确的普通实现、修复、测试 | Sol / `gpt-5.6-sol` / `high` |
| 限定调查、普通实现、批量处理、补充审查 | OpenCode DeepSeek V4.1 Flash；核验本机模型 ID 与实际请求 |
| 资料定位、机械修改、快速检查 | Astra / `low`，或 Spark CLI / `gpt-5.3-codex-spark` |
| 高风险独立审查 | 新上下文的 Astra / `high` |
| 明确且持续的推理瓶颈 | 按需选择 Astra / `max` |

## 选择与回退

按不确定性、影响边界和错误代价选择，不按文件类型或为消费额度分工。Sol 与 DeepSeek 职责可重叠，以任务验收表现选择；DeepSeek 暂不作为高风险改动的唯一审查者。其他独立审查按风险选择已授权执行者。

只提供必要上下文，不统一强制 1M；用户指定的模型与推理设置不擅自替换。取消、回退与升级见 [Agent 协作](agent_selection.md)。用可比任务的返工、遗漏、总耗时和实际用量评估分工；无任务证据不声称效率提升，记录留本机。

## 原生 Agent

传入表中模型、推理设置、限定任务和规则入口。宿主不支持时报告并按职责回退，不启动另一个 Root。

## Spark CLI

先核验 `codex exec --help` 与模型支持。示例使用默认推理设置；显式 `model_reasoning_effort` 只传已验证支持值：

```sh
codex exec --model gpt-5.3-codex-spark \
  --sandbox read-only --skip-git-repo-check --ephemeral \
  --cd /absolute/project/path \
  '作为 Worker 执行限定任务，返回证据，不递归委派或修改文件'
```

写任务经授权使用 `workspace-write`；不关闭沙箱或改动当前 Root、全局配置。

## DeepSeek Flash / OpenCode

V4.1 Flash 当前官方 API 名称为 `deepseek-flash`（[模型说明](https://api-docs.deepseek.com/quick_start/pricing/)）；OpenCode 使用实际可用的 provider/model ID。能力、服务可用性和工具权限分别核验；普通代码实现或测试需已有相应写入／执行授权，本分工不扩大示例权限。

只在选用时接入，不另建 Harness 或后台调度器。核验 `opencode run --help`、配置与服务当前提供的模型 ID，不把别名当固定版本。macOS 安装入口：

```sh
brew install anomalyco/tap/opencode
opencode --version
```

将 [示例](../examples/opencode.json) 比较合并到本机 `~/.config/opencode/opencode.json`，保留现有 JSON/JSONC 配置。示例默认只读，另有仅限 Markdown 的编辑角色；关闭分享、自动更新、shell、递归委派和隐式 Skill，拒绝常见凭据读取。需要测试或额外工具时由 Root 限定授权，不能一律放行。

跨项目使用时，在本机全局及两个角色的 `permission.external_directory` 放行共享仓库的准确路径（`<WORKFLOW_REPO>/*`）；编辑角色的 `permission.edit` 对同路径设 `deny`，置于通用 Markdown 放行规则之后。Root 传递所需指南；也可在本机 `instructions` 加载共享入口。项目配置可能覆盖全局配置，委派前核验有效权限；这些规则不是 OS 沙箱。

```sh
opencode auth login
```

选择 DeepSeek，交互录入 Key；也可用 `/connect`。不把 Key 写进聊天、命令参数、AGENTS 或仓库。凭据默认保存在 `~/.local/share/opencode/auth.json`，不是加密保险库；自定义 XDG 时使用实际路径：

```sh
chmod 600 ~/.local/share/opencode/auth.json
opencode models deepseek
opencode run --agent workflow-review --model deepseek/deepseek-flash \
  --format json '不要调用任何工具，只回复 READY'
```

未录入凭据不试探调用。安装、模型列表可见、请求成功、任务通过分别验证；最小请求成功后，再用非敏感文档检查读取、定位与角色权限：

```sh
opencode run --agent workflow-review --format json \
  --dir /absolute/project/path \
  '只读检查指定文档，返回位置和证据，不递归委派'
```

官方参考：[CLI](https://opencode.ai/docs/cli/) · [权限](https://opencode.ai/docs/permissions/) · [配置](https://opencode.ai/docs/config/)。
