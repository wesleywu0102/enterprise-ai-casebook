# Enterprise AI Casebook

**20 个已经上生产的企业 AI 案例 + 6 个可复用架构方案。每条都写清三件事：这个数字是谁说的、按什么口径算的、你不能拿它说什么。**

![cases](https://img.shields.io/badge/cases-20-blue)
![A-grade](https://img.shields.io/badge/A%20grade-8-brightgreen)
![retracted](https://img.shields.io/badge/retracted%20on%20record-1-red)
![license](https://img.shields.io/badge/license-CC%20BY%204.0-lightgrey)
![PRs](https://img.shields.io/badge/PRs-welcome-orange)

---

## 先看一条完整的记录

这是 [`cases/manufacturing/siemens-schaeffler-copilot.md`](cases/manufacturing/siemens-schaeffler-copilot.md) 的第 5 节和第 8 节，一字未改：

| 指标 | 数值 | 口径与基线 | 来源 |
|---|---|---|---|
| 自动化任务耗时 | "数周 → 数分钟" | 厂商通稿定性表述，**无任务定义、无样本** | Siemens/Microsoft 通稿 |
| 工程工时降幅 | **官方未披露** | — | 两份官方通稿均无百分比 |

**❌ 不能说**：「舍弗勒用 AI 把工程工时减少了 **35%**」——无一手来源
**✅ 可以说**：「该案例的官方材料中**没有任何百分比**形式的效益数据」

> 中文互联网上关于这个案例的文章，绝大多数写的是被划掉的那一句。西门子 2023-10 联合通稿、2023-11 舍弗勒新闻稿、舍弗勒官方故事页——三份一手材料全文都没有 35%。

**20 条案例都是这个形状。** 你不需要自己去猜厂商数字的真假，条目里已经写好了。

---

## 它能替你做的三件事

| 你要做的事 | 你会怎么用它 | 拿到什么 |
|---|---|---|
| **写稿** | `ls cases/healthcare/` | 4 条医疗案例，其中 2 条是同行综述级（NEJM 系、JAMA 系），可直接引用 |
| **被质疑** | 翻该案例的 `## 8. 引用边界` | ✅ 可以说 / ❌ 不能说 两栏清单，附原始链接 |
| **做方案 / 报价** | 看 `## 4. 落地方式` + `## 7. 可复用要点` | 谁交付的、嵌进哪个系统、翻车点在哪 |
| **判断"这是不是真 FDE"** | 读 [`fde/README.md`](fde/README.md) 第三节 | 5 个问题，30 秒出结论 |

**不适用的人**：想找"AI 提效 300%"这种数字来撑 PPT 的。这个库会告诉你那个数字不存在。

---

## 场景 → 方案：6 个可复用架构

`cases/` 记录**这一家做了什么**，[`solutions/`](solutions/) 回答**这一类该怎么搭**。6 个模式覆盖全部 20 条案例，每篇都有参考架构图、组件选型表、集成点、评测口径和真实失败模式。

| 你的场景 | 模式 | 参考架构的核心 | 最难的一步 |
|---|---|---|---|
| 员工找不到文档，找到了也不敢用 | [1 检索问答 RAG](solutions/01-retrieval-knowledge.md) | 混合召回 → 重排 → 强制引用 → 拒答 | 权限必须在**召回之前**过滤 |
| 专业人员的时间被文书吃掉 | [2 环境文书](solutions/02-ambient-documentation.md) | 听 → 结构化 → 写草稿进既有系统 → 人签 | 测审核后的总时间，不是生成速度 |
| 客服量大、诉求能被 API 化 | [3 对话拦截 Agent](solutions/03-deflection-agent.md) | 身份注入 → 政策判定 → 动作分级 → 转人工带上下文 | 动作分级 + 假解决率 |
| 调度、补货、排班靠人拍脑袋 | [4 运营编排](solutions/04-ops-orchestration.md) | 多源接入 → 语义层/本体 → 规则+优化 → 建议回流 | 对象建模（不是数据表） |
| 工程师写重复代码/配置 | [5 工程内嵌生成](solutions/05-embedded-codegen.md) | 上下文装配 → 生成草稿 → 编译/仿真挡错 → 人签 | 靠校验器，不靠提示词 |
| 全公司都要用但没明确任务 | [6 全员平台](solutions/06-employee-platform.md) | 统一入口 → 权限/数据边界 → 自建助手 → 治理 | 助手泛滥与无人维护 |

三条跨模式通则，在 20 条案例里都成立：

1. **嵌进既有工作流，不要新开入口。**（摩根士丹利接进写邮件流程、舍弗勒接进 TIA Portal、Lowe's 挂在店员手持机）
2. **AI 出草稿，人签署。**（病历、代码、客户答复、调度建议，四个模式都有这道闸门）
3. **先定义分母，再谈成效。**（Intercom 改过自己的分母、摩根士丹利 ">98%" 的分母是团队不是个人）

> ⚠️ 方案库是**模式归纳，不是客户的实现图纸**。企业几乎不公开分块策略、嵌入模型、提示词、编排框架；每篇末尾都写了"哪些是公开披露、哪些是通用还原"。

---

## 60 秒：三个最反直觉的发现

| 发现 | 证据 |
|---|---|
| **同类产品，两个同行评审研究差了 80 倍** | Jefferson Health 报「文书投入 **-84%**」（*effort* 评分，不是工时）；Providence 用 16,149 个观察月算出每次预约只省 **1 分钟**（7.1→6.1），且长期效应多数跨零。差别不在产品，在**怎么算**。 |
| **最贵的公共部门 AI 合同，监管要求官方加注「无法归因」** | 英国 NHS 联邦数据平台，7 年上限 3.3 亿英镑。英国统计监管办公室 2026-07 结论：NHS England 必须声明**不能把改善归因于该平台**。目前最硬的一条负面一手证据。 |
| **「FDE 已成标准交付形态」是叙事，还不是事实** | 10 个被贴上 FDE 标签的客户案例里，只有 **Palantir** 的条目能拿出「工程师常驻客户现场」的公开原文。其余 9 家是 `unknown` 或仅供应商单方说法。 |

---

## 全部案例

「证据」列见[分级规则](#证据分级)｜「FDE」列指是否有人在客户现场对结果负责。

| 企业 | 行业 | 场景 | 核心数字 | 证据 | FDE |
|---|---|---|---|---|---|
| [Jefferson Health](cases/healthcare/jefferson-abridge.md) | 医疗 | 门诊文书 | 文书投入 -84%（effort 非工时）；下班后文书 -9~17% | **A** | — |
| [Providence](cases/healthcare/providence-dragon-copilot.md) | 医疗 | 门诊文书 | 7.1→6.1 分钟/次；长期效应多数跨零 | **A** | — |
| [Tampa General](cases/healthcare/tampa-general-palantir.md) | 医疗 | 床位与容量调度 | 安置耗时 -83%；脓毒症住院日 -30%（无基线） | B | **驻场**（有原文） |
| [Cleveland Clinic](cases/healthcare/cleveland-clinic-palantir.md) | 医疗 | 虚拟指挥中心 | 容量测算 -75%；急诊滞留 -1h/人（仅厂商口径） | B | 共创 |
| [Moderna](cases/healthcare/moderna-chatgpt-enterprise.md) | 生物医药 | 员工自建 GPT | 750 个 GPT、法律 100% 采用；**0 条效益数字** | B | — |
| [摩根大通](cases/finance/jpmorgan-llm-suite.md) | 金融 | 全行 LLM 平台 | 覆盖 20 万 / 32 万（两口径并存）；KYC 单案成本 -40% | **A** | 甲方自建 |
| [摩根士丹利](cases/finance/morgan-stanley-ai-assistant.md) | 金融 | 顾问知识库 | 顾问团队 >98% 使用；文档可达 20%→80% | B | 未披露 |
| [BBVA](cases/finance/bbva-openai-enterprise.md) | 金融 | 全员 ChatGPT | 12 万人；80% 日活；每周省 3h（员工自报） | B | 未确认 |
| [ADT](cases/finance/adt-sierra-agent.md) | 安防 | 客服 agent | 聊天拦截 45%→60%；电话 16%→25% | **A** | 按结果付费 |
| [Klarna](cases/retracted/klarna-ai-assistant.md) | 金融 | 客服自动化 | 「相当于 700 名客服」→ CEO 承认质量下降、重新招人 | **X** | — |
| [美的集团](cases/manufacturing/midea-agents.md) | 制造 | 2 万个智能体 | 2025 降本 7–7.7 亿元（同一年多口径）；2026 目标 8.8 亿 | **A** | 甲方自建 |
| [舍弗勒 × 西门子](cases/manufacturing/siemens-schaeffler-copilot.md) | 制造 | PLC 代码生成 | 「数周」→「数分钟」，**官方全文无任何百分比** | B | — |
| [Lowe's](cases/retail/lowes-mylow.md) | 零售 | 导购助手 | 2,500 万问题；使用助手的顾客转化 3 倍 | **A** | 未披露 |
| [Wendy's / QSCC](cases/retail/wendys-qscc-palantir.md) | 零售 | 供应链 | 一次糖浆短缺：15 人一天 → 5 分钟（n=1） | C | 未披露 |
| [Walgreens](cases/retail/walgreens-palantir.md) | 零售药房 | 门店运营编排 | 10 店 → 约 4,000 店 / 8 个月；无效益数字 | C | 驻场 |
| [Intercom Fin](cases/software/intercom-fin.md) | 软件 | 一线客服 | 76%（官网）/ 65%（自家学习中心）；**2026-08 改过分母** | C | — |
| [T-Mobile](cases/telecom/tmobile-intentcx.md) | 电信 | 客服语音 | 人工通话 -55%；AI 承接 40% 接触 | B | 供应商侧 |
| [North Highland](cases/professional-services/north-highland-claude.md) | 专业服务 | 技术交付 | 1,400 人 30 天铺开；交付约快 50%（客户自发布） | B | 客户自采 |
| [英国 NHS](cases/public-sector/nhs-fdp-palantir.md) | 公共医疗 | 联邦数据平台 | 3.3 亿英镑 / 7 年上限；监管要求加注「不能归因」 | **A** | 未披露 |
| [美国国防部 Maven](cases/public-sector/dod-maven-smart-system.md) | 国防 | 目标识别 | 累计上限约 12.75 亿美元（**非已支付**）；2 万活跃用户 | **A** | 驻场 |

> A=8｜B=8｜C=3｜X=1。按行业、场景、证据、交付形态、方案模式切片的索引在 [`index/`](index/)（模式索引见 [`by-pattern`](index/by-pattern.md)）。

---

## 不要用这 8 个数字

它们都流传很广，但**指向的一手页面里没有这个数字**，或者已经被当事方自己推翻。

| 流传的说法 | 核查结果 | 能怎么用 |
|---|---|---|
| 西门子 Industrial Copilot「工程工时 **-35%**」 | 两份官方通稿 + 舍弗勒官方故事页，**全文无任何百分比** | 只能写「数周 → 数分钟」 |
| Moderna「**42 天**完成临床前序列设计」 | OpenAI 官方 Moderna 案例全文**没有任何周期数据** | 写「750 个 GPT」，别写 42 天 |
| Palantir Bootcamp 转化率 **21–34% / 70% / 75%** | 三个版本互斥，全部溯源失败；连场次数都有 660/680/915/1,300 四个版本。官方唯一硬数字是 Q1 2024 致股东信「单季 **660+** 场」 | 只引 660，不引转化率 |
| Klarna「相当于 **700 名客服**、年增 4 亿美元」 | 2024 年官方口径，2025 年 CEO 本人承认过度依赖、质量下降并重新招人 | 当**回撤样本**写，见 [`cases/retracted/`](cases/retracted/) |
| Salesforce Agentforce「**29,000 客户**」 | 原文是 29,000 **deals**（累计交易），2025-12 付费交易仅 9,500。deals ≠ 客户 ≠ 生产部署 | 纠正口径后才能提 |
| 「**Chubb** 保险用 Sierra，效果显著」 | Sierra 客户页里的是 **Chubbies**（男装短裤品牌）。Chubb Limited 与 Sierra 查不到任何关联 | 纯名称混淆 |
| John Deere × OpenAI「农药用量 **-70%**」 | 70% 是 **See & Spray** 摄像头 + 机器学习的硬件能力，与生成式 AI 无关；deere.com 站内检索 `OpenAI` **零命中** | 要写就写清是机器视觉 |
| Sierra 定价「**$1–2.5/次**解决」 | 官网 `/pricing` 返回 404；所有金额出自第三方站互相转引 | 只能写「按结果计费」 |

另有 10 个被**主动排除**的著名案例（Bridgewater、Novo Nordisk、Hitachi、Estée Lauder、Sonos、Bilt…）连同理由在 [`index/watchlist.md`](index/watchlist.md)。有人拿这些质询你时，翻那一节。

---

## FDE 专题：交付模式还是外包

FDE 不是「驻场外包」的高级说法。判断标准只有两条：**对业务结果负责**，**现场经验回流成产品**。缺一条就是外包。

| 问题 | 外包 | FDE |
|---|---|---|
| 谁付他工资？ | 按人天计费 | 厂商付薪，或甲方自建前沿团队 |
| KPI 是交付物还是业务指标？ | 「完成 12 个需求」 | 「排产响应从 3 天压到 1 天」 |
| 他走了以后客户剩什么？ | 一套系统 | 可复用组件、剧本、评测集 |
| 现场发现有没有改变产品路线图？ | 没有 | 有——定义性特征 |
| **有没有退场机制？** | 越驻越久 | 目标是让自己尽快不必要 |

最后一条最好用。高盛 CIO 原话：*"a specific kind of engagement whose job is to **become unnecessary in the shortest time possible**."*

五种形态：`vendor-embedded`（厂商 FDE）、`in-house`（甲方自建，中国更常见）、`si-partner`（集成商）、`none`（纯产品）、`unknown`。**20 条里 7 条是 `unknown`**——这就是「FDE 已成标准形态」这句话的真实边界。

模式笔记 5 篇：[OpenAI 把 FDE 做成职级](fde/openai-fde.md)（2025 年初成立，官方原话）｜[Anthropic Applied AI](fde/anthropic-applied-ai.md)（仍在组建期；「进五角大楼」是误读）｜[15 亿美元合资公司](fde/anthropic-goldman-jv.md)｜[Palantir Bootcamp](fde/palantir-bootcamp.md)（官方只说「5 天从 0 到用例」，**没承诺 5 天上生产**）｜[中国路径](fde/china-fde.md)

模式也有代价，一起写才完整：**不可线性扩张**（每客户 6–18 个月驻场）、**毛利被拉低**（服务收入稀释软件毛利）、**知识不转移**（团队撤走客户无法自迭代）。

---

## 开始用

```bash
git clone https://github.com/wesleywu0102/enterprise-ai-casebook.git
cd enterprise-ai-casebook
pip install -r requirements.txt
python scripts/validate.py --strict     # 20 cases, 0 issues
```

```bash
# 只要法定披露 / 同行评审级别的（可以直接引用）
grep -rl 'evidence_grade: "A"' cases/

# 只要有人常驻客户现场对结果负责的
grep -rl 'fde_involved: "vendor-embedded"' cases/
```

增删案例后重建索引：`python scripts/build_index.py`

---

## 证据分级

| 级 | 定义 | 典型来源 | 能否公开引用 |
|---|---|---|---|
| **A** | 法定披露或同行评审 | 年报 / 10-K、财报电话会、监管文件、NEJM / JAMA / Nature | ✅ 可引，仍需带口径 |
| **B** | 企业官方发布，含可核查数字 | 官方新闻稿、官方案例页、技术博客 | ✅ 可引，须注明「企业自述」 |
| **C** | 单方证言，无口径无基线 | 厂商客户引语、销售物料、大会演讲 | ⚠️ 仅作线索 |
| **D** | 二手报道 / 聚合站 | 媒体转述、行业报告汇编、榜单 | ❌ 必须回溯一手 |
| **X** | 已被回撤或重大修正 | 企业公开承认、后续财报修正 | ✅ 但必须同时给修正后说法 |

**硬规则**：任何案例至少要有 1 个 A 或 B 级来源，否则只能进 `index/watchlist.md`。D 级**不得**直接生成案例。细则见 [`taxonomy/evidence.md`](taxonomy/evidence.md)。

### 一条案例的结构

带 YAML front-matter 的 Markdown，既能被脚本校验成索引，又能直接当文章素材读。每个指标强制四件套：

```yaml
metrics:
  - name: "病历书写投入（HPI 与 A&P 部分）"
    value: "-84%"
    baseline: "部署前同科室均值"        # 跟什么比
    method: "平台内工作量评分，1,802 名活跃使用者"   # 谁算的、怎么算、样本量
    window: "部署后 4 个月"              # 时间窗
    direction: "effort-down"            # 注意是 effort，不是工时
```

正文固定 9 节：摘要 / 痛点 / 场景 / 落地方式 / 成效 / **存疑之处** / 可复用要点 / **引用边界** / 来源。

第 6 和第 8 节**不允许为空**——这是本库和「客户成功故事」的分界线。

### 引用格式

> 摩根士丹利称其财富管理条线超过 98% 的顾问团队在使用内部 AI 助手（来源：OpenAI 客户案例，B 级，企业自述，未披露统计分母）。

**四要素**：数字 + 来源 + 证据级别 + 口径限制。

---

## 如何贡献

```bash
cp cases/_TEMPLATE.md cases/<industry>/<company>-<scenario>.md
# 填 front-matter → 写满 9 节 → 跑校验 → 提 PR
python scripts/validate.py --strict
```

CI 会在 PR 上跑校验，并检查索引是否同步。评审清单见 [`CONTRIBUTING.md`](CONTRIBUTING.md)。

**不收**：只有发布会没有成效的、只有厂商单方口径的、链接打不开的、把「合作公告」当「已落地」的。这四类进 `index/watchlist.md`。

---

## 已知局限

- **幸存者偏差**：能查到细节的，本身就是愿意公开的少数；失败案例几乎不可见，只能靠回撤记录部分补偿。
- **效应量不可比**：不同企业的「提效 30%」口径互不相通。本库只保证口径被**记录**，不保证可比。
- **时间衰减**：每条有 `last_verified`，超 12 个月进 [`index/stale.md`](index/stale.md)。
- **语言偏斜**：英文一手来源更易获得，中文案例多依赖官媒转述，证据等级结构性偏低。

---

## 许可

案例正文 CC BY 4.0，脚本 MIT。引用请保留仓库链接与证据等级标注。

---

<details>
<summary><b>English TL;DR</b></summary>

20 enterprise AI deployments that actually reached production — each with a first-party source, a stated measurement basis, and an evidence grade (A = regulatory filing / peer-reviewed · B = official release with verifiable numbers · C = vendor claim only · X = retracted).

What makes it different from a case-study roundup: **every entry tells you what you cannot say.** Section 8 of each file is a two-column "✅ you can say / ❌ you cannot say" list, and section 6 records what remains unverifiable.

There is also a section of eight numbers you should **not** use — figures that are cited everywhere but do not appear on the pages they supposedly come from (e.g. Siemens' "35% engineering hours saved"), or were retracted by the company itself (Klarna's "700 agents").

The FDE (Forward Deployed Engineer) track asks whether the delivery model has any *client-side* evidence. Of 10 cases tagged as FDE work, only Palantir's contain first-party language about engineers embedded on site. That gap is itself the finding.

Written in Chinese; sources carry URLs and access dates.

</details>
