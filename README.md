> 🇨🇳 **中文版请点击** → [跳转到中文版 ↓](#-中文版)

---

# 付杰 · Jeff Fu

**AI-native Workflow Engineer · LLMOps / Agent Systems · Shanghai**

![GitHub Profile Views](https://komarev.com/ghpvc/?username=Fu-Jie&label=GitHub%20Profile%20Views&color=0e75b6&style=flat)
[![Profile Hits](https://hits.sh/github.com/Fu-Jie/Fu-Jie.svg?view=today-total&label=Profile%20Hits&color=0e75b6)](https://hits.sh/github.com/Fu-Jie/Fu-Jie/)

I build production-grade AI systems that turn multi-model reasoning, agent workflows, and business data operations into reliable software infrastructure.

My work focuses on one idea:

> **AI should not be treated as a chat box. It should become workflow infrastructure.**

---

## 🟢 Open to Opportunities

I’m currently open to roles where AI is used to redesign real workflows — not just generate text.

**Best-fit roles**
- AI-native Workflow Engineer
- Agent Workflow / AI Productivity Engineer
- LLMOps / AI Platform Engineer
- Full-stack Engineer for AI + data products
- Data Platform / Analytics Engineering with AI automation
- Developer tooling for AI-assisted engineering teams

**What I’m looking for**
- Teams that treat AI as workflow infrastructure, not just a chatbot
- Work involving agents, multi-model systems, orchestration, observability, and human-in-the-loop review
- Opportunities to turn AI demos into production-grade internal tools or business systems
- Shanghai on-site / hybrid, or global remote with async-first collaboration

📫 **Contact:** fj1945@live.cn  
📄 **Resume:** [datacareer.yangtzeaidata.site](https://datacareer.yangtzeaidata.site/?lang=en)

---

## Why Me

- **7+ years across data engineering, analytics automation, and AI tooling**
- Built production data infrastructure for a B2B e-commerce platform: **1.3M+ monthly scheduled tasks, 97%+ success rate**
- Built a production self-serve data retrieval agent that automated **70%+ of company-wide ad-hoc data requests**
- Active OpenWebUI ecosystem contributor: **230K+ profile views, 22K+ plugin downloads, 839+ followers**
- Strong at turning AI capabilities into reliable workflows: orchestration, retries, observability, routing, review, and governance

---

## Core Philosophy

Most AI tools stop at a single interaction:

```text
User asks → AI answers → Human copies result
```

I build systems around a different pattern:

```text
Human defines goal and constraints
  → Multiple AI models / agents explore in parallel
  → System extracts consensus, disagreement, evidence, and risks
  → Human reviews, verifies, and takes responsibility
  → Workflow is scheduled, observable, repeatable, and auditable
```

**AI handles broad exploration. Humans remain responsible for judgment, verification, and final decisions.**

---

## ⚙️ Productionizing Agents with Prefect + Agent SDK

Most agent projects are impressive demos but fragile workloads.

My approach is to treat every agent as a production workflow:

```text
Agent SDK defines the intelligence layer
  → tools · reasoning · structured output · business actions

Prefect provides the runtime layer
  → scheduling · retries · parameters · logs · alerts · run history · DAG orchestration
```

Any agent task — data analysis, report generation, monitoring, data retrieval, content processing, multi-step reasoning, consistency checks — gets the same production-grade treatment as a traditional data pipeline.

**Real-world case:** a self-serve data retrieval agent on this stack automated **70%+** of ad-hoc data requests for an entire company, running as a scheduled Prefect flow in production with full retry and failure recovery.

This is the layer I care about most: **turning agents from scripts into infrastructure.**

---

## Featured Work

### Collective Wisdom Synthesizer

[open-webui-pipeline-wisdom-synthesizer](https://github.com/Fu-Jie/open-webui-pipeline-wisdom-synthesizer)

An OpenWebUI pipeline that transforms multi-model answers into structured decision reports.

Instead of simply merging AI outputs, it treats multiple models as independent expert advisors and extracts:

- Core consensus
- Key disagreements
- Unique insights
- Actionable synthesis
- Human-review-ready conclusions

This project reflects my AI-native workflow philosophy: **AI expands the search space; humans review and decide.**

---

### MCAF: Multi-Core Agent Framework *(research · in use on InsightFlow)*

A filesystem-level coordination kernel for **heterogeneous AI agents working in parallel on the same codebase**.

The core problem: when you run Claude Code, GitHub Copilot, OpenAI Codex, Gemini Agent, or other coding agents simultaneously on the same repo, file conflicts, duplicate work, broken dependencies, and zombie locks are inevitable.

MCAF solves this by borrowing from **CPU multi-core architecture** — specifically MESI cache coherence and shared bus design.

```text
Claude Code ──┐
GitHub Copilot─┤                                   .core_bus/
OpenAI Codex ──┼──▶  MCAF Coordination Kernel  ──▶  filesystem as
Gemini Agent ──┘   Shared Bus · MESI+Q Locks        source of truth
                    Task DAG · Message Broker
```

Key properties:
- **Agent-agnostic** — any agent that can run shell commands works; no SDK lock-in
- **Zero-dependency** — Python 3 + filesystem; no database, message queue, or network service required
- **File-level MESI+Q locking** — prevents concurrent writes at individual file level
- **DAG task scheduler** — dependency-aware task queue; agents auto-block and unblock
- **Full observability** — structured event log, per-session mailboxes, health diagnostics, watchdog

Real usage on InsightFlow: **85 agent sessions · 94 tasks · 95.7% complete · 240 files tracked · 488 events logged · ~6,600 lines of Python · 32 CLI modules**

> MCAF is not another agent framework. It does not wrap LLM APIs or generate agents. It is **traffic control** — letting existing agents from different vendors safely share the same road.

---

### InsightFlow *(in development · not yet open source)*

A desktop-first, local-first visual thinking OS for analysis and decision-making.

Instead of treating AI as a chat box that emits long text, InsightFlow turns each assistant turn into a structured, interactive visual canvas. Inspired by project-oriented agent workbenches like Codex — but the primary artifact is a visual canvas, not a code diff.

Core ideas:
- Every problem becomes a **project**, rooted in a real local folder
- Every AI response becomes an **interactive HTML canvas** — explorable, comparable, composable
- Full tool-call visibility: no black boxes, just operational trace
- Local-first: filesystem + SQLite, secrets via OS keychain

Stack: `Electron 41` · `React 19 + TypeScript + Vite` · `Node.js 20+` · `SQLite + FTS5` · `Drizzle ORM`

---

## 📦 Open Source

| Project | Stars | Description |
|---|---:|---|
| [openwebui-extensions](https://github.com/Fu-Jie/openwebui-extensions) | 205 | OpenWebUI plugin ecosystem — Copilot integration, Excel/HTML rendering, MindMap generation, async context compression |
| [deepseek-free-api](https://github.com/Fu-Jie/deepseek-free-api) | 77 | Community-maintained DeepSeek API adapter — protocol fixes, R1 search citation parsing, multi-arch Docker |
| [open-webui-prompt-plus](https://github.com/Fu-Jie/open-webui-prompt-plus) | 39 | Frontend prompt management suite — spotlight search, AI-generated prompt categories, smart UI rendering |
| [openwebui-chat-client](https://github.com/Fu-Jie/openwebui-chat-client) | 31 | Stateful Python SDK for LLM dispatch — async/sync, multimodal, tool-use support |
| [mimo-free-api-mcp](https://github.com/Fu-Jie/mimo-free-api-mcp) | 11 | MiMo Free API MCP gateway — search, vision, long-text segmentation, SQLite persistence |
| [open-webui-pipeline-wisdom-synthesizer](https://github.com/Fu-Jie/open-webui-pipeline-wisdom-synthesizer) | 10 | OpenWebUI pipeline for structured multi-expert analysis reports |

**OpenWebUI Community:** [openwebui.com/u/Fu-Jie](https://openwebui.com/u/Fu-Jie)
· 230K+ profile views · 22K+ plugin downloads · 839+ followers
· Featured in official Newsletter ×2 · Recognized by project author tjbck

---

## 🛠 Tech Stack

**AI / LLM & Agent** — Prompt engineering · RAG · multi-model routing · LLM app development · Agent SDK · human-in-the-loop review · multi-agent coordination (MCAF) · OpenWebUI ecosystem

**Orchestration / Production Runtime** — Prefect · agent scheduling · workflow orchestration · retries · alerts · ETL · PostgreSQL · SQLite · SQL Server

**Backend / Data** — Python · FastAPI · PostgreSQL · SQLAlchemy · Pandas · JWT · Node.js

**Frontend / Product** — React (Vite) + TypeScript · Shadcn UI · Tailwind CSS · Zustand · Zod

**Visualization** — Dash · Plotly · ECharts · Recharts · Plotly.js · Power BI

**Desktop** — Electron · IPC · safeStorage · local sidecar architecture

---

## 💼 Background

7 years in data engineering and AI tooling. Most recently built and owned the data infrastructure for a B2B e-commerce platform: ETL pipelines, company-wide sales dashboards, metrics governance, and a production AI-powered self-serve data retrieval agent.

Outside of work: building InsightFlow, researching multi-agent parallel development coordination (MCAF), and contributing to the OpenWebUI open-source ecosystem.

---

## 📬 Get in Touch

| | |
|---|---|
| **Email** | fj1945@live.cn |
| **Resume** | [datacareer.yangtzeaidata.site](https://datacareer.yangtzeaidata.site/?lang=en) |
| **Location** | Shanghai, China |
| **Work mode** | Shanghai on-site / hybrid, or global remote |
| **Communication** | English text is fine; voice/video may require translation support |
| **Open to** | AI-native workflow · Agent workflow engineering · LLMOps · AI/data full-stack · data platform · developer tooling |

---

*Building things that make AI less like magic and more like infrastructure.*

---

## 🇨🇳 中文版

# 付杰 · Jeff Fu

**AI-native 工作流工程师 · LLMOps / Agent Systems · 上海**

我构建生产级 AI 系统，把多模型推理、Agent 工作流和业务数据流程变成可靠的软件基础设施。

我的核心观点：

> **AI 不应该只是聊天框，而应该成为工作流基础设施。**

---

## 🟢 正在关注机会

我正在关注真正 AI-native 的工程岗位：不是把 AI 当成聊天框或辅助工具，而是把多模型推理、Agent 调度、数据自动化和业务流程重构为可运行、可观测、可维护的软件系统。

**期望方向**
- AI-native Workflow Engineer / AI 工作流工程师
- Agent 工作流 / AI 提效工程师
- LLMOps / AI 平台工程师
- AI + 数据产品全栈工程师
- 数据平台 / 分析工程，偏 AI 自动化方向
- 面向 AI 辅助研发团队的开发者工具

**我适合的团队**
- 认可 AI 可以重构研发、分析和业务流程
- 重视 human-in-the-loop、评估、审查和可观测性
- 愿意把 AI 工具从 Demo 做到生产级系统
- 不只是“使用 ChatGPT”，而是建设 AI 工作流基础设施

📫 **邮箱：** fj1945@live.cn  
📄 **简历：** [datacareer.yangtzeaidata.site](https://datacareer.yangtzeaidata.site/?lang=zh-CN)

---

## 为什么是我

- **7 年+ 数据工程、分析自动化与 AI 工具开发经验**
- 曾负责 B2B 电商平台数据基础设施：**月均 130 万+ 调度任务，97%+ 成功率**
- 构建生产级 AI 自助取数 Agent，自动化处理**全公司 70%+ 日常取数需求**
- OpenWebUI 生态活跃贡献者：**23 万+ 主页浏览，22K+ 插件下载，839+ 关注者**
- 擅长把 AI 能力做成稳定工作流：编排、重试、可观测、多模型路由、人工 review、流程治理

---

## 核心理念

多数 AI 工具停留在单次交互：

```text
用户提问 → AI 回答 → 人复制结果
```

我构建的是另一种模式：

```text
人定义目标与约束
  → 多模型 / 多 Agent 并行探索
  → 系统提炼共识、分歧、证据与风险
  → 人类 review、验证并承担最终责任
  → 工作流可调度、可观测、可复用、可审计
```

**AI 负责大范围发散，人负责判断、验证和最终决策。**

---

## ⚙️ 用 Prefect + Agent SDK 将 Agent 生产化

多数 Agent 项目停留在一次性 Demo：能跑，但不可调度、不可观测、不可恢复。

我的做法是把每个 Agent 都当成生产工作流：

```text
Agent SDK 负责智能层
  → 工具调用 · 推理 · 结构化输出 · 业务动作

Prefect 负责运行层
  → 调度 · 重试 · 参数化 · 日志 · 告警 · 运行历史 · DAG 编排
```

无论是数据分析、报告生成、监控告警、数据检索、内容处理、多步推理，还是一致性检查，都应该像传统数据管道一样具备生产级运行能力。

**真实案例：** AI 自助取数 Agent 基于这套方式在生产运行，自动化处理全公司 **70%+** 日常取数需求，具备完整重试与故障恢复。

这也是我最关注的方向：**让 Agent 从脚本变成基础设施。**

---

## 代表项目

### Collective Wisdom Synthesizer：多模型智慧聚合管道

[open-webui-pipeline-wisdom-synthesizer](https://github.com/Fu-Jie/open-webui-pipeline-wisdom-synthesizer)

一个 OpenWebUI Pipeline，用于将多个模型的独立回答转化为结构化决策报告。

它不是简单拼接回答，而是把多个模型视为独立专家组，自动提炼：

- 核心共识
- 关键分歧
- 独特洞察
- 综合建议
- 适合人工 review 的最终结论

这个项目体现了我的 AI-native 工作流理念：**AI 扩大思考半径，人负责 review 和决策。**

---

### MCAF：多核 Agent 协调框架 *(研究中 · 已用于 InsightFlow 开发)*

一个文件系统级的协调内核，让 **Claude Code、GitHub Copilot、OpenAI Codex、Gemini Agent 等不同厂商的 AI Agent 在同一个代码库上安全并行工作**。

核心问题：多个 AI Agent 同时编辑同一个仓库时，文件冲突、重复工作、依赖断裂、僵尸锁是必然发生的问题。

MCAF 从 **CPU 多核架构**中汲取灵感，借鉴 MESI 缓存一致性协议和共享总线设计来解决这些问题。

```text
Claude Code ──┐
GitHub Copilot─┤                              .core_bus/
OpenAI Codex ──┼──▶  MCAF 协调内核  ──▶  文件系统即唯一数据源
Gemini Agent ──┘   共享总线 · MESI+Q 锁
                    DAG 任务调度 · 消息代理
```

核心特性：
- **Agent 无关** — 任何能执行 Shell 命令的 Agent 均可接入，无 SDK 绑定
- **零依赖部署** — 只需 Python 3 + 文件系统，无需数据库、消息队列或网络服务
- **文件级 MESI+Q 锁** — 在单个文件粒度上防止并发写冲突
- **DAG 任务调度器** — 感知依赖关系的任务队列，Agent 自动阻塞与解锁
- **完整可观测性** — 结构化事件日志、每会话信箱、健康诊断、看门狗

InsightFlow 真实运行数据：**85 个 Agent 会话 · 94 个任务 · 95.7% 完成 · 240 个文件追踪 · 488 条事件记录 · ~6,600 行 Python · 32 个 CLI 模块**

> MCAF 不是又一个 Agent 框架——它不生产 Agent，不包装 LLM API。它是**交通管制系统**，让来自不同厂商的 Agent 能安全地在同一条公路上并行行驶。

---

### InsightFlow *(开发中 · 暂未开源)*

一个以桌面端为核心、本地优先的可视化思维操作系统。不把 AI 当成输出长文本的聊天框，而是把每次 AI 响应转化为结构化、可交互的视觉画布。

核心设计：
- 每个问题都成为一个**项目**，绑定本地真实文件夹
- 每次 AI 响应都输出一个**交互式 HTML Canvas** —— 可探索、可对比、可组合
- 完整工具调用可视化：无黑盒，只有可见的操作追踪
- 本地优先存储：文件系统 + SQLite，密钥由 OS Keychain 管理

技术栈：`Electron 41` · `React 19 + TypeScript + Vite` · `Node.js 20+` · `SQLite + FTS5` · `Drizzle ORM`

---

## 📊 Community Stats

> ![updated](https://img.shields.io/endpoint?url=https%3A%2F%2Fgist.githubusercontent.com%2FFu-Jie%2Fdb3d95687075a880af6f1fba76d679c6%2Fraw%2Fbadge_updated.json&style=flat)

| 👤 Author | 👥 Followers | ⭐ Points | 🧩 Plugin Contributions |
| :---: | :---: | :---: | :---: |
| [Fu-Jie](https://openwebui.com/u/Fu-Jie) | ![home_followers](https://img.shields.io/endpoint?url=https%3A%2F%2Fgist.githubusercontent.com%2FFu-Jie%2Fdb3d95687075a880af6f1fba76d679c6%2Fraw%2Fbadge_home_followers.json&style=flat) | ![home_points](https://img.shields.io/endpoint?url=https%3A%2F%2Fgist.githubusercontent.com%2FFu-Jie%2Fdb3d95687075a880af6f1fba76d679c6%2Fraw%2Fbadge_home_points.json&style=flat) | ![home_contributions](https://img.shields.io/endpoint?url=https%3A%2F%2Fgist.githubusercontent.com%2FFu-Jie%2Fdb3d95687075a880af6f1fba76d679c6%2Fraw%2Fbadge_home_contributions.json&style=flat) |

| 📝 Posts | ⬇️ Plugin Downloads | 👁️ Plugin Views | 👍 Upvotes | 💾 Plugin Saves |
| :---: | :---: | :---: | :---: | :---: |
| ![home_posts](https://img.shields.io/endpoint?url=https%3A%2F%2Fgist.githubusercontent.com%2FFu-Jie%2Fdb3d95687075a880af6f1fba76d679c6%2Fraw%2Fbadge_home_posts.json&style=flat) | ![home_downloads](https://img.shields.io/endpoint?url=https%3A%2F%2Fgist.githubusercontent.com%2FFu-Jie%2Fdb3d95687075a880af6f1fba76d679c6%2Fraw%2Fbadge_home_downloads.json&style=flat) | ![home_views](https://img.shields.io/endpoint?url=https%3A%2F%2Fgist.githubusercontent.com%2FFu-Jie%2Fdb3d95687075a880af6f1fba76d679c6%2Fraw%2Fbadge_home_views.json&style=flat) | ![home_upvotes](https://img.shields.io/endpoint?url=https%3A%2F%2Fgist.githubusercontent.com%2FFu-Jie%2Fdb3d95687075a880af6f1fba76d679c6%2Fraw%2Fbadge_home_upvotes.json&style=flat) | ![home_saves](https://img.shields.io/endpoint?url=https%3A%2F%2Fgist.githubusercontent.com%2FFu-Jie%2Fdb3d95687075a880af6f1fba76d679c6%2Fraw%2Fbadge_home_saves.json&style=flat) |

---

## 📦 开源项目

| 项目 | Stars | 简介 |
|---|---:|---|
| [openwebui-extensions](https://github.com/Fu-Jie/openwebui-extensions) | 205 | OpenWebUI 插件生态系统：深度集成 GitHub Copilot，支持 Excel 渲染、思维导图生成及异步上下文压缩。 |
| [deepseek-free-api](https://github.com/Fu-Jie/deepseek-free-api) | 77 | DeepSeek API 社区适配版：修复原生协议问题，支持 R1 搜索引用解析，提供多架构 Docker 支持。 |
| [open-webui-prompt-plus](https://github.com/Fu-Jie/open-webui-prompt-plus) | 39 | OpenWebUI 提示词增强套件：提供 Spotlight 式搜索、AI 自动分类以及高度交互的提示词表单。 |
| [openwebui-chat-client](https://github.com/Fu-Jie/openwebui-chat-client) | 31 | 有状态的 Python SDK：专为 OpenWebUI 设计，支持异步/同步、多模态及复杂的工具调用流。 |
| [mimo-free-api-mcp](https://github.com/Fu-Jie/mimo-free-api-mcp) | 11 | MiMo Free API MCP 网关：基于官网逆向的高性能代理，支持搜索、识图、长文本分段及 SQLite 持久化。 |
| [open-webui-pipeline-wisdom-synthesizer](https://github.com/Fu-Jie/open-webui-pipeline-wisdom-synthesizer) | 10 | OpenWebUI 智慧聚合管道：模拟多专家会诊模式，将多路 AI 意见聚合为结构化专家分析报告。 |

**OpenWebUI 官方社区：** [openwebui.com/u/Fu-Jie](https://openwebui.com/u/Fu-Jie) · 23 万+ 浏览 · 22,042 插件下载 · 839+ 关注 · 官方 Newsletter 两次推荐

---

## 🛠 技术栈

**AI / LLM & Agent** — Prompt 工程 · RAG · 多模型路由 · LLM 应用开发 · Agent SDK · human-in-the-loop review · 多 Agent 并行协调（MCAF）· OpenWebUI 生态

**编排 & 生产运行层** — Prefect · Agent 调度 · 工作流编排 · 重试 · 告警 · ETL · PostgreSQL · SQLite · SQL Server

**后端 / 数据** — Python · FastAPI · PostgreSQL · SQLAlchemy · Pandas · JWT · Node.js

**前端 / 产品** — React (Vite) + TypeScript · Shadcn UI · Tailwind CSS · Zustand · Zod

**数据可视化** — Dash · Plotly · ECharts · Recharts · Plotly.js · Power BI

**桌面端** — Electron · IPC · safeStorage · 本地 Sidecar 架构

---

## 💼 工作背景

7 年数据工程与 AI 工具开发经验。上一份工作在 B2B 电商平台负责数据基础设施：ETL 调度、销售全链路看板、指标治理，以及一套部署在生产环境的 AI 自助取数 Agent。

业余时间：开发 InsightFlow、研究多 Agent 并行协调系统（MCAF）、活跃于 OpenWebUI 开源生态。

---

## 📬 联系方式

| | |
|---|---|
| **期望岗位** | AI-native 工作流 · Agent 工作流工程 · LLMOps · AI/数据全栈 · 数据平台 · 开发者工具 |
| **工作方式** | 上海线下/混合 或 全球远程 |
| **英语沟通** | 文字沟通可，包括 GitHub / Slack / 邮件 / 文档；语音/视频需翻译支持 |
| **邮件** | fj1945@live.cn |
| **简历** | [datacareer.yangtzeaidata.site](https://datacareer.yangtzeaidata.site/?lang=zh-CN) |

*让 AI 从魔法变成基础设施。*
