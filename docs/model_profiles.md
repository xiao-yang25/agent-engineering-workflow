# 模型设置

**简体中文** · [English](en/model_profiles.md) · [文档首页](../README.md#指南导航)

按职责选择已授权的执行者，并核验实际启动能力。

<details>
<summary>本页目录</summary>

- [默认模型选择](#默认模型选择)
- [选择与回退](#选择与回退)
- [原生 Agent](#原生-agent)
- [Spark CLI](#spark-cli)
- [DeepSeek Flash / OpenCode](#deepseek-flash--opencode)

</details>

这是可适配的默认路由，不是能力排名或账号可用性证明。使用者在本机入口确认执行者和资料范围；机制见 [Agent 协作](agent_selection.md)。

## 默认模型选择

| 职责 | 首选 | 设置与入口 |
| --- | --- | --- |
| 需求、架构取舍、拆分、最终验收 | 当前 Root | 保持当前模型与设置 |
| 跨文件调查、方案资料整理、独立审查 | Astra | `gpt-6-astra`，`low`；原生子 Agent |
| 实现、复杂修复、测试与失败分析 | Sol | `gpt-5.6-sol`，`high`；原生子 Agent |
| 边界明确的小改动、快速检查 | Spark | `gpt-5.3-codex-spark`；Codex CLI，按实际支持设置 |
| 文档整理、批量分析、低风险执行 | DeepSeek Flash | OpenCode CLI；本机选择明确模型 ID，录入凭据后验证 |

模型标识以宿主实际暴露的入口核验，不擅自替换用户指定模型。Spark 未指定固定推理强度，启动前核验支持值并记录选择。不统一强制 1M 上下文，只提供必要材料。

## 选择与回退

复杂实现优先 Sol，调查与独立评估优先 Astra；明确小任务可选 Spark，批量文档可选已配置的 DeepSeek。回退选择能承担同一职责的可用执行者，不固定轮询，不为消费额度制造任务。权限、取消和次数限制见 [可用性回退](agent_selection.md#排队与可用性回退)。

## 原生 Agent

启动时请求表中模型和推理强度，提供限定任务与规则入口。若宿主缺少模型或不支持覆盖设置，报告限制并按职责回退，不启动另一个 Root。

## Spark CLI

先核验 `codex exec --help` 和模型支持。只读示例：

```sh
codex exec --model gpt-5.3-codex-spark \
  --sandbox read-only --skip-git-repo-check --ephemeral \
  --cd /absolute/project/path \
  '作为 Worker 执行限定任务，返回证据，不递归委派或修改文件'
```

示例使用 CLI 默认推理设置；显式设置时只传已核验支持的 `model_reasoning_effort`。写任务按授权选择 `workspace-write`，不自动关闭沙箱。命令不修改当前 Root 或全局配置。

## DeepSeek Flash / OpenCode

采用 OpenCode 作为限定 Worker 入口，不额外引入自定义 Harness 或后台调度器。先核验 `opencode run --help`、`opencode models deepseek` 与配置；模型存在、鉴权成功不能替代任务验证。

官方于 2026-09 发布 V4.1-Flash，旧 `deepseek-v4-flash` 为临时兼容路由，不是固定版本。具体 ID 以当前服务和 CLI 为准，并写入本机配置。[官方公告](https://www.deepseek.com/en/news/deepseek-v4-1-flash/)

使用 [OpenCode 配置示例](../examples/opencode.json)，确认模型后调用：

```sh
opencode run --agent workflow-review --format json \
  --dir /absolute/project/path \
  '只读检查指定文档，返回位置和证据，不递归委派'
```

示例提供只读文档审查与有限编辑角色；禁用 shell、递归委派与隐式 Skill。需要测试或其他工具时，Root 按任务配置具体权限，不一律放行。权限配置不是 OS 沙箱。

API Key 通过 `opencode auth login` 在本机录入，默认保存在 `~/.local/share/opencode/auth.json`（自定义 XDG 目录时按实际位置），不放仓库、AGENTS、命令参数或任务提示。步骤见 [接入说明](../README.md#deepseek-接入)。

官方参考：[CLI](https://opencode.ai/docs/cli/)、[权限](https://opencode.ai/docs/permissions/)、[配置](https://opencode.ai/docs/config/)。文档存在不代表本机安装或 API 验证完成。
