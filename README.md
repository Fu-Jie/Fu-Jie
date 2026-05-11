> 🇨🇳 **中文版请点击** → [跳转到中文版 ↓](#-中文版)

---

# 付杰 · Jeff Fu

**AI Application Developer · Shanghai**

I build tools that make AI actually useful in real workflows — not just chat boxes, but systems that think, automate, and deliver structured results.

---

### 🟢 Open to Work

> I'm actively looking for my next opportunity.
>
> - 🏢 **On-site / Hybrid** — Shanghai only
> - 🌏 **Remote** — Open to global remote
> - 💬 **English** — Text only; voice calls require translation software
>
> **→ fj1945@live.cn** · [Resume](https://datacareer.yangtzeaidata.site/?lang=en)

---

## 🔨 What I'm Building

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

### MCAF: Multi-Core Agent Framework *(research · in use on InsightFlow)*

A filesystem-level coordination kernel for **heterogeneous AI agents working in parallel on the same codebase**.

The core problem: when you run Claude Code, GitHub Copilot, and OpenAI Codex simultaneously on the same repo, file conflicts, duplicate work, broken dependencies, and zombie locks are inevitable. MCAF solves this by borrowing from **CPU multi-core architecture** — specifically MESI cache coherence and shared bus design.

```
Claude Code ──┐
GitHub Copilot─┤                                   .core_bus/
OpenAI Codex ──┼──▶  MCAF Coordination Kernel  ──▶  (filesystem as
Gemini Agent ──┘   (Shared Bus · MESI+Q Locks        single source
                    Task DAG · Message Broker)        of truth)
```

Key properties:
- **Agent-agnostic** — any agent that can run shell commands works; no SDK lock-in
- **Zero-dependency** — just Python 3 + filesystem; no database, no message queue, no network service
- **File-level MESI+Q locking** — prevents concurrent writes at the individual file level
- **DAG task scheduler** — dependency-aware task queue; agents auto-block and unblock
- **Full observability** — structured event log, per-session mailboxes, health diagnostics, watchdog

Real usage on InsightFlow: 85 agent sessions · 94 tasks (95.7% complete) · 240 files tracked · 488 events logged · ~6,600 lines of Python · 32 CLI modules

> MCAF is not another agent framework. It doesn't wrap LLM APIs or generate agents. It's **traffic control** — letting existing agents from different vendors safely share the same road.

---

## ⚙️ How I Run AI Agents in Production

Most people run Agent SDK code as one-off scripts. I treat AI agents as first-class production workloads.

```
Design workflow
  → Write agent logic with Agent SDK
  → Wrap as Prefect flow  →  Deploy to scheduler
  → Run on schedule / event trigger / manual invoke
  → Full observability: logs · retries · alerts · run history
```

Any agent task — data analysis, report generation, monitoring & alerting, data retrieval, content processing, multi-step reasoning pipelines — gets the same production-grade treatment as a traditional data pipeline: scheduling, retries, observability, parameterization, DAG composition.

> Real-world: a self-serve data retrieval agent on this stack automated 70%+ of ad-hoc data requests for an entire company, running as a scheduled Prefect flow in production — with full retry and failure recovery, no babysitting required.

---

## 📦 Open Source

| Project | Stars | Description |
|---|---:|---|
| [openwebui-extensions](https://github.com/Fu-Jie/openwebui-extensions) | 205 | OpenWebUI plugin ecosystem — Copilot integration, Excel/HTML rendering, MindMap generation, async context compression |
| [deepseek-free-api](https://github.com/Fu-Jie/deepseek-free-api) | 77 | Community-maintained DeepSeek API adapter — protocol fixes, R1 search citation parsing, multi-arch Docker |
| [open-webui-prompt-plus](https://github.com/Fu-Jie/open-webui-prompt-plus) | 39 | Frontend prompt management suite — spotlight search, AI-generated prompt categories, smart UI rendering |
| [openwebui-chat-client](https://github.com/Fu-Jie/openwebui-chat-client) | 31 | Stateful Python SDK for LLM dispatch — async/sync, multimodal, tool-use support |
| [mimo-free-api-mcp](https://github.com/Fu-Jie/mimo-free-api-mcp) | 11 | MiMo Free API MCP gateway — search, vision, long-text segmentation, SQLite persistence |
| [open-webui-pipeline-wisdom-synthesizer](https://github.com/Fu-Jie/open-webui-pipeline-wisdom-synthesizer) | 10 | Open WebUI pipeline for structured multi-expert analysis reports |

**OpenWebUI Community:** [openwebui.com/u/Fu-Jie](https://openwebui.com/u/Fu-Jie)
· 230K+ profile views · 22K+ plugin downloads · 839+ followers
· Featured in official Newsletter ×2 · Recognized by project author tjbck

---

## 🛠 Tech Stack

**AI / LLM & Agent** — Prompt engineering · RAG · multi-model routing · LLM app development · Agent SDK · Multi-agent coordination (MCAF) · OpenWebUI ecosystem

**Orchestration** — Prefect (agent scheduling + workflow orchestration) · ETL · PostgreSQL · SQLite · SQL Server

**Frontend** — React (Vite) + TypeScript · Shadcn UI · Tailwind CSS · Zustand · Zod

**Visualization** — Dash · Plotly · ECharts · Recharts · Plotly.js · Power BI

**Backend** — FastAPI · PostgreSQL · SQLAlchemy · Pandas · JWT · Node.js

**Desktop** — Electron · IPC · safeStorage · local sidecar architecture

---

## 💼 Background

7 years in data engineering and AI tooling. Most recently built and owned the entire data infrastructure for a B2B e-commerce platform — ETL pipelines (1.3M+ monthly tasks, 97%+ success rate), company-wide sales dashboards and metrics system, and an AI-powered self-serve data retrieval agent deployed as a scheduled Prefect flow in production.

Outside of work: building InsightFlow, researching multi-agent parallel development coordination (MCAF), contributing to the OpenWebUI open-source ecosystem.

---

## 📬 Get in Touch

| | |
|---|---|
| **Email** | fj1945@live.cn |
| **Resume** | [datacareer.yangtzeaidata.site](https://datacareer.yangtzeaidata.site/?lang=en) |
| **Location** | Shanghai, China |
| **Remote** | Yes — async / text-based preferred |
| **Open to** | AI app dev · Full-stack (AI/data) · Developer tooling · Data platform · Agent workflow engineering |

> 💬 **Language note:** English communication is text only — GitHub, Slack, email, docs, code review all good. Voice or video calls in English are not possible without translation software.

---

*Building things that make AI less like magic and more like infrastructure.*

---

## 🇨🇳 中文版

**AI 应用开发者 · 上海**

我构建让 AI 真正嵌入实际工作流的工具 —— 不只是聊天框，而是能思考、自动化、输出结构化结果的系统。

---

### 🟢 正在找工作

> 我正在积极寻找下一份工作机会。
>
> - 🏢 **线下 / 混合办公** — 仅限上海
> - 🌏 **远程** — 接受全球远程
> - 💬 **英语** — 仅限文字沟通；如必须语音通话，需借助翻译软件
>
> **→ fj1945@live.cn** · [简历](https://datacareer.yangtzeaidata.site/?lang=zh-CN)

---

### 🔨 正在构建

**InsightFlow** *(开发中 · 暂未开源)*

一个以桌面端为核心、本地优先的可视化思维操作系统。不把 AI 当成输出长文本的聊天框，而是把每次 AI 响应转化为结构化、可交互的视觉画布。

核心设计：
- 每个问题都成为一个**项目**，绑定本地真实文件夹
- 每次 AI 响应都输出一个**交互式 HTML Canvas** —— 可探索、可对比、可组合
- 完整工具调用可视化：无黑盒，只有可见的操作追踪
- 本地优先存储：文件系统 + SQLite，密钥由 OS Keychain 管理

技术栈：`Electron 41` · `React 19 + TypeScript + Vite` · `Node.js 20+` · `SQLite + FTS5` · `Drizzle ORM`

---

**MCAF：多核 Agent 协调框架** *(研究中 · 已用于 InsightFlow 开发)*

一个文件系统级的协调内核，让 **Claude Code、GitHub Copilot、OpenAI Codex 等不同厂商的 AI Agent 在同一个代码库上安全并行工作**。

核心问题：同时运行多个 AI Agent 编辑同一个仓库时，文件冲突、重复工作、依赖断裂、僵尸锁是必然发生的问题。MCAF 从 **CPU 多核架构**中汲取灵感——借鉴 MESI 缓存一致性协议和共享总线设计来解决这些问题。

```
Claude Code ──┐
GitHub Copilot─┤                              .core_bus/
OpenAI Codex ──┼──▶  MCAF 协调内核  ──▶  （文件系统即唯一数据源）
Gemini Agent ──┘   （共享总线 · MESI+Q 锁
                    DAG 任务调度 · 消息代理）
```

核心特性：
- **Agent 无关** — 任何能执行 Shell 命令的 Agent 均可接入，无 SDK 绑定
- **零依赖部署** — 只需 Python 3 + 文件系统，无需数据库、消息队列或网络服务
- **文件级 MESI+Q 锁** — 在单个文件粒度上防止并发写冲突
- **DAG 任务调度器** — 感知依赖关系的任务队列，Agent 自动阻塞与解锁
- **完整可观测性** — 结构化事件日志、每会话信箱、健康诊断、看门狗

InsightFlow 真实运行数据：85 个 Agent 会话 · 94 个任务（95.7% 完成）· 240 个文件追踪 · 488 条事件记录 · ~6,600 行 Python · 32 个 CLI 模块

> MCAF 不是又一个 Agent 框架——它不生产 Agent，不包装 LLM API。它是**"交通管制系统"**，让来自不同厂商的 Agent 能安全地在同一条公路上并行行驶。

---

### ⚙️ 如何让 AI Agent 跑在生产环境

大多数人用 Agent SDK 只是跑一次性脚本。我把 AI Agent 当作一等生产工作负载来对待。

```
设计工作流  →  用 Agent SDK 编写逻辑  →  封装为 Prefect Flow
  →  部署到调度系统  →  定时 / 事件触发 / 手动调用
  →  完整可观测性：日志 · 重试 · 告警 · 运行历史
```

**Prefect 让 Agent 从脚本变成基础设施。**

> 实际案例：AI 自助取数 Agent 以 Prefect Scheduled Flow 形式在生产运行，自动化处理全公司 70%+ 的日常取数需求，具备完整重试与故障恢复，无需人工值守。

---


## 📊 Community Stats
> ![updated](https://img.shields.io/endpoint?url=https%3A%2F%2Fgist.githubusercontent.com%2FFu-Jie%2Fdb3d95687075a880af6f1fba76d679c6%2Fraw%2Fbadge_updated.json&style=flat)

| 👤 Author | 👥 Followers | ⭐ Points | 🧩 Plugin Contributions |
| :---: | :---: | :---: | :---: |
| [Fu-Jie](https://openwebui.com/u/Fu-Jie) | ![home_followers](https://img.shields.io/endpoint?url=https%3A%2F%2Fgist.githubusercontent.com%2FFu-Jie%2Fdb3d95687075a880af6f1fba76d679c6%2Fraw%2Fbadge_home_followers.json&style=flat) | ![home_points](https://img.shields.io/endpoint?url=https%3A%2F%2Fgist.githubusercontent.com%2FFu-Jie%2Fdb3d95687075a880af6f1fba76d679c6%2Fraw%2Fbadge_home_points.json&style=flat) | ![home_contributions](https://img.shields.io/endpoint?url=https%3A%2F%2Fgist.githubusercontent.com%2FFu-Jie%2Fdb3d95687075a880af6f1fba76d679c6%2Fraw%2Fbadge_home_contributions.json&style=flat) |

| 📝 Posts | ⬇️ Plugin Downloads | 👁️ Plugin Views | 👍 Upvotes | 💾 Plugin Saves |
| :---: | :---: | :---: | :---: | :---: |
| ![home_posts](https://img.shields.io/endpoint?url=https%3A%2F%2Fgist.githubusercontent.com%2FFu-Jie%2Fdb3d95687075a880af6f1fba76d679c6%2Fraw%2Fbadge_home_posts.json&style=flat) | ![home_downloads](https://img.shields.io/endpoint?url=https%3A%2F%2Fgist.githubusercontent.com%2FFu-Jie%2Fdb3d95687075a880af6f1fba76d679c6%2Fraw%2Fbadge_home_downloads.json&style=flat) | ![home_views](https://img.shields.io/endpoint?url=https%3A%2F%2Fgist.githubusercontent.com%2FFu-Jie%2Fdb3d95687075a880af6f1fba76d679c6%2Fraw%2Fbadge_home_views.json&style=flat) | ![home_upvotes](https://img.shields.io/endpoint?url=https%3A%2F%2Fgist.githubusercontent.com%2FFu-Jie%2Fdb3d95687075a880af6f1fba76d679c6%2Fraw%2Fbadge_home_upvotes.json&style=flat) | ![home_saves](https://img.shields.io/endpoint?url=https%3A%2F%2Fgist.githubusercontent.com%2FFu-Jie%2Fdb3d95687075a880af6f1fba76d679c6%2Fraw%2Fbadge_home_saves.json&style=flat) |

### 📦 开源项目

| 项目 | Stars | 简介 |
|---|---:|---|
| [openwebui-extensions](https://github.com/Fu-Jie/openwebui-extensions) | 205 | OpenWebUI 插件生态系统：深度集成 GitHub Copilot，支持 Excel 渲染、思维导图生成及异步上下文压缩。 |
| [deepseek-free-api](https://github.com/Fu-Jie/deepseek-free-api) | 77 | DeepSeek API 社区适配版：修复原生协议问题，支持 R1 搜索引用解析，提供多架构 Docker 支持。 |
| [open-webui-prompt-plus](https://github.com/Fu-Jie/open-webui-prompt-plus) | 39 | OpenWebUI 提示词增强套件：提供 Spotlight 式搜索、AI 自动分类以及高度交互的提示词表单。 |
| [openwebui-chat-client](https://github.com/Fu-Jie/openwebui-chat-client) | 31 | 有状态的 Python SDK：专为 OpenWebUI 设计，支持异步/同步、多模态及复杂的工具调用流。 |
| [mimo-free-api-mcp](https://github.com/Fu-Jie/mimo-free-api-mcp) | 11 | MiMo Free API MCP 网关：基于官网逆向的高性能代理，支持搜索、识图、长文本分段及 SQLite 持久化。 |
| [open-webui-pipeline-wisdom-synthesizer](https://github.com/Fu-Jie/open-webui-pipeline-wisdom-synthesizer) | 10 | Open WebUI 智慧聚合管道：模拟多专家会诊模式，将多路 AI 意见聚合为结构化的专家分析报告。 |

**OpenWebUI 官方社区：** [openwebui.com/u/Fu-Jie](https://openwebui.com/u/Fu-Jie) · 23 万+ 浏览 · 22,042 插件下载 · 839+ 关注 · 官方 Newsletter 两次推荐

---

### 🛠 技术栈

**AI / LLM & Agent** — Prompt 工程 · RAG · 多模型路由 · LLM 应用开发 · Agent SDK · 多 Agent 并行协调（MCAF）· OpenWebUI 生态

**编排 & 自动化** — Prefect（Agent 调度 + 工作流编排）· ETL · PostgreSQL · SQLite · SQL Server · 慢查询审计

**前端** — React (Vite) + TypeScript · Shadcn UI · Tailwind CSS · Zustand · Zod

**数据可视化** — Dash · Plotly · ECharts · Recharts · Plotly.js · Power BI · AI 辅助可视化 Web 应用交付

**后端** — FastAPI · PostgreSQL · SQLAlchemy · Pandas · JWT · Node.js

**桌面端** — Electron · IPC · safeStorage · 本地 Sidecar 架构

---

### 💼 工作背景

7 年数据工程与 AI 工具开发经验。上一份工作在 B2B 电商平台独立负责全公司数据基础设施 —— ETL 调度平台（月均 130 万+ 任务，97%+ 成功率）、销售全链路看板与指标体系、以及一套部署在生产环境的 AI 自助取数 Agent。

业余时间：开发 InsightFlow、研究多 Agent 并行协调系统（MCAF）、活跃于 OpenWebUI 开源生态。

---

### 📬 联系方式

| | |
|---|---|
| **期望岗位** | AI 应用开发 · 全栈工程师（AI/数据方向）· Agent 工作流工程 · 开发者工具 · 数据平台 |
| **工作方式** | 上海线下/混合 或 全球远程 |
| **英语沟通** | 仅限文字（GitHub / Slack / 邮件 / 文档）· 语音通话需翻译软件 |
| **邮件** | fj1945@live.cn |
| **简历** | [datacareer.yangtzeaidata.site](https://datacareer.yangtzeaidata.site/?lang=zh-CN) |

*让 AI 从魔法变成基础设施。*

