# Agent Engineering Workflow

**简体中文** · [English](README.en.md)

**让 Agent 工程任务有清晰的约束、可执行的步骤和可核验的结果。**

一套可直接引用的工程指南，覆盖设计、实现、调试、审查与多 Agent 协作。共享方法留在仓库，项目事实留在项目，个人配置留在本机。

[快速开始](#快速开始) · [指南导航](#指南导航) · [本机适配](#公开版本与本机适配) · [维护](#验证与维护)

- **按需使用** — 从一个任务开始，只读取当前阶段需要的指南。
- **职责明确** — 当前 Root 做架构取舍与最终验收，Worker 提供限定范围内的执行和证据。
- **便于迁移** — 普通任务可仅使用当前 Root；额外模型和工具按需接入。

## 快速开始

1. 将本仓库 clone 到长期保留的位置。
2. 阅读规则，将 [全局入口模板](examples/global-AGENTS.md) 中 `<WORKFLOW_REPO>` 替换为实际绝对路径，再合并到 `~/.codex/AGENTS.md`。不要直接覆盖已有个人配置。
3. 最小接入只使用当前 Root；无需先安装 OpenCode 或配齐所有模型。选用其他执行者时，再在本机入口确认启用项、允许发送的资料范围与必要限制。默认偏好见 `docs/model_profiles.md`；启用必须沿用宿主能力和权限。
4. 检查共享入口可达性；对实际选用的 CLI 和模型，用有明确预期的小任务验证。安装成功不等于模型调用成功。当前 Root 可以处理普通任务；需要独立审查却没有可用审查者时，按 `docs/engineering.md` 保留验收缺口。
5. 在新 Codex 会话中核验全局入口是否加载。若设置了 `CODEX_HOME`，应适配实际位置；还需检查 `AGENTS.override.md` 是否覆盖正常入口。

个人路径只写本机入口，不反向提交到本仓库。不建议把完整仓库 AGENTS 符号链接到全局位置：本机入口需要记录适配信息，并让指南引用始终相对于仓库解析。[Codex 官方加载规则](https://learn.chatgpt.com/docs/agent-configuration/agents-md)

仓库更新后复核模型/权限等语义差异，再用于后续任务；文档更新不代表宿主已动态重新加载或 CLI 配置已同步。

从旧的平铺目录升级时，共享指南已移至 `docs/`，空白日志模板已移至 `examples/`。本机入口仍指向根目录 `AGENTS.md`；若它另有直接引用，请同步将模型与协作路径改为 `docs/model_profiles.md`、`docs/agent_selection.md`，模板路径改为 `examples/workflow_evolution_log.md`。本机实际日志位置保持不变。

### 在业务项目中使用

在目标项目打开新的 Codex 会话，先用下面的只读任务核验接入：

> 列出当前生效的全局与项目指令来源，读取本机入口指向的共享 AGENTS.md，确认指南路径可达；说明本任务应加载哪些指南，不修改文件。

预期能定位本机入口、共享仓库及已有的项目规则，且不把 `<WORKFLOW_REPO>` 当成实际路径。入口不可达时先修正本机路径。其他 CLI 需要按自身机制传递规则入口，不能假定它们自动加载 Codex 配置。

随后直接描述目标和验收要求，例如“实现 XXX 并验证”“排查 XXX 的根因并修复”或“审查当前修改并报告证据”。Agent 从共享入口按需加载方法，无需每次粘贴全套文档。

首次为业务项目补齐规范时，可使用：

> 按 docs/project_workflow.md 的已有项目路径，检查当前项目的规则、需求、构建和测试入口，保留已有约定，补齐必要缺口。

项目只维护自己的具体事实和约束。通用方法留在共享仓库；Skill 的显式启用规则沿用 [AGENTS.md](AGENTS.md#skill-使用)。

## 指南导航

从 [Agent 入口](AGENTS.md) 按任务选择，详细规则无需全部同时加载。

| 想完成什么 | 阅读指南 |
| --- | --- |
| 确定流程深度、证据和完成条件 | [工程原则](docs/engineering.md) |
| 做结构决定与架构取舍 | [架构设计](docs/design.md) |
| 实现明确的行为或修复 | [编码实现](docs/coding.md) |
| 定位故障并验证根因 | [故障调试](docs/debugging.md) |
| 检查正确性与验收证据 | [工程审查](docs/review.md) |
| 接入或维护业务项目 | [项目接入](docs/project_workflow.md) |
| 分配任务、交接和回退 | [Agent 协作](docs/agent_selection.md) |
| 选择模型与启动参数 | [模型设置](docs/model_profiles.md) |
| 根据实际问题改进工作流 | [工作流改进](docs/workflow_evolution.md) |

```text
.
├── README.md / README.en.md   # 中文 / English
├── AGENTS.md                 # Agent 默认入口
├── docs/                     # 中文指南；en/ 为英文版本
├── examples/                 # 本机适配模板；en/ 为英文版本
└── scripts/                  # 离线检查
```

## 公开版本与本机适配

共享指南直接使用下载或 clone 的这一份，不再复制一套正文作为“本地版本”。需要按人、机器或账号调整的信息，放在仓库外的本机入口和工具配置中。这样共享规则只有一个维护来源，更新时也无需合并两套指南。

| 内容 | 公开仓库中的来源 | 本机如何使用 |
| --- | --- | --- |
| 通用规则、任务路由和专项方法 | `AGENTS.md`、`docs/engineering.md`、设计/编码/调试/审查等指南 | 直接引用；通用改进在仓库维护 |
| 默认执行者偏好 | `docs/model_profiles.md`、`docs/agent_selection.md` | 作为可选默认；个人启用、替代模型和资料范围写本机入口 |
| 全局入口 | `examples/global-AGENTS.md` | 替换占位符后合并到 Codex home 下的 `AGENTS.md` |
| OpenCode 角色示例 | `examples/opencode.json` | 仅在选用该工具时合并到仓库外的有效配置，适配路径与模型 |
| 审视日志模板 | `examples/workflow_evolution_log.md` | 需要记录时复制到仓库外；原模板保持空白 |
| 业务项目约束、构建和测试入口 | 由业务项目维护 | 写在该项目的 `AGENTS.md` 或已有文档中 |

只复制需要实例化的模板，不在公开目录填写真实机器路径、账号状态、密钥或个人任务记录。`~/.codex` 等路径是默认位置说明，`<WORKFLOW_REPO>` 等是人工替换标记；平台、`CODEX_HOME` 或工具配置目录不同的使用者应采用自己的实际位置。复制入口不需要改写共享指南中的相对引用。

## DeepSeek 接入

<details>
<summary>可选：通过 OpenCode 配置 DeepSeek Worker</summary>

本节是可选扩展，不是使用共享文档的前置条件。

默认使用 DeepSeek 官方 API，通过 OpenCode 执行限定 Worker。需要安装 OpenCode 时，macOS 可使用官方 Homebrew 源：

```sh
brew install anomalyco/tap/opencode
opencode --version
```

将 [配置示例](examples/opencode.json) 合并到 `~/.config/opencode/opencode.json`；已有 JSON/JSONC 配置时先比较，不覆盖。示例不包含密钥，默认选择 `deepseek/deepseek-flash`，提供 `workflow-review` 和 `workflow-edit`，关闭会话分享及自动更新。

跨项目使用时，在**本机配置**的全局及两个角色的 `permission.external_directory` 中允许共享仓库的准确绝对路径（例如占位形式 `<WORKFLOW_REPO>/*`），并在编辑角色的 `permission.edit` 中对同一路径设置 `deny`，放在通用 Markdown 允许规则之后。不要将个人路径写回公开示例。由 Root 在任务说明中提供所需指南入口；本机也可用 `instructions` 加载共享 AGENTS。

示例默认只读，编辑角色仅开放 Markdown 编辑，均显式拒绝 `.env`、凭据 JSON、密钥文件和常见凭据目录的读取，禁用 shell、递归委派和 Skill 工具。需要运行测试时由 Root 另外定义任务范围与工具权限。项目配置可覆盖全局设置，委派前应核验有效配置；这些规则不是 OS 沙箱。[配置合并](https://opencode.ai/docs/config/)、[权限说明](https://opencode.ai/docs/permissions/)

### 录入 API Key

在本机终端运行：

```sh
opencode auth login
```

选择 **DeepSeek**，在交互输入框粘贴 API Key。也可启动 `opencode` 后输入 `/connect` 并选择 DeepSeek。不要在命令参数、聊天、AGENTS 或仓库 `.env` 中填写 Key。

默认凭据文件为 `~/.local/share/opencode/auth.json`，它是本地文件存储，并非加密保险库。录入后限制文件访问权限：

```sh
chmod 600 ~/.local/share/opencode/auth.json
opencode models deepseek
```

自定义 XDG 数据目录时使用实际凭据路径。模型列表只证明模型元数据可见；用下面的最小请求验证调用：

```sh
opencode run --agent workflow-review --model deepseek/deepseek-flash \
  --format json '不要调用任何工具，只回复 READY'
```

请求成功后再用非敏感文档验证读取、结果定位及角色权限。API Key 未录入前，模型连通性与任务效果均为待验证。[官方凭据与 CLI 文档](https://opencode.ai/docs/cli/)


</details>

## 隐私与本机记录

- 公开目录不保存真实凭据、个人绝对路径、私有任务/调度标识、账号状态或个人历史。
- [审视日志](examples/workflow_evolution_log.md) 是空白模板；实际记录复制到仓库外，位置登记在本机入口中。
- `.gitignore` 辅助排除本地状态；发布前仍检查待提交文件与 Git 历史，不把忽略规则当作秘密扫描器。
- 周期审视需要使用者明确配置调度；本仓库不会创建自动化、后台服务或定时器。

## 验证与维护

本项目交付共享文档与配置模板，没有产品服务需要启动。需求与使用边界在本 README 维护，通用政策由 `docs/` 中的指南维护，本仓库的操作入口由根目录 `AGENTS.md` 导航。`examples/` 只保存待实例化模板，避免因本机适配另建一套规则正文。

安装了 Python 3 的维护者可在仓库根目录执行离线检查，无需第三方依赖或 API 凭据：

```sh
python3 scripts/check_docs.py
```

检查脚本位于 [scripts/check_docs.py](scripts/check_docs.py)。其范围是根目录、`docs/`、`examples/` 中的 Markdown 和 `examples/` 中的 JSON，检查本地链接、锚点、围栏、JSON 语法、双语文件配对及常见个人路径/密钥特征；发现问题时返回非零退出码。它不是完整的 Markdown 渲染器或秘密扫描器，不检查外部网页可达性，也不读取本机配置。

| 改动范围 | 必要验证与证据 |
| --- | --- |
| Markdown 与示例 JSON | 运行上述脚本；人工检查受影响的标题、表格和渲染结构；检查本次 diff |
| 接入步骤或模板 | 在仓库外临时目录替换占位符，核对目标指南可达；真实宿主加载与工具调用另行验证 |
| shell 示例 | 对受影响代码块做 shell 语法检查；执行依赖工具、权限与服务的命令时记录真实结果 |
| 模型路由、权限或验收规则 | 静态检查之外安排独立审查；涉及运行时保证时补充对应行为验证 |
| 发布准备 | 核对实际待提交文件及 Git 历史中的个人信息；忽略规则和脚本不能替代人工核验 |

检查结果关联所改版本，个人运行日志与历史证据保留在仓库外。通用规则更新直接修改对应权威指南；模板更新由各使用者比较后合并到本机配置，不自动覆盖。静态文档验证不能代替真实 CLI/API 或工程任务验证，完成条件沿用 `docs/engineering.md`。

中英文版本在同一次规则修改中同步。保留既有锚点和技术标识；使用一种语言完成任务，无需把译文再加载一遍。Commit message 使用英文，例如 `docs: improve navigation and add English translations`；不自动改写已发布历史。
