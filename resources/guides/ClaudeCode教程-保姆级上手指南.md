# 【教程】Claude Code — 保姆级上手指南

> 适用版本：Claude Code 2026（CLI / VS Code / Desktop / Web）
> 更新日期：2026-07-29
> 难度：★★☆☆☆（新手友好）
> 适用人群：独立开发者、OPC超级个体、技术创业者

---

## 一、这是什么工具？

**Claude Code** 是 Anthropic 推出的终端原生AI编程智能体。和Codex一样，它住在你的终端里，能读取代码库、编写代码、执行命令、自主迭代。

但与Codex最大的区别：**Claude Code更擅长深度推理——处理复杂架构问题、大规模重构、多步骤决策任务时表现更出色。**

### 核心能力

| 能力 | 说明 |
|------|------|
| 深度代码理解 | 1M token上下文窗口，能理解整个大型项目 |
| 自主规划执行 | 先规划方案，确认后逐步实施 |
| 多文件编辑 | 一次修改几十个文件，保持一致性 |
| 自动测试修复 | 改完代码自动运行测试，失败自动修复 |
| MCP协议 | 连接数据库、API、设计稿等外部工具 |
| Hooks机制 | 在特定事件触发自动化检查（如自动格式化代码） |
| 子Agent | 分支出一个独立Agent处理子任务 |

### Claude Code vs Codex vs Cursor

| 对比 | Claude Code | Codex | Cursor |
|------|-------------|-------|--------|
| 核心模型 | Claude Opus 4.8 | GPT-5.3-Codex | 多模型 |
| 擅长 | 深度推理、复杂重构 | 速度、并行任务 | 日常编码 |
| 上下文 | 1M tokens | 1.05M tokens | 视模型而定 |
| 价格起点 | $20/月 (Claude Pro) | $20/月 (ChatGPT Plus) | $20/月 |
| MCP | 原生支持（Anthropic创建） | 支持 | 支持 |
| 开源 | CLI 开源 | CLI 开源 (Apache 2.0) | 否 |

> **一句话选**：复杂任务找Claude Code，常规开发用Cursor，自动化任务用Codex。

---

## 二、安装与设置（3分钟上手）

### 2.1 准备工作

- Anthropic账号（console.anthropic.com）
- Claude订阅：Pro ($20/月) 或 Max ($100-200/月)
- 终端：macOS/Linux Terminal，Windows WSL2

### 2.2 安装方式（三选一）

**方式A：桌面版（新手推荐）**
```text
1. 下载 Claude 桌面应用（claude.ai/download）
2. 登录后，在对话输入框找到 Codex 图标旁边的 Claude Code 图标
3. 点击启用，选择你的项目目录
4. 直接输入自然语言描述任务
```

**方式B：CLI终端版（开发者推荐）**
```bash
# macOS安装
brew install claude-code

# 或用npm安装
npm install -g @anthropic/claude-code

# 验证安装
claude --version

# 设置API密钥（二选一）
export ANTHROPIC_API_KEY="sk-ant-xxxx"
# 或在 ~/.claude/config.toml 中配置
```

**方式C：VS Code扩展**
```text
1. 扩展市场搜索 "Claude Code"
2. 安装官方扩展
3. Cmd+Shift+P -> "Claude Code: Start Session"
4. 选择项目目录开始对话
```

### 2.3 首次运行

```bash
cd your-project
claude
# 进入交互模式，直接输入你的需求
```

Claude Code启动后会先扫描你的项目结构，了解代码库的概况，然后等待你的指令。

---

## 三、核心功能与命令速查

### 3.1 四种操作模式

| 模式 | 命令/场景 | 说明 |
|------|----------|------|
| **对话模式** | `claude` 直接进入 | 像聊天一样指挥它干活 |
| **单次命令** | `claude -p "任务"` | 一条指令执行完后退出 |
| **管道模式** | `cat error.log | claude -p "分析错误"` | 把数据管道传给Claude |
| **自动模式** | `claude -p "任务" --auto` | 自动执行，不需要逐条确认 |

### 3.2 核心Slash命令

| 命令 | 作用 | 使用时机 |
|------|------|---------|
| `/plan` | 制定执行方案 | 所有复杂任务的第一步 |
| `/review` | 审查最近修改的代码 | 功能完成后的质量检查 |
| `/test` | 生成并运行测试 | 为新功能补充测试 |
| `/fix` | 自动修复错误 | 测试失败或编译报错时 |
| `/compact` | 压缩对话上下文 | 对话超过30轮后清理 |
| `/init` | 初始化 CLAUDE.md | 新项目建立规范文件 |
| `/status` | 查看已修改的文件列表 | 想知道改了哪些文件时 |
| `/diff` | 查看所有修改的diff | 审查变更时 |
| `/undo` | 撤销最后一次修改 | 不满意的改动 |
| `/cost` | 查看本次会话消耗 | 关注费用的用户 |

### 3.3 MCP（模型上下文协议）

MCP是Claude Code独有的核心能力——让AI可以连接外部工具：

```text
# 安装MCP服务器后，Claude Code可以：
"读取JIRA任务ENG-4521，修复代码后发到Slack"
"检查Sentry最新错误，到数据库查受影响用户"
"读取Figma设计稿，更新UI组件"
```

MCP服务器配置在 `~/.claude/mcp.json` 中。

---

## 四、正确使用姿势（精华）

### 4.1 黄金法则：先规划再执行

这是Claude Code最核心的原则，比Codex更需要遵循——因为Claude Code的深度推理能力很强，但如果你不给定方向，它可能会过度设计。

**错误示范**：
```
帮我优化这个项目的性能
（结果：Claude改了50个文件，改了你不想要的方向）
```

**正确示范**：
```
/plan 我想优化首页加载性能，
当前LCP是4.5秒，目标是2秒以内。
不要改动后端API，只优化前端渲染。
先出方案，我确认后再执行。
```

### 4.2 CLAUDE.md：你的永久指令手册

和Codex的AGENTS.md一样，CLAUDE.md是Claude Code的"记忆系统"。每次启动自动读取。

**创建方式**：在项目目录执行 `/init`

**优秀CLAUDE.md示例**：
```
# 项目规范

## 技术栈
- 前端: React 18 + TypeScript + Tailwind CSS
- 后端: Node.js + Express + PostgreSQL
- 测试: Jest + React Testing Library

## 代码规范
- 所有新功能必须先编写测试
- API路由放在 /src/routes/ 目录
- 数据库查询使用参数化查询，避免SQL注入
- 每次修改后运行 npm run typecheck

## 架构原则
- 保持模块单一职责
- 避免循环依赖
- 业务逻辑与数据访问层分离

## 审查要求
- 提交前必须运行全量测试
- 检查是否有未处理的异常
- 确认没有硬编码的密钥或URL
```

**层级配置**：
```
~/.claude/CLAUDE.md        ← 全局个人规范
~/project/CLAUDE.md         ← 项目规范（优先级更高）
~/project/src/CLAUDE.md     ← 模块规范（最高优先级）
```

### 4.3 Hooks：自动化质量门禁

Hooks是Claude Code的"自动检查员"——在特定事件（如写完代码后、执行命令前）自动触发检查：

```yaml
# ~/.claude/hooks.yaml
hooks:
  # 每次写入文件后自动格式化
  PostToolUse:
    - match: "Write|Edit"
      command: "npx prettier --write"
  
  # 提交前运行测试
  PreToolUse:
    - match: "ExecuteCommand"
      command: "npm test"
```

### 4.4 Skills：重复任务一键执行

把常用的复杂操作保存为Skill：

```yaml
# ~/.claude/skills/deploy.yaml
name: "deploy"
description: "构建并部署到生产环境"
steps:
  - "运行 npm run build"
  - "运行 npm test"
  - "部署到Vercel"
```

下次只需：`/skill deploy`

---

## 五、实战场景（含完整指令）

### 场景1：大规模代码重构

这是Claude Code的强项——处理需要深入理解代码逻辑的重构任务。

**完整指令**：
```
/plan

我要把项目的用户认证模块从JWT方案迁移到Session方案。

当前情况：
- 认证代码分散在 /src/auth/ 和 /src/middleware/ 两个目录
- 使用了 jsonwebtoken 和 bcrypt 两个包
- 前端在 localStorage 中存储token

迁移要求：
1. 用 express-session + connect-redis 替换 JWT
2. 前端从localStorage改为cookie（httpOnly）
3. 保持现有的API接口不变（返回格式、状态码等）
4. 数据库用户表结构不改

执行计划：
1. 先分析所有受影响文件的依赖关系
2. 按「后端中间件 → 路由 → 前端适配」的顺序修改
3. 每改完一个模块运行 npm test 验证
4. 全部完成后进行集成测试

请先输出详细方案，我确认再开始。
```

**预期效果**：
```text
手动做：3-5天，容易遗漏
Claude Code做：2-3小时（你确认方案后）
```

---

### 场景2：调试疑难Bug

Claude Code最实用的能力之一——给一段错误信息和错误栈，它能定位根因并修复。

**完整指令**：
```
我遇到一个生产环境的Bug，以下是信息：

错误信息：
TypeError: Cannot read properties of undefined (reading 'map')
    at UserList.render (/src/components/UserList.tsx:45:23)
    at updateContextConsumer (/node_modules/react-dom/...)

触发条件：
- 在用户搜索页面，输入特殊字符时偶发
- 本地开发环境无法复现
- 生产环境大约5%的请求会出现

相关代码文件：
- /src/components/UserList.tsx
- /src/hooks/useUsers.ts
- /src/api/users.ts

请：
1. 分析可能的原因（列出3种可能性）
2. 添加防御性代码
3. 添加错误边界组件
4. 添加日志，方便下次定位
5. 运行测试验证修复
```

---

### 场景3：搭建完整API后端

作为OPC，你需要快速搭建一个后端服务。Claude Code可以从零生成完整的API。

**完整指令**：
```
/plan

请帮我创建一个完整的REST API后端项目。

技术选型：
- Node.js + Express + TypeScript
- 数据库：PostgreSQL（用 Prisma ORM）
- 认证：JWT
- 测试：Jest + Supertest

功能需求：
1. 用户注册/登录（邮箱+密码）
2. 用户资料CRUD
3. 文章发布和管理
4. 文件上传（本地存储）

项目结构：
```
src/
  routes/        # 路由
  controllers/   # 控制器
  models/        # 数据模型
  middleware/    # 中间件
  utils/         # 工具函数
  types/         # 类型定义
```

执行顺序：
1. 项目初始化和TypeScript配置
2. 数据库Schema和Prisma配置
3. 用户认证模块
4. 用户资料模块
5. 文章模块
6. 文件上传模块
7. API文档（用swagger）

每个步骤完成后等我确认。先输出方案。
```

---

### 场景4：性能分析与优化

Claude Code能分析代码并给出优化建议。

**完整指令**：
```
/plan

分析 /src/api/products.ts 的性能瓶颈。

当前问题：
- 接口响应时间平均2.3秒
- 包含大量数据库查询
- 存在N+1查询问题

请：
1. 分析当前代码的性能问题
2. 给出优化方案（包括预期提升）
3. 逐步实施优化
4. 每次优化后运行测试验证
5. 输出优化前后的性能对比

特别注意：
- 不要修改API返回格式
- 不要引入新的数据库连接
- 保持代码可读性
```

---

## 六、常见错误与避坑

### 六个新手必犯的错误

| # | 错误 | 正确做法 |
|:-:|------|---------|
| 1 | 不先/plan直接执行 | 复杂任务先出方案，确认方向再动手 |
| 2 | 对话超过30轮不压缩 | 定期用 /compact 清理上下文 |
| 3 | 把规则写在prompt里 | 写到 CLAUDE.md 中 |
| 4 | 不设hooks做质量门禁 | 用 hooks 自动格式化、运行测试 |
| 5 | 同时改太多文件 | 一次聚焦一个模块，分批进行 |
| 6 | 不给验证方法 | 每条指令末尾加验证步骤 |

### 权限系统说明

Claude Code的权限系统比较严格，新手可能会觉得烦，但这是为了安全：

```text
默认情况下，Claude Code在以下操作时会征求你同意：
- 读取文件（可以设置为自动）
- 写入文件（默认需要确认）
- 执行命令（默认需要确认）
- 网络访问（默认需要确认）

建议：初期保持默认，熟悉后再放宽权限
```

---

## 七、OPC实战建议

### 分阶段使用

| 阶段 | 推荐配置 | 侧重点 |
|------|---------|--------|
| 新手期 | 桌面版 + CLAUDE.md | 熟悉能力，建立规范 |
| 成长期 | CLI + CLAUDE.md + MCP | 连接数据库和外部工具 |
| 高效期 | CLI + Skills + Hooks + 子Agent | 自动化质量门禁和重复任务 |

### Claude Code + Codex 搭配策略

它们不是替代关系，而是互补：

```text
Claude Code负责：
- 复杂架构决策
- 大规模重构
- 调试疑难Bug
- 代码审查

Codex负责：
- 日常功能开发
- 批量文件操作
- 并行任务
- 周报等自动化

工作流示例：
1. Claude Code做架构设计 → 确认方案
2. Codex拆解为多个并行任务 → 同时开发
3. Claude Code做最终审查和整合
```

### 订阅推荐

| 使用强度 | 推荐 | 月费 |
|---------|------|:----:|
| 偶尔使用 | Claude Pro | $20 |
| 日常使用 | Claude Max 5x | $100 |
| 重度使用 | Claude Max 20x | $200 |

---

## 参考链接

- 官方文档：docs.anthropic.com/en/docs/claude-code
- 最佳实践：anthropic.com/engineering/claude-code-best-practices
- GitHub：github.com/anthropics/claude-code
- MCP文档：modelcontextprotocol.io
- 社区模板：github.com/davepoon/claude-code-subagents-collection
