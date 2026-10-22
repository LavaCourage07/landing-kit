# Landing Kit

> Quickly get up to speed with any codebase.

Landing Kit 是一组面向陌生软件仓库的 AI Skills，帮助开发者建立有证据的项目认知、绘制可追溯地图、追踪业务链路、安全修改、验证结果，并把已经确认的知识增量沉淀下来。

核心闭环：

`Understand → Map → Trace → Change → Verify → Capture → Understand Better`

## 第一版包含什么

| Skill | 适用目标 | 主要产出 |
| --- | --- | --- |
| `landing-scan` | 初次接手仓库 | 项目概览、目录职责、运行指南、默认项目地图 |
| `landing-map` | 看清结构或流程 | Archify 交互图，或 Mermaid 降级图及源码证据 |
| `landing-trace` | 理解一个具体行为 | 端到端调用链、数据变化、异常分支、风险点 |
| `landing-change` | 实施已授权修改 | 验收标准、影响分析、最小实现、验证交接 |
| `landing-verify` | 判断修改是否完成 | 测试矩阵、实际命令与结果、差异审查、剩余风险 |
| `landing-capture` | 保存已确认知识 | 增量文档、决策与排查经验、受影响地图更新 |

六个 Skill 不要求每次全部执行。初次上手通常从 `landing-scan` 开始；已知入口的窄问题可直接使用 `landing-trace`；代码修改应由 `landing-change` 交给 `landing-verify` 收尾。

## 安装

### Codex

在 Codex CLI 中添加 Landing Kit marketplace：

```bash
codex plugin marketplace add LavaCourage07/landing-kit
```

然后安装插件：

```bash
codex plugin add landing-kit@landing-kit
```

安装完成后请启动一个新的 Codex 会话，让六个 Skill 被重新发现。可以用下面的提示验证：

```text
Use $landing-scan to help me get oriented in this repository.
```

更新到仓库发布的新版本：

```bash
codex plugin marketplace upgrade landing-kit
codex plugin add landing-kit@landing-kit
```

这是一条由 GitHub 仓库提供的 marketplace 分发路径，不代表 Landing Kit 已进入 ChatGPT/Codex 公共插件目录。

若只需在某个仓库试用，也可以把 `skills/landing-*` 复制或链接到该仓库的 `.agents/skills/`，然后启动一个新会话确认六个 Skill 的名称与描述已被发现。不同 Codex 客户端的插件入口可能不同，请以当前官方文档为准。

### Claude Code

仓库包含 `.claude-plugin/plugin.json`，公共 Skill 位于 `skills/`。可将本 GitHub 仓库加入 Claude Code marketplace 后安装插件；开发期间也可把各 `skills/landing-*` 复制或链接到项目的 `.claude/skills/` 或个人的 `~/.claude/skills/`。重启会话后，用 `/landing-scan` 等命令检查发现状态。

平台差异和验证方式见 [references/cross-platform.md](references/cross-platform.md)。

## 快速开始

在一个准备接手的代码仓库中提出：

```text
Use $landing-scan to help me get oriented in this repository.
```

首次扫描会默认尝试使用 `landing-map`。若已安装 Archify，将优先生成可交互地图；否则会先说明安装选项，并在未安装时用 Mermaid 继续完成基础地图，不阻塞上手。

继续追踪具体功能：

```text
Use $landing-trace to trace what happens after a user submits the sign-in form,
including validation, errors, persistence, and tests.
```

实施与验证修改：

```text
Use $landing-change to add the requested behavior and preserve all existing work.
Then use $landing-verify against the agreed acceptance criteria.
```

## 可选依赖

- [Archify](https://github.com/tt-a1i/archify)：地图首选渲染器；缺失时降级为 Mermaid。
- [Superpowers](https://github.com/obra/superpowers)：规划、TDD、调试和交付工作流；缺失时使用 Landing Kit 的基础流程。
- [Xiaohei Illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations)：知识沉淀阶段的可选解释性插图。

Landing Kit 不会未经许可安装依赖，也不会因为可选依赖缺失而虚构已完成的能力。完整依赖规则见 [references/dependencies.md](references/dependencies.md)。

## 开发与校验

```bash
python3 scripts/validate_repository.py
```

该命令检查六个 Skill 的基本契约、元数据、共享引用与插件清单。它是静态校验，不替代真实仓库中的触发、行为、视觉和安全评测。评测定义见 [evals/README.md](evals/README.md)。

开发规格见 [DEVELOPMENT.md](DEVELOPMENT.md)，当前实现与限制见 [STATUS.md](STATUS.md)。

## 许可证

[MIT](LICENSE)
