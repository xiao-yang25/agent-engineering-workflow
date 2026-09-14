# 模型设置

**简体中文** · [English](en/model_profiles.md) · [文档首页](../README.zh-CN.md#指南导航)

## 默认模型选择

以下是可选默认，不是能力排名或可用性证明；启用项和允许发送的资料范围写本机入口。

| 职责 | 执行者 | 设置 |
| --- | --- | --- |
| 架构、拆分、最终验收 | 当前 Root | 保持模型与设置 |
| 调查、资料整理、独立审查 | 原生 Astra | `gpt-6-astra` / `low` |
| 实现、复杂修复、测试 | 原生 Sol | `gpt-5.6-sol` / `high` |
| 明确小任务、快速检查 | Spark CLI | `gpt-5.3-codex-spark`；核验支持的推理设置 |
| 文档、批量分析、低风险执行 | OpenCode DeepSeek Flash | 核验本机模型 ID、凭据和实际请求 |

## 选择与回退

按职责选择，不为消费额度制造任务。用户指定模型不擅自替换；只提供必要上下文，不统一强制 1M。取消与次数限制见 [可用性回退](agent_selection.md#排队与可用性回退)。

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
