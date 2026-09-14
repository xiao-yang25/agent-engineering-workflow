# Agent Engineering Workflow

**简体中文** · [English](README.md)

用于设计、编码、调试和审查的 Agent 工程指南。按任务读取，按证据验收。

## 快速开始

1. Clone 到固定位置，将 [入口模板](examples/global-AGENTS.md) 中的 `<WORKFLOW_REPO>` 替换为仓库绝对路径。
2. 合并到 `~/.codex/AGENTS.md`，保留原有规则；自定义 `CODEX_HOME` 时使用对应目录，注意 `AGENTS.override.md` 的覆盖。
3. 在业务项目中新开会话，要求 Agent 列出已加载的规则并确认指南可达，再描述任务与验收要求。

普通任务可只用当前 Root。额外模型需先授权并验证；必需的独立审查不能用自审替代。其他 CLI 须单独传递规则入口。[加载规则](https://learn.chatgpt.com/docs/agent-configuration/agents-md)

## 指南导航

| 主题 | 文档 |
| --- | --- |
| 规则与验收 | [Agent 入口](AGENTS.md) · [工程原则](docs/engineering.md) |
| 日常开发 | [设计](docs/design.md) · [编码](docs/coding.md) · [调试](docs/debugging.md) · [审查](docs/review.md) |
| 项目与协作 | [项目接入](docs/project_workflow.md) · [Agent 协作](docs/agent_selection.md) |
| 执行与改进 | [模型配置](docs/model_profiles.md) · [工作流改进](docs/workflow_evolution.md) |

## 公开版本与本机适配

`docs/` 保存共享指南，`examples/` 保存模板，`scripts/` 保存检查工具；英文版本位于各目录的 `en/`。

共享正文直接引用，只复制需要适配的模板。个人路径、凭据、启用状态和实际日志留在仓库外；业务约束与测试命令留在业务项目。引用相对于各指南所在目录解析，不把整套指南复制或链接成全局入口。

更新后比较并合并本机模板，重新开启会话；不会自动覆盖配置或启用调度。旧版根目录指南已移至 `docs/`，日志模板移至 `examples/`，直接引用需同步，实际私有日志位置不变。

<a id="deepseek-接入"></a>

可选工具接入：[Spark 与 DeepSeek / OpenCode](docs/model_profiles.md)。

<a id="隐私与本机记录"></a>

## 验证与维护

```sh
python3 scripts/check_docs.py
```

检查链接、锚点、围栏、JSON、双语配对及常见敏感信息；不能代替完整秘密扫描、实际工具调用或人工审查。维护步骤见 [Agent 入口](AGENTS.md#公开仓库维护)。

中英文同步更新，commit message 使用英文。检查通过后仍需核对待提交文件和历史中的个人信息；不自动改写已发布历史。
