# -*- coding: utf-8 -*-
"""
OPC成长之路 · AI知识工作者学习资源中心 —— 站点生成器
运行: python3 build_site.py
输出: 同目录下 index/methods/tools/practices/courses.html
数据更新：改下方 DATA 区即可，无需动模板。
"""
import os, shutil, json

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE_NAME = "OPC成长之路 · AI知识工作者学习资源中心"
TAGLINE = "一个人运行一个硅基团队"

NAV = [
    ("index.html",    "首页"),
    ("playbook.html", "现场跟练"),
    ("methods.html",  "高效工作法"),
    ("tools.html",    "AI工具库"),
    ("practices.html","最佳实践"),
    ("courses.html",  "课程与行动"),
]

# ============================================================
# DATA
# ============================================================

LEVELS = [
    dict(no="L0", color="#b85a30", name="认知觉醒", desc="为什么 AI 时代人人都是 OPC？三大能力、工具链五层、碳硅共生——建立完整认知地图，找到你的起点。",
         tags=["概念卡","三大能力","工具链五层","碳硅共生"], link="methods.html", goal="找到你的基线"),
    dict(no="L1", color="#2563eb", name="方法掌握", desc="八大知识工作者高效工作法：深度研究、AI写作、第二大脑、会议效率、文档处理、数据分析、自动化、Agent构建。",
         tags=["8大工作流","最佳实践","人机分工"], link="methods.html", goal="掌握核心方法"),
    dict(no="L2", color="#00aa55", name="工具驾驭", desc="按场景分类的 AI 工具库：国内外双维度、定位、优势、定价一表尽览，附新人入门/出海/自动化选型组合。",
         tags=["工具地图","国内外双维度","选型组合"], link="tools.html", goal="选对你的工具"),
    dict(no="L3", color="#7c3aed", name="实践深化", desc="2026 高 ROI 场景、人机协作回路、真实性铁律、保姆级教程与可复制提示词模板——把方法变成肌肉记忆。",
         tags=["高ROI场景","回路六要素","保姆级教程","提示词模板"], link="practices.html", goal="从会用到用好"),
    dict(no="L4", color="#0d2818", name="行动变现", desc="从一天觉醒到一月启航：OPC 课程三档、30 天路线图、同行者社群——把能力变成产品，把产品变成收入。",
         tags=["课程三档","30天路线图","社群"], link="courses.html", goal="把能力变成收入"),
]

ABILITIES = [
    dict(icon="🚀", name="AI 驾驭力", desc="沿工具链逐级升级：提示词 → 智能体 → 技能 → 知识库 → 多智能体编排。你的角色从提问者一路演化为 Orchestrator。"),
    dict(icon="🌉", name="碳硅翻译力", desc="人类意图 → AI 指令 + AI 产出 → 人类价值的双向翻译。说得清、接得住，是 AI 时代最稀缺的元技能。"),
    dict(icon="🧭", name="意义创造力", desc="定义「什么值得做」「做到多好算好」「释放的时间用来创造什么」。AI 负责效率，你负责方向。"),
]

LADDER = [
    ("提示词", "提问者", "把需求说清楚，AI 单次回答"),
    ("智能体", "管理者", "AI 自主规划并执行多步骤任务"),
    ("技能", "沉淀者", "把成功做法固化为可复用技能"),
    ("知识库", "策展人", "给 AI 动态上下文，越用越懂你"),
    ("多智能体编排", "Orchestrator", "多个 AI 协作，你只做决策"),
]

METHODS = [
    dict(icon="🔬", name="深度研究法", tagline="多源搜索 → 信源验证 → 交叉确认 → 结构化输出",
         steps=["用 Perplexity / Gemini Notebook 做多源检索，形成研究骨架",
                "回到原文：至少 2 家独立信源交叉验证，数字逐字对照原文",
                "把验证后的内容沉淀进知识库，标注信源与日期",
                "结构化输出：框架化、带引用、可复用"],
         tools="Perplexity.ai · Gemini Notebook（原 NotebookLM）· 原文/官方文档",
         tip="铁律：NotebookLM / LLM 摘要只作选题线索，绝不直接作为信源。",
         skill="研究简报技能：多源检索 → 信源验证 → 结构化简报（带引用+标注日期）",
         tools_ext="Perplexity（检索入口）→ Gemini Notebook（深度研究）→ 研究知识库（沉淀）",
         expand="进阶：研究流程固化为技能 → 接入知识库 → 升级为「自动研究Agent」：触发→检索→验证→简报→自动入库"),
    dict(icon="✍️", name="AI 协作写作法", tagline="人机共创 → 多智能体审阅 → 迭代打磨",
         steps=["人定框架与立场，AI 出第一稿素材",
                "多智能体并行审阅（创意/读者/编辑三视角），输出原始反馈",
                "你对照反馈逐条修订——AI 不替你决定，替你放大判断",
                "事实核查 + 风格统一后定稿"],
         tools="Claude · ChatGPT · 多智能体审阅工作流 · 公众号爆款结构",
         tip="人机协同写作的正确姿势：AI 负责速度，你负责标准。",
         skill="写作风格技能：人设+语气+禁语+结构模板，一次定义反复调用",
         tools_ext="Claude（主写）→ 多智能体审阅（创意/读者/编辑）→ 发布管道（公众号/星球）",
         expand="进阶：风格技能+知识库=「你的内容工厂」→ 多智能体评审闭环 → 定时自动生产+人工把关"),
    dict(icon="🧠", name="第二大脑法", tagline="输入低摩擦 → 核心 AI 内化 → 输出最短路径",
         steps=["输入：信息自动流入（RSS/订阅/同步），降低采集摩擦",
                "核心：Obsidian/IMA 连接知识，AI 加速内化（问答/摘要/提炼）",
                "输出：从笔记到成品距离越短越好——笔记即草稿",
                "定期巡检：清理孤岛笔记、死链接、观点矛盾"],
         tools="Obsidian · IMA · Gemini Notebook · 飞书知识库",
         tip="知识工作流三层架构：输入降摩擦，核心用 AI 连接，输出走最短路径。",
         skill="笔记整理技能：自动分类+要点提炼+双向链接，让知识自动长成网",
         tools_ext="Obsidian（存储）→ IMA（AI问答）→ Gemini Notebook（研究）→ RSS 同步（输入）",
         expand="进阶：笔记自动流入→AI提炼→定期巡检（孤岛/死链/矛盾）→ 知识库成为你的数字分身"),
    dict(icon="🎙️", name="会议效率法", tagline="自动纪要 → 待办提取 → 摘要分发",
         steps=["AI 自动转录并生成会议纪要（飞书妙记等）",
                "自动提取待办事项与负责人，同步到任务系统",
                "生成「与我相关」的个性化摘要，而不是全文转发",
                "会前用 AI 聚合资料，会中只做判断"],
         tools="飞书妙记 · Lindy（AI 行政助理）· 通义听悟类工具",
         tip="会议的最高产出不是纪要，是决策与待办——让 AI 承担记录，人承担判断。",
         skill="会议纪要技能：转录→纪要→待办提取→定向分发",
         tools_ext="飞书妙记（转录）→ Lindy（行政自动化）→ 任务系统同步 → 日历聚合",
         expand="进阶：纪要→待办自动同步任务系统 → 会前AI聚合资料 → 会议只做判断"),
    dict(icon="📄", name="文档处理法", tagline="2026 知识工作者 ROI 最高的场景",
         steps=["合同/协议审查：AI 提取条款、标出风险点",
                "发票/单据提取：结构化数据自动入库",
                "报告生成：数据入 → 结构化报告出",
                "人只做最后签字确认与判断"],
         tools="Claude/GPT 类模型 · 文档解析工具 · n8n 流水线",
         tip="文档处理、报告生成是 2026 年回报最清晰的知识工作 AI 应用。",
         skill="文档审查技能：条款提取+风险标注+修改建议（一页纸摘要）",
         tools_ext="Claude/GPT（审查）→ 文档解析工具 → n8n（流水线）→ 文档知识库",
         expand="进阶：合同/发票/报告流水线自动化 → 异常标记人复核 → 覆盖全类型文档"),
    dict(icon="📊", name="数据分析法", tagline="报表自动化 → 财务自动化 → 决策支持",
         steps=["数据接入：表格/数据库/API 自动同步",
                "AI 生成周报月报：结构固定、数据自动填充",
                "异常检测：AI 标记偏离，人只看异常",
                "沉淀指标体系，越用越准"],
         tools="飞书多维表格 · n8n · AI 报表工具 · Excel/Python 脚本",
         tip="先固定报表结构，再接入自动化——AI 填数，人看异常与方向。",
         skill="周报生成技能：数据接入→结构固定→异常标记→决策摘要",
         tools_ext="飞书多维表格（数据）→ n8n（自动同步）→ AI 报表 → 仪表盘",
         expand="进阶：报表结构固化→数据自动填充→异常检测→决策支持仪表盘"),
    dict(icon="⚙️", name="自动化法", tagline="识别重复 → 搭建工作流 → 无人值守",
         steps=["盘点：列出每周重复 3 次以上的操作",
                "从低代码开始：飞书多维表格 / Zapier 搭建第一条流水线",
                "升级到 n8n：自部署、无限量、4000+ 社区模板",
                "加上 AI 步骤：让自动化拥有判断能力"],
         tools="n8n · Make · Zapier · 飞书多维表格自动化 · Pipedream",
         tip="自动化三剑客：n8n（无限量）+ Claude Code（复杂任务）+ 营销/行政 AI。",
         skill="流程自动化技能：触发条件+执行步骤+异常处理+运行日志",
         tools_ext="飞书多维表格（零门槛）→ Zapier（快速连接）→ n8n（无限量/自部署）",
         expand="进阶：加AI节点让流水线有判断 → 多流程编排 → 无人值守业务"),
    dict(icon="🤖", name="Agent 构建法", tagline="2026 最值钱技能：管理 AI 智能体",
         steps=["从提示词固化开始：跑通的流程沉淀为技能",
                "构建单 Agent：明确职责、输入输出、不做清单",
                "接知识库：给 Agent 动态上下文",
                "多智能体编排：分工协作，人做仲裁与决策"],
         tools="Coze（扣子）· Dify · Claude Code · n8n · 自建编排",
         tip="工具链爬得高不是目的，组装成「自闭环回路」才是。每天问：今天哪件事能再往上爬一层？",
         skill="Agent定义技能：职责边界+输入输出+不做清单+验收标准",
         tools_ext="Coze（快速Bot）→ Dify（深度定制）→ Claude Code（复杂任务）→ 自建编排（Hermes等）",
         expand="进阶：单Agent→技能固化→知识库接入→多智能体编排→你成为 Orchestrator"),
]

TOOL_CATS = [
    dict(name="💬 AI 对话与写作", note="通用大模型，知识工作者的第一块敲门砖",
         tools=[
            ("Claude", "intl", "深度写作、长文推理、代码能力强，Agent 生态领先", "写作/研究/编程主力", "订阅制"),
            ("ChatGPT", "intl", "生态最完整，多模态、插件、记忆", "通用助手/日常问答", "免费+订阅"),
            ("DeepSeek", "cn", "性价比之王，推理强、开源", "中文场景/成本敏感", "低价 API"),
            ("Kimi", "cn", "长文本处理出色，多模态", "长文档阅读/研究", "免费+订阅"),
            ("Gemini", "intl", "谷歌生态整合，多模态原生", "搜索联动/多模态", "免费+订阅"),
         ]),
    dict(name="🔍 深度研究与检索", note="知识工作者的信源入口，必须多源交叉验证",
         tools=[
            ("Perplexity.ai", "intl", "AI 搜索引擎，实时联网、附引用", "技术调研/市场研究", "免费+Pro"),
            ("Gemini Notebook", "intl", "原 NotebookLM（2026.7 更名），基于你的源文件深度研究，生成播客/导图/PPT", "主题研究/课程备课", "免费"),
            ("Google/官方文档", "intl", "一手信源的终点站", "事实核查", "免费"),
            ("知乎/公众号/知识星球", "cn", "中文高质量实践内容", "中文实践参考", "免费+订阅"),
         ]),
    dict(name="🗂️ 知识库与笔记", note="第二大脑的地基：本地优先 + AI 内化",
         tools=[
            ("Obsidian", "intl-free", "本地 Markdown、图谱视图、插件生态", "个人知识管理主库", "免费"),
            ("IMA", "cn", "腾讯知识库，支持上传与 AI 问答", "知识库沉淀/问答", "免费"),
            ("Notion", "intl", "文档+数据库+Wiki+项目一体", "团队协作/项目管理", "$0-10/月"),
            ("飞书文档+知识库", "cn", "多维表格+文档+OKR 一体化，AI 赋能", "团队协作首选", "免费+企业版"),
            ("NotebookLM→Gemini Notebook", "intl-free", "基于源文件的研究型笔记", "研究助手", "免费"),
         ]),
    dict(name="🎙️ 会议与行政效率", note="让 AI 承担记录，人承担判断",
         tools=[
            ("飞书妙记", "cn", "会议自动转录+纪要+待办提取", "会议效率", "免费"),
            ("Lindy", "intl", "AI 行政助理：邮件/日程/纪要自动处理", "行政自动化", "订阅制"),
            ("Motion", "intl", "AI 日程+任务管理，自动时间块排期", "个人时间管理", "$29/月"),
            ("通义听悟", "cn", "音视频转写与摘要", "课程/会议转写", "免费额度"),
         ]),
    dict(name="💻 AI 编程与开发", note="Agentic IDE 时代：从代码补全到自主重构",
         tools=[
            ("Cursor", "intl", "Agentic IDE 标杆，多模型路由", "全栈开发主力 IDE", "$20/月"),
            ("Claude Code", "intl", "命令行 AI 智能体，复杂多步任务", "重构/复杂任务", "$20+API"),
            ("OpenAI Codex", "intl", "深度集成 GPT 生态，多文件编辑", "OpenAI 生态", "$20/月"),
            ("Trae", "cn", "字节出品，国内份额领先，Figma 转代码", "国内前端全栈首选", "$10/月"),
            ("Kimi Code", "cn", "多模态输入（截图→代码），Agent 自主规划", "强推理+视觉", "¥49-199/月"),
            ("GitHub Copilot", "intl", "VS Code 深度集成，份额大", "微软生态默认", "$10-19/月"),
            ("MarsCode", "cn-free", "云端 IDE，零配置启动", "轻量开发/原型", "免费"),
         ]),
    dict(name="⚡ 自动化与 AI 工作流", note="把重复劳动交给流水线",
         tools=[
            ("n8n", "open", "开源自动化之王，自部署无限量，4000+ 模板", "重度/隐私敏感", "自部署免费"),
            ("Make", "intl", "可视化自动化，场景编辑器强大", "运营日常自动化", "免费+订阅"),
            ("Zapier", "intl", "7000+ 集成，最简单", "非技术快速连接", "免费+订阅"),
            ("飞书多维表格自动化", "cn", "飞书生态内零成本自动化", "Ops/PM 首选", "免费"),
            ("Coze（扣子）", "cn", "AI Bot 构建平台，对接抖音/飞书", "Bot 开发", "免费+用量"),
            ("Dify", "open", "开源 LLM 应用搭建，可自部署", "深度定制", "开源免费"),
            ("百度秒哒/阿里Meoo", "cn", "零代码全栈应用生成", "快速验证想法", "按量"),
         ]),
    dict(name="🧩 多智能体编排", note="2026 最值钱技能：管理 AI 智能体",
         tools=[
            ("Claude Code 多 Agent", "intl", "规划/执行分离，子 Agent 并行工作", "复杂工程任务", "$20+API"),
            ("OpenAI Codex", "intl", "并行任务处理，桌面级集成", "批量任务", "$20/月"),
            ("自建编排（Hermes 等）", "open", "个人 AI 中控：技能/记忆/cron/多平台", "一人运行一个硅基团队", "自部署"),
            ("n8n AI Agent", "open", "工作流内嵌 Agent 节点", "业务自动化", "免费"),
            ("LangGraph", "open", "图状多 Agent 编排框架", "复杂状态流", "开源"),
         ]),
    dict(name="💳 变现与增长", note="OPC 的生存底线：把能力变成收入",
         tools=[
            ("Stripe", "intl", "全球收款标准 API", "出海 SaaS 收款", "2.9%+$0.30"),
            ("Lemon Squeezy", "intl", "OPC 友好 MoR，内置联盟营销", "独立开发者首选", "5%+$0.50"),
            ("Paddle", "intl", "企业级 MoR，自动税务合规", "B2B SaaS", "5%+$0.50"),
            ("万里汇 WorldFirst", "cn", "蚂蚁国际，出海收款提现", "收入回到国内", "0.5-1%"),
            ("Resend", "intl", "开发者邮件发送，送达率高", "产品邮件", "免费+用量"),
            ("Beehiiv", "intl", "Newsletter 一站式", "内容创作者", "免费+订阅"),
            ("Perplexity.ai", "intl", "市场调研信息源", "增长决策", "免费+Pro"),
         ]),
    dict(name="🏗️ 全栈基建（进阶）", note="能不自己写就不写，能不自己运维就不运维",
         tools=[
            ("Next.js", "open", "全栈 React 框架，生态最大", "Web 应用首选", "开源"),
            ("Astro", "open", "内容型站点，极致静态性能", "博客/文档", "开源"),
            ("shadcn/ui + Tailwind", "open", "行业标准 UI 方案", "前端组件", "开源"),
            ("Supabase", "open", "开源 Firebase 替代", "后端即服务", "免费+用量"),
            ("Vercel", "intl", "零配置 CI/CD 部署", "前端部署", "免费+用量"),
            ("Cloudflare", "intl", "边缘计算，出海成本之王", "全球加速", "免费+用量"),
         ]),
]

PACKS = [
    dict(icon="🟢", name="新人入门三件套（国际版）", items=["Cursor — AI 编程主力 IDE", "Next.js + shadcn/ui + Tailwind — 全栈标配", "Vercel + Supabase — 零运维部署"]),
    dict(icon="🔵", name="新人入门三件套（国内版）", items=["Trae — AI 编程主力 IDE", "Next.js + shadcn/ui 或 飞书多维表格+小程序", "Vercel + 阿里云/腾讯云"]),
    dict(icon="🌊", name="出海必备五件套", items=["Stripe + Lemon Squeezy — 收款+税务合规", "Resend — 邮件发送", "Cloudflare — 部署/加速/边缘", "Supabase — 后端即服务", "Perplexity.ai — 市场调研"]),
    dict(icon="⚡", name="AI 自动化三剑客", items=["n8n — 工作流自动化（自部署无限量）", "Claude Code — 编程智能体（复杂任务）", "Lindy/NoimosAI — 行政/营销自动化"]),
]

PRACTICES = [
    dict(name="2026 知识工作者 AI 应用 ROI 排行榜", body="multi-source",
         content="""
<div class="rank-list">
  <div class="rank-item"><div class="rank-no"></div><div><h4>文档处理</h4><p>合同审查、发票提取、报告生成——回报最清晰、最易上手的场景</p></div></div>
  <div class="rank-item"><div class="rank-no"></div><div><h4>研究综合与竞争情报</h4><p>多源资料聚合、要点提炼、竞品动态追踪</p></div></div>
  <div class="rank-item"><div class="rank-no"></div><div><h4>财务报告自动化</h4><p>数据入、报告出，分析师效率提升显著</p></div></div>
  <div class="rank-item"><div class="rank-no"></div><div><h4>代码辅助</h4><p>从补全到 Agent 自主执行，工程师生产力倍增</p></div></div>
  <div class="rank-item"><div class="rank-no"></div><div><h4>会议摘要</h4><p>自动纪要+待办提取，会议效率质变</p></div></div>
</div>
<div class="note-box">📌 <b>最强收益角色</b>：研究分析师、财务分析师、律师/法务、软件工程师、运营与策略岗（高文档量岗位）。<br>📌 <b>趋势信号</b>：2026 最值钱技能 = 「管理 AI 智能体」——你不是被 AI 替代，是被会用 AI 的人替代。</div>
"""),
    dict(name="人机协作回路六要素", body="multiline",
         content="""
<p>AI 时代的工作单元不是「单个任务」，而是「自闭环回路」：</p>
<ul>
  <li><b>① 输入</b>（触发条件） → <b>② 碳硅分工</b>（AI 覆盖 vs 人判断） → <b>③ 执行/处理</b> → <b>④ 输出</b>（交付物）</li>
  <li><b>⑤ 验证信号</b>（衡量回路健康度） → <b>⑥ 知识沉淀</b>（回路跑完留下什么可复用）</li>
</ul>
<p style="margin-top:10px;">验收标准要轻：AI 至少完成一个子步骤 + 有明确验证信号 + 沉淀了链路卡。工具链是零件，回路是总成——只攒零件不组装，永远开不了车。</p>
"""),
    dict(name="碳硅分工原则", body="multiline",
         content="""
<ul>
  <li><b>AI 覆盖</b>：信息检索、初稿生成、格式转换、重复劳动、规模化处理</li>
  <li><b>人判断</b>：定义「什么值得做」、设定质量标准、最终决策、关系与信任</li>
  <li><b>提问者 → 管理者 → 沉淀者 → 策展人 → Orchestrator</b>：你的角色由工具链高度决定</li>
  <li>每天问自己一句话：<b>我今天的哪一件事，可以再往工具链上爬一层？</b></li>
</ul>
"""),
    dict(name="真实性铁律（血的教训）", body="multiline",
         content="""
<ul>
  <li>绝对禁止编造/虚构信息交付——<b>没验证 = 不存在</b></li>
  <li>所有网络来源必须<b>多方验证</b>：至少 2 家独立媒体交叉确认才能写入</li>
  <li>LLM/NotebookLM 摘要仅作选题线索，<b>禁止作为信源</b></li>
  <li>数字、岗位名称、时间线必逐字对照原文</li>
  <li>检验三问：独立信源数 ≥2？读过原文？数字逐字对照？</li>
</ul>
"""),
    dict(name="可复用提示词模板", body="multiline",
         content="""
<p style="margin-bottom:8px;">以下模板直接复制可用：</p>
<div class="prompt-box"><span class="plabel">🔬 深度研究</span>请对「{主题}」做系统性研究。要求：1) 找出至少3个独立信源，2) 每个关键数字标注出处并给出原文链接，3) 输出带引用的结构化报告，4) 明确区分「已验证事实」和「待确认信息」。</div>
<div class="prompt-box"><span class="plabel">✍️ 写作初稿</span>你是资深商业写作者。基于以下素材/要点，写一篇面向{读者}的{体裁}，要求：HBR 级分析深度、开头用场景钩子、每段一个论点、结尾给出行动建议。素材：{粘贴}</div>
<div class="prompt-box"><span class="plabel">📄 文档审查</span>审查这份{合同/报告}：1) 提取关键条款，2) 标出风险点与对我方不利的表述，3) 给出修改建议，4) 输出一页纸摘要。全文：{粘贴}</div>
<div class="prompt-box"><span class="plabel">⚙️ 流程固化</span>把以下操作步骤固化为一个可复用技能：任务描述、输入格式、执行步骤、输出格式、验收标准、常见错误。步骤：{粘贴}</div>
"""),
    dict(name="保姆级教程（本站资源）", body="multiline",
         content="""
<p>面向终端用户的零基础上手教程，全部来自 OPC 研究工厂实战沉淀：</p>
<ul>
  <li>📘 <a href="resources/guides/ClaudeCode教程-保姆级上手指南.md">Claude Code 保姆级上手指南</a> —— 住在终端里的程序员</li>
  <li>📘 <a href="resources/guides/Codex教程-保姆级上手指南.md">OpenAI Codex 保姆级上手指南</a></li>
  <li>📘 <a href="resources/guides/n8n教程-保姆级上手指南.md">n8n 保姆级上手指南</a> —— 开源自动化之王</li>
  <li>📘 <a href="resources/guides/ima教程-保姆级上手指南.md">IMA 保姆级上手指南</a> —— 个人知识库</li>
  <li>📘 <a href="resources/guides/WorkBuddy教程-保姆级上手指南.md">WorkBuddy 保姆级上手指南</a></li>
  <li>🗺️ <a href="resources/OPC独立开发者全栈工具地图2026-完整版.md">OPC 独立开发者全栈工具地图 2026（完整版）</a></li>
</ul>
"""),
]

COURSES = [
    dict(phase="PHASE 01 · 认知", name="1 天觉醒营", sub="从「知道 AI」到「看清自己」", price="¥399–4999",
         hot=False, items=["三大能力定位：AI驾驭力·碳硅翻译力·意义创造力", "工具链五层自诊，找到你的基线", "一个自闭环回路：跑通一条 AI 执行", "带走：个人定位卡 + 回路设计 + 30 天路线图"]),
    dict(phase="PHASE 02 · 落地", name="1 周实战营", sub="从「看清自己」到「跑通回路」", price="¥2999–5999",
         hot=True, items=["3 条核心回路深度打磨，全部跑通", "2 个可复用技能固化入库", "知识库搭建：给 AI 动态上下文", "每天验收信号 + 助教反馈", "带走：技能包 + 知识库 + 验证报告"]),
    dict(phase="PHASE 03 · 启航", name="1 月启航营", sub="从「跑通回路」到「项目启航」", price="¥8999–19999",
         hot=False, items=["真实项目原型从 0 到 1", "多智能体编排落地：你的硅基团队", "变现路径设计：把能力变成收入", "H 博士 × 何义情 双导师陪跑", "带走：可交付的项目原型 + 商业路径"]),
]

ROADMAP = [
    ("第 1 周", "觉醒", "完成工具链自诊，选定一个核心场景，跑通第一条 AI 执行"),
    ("第 2 周", "固化", "把成功流程沉淀为技能，建起个人知识库雏形"),
    ("第 3 周", "组装", "技能+知识库组装成自闭环回路，设定验证信号"),
    ("第 4 周", "放大", "回路稳定运行，开始输出作品/内容，进入同行者社群"),
]

# ============================================================
# TEMPLATE
# ============================================================

def shell(title, active, hero, body, extra_css=""):
    nav_links = ""
    for href, label in NAV:
        cls = "active" if href == active else ""
        nav_links += f'<a href="{href}" class="{cls}">{label}</a>'
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} · {SITE_NAME}</title>
<meta name="description" content="AI 知识工作者一站式学习资源中心：高效工作法、AI 工具库、最佳实践、OPC 课程。一个人运行一个硅基团队。">
<link rel="stylesheet" href="css/style.css">
{extra_css}
</head>
<body>
<nav class="nav">
  <div class="container nav-inner">
    <a class="brand" href="index.html"><span class="logo">OPC</span><span>{SITE_NAME.split('·')[0].strip()}学习中心</span></a>
    <div class="search-wrap"><input id="site-search" class="site-search" type="search" placeholder="搜索方法/工具/实践..." aria-label="站内搜索"></div>
    <button class="nav-menu-toggle" aria-label="菜单" onclick="document.querySelector('.nav-links').classList.toggle('mobile-open')">☰ 菜单</button>
    <div class="nav-links">{nav_links}<a class="nav-cta" href="courses.html">立即报名</a></div>
  </div>
</nav>
{hero}
{body}
<footer>
  <div class="container">
    <div class="footer-grid">
      <div>
        <h4>{SITE_NAME}</h4>
        <p style="color:#a8b5ac;font-size:0.85rem;">{TAGLINE}。<br>碳硅组织研习社旗下 OPC 子品牌「OPC成长之路」的常设学习资源中心。<br>认知到行动的最小闭环。</p>
      </div>
      <div>
        <h4>学习路径</h4>
        <a href="methods.html">高效工作法</a>
        <a href="tools.html">AI 工具库</a>
        <a href="practices.html">最佳实践</a>
        <a href="courses.html">课程与行动</a>
      </div>
      <div>
        <h4>找到我们</h4>
        <a href="courses.html">OPC 课程三档</a>
        <a href="#">公众号「OPC成长之路」</a>
        <a href="#">星球「OPC超级个体加速器」</a>
        <a href="#">公众号「进化型组织联盟」</a>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 碳硅组织研习社 · OPC成长之路</span>
      <span>本站内容均经多源交叉验证 · 更新日期 2026-08-19</span>
    </div>
  </div>
</footer>
<script src="js/search.js"></script>
</body>
</html>"""

def hero_block(eyebrow, h1, sub, btns):
    b = "".join(f'<a class="btn {k}" href="{href}">{t}</a>' for k, href, t in btns)
    return f"""<header class="hero">
  <div class="container">
    <span class="eyebrow">{eyebrow}</span>
    <h1>{h1}</h1>
    <p class="sub">{sub}</p>
    <div class="hero-btns">{b}</div>
  </div>
</header>"""

# ============================================================
# PAGES
# ============================================================

QUIZ = [
    dict(q="你现在怎么用 AI？",
         opts=[("偶尔问两句，当高级搜索引擎用", 0), ("让 AI 帮我写文档/做具体任务", 1),
               ("有自己的提示词模板反复用", 2), ("建了个人知识库喂给 AI", 3),
               ("多个 AI/Agent 协作跑流程", 4)]),
    dict(q="你每周重复最多的任务是什么？",
         opts=[("搜索资料、看文章，没沉淀", 0), ("写文档/报告/周报", 1),
               ("固定格式的内容生产", 2), ("整理资料/做研究", 3),
               ("跨系统数据搬运/流程运转", 4)]),
    dict(q="你的 AI 产出稳定吗？",
         opts=[("没概念，每次随缘", 0), ("能用，但每次要重新教", 1),
               ("有模板，输出比较稳定", 2), ("会用我的资料回答，较准", 3),
               ("有验收标准和回退机制", 4)]),
    dict(q="你对 AI 的期望是？",
         opts=[("先搞清楚它到底能干嘛", 0), ("帮我把活干完", 1),
               ("把重复活自动化", 2), ("成为我的第二大脑", 3),
               ("替我运营一个硅基团队", 4)]),
]

LEVEL_NAMES = ["认知觉醒", "方法掌握", "工具驾驭", "实践深化", "行动变现"]
LEVEL_HINTS = [
    "从 L0 开始：先建立认知地图，搞清三大能力与工具链五层。",
    "从 L1 开始：选与你工作重合度最高的 1-2 条工作法跑通。",
    "从 L2 开始：按场景配齐工具链，抄「选型组合」作业。",
    "从 L3 开始：用高 ROI 场景 + 回路方法论，把会用变成用好。",
    "从 L4 开始：直接进入行动变现，同时用案例反哺认知。",
]
LEVEL_LINKS = ["index.html#levels", "methods.html", "tools.html", "practices.html", "courses.html"]

def quiz_html():
    qs = ""
    for i, item in enumerate(QUIZ, 1):
        opts = ""
        for label, val in item["opts"]:
            opts += f'<label class="quiz-opt"><input type="radio" name="q{i}" value="{val}"><span>{label}</span></label>'
        qs += f'<div class="quiz-q"><h4>{i}. {item["q"]}</h4><div class="quiz-opts">{opts}</div></div>'
    names_js = json.dumps(LEVEL_NAMES, ensure_ascii=False)
    hints_js = json.dumps(LEVEL_HINTS, ensure_ascii=False)
    links_js = json.dumps(LEVEL_LINKS, ensure_ascii=False)
    return f"""
<div class="quiz" id="quiz">
  <div class="sec-head">
    <span class="sec-label">SELF-DIAGNOSIS · 60秒</span>
    <h2 class="sec-title">工具链自测：你现在在哪一层？</h2>
    <p class="sec-desc">回答 4 个问题，系统基于「工具链五层」模型定位你的基线，并推荐你的下一站——与 OPC 工作坊课前诊断同一套方法论。</p>
  </div>
  {qs}
  <div class="quiz-actions">
    <button class="btn" onclick="runQuiz()">🔍 测出我的层级</button>
  </div>
  <div id="quiz-result" class="quiz-result"></div>
</div>
<script>
var QUIZ_NAMES = {names_js};
var QUIZ_HINTS = {hints_js};
var QUIZ_LINKS = {links_js};
function runQuiz(){{
  var qs = document.querySelectorAll('.quiz-q');
  var scores = [0,0,0,0,0];
  for (var i = 0; i < qs.length; i++) {{
    var c = qs[i].querySelector('input:checked');
    if (!c) {{ alert('请完成第 ' + (i+1) + ' 题'); return; }}
    scores[parseInt(c.value,10)]++;
  }}
  var best = 0;
  for (var j = 1; j < 5; j++) {{ if (scores[j] > scores[best]) best = j; }}
  var el = document.getElementById('quiz-result');
  el.innerHTML = '<div class="qr-box"><div class="qr-lv">L' + best + ' · ' + QUIZ_NAMES[best] + '</div><p>' + QUIZ_HINTS[best] + '</p><a class="btn btn-sm" href="' + QUIZ_LINKS[best] + '">前往我的下一站 →</a></div>';
  el.scrollIntoView({{behavior:'smooth', block:'center'}});
}}
</script>"""

# ============================================================
# 现场跟练手册（playbook.html）— 素材全部源自 超级个体赋能营_一天流程_v6.0.md
# ============================================================

PLAYBOOK_CONCEPTS = [
    dict(icon="🔄", name="三个关键切换", desc="超级个体 ≠ 会用 AI 的人。真正改变工作方式的三切换：从「自己做」→「定义任务」；从「一次性的」→「可复用的」；从「一个人」→「一个组织」。"),
    dict(icon="🗺️", name="AI 工具地图", desc="三类工具：通用助手（ChatGPT/Claude）· 垂直智能体（研究/写作/编程/设计）· 个人工作台（Workbuddy/IMA/Obsidian）。今天只用两三种，但知道地图在哪。"),
    dict(icon="🔁", name="人机协作回路", desc="五节点：输入 → AI处理 → 你的判断 → AI执行 → 你验收。人的价值：给方向、做判断、验收结果；AI 负责执行。下午亲手把它建出来。"),
    dict(icon="🧱", name="四堵墙", desc="为什么装了 AI 效率反而下降：习惯墙（老方法做事）· 翻译墙（说不清要什么）· 信任墙（一次不好就不用）· 整合墙（散事没串成线）。认领你卡在哪堵，今天下午拆它。"),
    dict(icon="🚫", name="四条红线", desc="🔴数据红线：上传前必须脱敏 ｜ 🔴外发红线：发出去前必须经你眼看 ｜ 🔴判断红线：定价/承诺/法律 AI 只给建议你拍板 ｜ 🔴质量红线：最终交付质量你说了算。"),
    dict(icon="⚙️", name="Skill 是什么", desc="用自然语言描述、让智能体自动构建、可反复调用的能力模块。封装了经验+判断标准+输出格式。建完不用每次重写提示词——直接调用。不需要会编程。"),
    dict(icon="📚", name="知识库接入", desc="技能是「通用」的，知识库让它变成「你的」。在 IMA 上传你的材料（先求最小可用：3 份跑通即可），接入技能——AI 的输出开始像你。"),
    dict(icon="🏗️", name="项目原型", desc="技能 + 知识库 = 你的第一个 AI 工作系统。标准只有一条：让一个真实业务任务，从输入到输出，完整地跑一次。这就是你今天的作品。"),
]

PLAYBOOK_MODULES = [
    dict(no="00", time="08:30–09:00", name="到场准备", goal="账号就绪，站点眼熟",
         steps=["登录 Workbuddy + IMA（+可选 Obsidian），确认可用", "浏览学习站点，眼熟今天的知识卡片", "大屏循环播放 H 博士工作流展示"],
         prompt="", check="账号全部登录成功", fallback="",
         tools="Workbuddy + IMA + Obsidian（三件套）", skills="账号就绪检查（登录态确认清单）",
         expand="课前3天完成安装 → 现场省20分钟 → 余力先浏览站点各页"),
    dict(no="①", time="09:00–09:50", name="诊断 · 你的 AI 起点", goal="认领你的墙 + 写下承诺",
         steps=["看全班数据分布：你不是一个人", "认领四堵墙之一，贴名字到白板", "便利贴写：「今天结束后我最想做到的一件事是___」"],
         prompt="", check="完成认领 + 承诺便利贴", fallback="",
         tools="AI能力自测问卷 + 个人诊断报告", skills="基线诊断（四堵墙定位）",
         expand="四堵墙→下午拆墙策略：习惯墙靠定义任务·翻译墙靠澄清模板·信任墙靠验收标准·整合墙靠回路"),
    dict(no="②", time="09:50–10:25", name="认知 · 三大能力", goal="三切换 + 工具地图 + 回路",
         steps=["听三件事：三切换/工具地图/人机协作回路", "每讲完一件，翻站点对应知识卡片", "不用记笔记——站点就是你的笔记本"],
         prompt="", check="能向邻座讲出回路五节点", fallback="",
         tools="站点 8 张知识卡片", skills="知识卡片速读（概念→示例→自检）",
         expand="三切换→映射你的业务：哪个任务可以开始「定义任务」而不是自己做"),
    dict(no="③", time="10:40–10:55", name="案例演示 · 看见才相信", goal="看清一条真实回路",
         steps=["看何义情现场跑一条真实回路（15分钟）", "注意：AI 执行时人在哪个节点停下说「这里不对」", "记住一句话：人给方向、做判断、验收；AI 负责执行"],
         prompt="", check="能指出演示中的判断节点", fallback="",
         tools="案例演示回放 + 大屏", skills="回路拆解（识别判断节点）",
         expand="把演示中的判断节点→下午在自己回路里标出来"),
    dict(no="④", time="10:55–12:00", name="澄清意图 · 从模糊到可执行", goal="需求文档 + 回路草图",
         steps=["用下面模板和 AI 对话，挖清你的真实意图", "产出：结构化任务需求文档（给谁用/解决什么/交付什么/怎么算成功）", "画 A4 回路草图（输入→AI处理→你判断→AI执行→你验收），卡住处打问号", "邻座互检：对方能否一眼看懂你要做什么"],
         prompt="我有一个模糊的想法：___。请通过提问帮我把它澄清成一份结构化任务需求文档，必须包含：①给谁用 ②解决什么问题 ③最终交付什么 ④怎么算成功。先问我不清楚的地方，再输出文档。",
         check="需求文档四要素齐全 + 回路草图完成", fallback="",
         tools="Workbuddy 对话 + 需求文档模板", skills="意图澄清技能（四要素：给谁用/解决什么/交付什么/怎么算成功）",
         expand="需求文档→沉淀为你的可复用模板库 → 进阶：意图澄清→需求文档自动生成"),
    dict(no="⑤", time="13:30–14:15", name="人机分工 · 设计碳硅回路", goal="正式回路 + 四条红线",
         steps=["把草图画实：输入（材料哪来）/AI处理（提取分析生成什么）/你的判断（哪个节点拍板？标准？）/AI执行（什么格式模板）/你验收（怎么算合格）", "标出四条红线：数据/外发/判断/质量", "邻座互检：问「这个判断节点，真的需要你，还是可以交给 AI？」"],
         prompt="这是我要构建的人机协作回路，请帮我审查分工是否合理：输入=___，AI处理=___，我的判断=___，AI执行=___，我验收=___。请指出：哪些判断其实可以交给AI？哪些步骤缺少明确验收标准？",
         check="回路五格填实 + 四红线标注 + 教练🟢标记", fallback="",
         tools="A3 回路画布 + 四红线贴纸", skills="回路设计技能（五格+红线+验收信号）",
         expand="回路画实→下午⑥直接可建 → 进阶：判断节点能不能再交给 AI（人只留真判断）"),
    dict(no="⑥", time="14:15–15:30", name="构建技能 ★核心环节", goal="用自然语言打造专属 AI 能力",
         steps=["5分钟演示：H博士用自然语言让 Workbuddy 生成竞品分析技能", "基于意图+回路，用下面模板在 Workbuddy 构建你的 skill", "拿真实材料跑一次：跑通=AI 按你设计的逻辑处理、在该停的判断节点停下、输出符合格式", "没跑通→叫教练；15:00 仍失败→用兜底模板替换"],
         prompt="我需要一个帮我做___的技能。请先追问我几个关键问题（输入材料是什么？输出格式是什么？判断标准是什么？常见错误有哪些？），然后基于我的回答生成一个可调用的 skill。",
         check="真实材料跑通 + 拍照存档（验收标准：AI 给的结果你能用，或明确知道哪里要改）",
         fallback="🎯 兜底方案：3 个预置通用技能模板（内容生成类/信息整理类/客户响应类），选最接近的 5 分钟替换——没有人在这一步空手离开。",
         tools="Workbuddy（技能构建）+ 3 预置模板", skills="技能构建器（meta-skill：描述→追问→生成→验收）",
         expand="课后把常用场景都固化成技能 → 进阶：技能+知识库 → 技能市场/技能交换"),
    dict(no="⑦", time="15:45–16:15", name="接入知识库 · 让 AI 懂你", goal="技能 + 业务上下文",
         steps=["在 IMA 创建个人知识库，上传脱敏材料（至少3份跑通，先最小可用）", "在技能里配置知识库接入", "教练检查接入是否生效：技能调用时确实能读到知识库"],
         prompt="我上传了以下材料到知识库：___。请基于这些材料，调整我技能的输出风格和判断逻辑，使其符合我的业务背景。",
         check="技能调用时能读取知识库内容（教练确认）", fallback="",
         tools="IMA（知识库）+ 脱敏材料", skills="知识库接入技能（最小可用3份→检索调优）",
         expand="课后扩充到 10+ 份 → 进阶：知识库结构化（分类/标签/权限/版本）"),
    dict(no="⑧", time="16:15–16:50", name="项目原型 · 整合你的系统", goal="技能+知识库=可运行项目",
         steps=["在 Workbuddy 把技能+知识库整合成项目", "让一个真实业务任务从输入到输出完整跑一次", "保存、确认可调用，截图存档"],
         prompt="", check="项目已保存可调用 + 截图", fallback="",
         tools="Workbuddy（项目整合）", skills="项目组装技能（技能串联+知识库支撑+完整验收）",
         expand="单项目跑通 → 进阶：多项目/多技能编排 → 你的硅基团队雏形"),
    dict(no="⑨", time="16:50–17:10", name="展示 · 承诺", goal="1.5分钟路演 + 72小时承诺",
         steps=["每人1.5分钟：你做了什么/给谁用/今天跑通没有", "写 72 小时行动卡：72小时内用今天建的技能处理一件真实工作", "邻座签名做见证人，举卡合影"],
         prompt="", check="行动卡完成 + 见证人签名", fallback="",
         tools="路演卡 + 72小时行动卡", skills="作品路演（1.5分钟结构化表达：做了什么/给谁用/跑通没有）",
         expand="Day7 复盘诊所 → Day30 最佳作品评选 → 进阶：作品集沉淀为你的案例库"),
    dict(no="⑩", time="17:10–17:20", name="Check-out · 灵魂三问", goal="回望承诺，锚定意义",
         steps=["回看早上那张便利贴：你做到了吗？", "灵魂三问：省下来的时间，去做更多同样的事 / 去做以前做不到的事 / 去做一直想做但没时间做的事", "记住：你不再是一个人完成所有任务——你是在设计任务、分配任务、确认任务。你是一家公司。"],
         prompt="", check="合影 + 填反馈", fallback="",
         tools="反馈表 + 合影", skills="复盘技能（灵魂三问框架）",
         expand="30天路线图（觉醒→固化→组装→放大）→ 进阶：把回路变产品、把能力变收入"),
]

PLAYBOOK_SETUP = [
    dict(icon="⚡", name="Workbuddy（主平台）", desc="今天的主战场：构建技能、整合项目都在这里。课前3天按指南安装注册，现场需要登录态。"),
    dict(icon="📚", name="IMA（知识库）", desc="模块⑦使用：创建个人知识库，上传你的脱敏材料。先求最小可用——3份就能跑通。"),
    dict(icon="🗂️", name="Obsidian（可选）", desc="个人知识管理的持续记录本。今天把技能清单/回路画布/操作说明存进去，作为你个人AI系统的记录。没有也不影响。"),
    dict(icon="🔒", name="数据安全 · 脱敏", desc="不能传：客户资料/合同原文/医疗法律财务敏感数据/可识别身份信息。能传：脱敏后保留逻辑与结构的业务内容。做法：客户名换代号、联系方式删除、金额模糊化（约10万级）、敏感条款只留结构。不确定先问教练。"),
]

def page_playbook():
    concepts = ""
    for c in PLAYBOOK_CONCEPTS:
        concepts += f'<div class="card"><span class="c-icon">{c["icon"]}</span><h3>{c["name"]}</h3><p>{c["desc"]}</p></div>'

    mods = ""
    for m in PLAYBOOK_MODULES:
        steps = "".join(f'<li>{s}</li>' for s in m["steps"])
        prompt = f'<div class="prompt-box"><span class="plabel">📋 提示词模板（复制用）</span>{m["prompt"]}</div>' if m["prompt"] else ""
        fallback = f'<div class="note-box" style="border-left-color:#b85a30;">{m["fallback"]}</div>' if m["fallback"] else ""
        mods += f"""<div class="method" style="border-left-color:var(--l0);" id="mod-{m['no']}">
  <h3>{m['no']} {m['name']} <span class="tag" style="margin-left:8px;">{m['time']}</span></h3>
  <div class="m-tagline">🎯 {m['goal']}</div>
  <div class="m-steps" style="grid-template-columns:1fr;">{"".join(f'<div class="m-step"><span class="n">▸</span>{s}</div>' for s in m["steps"])}</div>
  {prompt}
  {fallback}
  <div class="m-ske">
    <span>🧰 工具：<b>{m['tools']}</b></span>
    <span>🛠️ 可构建技能：<b>{m['skills']}</b></span>
    <span>📈 拓展学习：<b>{m['expand']}</b></span>
  </div>
  <div class="m-foot"><span>✅ 验收标准：<b>{m['check']}</b></span></div>
</div>"""

    setup = ""
    for s in PLAYBOOK_SETUP:
        setup += f'<div class="card"><span class="c-icon">{s["icon"]}</span><h3>{s["name"]}</h3><p>{s["desc"]}</p></div>'

    hero = hero_block("现场跟练手册 · 超级个体赋能营 v6.0", "跟着课表走，<br><em>一步都不迷路</em>",
                      "全天 10 个模块的跟练导航：每步的知识卡片、提示词模板、操作动作、验收标准、兜底方案，全部在这一页。来源：赋能营一天流程 v6.0（何义情 × H博士）。",
                      [("", "从模块 00 开始", "#mod-00"), ("line", "先看知识卡片", "#concepts")])

    body = f"""
<section id="concepts">
  <div class="container">
    <div class="sec-head">
      <span class="sec-label">KNOWLEDGE CARDS</span>
      <h2 class="sec-title">8 张知识卡片</h2>
      <p class="sec-desc">模块②认知环节对照使用——讲完一张翻一张，不用记笔记。</p>
    </div>
    <div class="grid">{concepts}</div>
  </div>
</section>
<section>
  <div class="container">
    <div class="sec-head">
      <span class="sec-label">MODULE PLAYBOOK</span>
      <h2 class="sec-title">全天模块跟练</h2>
      <p class="sec-desc">按课表顺序排列。每步：做什么 → 提示词模板（可直接复制）→ 验收标准 → 兜底方案。</p>
    </div>
    {mods}
    <div class="note-box">🧭 <b>核心提醒</b>：工具链爬得高不是目的，组装成能跑的自闭环回路才是。跑通的标准：AI 给的结果你能用，或明确知道哪里要改。</div>
  </div>
</section>
<section class="dark-section">
  <div class="container">
    <div class="sec-head">
      <span class="sec-label">TOOL SETUP</span>
      <h2 class="sec-title">工具准备与数据安全</h2>
      <p class="sec-desc">课前3天装好三件套，现场直接进入状态。数据红线第一条：先脱敏，再上传。</p>
    </div>
    <div class="dark-cards">{setup}</div>
  </div>
</section>"""
    return shell("现场跟练", "playbook.html", hero, body)

def page_index():
    levels = ""
    for lv in LEVELS:
        tags = "".join(f'<span class="tag">{t}</span>' for t in lv["tags"])
        levels += f"""<div class="level">
  <div class="level-bar" style="background:{lv['color']}"></div>
  <div class="level-body">
    <div class="level-no" style="color:{lv['color']}">{lv['no']}</div>
    <div class="level-info">
      <h3>{lv['name']}</h3>
      <p>{lv['desc']}</p>
      <div class="level-tags">{tags}</div>
    </div>
    <div class="level-go"><a href="{lv['link']}">{lv['goal']} →</a></div>
  </div>
</div>"""

    ab = "".join(f"""<div class="fw"><span class="fw-num">{a['icon']}</span><h3>{a['name']}</h3><p>{a['desc']}</p></div>""" for a in ABILITIES)

    ladder = ""
    prev_role = None
    for name, role, desc in LADDER:
        arrow = '<span class="ladder-arrow">→</span>' if prev_role else ""
        ladder += f"""<div class="ladder-row">{arrow}<span class="l-name">{name}</span><span class="l-role">{role}</span><span class="l-desc">{desc}</span></div>"""
        prev_role = role

    cards = "".join(f"""<div class="card"><span class="c-icon">{c['icon']}</span><h3>{c['title']}</h3><p>{c['desc']}</p><a class="more" href="{c['link']}">进入 →</a></div>"""
                    for c in [
                        dict(icon="🔬", title="高效工作法", desc="8 大知识工作者工作流：深度研究、AI 写作、第二大脑、会议、文档、数据、自动化、Agent。", link="methods.html"),
                        dict(icon="🧰", title="AI 工具库", desc="9 大类 50+ 工具，国内外双维度、定位优势定价一表尽览，附选型组合。", link="tools.html"),
                        dict(icon="🏆", title="最佳实践", desc="2026 高 ROI 场景、人机协作回路、真实性铁律、保姆级教程与提示词模板。", link="practices.html"),
                        dict(icon="🚀", title="课程与行动", desc="1 天觉醒营 → 1 周实战营 → 1 月启航营，30 天路线图，把能力变成收入。", link="courses.html"),
                    ])

    hero = hero_block("碳硅组织研习社 · OPC成长之路", "AI 知识工作者<br><em>一站式学习资源中心</em>",
                      "一个人运行一个硅基团队。从认知觉醒到行动变现，渐进式五层路径，带你完成「认知到行动的最小闭环」。",
                      [("", "从 L0 开始我的路径", "#levels"), ("line", "浏览工具库", "tools.html")])

    body = f"""
<section id="quiz-sec">
  <div class="container">
    {quiz_html()}
  </div>
</section>

<section id="levels">
  <div class="container">
    <div class="sec-head">
      <span class="sec-label">PROGRESSIVE PATH</span>
      <h2 class="sec-title">渐进式学习路径</h2>
      <p class="sec-desc">不要求你学会所有 AI 工具——只需要从今天所在的那一层，往上走一层。站点按五层组织，任何入口进入都能找到自己的下一站。</p>
    </div>
    <div class="levels">{levels}</div>
  </div>
</section>

<section>
  <div class="container">
    <div class="sec-head">
      <span class="sec-label">THREE CAPABILITIES</span>
      <h2 class="sec-title">超级个体三大能力</h2>
      <p class="sec-desc">AI 时代的知识工作者，核心竞争力归结为三件事：驾驭 AI、翻译碳硅、创造意义。</p>
    </div>
    <div class="fw-strip">{ab}</div>
  </div>
</section>

<section class="dark-section">
  <div class="container">
    <div class="sec-head">
      <span class="sec-label">TOOLCHAIN LADDER</span>
      <h2 class="sec-title">工具链五层：你的角色由高度决定</h2>
      <p class="sec-desc">每往上爬一层，你作为人的角色就改变一次。从提问者到 Orchestrator——这不是工具的升级，是你的升级。</p>
    </div>
    <div class="ladder">{ladder}</div>
  </div>
</section>

<section>
  <div class="container">
    <div class="sec-head">
      <span class="sec-label">CONTENT MAP</span>
      <h2 class="sec-title">四大内容模块</h2>
      <p class="sec-desc">方法、工具、实践、行动——从知道到做到，一站式配齐。</p>
    </div>
    <div class="grid">{cards}</div>
  </div>
</section>

<section>
  <div class="container">
    <div class="cta">
      <h3>周日 · OPC 一天觉醒营</h3>
      <p>现场实时上演：从你的基线出发，往上爬一层。带走个人定位卡、一个自闭环回路、30 天路线图。</p>
      <a class="btn" href="courses.html">查看课程详情</a>
    </div>
  </div>
</section>"""
    return shell("首页", "index.html", hero, body)

def page_methods():
    ms = ""
    for m in METHODS:
        steps = ""
        for i, s in enumerate(m["steps"], 1):
            steps += f'<div class="m-step"><span class="n">{i}.</span>{s}</div>'
        ms += f"""<div class="method">
  <h3>{m['icon']} {m['name']}</h3>
  <div class="m-tagline">{m['tagline']}</div>
  <div class="m-steps">{steps}</div>
  <div class="m-ske">
    <span>🛠️ 核心技能：<b>{m['skill']}</b></span>
    <span>🧰 工具链：<b>{m['tools_ext']}</b></span>
    <span>📈 拓展学习：<b>{m['expand']}</b></span>
  </div>
  <div class="m-foot"><span>🧰 代表工具：<b>{m['tools']}</b></span><span>💡 {m['tip']}</span></div>
</div>"""

    hero = hero_block("LEARNING PATH · L1", "高效工作法：<br><em>八大知识工作者工作流</em>",
                      "2026 年知识工作者 AI 应用已形成清晰范式。按「研究 → 写作 → 知识 → 会议 → 文档 → 数据 → 自动化 → Agent」八条主线掌握，每条都是已验证的实战方法。",
                      [("", "选工具 →", "tools.html"), ("line", "看实践案例", "practices.html")])

    body = f"""
<section>
  <div class="container">
    <div class="sec-head">
      <span class="sec-label">METHODS · 8 WORKFLOWS</span>
      <h2 class="sec-title">八大工作法</h2>
      <p class="sec-desc">每个方法 = 核心步骤 + 代表工具 + 一句最佳实践。方法比工具重要：先掌握方法，工具只是方法的手。</p>
    </div>
    {ms}
    <div class="note-box">🧭 <b>方法论优先级</b>：先从与你工作重合度最高的 1-2 条入手，跑通后再扩展。贪多嚼不烂——渐进式升级的核心是「往上爬一层」。</div>
  </div>
</section>"""
    return shell("高效工作法", "methods.html", hero, body)

def page_tools():
    cats = ""
    for cat in TOOL_CATS:
        rows = ""
        for name, badge, desc, fit, price in cat["tools"]:
            bmap = dict(intl="badge-intl 国外", cn="badge-cn 国内", free="badge-free 免费", open="badge-open 开源",
                        intl_free="badge-intl 国外·免费", cn_free="badge-cn 国内·免费")
            b = f'<span class="badge {bmap[badge].split()[0]}">{bmap[badge].split()[1]}</span>' if badge in bmap else ""
            rows += f"""<tr><td class="tool-name">{name}{b}</td><td>{desc}</td><td>{fit}</td><td class="pricing">{price}</td></tr>"""
        cats += f"""<div class="toolcat">
  <div class="toolcat-head"><h3>{cat['name']}</h3><span class="note">{cat['note']}</span></div>
  <table class="tool-table">
    <thead><tr><th style="width:22%">工具</th><th style="width:42%">定位与优势</th><th>适合场景</th><th style="width:14%">定价</th></tr></thead>
    <tbody>{rows}</tbody>
  </table>
</div>"""

    packs = ""
    for p in PACKS:
        items = "".join(f"<li><b>{i.split(' — ')[0]}</b> — {i.split(' — ')[1] if ' — ' in i else ''}</li>" for i in p["items"])
        packs += f"""<div class="pack"><h3>{p['icon']} {p['name']}</h3><ol>{items}</ol></div>"""

    hero = hero_block("LEARNING PATH · L2", "AI 工具库：<br><em>按场景选工具，而不是被工具绑架</em>",
                      "9 大类 50+ 工具，国内外双维度覆盖。每个工具标注定位、核心优势、适用场景与定价——全部经多源交叉验证，标注更新日期。",
                      [("", "先学方法", "methods.html"), ("line", "看最佳实践", "practices.html")])

    body = f"""
<section>
  <div class="container">
    <div class="sec-head">
      <span class="sec-label">TOOLBOX · VERIFIED 2026-08</span>
      <h2 class="sec-title">按场景分类的工具库</h2>
      <p class="sec-desc">基于 OPC 独立开发者全栈工具地图 2026（多源验证：腾讯云开发者社区、知乎测评、Reddit/HN、GitHub、官方定价页）整理。定价以官网为准，可能变动。</p>
    </div>
    {cats}
  </div>
</section>
<section>
  <div class="container">
    <div class="sec-head">
      <span class="sec-label">READY-MADE STACKS</span>
      <h2 class="sec-title">选型组合：直接抄作业</h2>
      <p class="sec-desc">按场景组合好的一整套工具链，新人照单配齐即可开工。</p>
    </div>
    <div class="grid">{packs}</div>
  </div>
</section>"""
    return shell("AI工具库", "tools.html", hero, body)

def page_practices():
    ps = ""
    for p in PRACTICES:
        ps += f"""<div class="practice"><h3>{p['name']}</h3>{p['content']}</div>"""

    hero = hero_block("LEARNING PATH · L3", "最佳实践：<br><em>从「会用」到「用好」</em>",
                      "工具遍地都是，稀缺的是判断力。这里沉淀的是经过验证的高 ROI 场景、人机协作方法论，以及用真实教训换来的铁律。",
                      [("", "回到工作法", "methods.html"), ("line", "去行动", "courses.html")])

    body = f"""
<section>
  <div class="container">
    <div class="sec-head">
      <span class="sec-label">BEST PRACTICES</span>
      <h2 class="sec-title">实践深化</h2>
      <p class="sec-desc">内容来源：MindStudio 等 2026 知识工作者 AI 应用调研（多源交叉）、OPC 工作坊方法论、碳硅组织运营真实教训。</p>
    </div>
    {ps}
  </div>
</section>"""
    return shell("最佳实践", "practices.html", hero, body)

def page_courses():
    tiers = ""
    for t in COURSES:
        hot = " hot" if t["hot"] else ""
        badge = '<span class="t-badge">🔥 最受欢迎</span>' if t["hot"] else ""
        items = "".join(f"<li>{i}</li>" for i in t["items"])
        tiers += f"""<div class="tier{hot}">{badge}
  <span class="t-phase">{t['phase']}</span>
  <h3>{t['name']}</h3>
  <p class="t-sub">{t['sub']}</p>
  <div class="t-price">{t['price']}<small> / 人</small></div>
  <ul>{items}</ul>
  <a class="btn" href="index.html">联系报名</a>
</div>"""

    rms = ""
    for wk, name, desc in ROADMAP:
        rms += f"""<div class="rm"><div class="rm-wk">{wk}</div><div class="rm-body"><h4>{name}</h4><p>{desc}</p></div></div>"""

    hero = hero_block("LEARNING PATH · L4", "课程与行动：<br><em>把能力变成收入</em>",
                      "认知到行动的最小闭环。三档课程对应三条进化线：看清自己 → 跑通回路 → 项目启航。每一档都是上一档的放大器，而不是重复。",
                      [("", "加入星球", "courses.html"), ("line", "回到起点 L0", "index.html#levels")])

    body = f"""
<section>
  <div class="container">
    <div class="sec-head">
      <span class="sec-label">OPC COURSES</span>
      <h2 class="sec-title">课程三档</h2>
      <p class="sec-desc">一天觉醒营是入口，一周实战营是加速器，一月启航营是放大器。建议路径：先觉醒，再实战，后启航。</p>
    </div>
    <div class="tier-grid">{tiers}</div>
  </div>
</section>
<section>
  <div class="container">
    <div class="sec-head">
      <span class="sec-label">30-DAY ROADMAP</span>
      <h2 class="sec-title">30 天路线图</h2>
      <p class="sec-desc">工作坊带走的是路线图，这里是你每天的落点。</p>
    </div>
    <div class="roadmap">{rms}</div>
  </div>
</section>
<section>
  <div class="container">
    <div class="cta">
      <h3>加入同行者社群</h3>
      <p>星球「OPC超级个体加速器」：案例工厂、工具评测、每周选题、同行者互相验收回路。<br>公众号「OPC成长之路」：每周三、周日 20:00 更新。</p>
      <a class="btn" href="index.html">扫码加入 · 认知到行动的最小闭环</a>
    </div>
  </div>
</section>"""
    return shell("课程与行动", "courses.html", hero, body)

# ============================================================
# BUILD
# ============================================================

PAGES = {
    "index.html": page_index,
    "playbook.html": page_playbook,
    "methods.html": page_methods,
    "tools.html": page_tools,
    "practices.html": page_practices,
    "courses.html": page_courses,
}

def main():
    os.makedirs(ROOT, exist_ok=True)
    os.makedirs(os.path.join(ROOT, "resources", "guides"), exist_ok=True)

    # 复制保姆级教程与工具地图进站内资源
    src_notes = os.path.expanduser("~/Documents/OPC研究工厂/整理笔记")
    copies = [
        ("ClaudeCode教程-保姆级上手指南.md", "ClaudeCode教程-保姆级上手指南.md"),
        ("Codex教程-保姆级上手指南.md", "Codex教程-保姆级上手指南.md"),
        ("n8n教程-保姆级上手指南.md", "n8n教程-保姆级上手指南.md"),
        ("ima教程-保姆级上手指南.md", "ima教程-保姆级上手指南.md"),
        ("WorkBuddy教程-保姆级上手指南.md", "WorkBuddy教程-保姆级上手指南.md"),
        ("OPC独立开发者全栈工具地图2026-完整版.md", "OPC独立开发者全栈工具地图2026-完整版.md"),
    ]
    copied = []
    for src_name, dst_name in copies:
        src = os.path.join(src_notes, src_name)
        dst = os.path.join(ROOT, "resources", "guides", dst_name) if "教程" in src_name else os.path.join(ROOT, "resources", dst_name)
        if os.path.exists(src):
            shutil.copy2(src, dst)
            copied.append(dst)

    for fname, fn in PAGES.items():
        with open(os.path.join(ROOT, fname), "w", encoding="utf-8") as f:
            f.write(fn())
        print(f"✅ {fname}")

    print(f"\n📁 站点根目录: {ROOT}")
    print(f"📄 生成页面: {len(PAGES)} 个")
    print(f"📚 复制资源: {len(copied)} 个")
    print("完成。本地预览: open " + os.path.join(ROOT, "index.html"))

if __name__ == "__main__":
    main()
