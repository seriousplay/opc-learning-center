# OPC成长之路 · AI知识工作者学习资源中心

> 渐进式学习资源站点 · 一站式学习与资源中心
> 碳硅组织研习社 · OPC 子品牌「OPC成长之路」
> 更新日期：2026-08-19

## 站点定位

面向知识工作者的 AI 高效工作法、工具、最佳实践的一站式渐进式学习资源中心。
核心主张：**一个人运行一个硅基团队** · **认知到行动的最小闭环**。

渐进式五层路径（与 OPC 工作坊「从基线往上爬一层」理念一致）：

| 层级 | 名称 | 对应页面 | 内容 |
|:---:|------|---------|------|
| L0 | 认知觉醒 | index.html | 三大能力、工具链五层、渐进式路径 |
| L1 | 方法掌握 | methods.html | 8 大知识工作者工作流 |
| L2 | 工具驾驭 | tools.html | 9 大类 50+ 工具 + 选型组合 |
| L3 | 实践深化 | practices.html | ROI 排行榜、回路六要素、铁律、教程、提示词模板 |
| L4 | 行动变现 | courses.html | 课程三档、30 天路线图、社群 |

## 文件结构

```
OPC学习资源中心/
├── index.html          首页（渐进式路径总览）
├── methods.html        高效工作法（8 大工作流）
├── tools.html          AI 工具库（9 大类）
├── practices.html      最佳实践与案例
├── courses.html        课程与行动
├── css/style.css       设计系统（碳硅绿 × 暖纸色）
├── build_site.py       站点生成器（数据驱动，改数据即改站）
├── resources/
│   ├── guides/         保姆级教程（5 篇）
│   └── OPC独立开发者全栈工具地图2026-完整版.md
└── README.md
```

## 更新维护

**方法一（推荐）**：编辑 `build_site.py` 中的 DATA 区（LEVELS / METHODS / TOOL_CATS / PRACTICES / COURSES），
然后运行：

```bash
cd "/Users/heyiqing/Documents/OPC研究工厂/OPC学习资源中心"
env -u PYTHONPATH python3 build_site.py
```

**方法二**：直接编辑对应 HTML 文件（不推荐，下次 build 会被覆盖）。

### 工具库更新铁律（tool-research-methodology）

- 新工具必须**至少 2 个独立信源交叉验证**才可写入（官方文档 + 社区实测）
- 定价一律以官网为准，标注日期
- 国内/国外双维度覆盖
- 工具更名要同步（例：NotebookLM → Gemini Notebook，2026-07）

### 内容真实性铁律

- 禁止编造；没验证 = 不存在
- 网络来源多方验证；LLM 摘要只作选题线索，不作信源
- 数字/名称/时间线逐字对照原文

## 部署

**线上地址（GitHub Pages）：** https://seriousplay.github.io/opc-learning-center/
**仓库：** github.com/seriousplay/opc-learning-center（公开）

```bash
# 更新推送
cd "/Users/heyiqing/Documents/OPC研究工厂/OPC学习资源中心"
git add -A && git commit -m "更新"
git -c http.proxy= -c https.proxy= push   # ⚠️ 本机git全局代理指向127.0.0.1:7890但代理常未运行，需绕过
```

备选：Netlify `npx netlify deploy --prod --dir=.`（需先登录）

> ⚠️ **代理坑**：`git config --global http.proxy` = `http://127.0.0.1:7890`（Clash 类代理），代理软件未运行时 push 会报 `Failed to connect to 127.0.0.1 port 7890`。用 `git -c http.proxy= -c https.proxy= push` 临时绕过，无需改全局配置。

## 演进路线

与 `../工作坊设计/赋能站点_升级规划_v1.0.md` 衔接：

- **本期（MVP）**：本静态站点，周日前可作为觉醒营的课程入口 + 课后资源中心
- **下期（V1）**：接入学员报名/问卷，内容挂到 Next.js workshops 应用
- **远期（V2）**：学员中心 + 作品库 + 资源库后台，成为四合一赋能平台

## 配套资产

- 工作坊设计：`../工作坊设计/`（brochure/poster/落地页/流程 v6.0）
- 工具研究：`../整理笔记/`（保姆级教程、工具地图）
- 方法论技能：`opc-workshop-design` / `personal-brand-site` / `tool-research-methodology`
