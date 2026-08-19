# 【教程】n8n — 保姆级上手指南

> 适用版本：n8n 2026（Cloud / Self-hosted / Docker）
> 更新日期：2026-07-29
> 难度：★★★☆☆（需要基础技术理解）
> 适用人群：OPC超级个体、技术创业者、需要自动化的知识工作者

---

## 一、这是什么工具？

**n8n** 是一个开源的自动化工具，通过可视化方式把不同的软件和服务连接起来，让它们自动协作。你可以把它理解为：**一个"数字万能胶水"，把你用的所有工具粘在一起，自动跑。**

举个例子：每天早上9点，n8n可以自动抓取昨天的销售数据→用AI分析→生成报告→发到你的微信。整个过程你不需要打开任何一个软件。

### 核心能力

| 能力 | 一句话说明 |
|------|-----------|
| 连接400+应用 | 打通各种SaaS工具（无需编程） |
| 可视化工作流 | 拖拽式搭建，看得见的数据流动 |
| 自定义代码 | 支持JavaScript/Python，灵活性极高 |
| 4000+模板 | 社区已建好的工作流，拿来即用 |
| AI集成 | 接入任何LLM（GPT/Claude/DeepSeek等） |
| 自部署 | 可以装在自己的服务器上，数据不外传 |

### n8n vs 同类工具

| 对比 | n8n | Zapier | Make (Integromat) |
|------|-----|--------|-------------------|
| 开源 | 是（Fair-code） | 否 | 否 |
| 自部署 | 支持（Docker一键） | 不支持 | 不支持 |
| 价格 | 免费自部署 / 云版$20起 | $30/月起 | $10/月起 |
| 任务次数 | 不限（自部署） | 按量计费 | 按量计费 |
| 代码扩展 | JS/Python | 有限 | 有限 |
| 难度 | 中等 | 简单 | 简单 |

---

## 二、安装与设置（5分钟上手）

n8n有两种使用方式，新手推荐先试云版，熟练后用自部署：

### 方式A：云版（新手推荐，免费试用）

```text
1. 打开 n8n.io，点击 "Get started for free"
2. 用邮箱或Google注册
3. 登录后你会看到一个空白的画布——这就是你的自动化工作台
```

云版免费额度约50次执行/月，适合测试和入门。

### 方式B：自部署（OPC推荐，完全免费不限量）

```text
# 用Docker一键安装（最简单）
docker run -it --rm \
  --name n8n \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  n8nio/n8n

# 安装完成后，浏览器打开 http://localhost:5678
```

**三种安装方式对比**：

| 方式 | 难度 | 月费 | 适用场景 |
|------|:----:|:----:|---------|
| 云版免费 | ★☆☆ | $0 | 试用、学习 |
| 云版付费 | ★☆☆ | $20起 | 不想折腾服务器 |
| Docker自部署 | ★★☆ | $0 | 生产环境、数据隐私敏感 |

### 2.3 界面速览

安装完成后，你看到的是n8n的主界面：

```text
┌─────────────────────────────────────────────────┐
│ 左侧面板：可用节点列表    │ 中间：画布（搭建流程）│
│    ─ 触发器（Trigger）   │                      │
│    ─ 动作（Action）      │  节点1 → 节点2 → 节点3│
│    ─ AI节点             │                      │
│    ─ 自定义代码          │                      │
├─────────────────────────┴───────────────────────┤
│ 底部：执行日志、输出预览、调试信息                │
└─────────────────────────────────────────────────┘
```

---

## 三、核心概念与节点速查

### 3.1 核心概念

| 概念 | 解释 | 类比 |
|------|------|------|
| **工作流（Workflow）** | 一个完整的自动化流程 | 像一条流水线 |
| **节点（Node）** | 流程中的每一步操作 | 流水线上的一个人 |
| **触发器（Trigger）** | 启动流程的事件 | 按下开关 |
| **连接（Connection）** | 节点之间的数据传递方向 | 传送带 |
| **执行（Execution）** | 工作流实际运行一次 | 生产一件产品 |

### 3.2 必知节点

| 节点类型 | 节点名 | 用途 | 首次使用频率 |
|---------|--------|------|:-----------:|
| **触发器** | Schedule Trigger | 定时执行（每天/每周/每月） | ⭐⭐⭐⭐⭐ |
| **触发器** | Webhook | 外部事件触发（收到数据时启动） | ⭐⭐⭐⭐ |
| **触发器** | Manual Trigger | 手动点击执行（测试用） | ⭐⭐⭐⭐⭐ |
| **动作** | HTTP Request | 调用任意API | ⭐⭐⭐⭐⭐ |
| **动作** | OpenAI / Claude | 调用AI模型 | ⭐⭐⭐⭐ |
| **动作** | Google Sheets | 读写Google表格 | ⭐⭐⭐⭐ |
| **动作** | Email (IMAP/SMTP) | 收发邮件 | ⭐⭐⭐ |
| **动作** | Telegram / Slack | 发消息通知 | ⭐⭐⭐⭐ |
| **数据** | Code (JS/Python) | 自定义数据处理 | ⭐⭐⭐⭐ |
| **数据** | Switch / Filter | 条件分支、数据筛选 | ⭐⭐⭐ |
| **数据** | Merge / Split | 合并/拆分数据集 | ⭐⭐⭐ |
| **AI** | AI Agent | 构建智能Agent | ⭐⭐⭐⭐ |

---

## 四、正确使用姿势（精华）

### 4.1 新手第一条工作流：定时发早安

这是最简单的入门工作流，5分钟就能搭好：

```text
步骤：
1. 拖一个 Schedule Trigger 到画布
   → 设置：每天 09:00 执行

2. 连接一个 Code 节点
   → 输入JS代码生成今日祝福语
   → 内容：`"早安！今天是" + new Date().toLocaleDateString()`

3. 连接一个 Telegram 节点
   → 把上一步生成的文字发到你的Telegram

4. 点击「Execute Workflow」测试
5. 测试通过后点击「Publish」
```

### 4.2 设计工作流的关键原则

**1. 从触发器开始思考**

每一条工作流都始于一个问题："什么事件触发这个流程？"

| 触发场景 | 对应触发器 |
|---------|-----------|
| 每天固定时间执行 | Schedule Trigger |
| 收到新邮件时 | Email Trigger (IMAP) |
| 别人调用你的接口时 | Webhook |
| 数据库中新增记录时 | 数据库 Trigger |
| 手动需要时 | Manual Trigger |

**2. 小步验证，不要一次搭完**

```text
错误做法：一口气搭10个节点再测试
正确做法：每搭1-2个节点就点一下「Execute Node」测试当前步骤
```

**3. 善用4000+社区模板**

在n8n中点击「Templates」→ 搜索你需要的场景 → 一键导入 → 修改参数即可。

热门模板：
- "AI客服机器人" → 自动回复客户问答
- "日报生成器" → 汇总当日数据生成日报
- "RSS监控" → 监控竞品动态并通知
- "数据同步" → 两个系统之间自动同步数据

### 4.3 用n8n AI Assistant搭建工作流

2026年n8n内置了AI Assistant，你只需要用自然语言描述需求，它自动帮你生成工作流：

```text
在n8n中输入：
"每天早上9点抓取Hacker News首页，
用AI总结成3条关键动态，
发到我的Telegram"

AI Assistant会自动生成：
Schedule Trigger → HTTP Request(HN API) → OpenAI(总结) → Telegram
```

---

## 五、实战场景（含完整配置）

### 场景1：竞品监控 + AI日报（OPC最实用）

每天自动监控竞品动态，用AI总结后发到你微信/Telegram。

**工作流结构**：
```text
Schedule Trigger (每天09:00)
  → HTTP Request (抓取竞品RSS/API)
  → Code (提取标题和链接)
  → OpenAI (总结关键动态)
  → Telegram / 微信 (发通知)
```

**各节点配置**：

**节点1：Schedule Trigger**
```text
触发规则：每天 09:00
时段：周一到周五
```

**节点2：HTTP Request（抓取竞品RSS）**
```text
Method: GET
URL: https://example-competitor.com/rss
Response Format: JSON / XML（按实际调整）
```

**节点3：Code（提取数据）**
```javascript
// 从RSS中提取标题和链接
const items = $input.first().json;
return items.map(item => ({
  title: item.title,
  link: item.link,
  summary: item.description?.substring(0, 200)
}));
```

**节点4：OpenAI（AI总结）**
```text
Model: GPT-4o-mini（性价比高）
Prompt: "以下是今天竞品动态，请用中文总结3条最关键的信息"
Input: 上一步输出的标题列表
```

**节点5：Telegram（发送到我）**
```text
Chat ID: 你的Telegram ID
Message: 上一步AI生成的总结
```

---

### 场景2：自动回复客户邮件（OPC省时间利器）

客户发邮件来咨询，AI自动回复，只有AI处理不了时才转人工。

**工作流结构**：
```text
Email Trigger (收到新邮件)
  → AI Agent (理解邮件内容)
    → 如果是简单问题 → AI生成回复 → 自动发送
    → 如果是复杂问题 → 转发到你的邮箱
  → 记录到Google Sheets（留档）
```

**AI Agent配置**：
```text
System Prompt: "
你是一个OPC的AI客服助理。
- 如果你能明确回答客户的问题，直接生成回复邮件
- 如果问题需要创始人亲自处理，回复客户'已转交相关负责人，将在24小时内回复'
- 判断标准：涉及价格、排期、合作方式等标准问题可以直接回复
- 涉及定制开发、合同条款等需要转交人工

回复语言：和客户来信语言一致
"
Model: GPT-4o-mini（成本敏感用这个）
Temperature: 0.3（越低越保守）
```

> 这个工作流可以帮OPC省下每天30-60分钟的回邮件时间。

---

### 场景3：自动整理微信读书/公众号文章到知识库

让n8n自动把你收藏的文章抓取下来，用AI提炼摘要，存到数据库。

**工作流结构**：
```text
Schedule Trigger (每天20:00)
  → HTTP Request (抓取你的微信读书标注)
  → Code (提取文章URL和标题)
  → HTTP Request (逐个抓取文章正文)
  → OpenAI (生成300字摘要)
  → Google Sheets (存入表格)
  → Telegram (通知今日整理完成)
```

**为什么这个场景对OPC有价值**：
```text
手动做：每天看到好文章→复制链接→手动写笔记→存起来
自动做：n8n自动抓取→AI摘要→自动入库→只需每周review一次
```

---

### 场景4：自动监控网站变化并通知

如果你需要监控某个网站（如竞品价格、政策更新、工作机会等），n8n可以自动对比变化。

**工作流结构**：
```text
Schedule Trigger (每小时)
  → HTTP Request (抓取目标网页)
  → Code (对比上一次抓取的内容)
  → 如果内容有变化 → Telegram通知
  → 把新内容存起来（供下次对比）
```

**Code节点的变化检测逻辑**：
```javascript
// 简化版：检测页面内容是否变化
const oldContent = $input.first().json.previousContent || '';
const newContent = $input.first().json.currentContent;
const hash = require('crypto')
  .createHash('md5')
  .update(newContent)
  .digest('hex');

// 如果MD5不一样，说明有变化
if (hash !== oldHash) {
  return { changed: true, content: newContent };
}
return { changed: false };
```

---

## 六、常见错误与避坑

### 五个新手必犯的错误

| # | 错误 | 正确做法 |
|:-:|------|---------|
| 1 | 一次搭10个节点再测试 | 每加1-2个节点就执行一次测试 |
| 2 | 不设错误处理 | 加一个「Error Trigger」捕获失败时通知自己 |
| 3 | API密钥写死在节点里 | 用n8n的Credentials管理，加密存储 |
| 4 | 自部署不设访问密码 | `docker run`时加 `-e N8N_ENCRYPTION_KEY` |
| 5 | 定时任务设太频繁 | 按实际需要设，别每1分钟跑一次 |

### 安全提醒

```text
1. 自部署时确保n8n的接口不暴露在公网
2. API密钥用n8n的Credentials系统管理，不要硬编码
3. 涉及财务数据的工作流要加人工确认环节
4. 定期检查工作流的执行日志，发现异常立即停止
```

---

## 七、OPC实战建议

### 建议优先搭建的3条工作流

| 优先级 | 工作流 | 每天节省时间 |
|:------:|--------|:-----------:|
| 1 | 竞品监控+AI日报 | 30分钟 |
| 2 | AI客服自动回复邮件 | 30-60分钟 |
| 3 | 日报/周报自动生成 | 15-30分钟 |

### n8n + 其他工具的组合

```text
n8n + OpenClaw/Hermes = AI Agent集群自动处理复杂任务
n8n + ima = 自动采集数据 → 存入知识库
n8n + Telegram = 随时随地接收通知和指令
n8n + Google Sheets = 轻量级CRM/项目管理系统
n8n + Supabase = 数据自动收集和分析
```

### 每日自动化全景

```text
07:00  n8n抓取昨天销售数据 → AI分析 → 发到微信
09:00  n8n监控竞品动态 → AI对比 → 如有更新发通知
10:00  客户邮件到 → AI自动回复（复杂转人工）
20:00  n8n整理今日收藏文章 → AI摘要 → 存入知识库
22:00  n8n生成今日工作日志 → 存档
```

---

## 参考链接

- 官网：n8n.io
- 社区模板：n8n.io/workflows（4000+）
- 官方文档：docs.n8n.io
- 社区论坛：community.n8n.io
- GitHub：github.com/n8n-io/n8n（67K+ Stars）
- Docker部署指南：docs.n8n.io/hosting/installation/docker/
