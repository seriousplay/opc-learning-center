# 【教程】OpenAI Codex — 保姆级上手指南（模版）

> 适用版本：Codex CLI 2026 / IDE Extension / ChatGPT Desktop
> 更新日期：2026-07-29
> 难度：★★☆☆☆（新手友好）
> 适用人群：独立开发者、OPC超级个体、技术创业者
> 教程编号：T001 | **本文同时也是后续教程的模版**

---

## 一、这是什么工具？

**Codex** 是 OpenAI 推出的终端原生AI编程智能体（Coding Agent）。你可以把它理解为：**一个用自然语言指挥的专业程序员，住在你的终端里。**

### 核心能力

| 能力 | 一句话说明 |
|------|-----------|
| 阅读代码库 | 理解整个项目结构和代码逻辑 |
| 编写代码 | 根据描述生成完整功能代码 |
| 执行命令 | 自动安装依赖、运行测试、部署 |
| 自主迭代 | 写代码->运行->发现错误->修复->再运行 |
| 并行工作 | 多个Codex同时处理不同任务 |
| 代码审查 | 自动审查PR，检查逻辑错误和安全问题 |

### 与其他工具的关系

| 对比 | Codex | Claude Code | Cursor |
|------|-------|-------------|--------|
| 形态 | 终端CLI+IDE插件 | 终端CLI+IDE插件 | AI原生IDE |
| 核心模型 | GPT-5.3-Codex | Claude Opus 4.8 | 多模型 |
| 开源 | Apache 2.0 (CLI) | (CLI) | 闭源 |
| 价格起点 | $20/月 (ChatGPT Plus) | $20/月 (Claude Pro) | $20/月 |
| 擅长 | 复杂自动化任务 | 深度推理任务 | 日常编码主力 |

---

## 二、安装与设置（3分钟上手）

### 2.1 准备工作

- OpenAI账号 (platform.openai.com)
- ChatGPT订阅：Plus ($20/月) 或 Pro ($200/月)
- 终端：macOS的Terminal，Windows的PowerShell/WSL2

### 2.2 安装方式（三选一）

**方式A：ChatGPT桌面版（新手推荐）**
- 下载桌面应用 (chatgpt.com/download)
- 登录，找到 Codex 图标并启用
- 选择项目目录，直接输入自然语言即可

**方式B：CLI终端版（开发者推荐）**
```bash
# macOS安装
brew install openai/codex/codex

# 验证安装
codex --version

# 设置API密钥
export OPENAI_API_KEY="sk-xxxx"
```

**方式C：VS Code扩展**
在扩展市场搜索 "Codex"，安装后 Cmd+Shift+P -> "Codex: Start Session"

### 2.3 安全设置

新手请保持默认的「建议模式」：Codex只展示修改建议，你确认后才执行。

---

## 三、核心功能与命令速查

### 3.1 四大操作模式

| 模式 | 命令 | 说明 |
|------|------|------|
| 直接询问 | codex -- "问题" | 快速问答 |
| 建议模式 | 默认 | Codex展示修改建议，你确认后执行 |
| 自动编辑 | codex auto | Codex自动修改，你审查diff |
| 全自动 | codex auto -- "任务" | 自动执行+运行测试验证 |

**新手路线**：建议模式 -> 自动编辑 -> 全自动模式

### 3.2 核心Slash命令

| 命令 | 作用 | 使用时机 |
|------|------|---------|
| /plan | 先规划再执行 | 复杂任务必须先出方案 |
| /review | 审查最近修改 | 完成功能后检查质量 |
| /test | 生成并运行测试 | 新功能补全测试 |
| /fix | 自动修复错误 | 测试失败后快速修复 |
| /compact | 压缩对话上下文 | 对话太长时清理 |
| /fork | 分支新对话 | 探索另一个方向 |
| /init | 初始化AGENTS.md | 新项目快速配置 |
| /diff | 查看所有修改 | 审查所有文件变更 |
| /undo | 撤销最后一次修改 | 回退不满意的改动 |

### 3.3 视觉模式（2026新增）

Codex支持截图输入！把设计稿或报错截图直接发给它。

---

## 四、正确使用姿势（精华）

### 4.1 黄金法则：先规划再执行

**错误做法**：直接说"帮我做个XXX"，结果不满意。

**正确做法**：
```
codex -- "/plan 我要给项目添加用户认证功能，帮我设计方案"
# Codex输出方案后，你确认方向，再开始编码
```

### 4.2 AGENTS.md：你的永久指令手册

AGENTS.md 是Codex的"记忆系统"，每次启动自动读取。

**创建方式**：在项目目录执行 codex -- "/init"

**示例内容**：
```
# 项目规范
## 技术栈
- 语言: TypeScript + Next.js 15
- UI: shadcn/ui + Tailwind CSS
- 数据库: Supabase
- 测试: Vitest

## 规范
- 修改后运行 pnpm typecheck
- 新功能必须包含单元测试
- commit格式: type(scope): description
```

### 4.3 Prompt四要素

| 要素 | 问题 | 示例 |
|------|------|------|
| 任务描述 | 要做什么？ | "添加邮箱验证功能" |
| 范围边界 | 哪些不能碰？ | "不要修改已有的认证中间件" |
| 质量标准 | 什么叫做好了？ | "新增代码覆盖率达到80%" |
| 验证方法 | 怎么确认成功？ | "运行 pnpm test:auth" |

### 4.4 MCP：连接外部世界

让Codex连接数据库、API、设计稿：
```toml
# ~/.codex/config.toml
[mcp_servers.postgres]
command = "npx"
args = ["-y", "@modelcontextprotocol/server-postgres", "postgresql://localhost/mydb"]
```

### 4.5 Skills：重复任务一键执行

```toml
# ~/.codex/skills/deploy.toml
name = "deploy"
description = "构建并部署到生产环境"
```
创建后只需：codex -- "/skill deploy"

---

## 五、实战场景

### 场景1：添加新功能

```
codex -- "
/plan
给用户管理页面添加搜索功能：
1. 支持按用户名和邮箱模糊搜索
2. 搜索结果分页，每页20条
3. 使用URL参数保持搜索状态
边界：只修改 /app/users/ 目录
验证：运行 pnpm test:users
"
```

### 场景2：并行开发（git worktree）

```bash
git worktree add ../feature-auth feature/auth
git worktree add ../feature-search feature/search

cd ../feature-auth && codex -- "实现用户认证"
cd ../feature-search && codex -- "实现搜索功能"
```

### 场景3：代码迁移

```
/plan 把项目从JavaScript迁移到TypeScript。
先分析所有.js文件输出迁移清单。
逐个迁移，每个完成后运行 pnpm typecheck。
完成后运行全量测试。
```

---

## 六、常见错误与避坑

### 六个必须避免的错误

| # | 错误 | 正确做法 |
|:-:|------|---------|
| 1 | 一次对话干太多事 | 一个对话只做一件事 |
| 2 | 不教Codex怎么验证 | 每个prompt末尾加验证命令 |
| 3 | 规则写在prompt里 | 写到AGENTS.md中 |
| 4 | 多个Codex同时改同一文件 | 用Git Worktree隔离 |
| 5 | 塞太多上下文 | 只提供相关文件 |
| 6 | 跳过/plan直接执行 | 复杂任务先出方案 |

### 安全红线

| 不要做的事 | 原因 |
|-----------|------|
| API密钥写在prompt里 | 会被记录到日志 |
| 非沙盒模式操作敏感文件 | Codex可能误删 |
| 同时开启读写+网络+文件访问 | "致命三连"最危险 |

---

## 七、OPC实战建议

### 分阶段配置

| OPC阶段 | 推荐配置 | 侧重点 |
|---------|---------|--------|
| 新手期 | ChatGPT桌面版 + AGENTS.md | 感受能力，建立习惯 |
| 成长期 | CLI + AGENTS.md + MCP | 连接数据库和设计工具 |
| 高效期 | CLI + Skills + Git Worktree | 并行任务，自动化 |

### 订阅推荐

| 使用强度 | 推荐 | 月费 |
|---------|------|:----:|
| 偶尔使用 | ChatGPT Plus | $20 |
| 日常使用 | Plus + API按需 | $20+ |
| 重度使用 | ChatGPT Pro + API | $200 |

---

## 参考链接

- [Codex官方文档](https://learn.chatgpt.com/docs/codex/cli)
- [最佳实践指南](https://learn.chatgpt.com/guides/best-practices)
- [GitHub: openai/codex](https://github.com/openai/codex)
- [Codex安装指南](https://learn.chatgpt.com/docs/codex/installation)

---

> **教程模版说明**
> 本文采用以下七段结构，作为后续所有工具教程的标准模版：
>
> 一、这是什么工具？（一句话定位 + 核心能力表 + 竞品对比）
> 二、安装与设置（多种方式，新手优先）
> 三、核心功能与命令速查（精华命令表）
> 四、正确使用姿势（核心方法论）
> 五、实战场景（3个典型场景）
> 六、常见错误与避坑（错误表 + 安全红线）
> 七、OPC实战建议（分阶段配置 + 工作流 + 订阅）
