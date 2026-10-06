# 模型设置

**简体中文** · [English](en/model_profiles.md) · [文档首页](../README.zh-CN.md#指南导航)

## 默认模型选择

以下是待任务验证的选择建议，不是能力排名或可用性证明；启用项和允许发送的资料范围写本机入口。当前 Root 保持用户模型与推理设置，架构、拆分和最终验收仍由它负责；表中建议不自动切换 Root。

| 工作 | 建议执行者与设置 |
| --- | --- |
| 日常工程 Root、契约明确的实现、修复、测试 | 6.1 Sol / `gpt-6.1-sol` / `high`；任务简单且易检查时用 `medium` |
| 复杂跨文件实现、一般根因调查、普通独立审查 | 6.1 Sol / `gpt-6.1-sol` / `high`；仍有具体推理瓶颈时升 `xhigh` |
| 高度模糊、难解竞态、重大且难撤销的架构取舍 | Astra / `gpt-6-astra` / `high`–`xhigh`；架构决定留当前 Root |
| 限定调查、普通实现、批量处理、补充审查 | OpenCode DeepSeek V4.1 Flash；核验本机模型 ID 与实际请求 |
| 明确、重复、大量的资料定位、提取、机械转换 | 可选 Luna / `gpt-6-luna` / `high`；需要判断隐含约束或冲突时用 6.1 Sol |
| 高风险独立审查 | 新上下文的 Astra / `high` |
| 证据充分但仍有明确、持续的推理瓶颈 | 按需选择当前模型的 `max`；难以撤销的取舍仍由 Astra 候选 |

## 选择与回退

上述分工依据 [OpenAI 模型指南](https://learn.chatgpt.com/docs/models) 与 [模型选择建议](https://developers.openai.com/api/docs/guides/model-selection)，是本工作流的起步建议。6.1 Sol 是日常 Root、复杂编码和多步 Worker 的默认候选；Luna 只在任务明确、重复且可批量验收时作为效率候选。Root 可以使用 6.1 Sol 负责架构判断和最终验收，不因职责名称自动升级到 Astra。不同代模型的同名推理档位不等价，不机械沿用旧档位，也不默认使用 `max`。API 默认值与 Codex 建议须区分；实际可用模型和档位以宿主及账号为准。

迁移时，6.1 Sol 优先承接旧 `gpt-5.6-sol` 的实现角色；6 Luna 承接明确、重复的限定任务。`gpt-5.6-luna` / `high` 仍可胜任本指南这类范围明确的文档修改、提取和机械转换，但仅作为可验证的兼容回退，不作为新的默认模型。模型可见性和客户端支持须单独核验，不据此宣称全面替代或更低延迟。DeepSeek 可继续承担表中工作；不因新模型发布自动停用。复杂决策和高风险审查仍保留 Astra 候选。

档位按任务难度递增使用：`low` 适合小范围、规则清楚且易检查的修改；`medium` 适合常规实现和已知原因修复；`high` 适合跨文件逻辑、边界检查和独立审查；`xhigh` 适合多个状态、假设或约束相互影响的调查；`max` 只用于证据充分但仍存在具体推理瓶颈的单项任务。Ultra 涉及可独立验收的子 Agent 并行，不等同于单个模型的更深推理。速度模式另行选择，Standard 是默认起点，Fast 只在等待时间值得增加用量时启用。

按不确定性、影响边界和错误代价选择，不按文件类型或为消费额度分工。Sol 与 DeepSeek 职责可重叠，以任务验收表现选择；DeepSeek 暂不作为高风险改动的唯一审查者。其他独立审查按风险选择已授权执行者。

只提供必要上下文，不统一强制 1M；用户指定的模型与推理设置不擅自替换。取消、回退与升级见 [Agent 协作](agent_selection.md)。用可比任务的返工、遗漏、总耗时和实际用量评估分工；无任务证据不声称效率提升，记录留本机。

## 原生 Agent

传入表中模型、推理设置、限定任务和规则入口。宿主不支持时报告并按职责回退，不启动另一个 Root。

## Sol / Luna CLI

先核验 `codex exec --help` 和宿主模型支持。以下是只读 Worker 示例，不改变当前 Root 或全局设置；成功请求与实际任务质量须分别验证：

```sh
codex exec --model gpt-6.1-sol -c 'model_reasoning_effort="medium"' \
  --sandbox read-only --ephemeral --cd /absolute/project/path \
  '作为 Worker 只读分析指定问题，返回位置、证据和未决项，不递归委派或修改文件'

codex exec --model gpt-6-luna -c 'model_reasoning_effort="high"' \
  --sandbox read-only --ephemeral --cd /absolute/project/path \
  '作为 Worker 在指定文件内提取所需信息，按约定格式返回证据，不递归委派或修改文件'
```

实际委派补齐 [执行包](agent_selection.md#执行包与并行) 中的目标、范围、验收和规则入口。写任务仅在已有授权下使用 `workspace-write`；可见模型不等于授权启用，本文示例不证明服务可用。

旧版 Spark CLI 示例已移除：GPT-5.3-Codex-Spark 已于 2026-09-14 从 Codex CLI、桌面端和 IDE 退役。需要快速、明确的 Worker 时，先核验可用的 6 Luna 或 6.1 Sol；写任务经授权使用 `workspace-write`，不关闭沙箱或改动当前 Root、全局配置。

## DeepSeek Flash / OpenCode

V4.1 Flash 当前官方 API 名称为 `deepseek-flash`（[模型说明](https://api-docs.deepseek.com/quick_start/pricing/)）；OpenCode 使用实际可用的 provider/model ID。能力、服务可用性和工具权限分别核验；普通代码实现或测试需已有相应写入／执行授权，本分工不扩大示例权限。

只在选用时接入，不另建 Harness 或后台调度器。核验 `opencode run --help`、配置与服务当前提供的模型 ID，不把别名当固定版本。macOS 安装入口：

```sh
brew install anomalyco/tap/opencode
opencode --version
```

将 [示例](../examples/opencode.json) 比较合并到本机 `~/.config/opencode/opencode.json`，保留现有 JSON/JSONC 配置。示例默认只读，另有仅限 Markdown 的编辑角色；关闭分享、自动更新、shell、内容搜索（`grep`）、递归委派和隐式 Skill，拒绝通过 `read` 直接读取常见凭据路径。`read` 的路径拒绝不保护其他内容读取渠道；若确需搜索，只在已筛选、无敏感材料的任务副本中限定启用，不能把文件路径拒绝规则直接复制到按查询正则鉴权的 `grep`。需要测试或额外工具时由 Root 限定授权，不能一律放行。

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

未录入凭据不试探调用。安装、模型列表可见、请求成功、任务通过分别验证；最小请求成功后，再用非敏感文档检查读取、定位与角色权限；使用纯合成标记核验两个角色对允许文档、禁止文件的读取与搜索限制，记录实际安装版本、有效配置及结果，不用真实凭据测试。静态配置检查不证明运行时限制已生效：

```sh
opencode run --agent workflow-review --format json \
  --dir /absolute/project/path \
  '只读检查指定文档，返回位置和证据，不递归委派'
```

官方参考：[CLI](https://opencode.ai/docs/cli/) · [权限](https://opencode.ai/docs/permissions/) · [配置](https://opencode.ai/docs/config/)。
