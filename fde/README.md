# FDE 专题：前沿部署工程师（Forward Deployed Engineer）

> FDE 不是"驻场外包"的高级说法。判断标准只有两条：**对业务结果负责**，**现场经验回流成产品能力**。缺一条，就是外包。

---

## 一、为什么这个专题值得单列

2026 年，企业 AI 的瓶颈已经从"模型够不够强"转移到"谁能把它装进业务里"。这个判断有三个可观察的证据：

1. **模型厂商自己开始招 FDE。** OpenAI 的 Forward Deployed Engineering 团队已按行业分设岗位（金融服务、AI 基础设施、区域市场），岗位描述里明确写"以生产采用率、工作流效率、风险降低、收入影响衡量成功"。
2. **FDE 被资本化。** 2026 年 5 月，Anthropic 与黑石、Hellman & Friedman、高盛共同成立 15 亿美元的 AI 原生服务公司，核心卖点就是"让中型企业也能用上前沿部署工程师"。
3. **FDE 被政策化。** 上海把"加快培育前沿部署工程师队伍"写进《支持先进制造业转型升级三年行动方案（2026—2028）》；南京软件谷成立全市首个 FDE 联盟。

所以更准确的说法是：**FDE 正在成为一种被资本押注的组织形态，但它是不是客户侧普遍发生的交付事实，公开证据还不够。** 本库 20 条案例里 `fde_involved=unknown` 有 7 条，能拿出客户方原文说"工程师常驻现场"的只有 Palantir 的条目。「FDE 已是行业标准交付形态」这句话，本库不采信。

另见 [`findings/03-fde-is-a-margin-structure.md`](../findings/03-fde-is-a-margin-structure.md)：一个比"标准形态"更能解释上述四种动作的判断——FDE 是产品还不够标准化时的毛利安排。该篇推翻了本文件先前写下的结论。

---

## 二、FDE 的五种形态

详细定义见 [`../taxonomy/deployment.yml`](../taxonomy/deployment.yml)。要点：

| 形态 | 谁的人 | 坐在哪 | 对什么负责 | 案例 |
|---|---|---|---|---|
| **none** | — | — | — | Jefferson Health、Moderna（纯产品交付） |
| **vendor-embedded** | 模型/平台厂商 | 客户现场 | 生产指标，并把经验回流产品 | OpenAI FDE、Palantir FDE、Anthropic 合资公司 |
| **si-partner** | 集成商/服务商 | 客户现场 | 里程碑交付 | 云巴巴、嘉环科技、上海电信 |
| **in-house** | 甲方自己 | 业务一线 | 业务成效（不是需求交付） | 中国联通软研院、美的 AI 军团 |
| **unknown** | — | — | — | 摩根士丹利（公开信息不足） |

注意：**in-house 形态在中国更常见**，且被官方话语体系称为"研发前置""嵌入式支撑"。评价它时不能套用外包的框架。

**但形态不由行业决定。** 医疗内部就是反例：Jefferson / Providence 做病历文书是 `none`，Tampa / Cleveland 做床位调度是 `vendor-embedded`。差别在 AI 的输出要不要改动别人已有的工作方式。按行业选方案会漏掉这件事，完整判断见 [`findings/05-industry-is-the-constraint.md`](../findings/05-industry-is-the-constraint.md)。

---

## 三、怎么判断一个"FDE 故事"是真的

写案例或读厂商材料时，用这五个问题过一遍：

1. **谁付钱给这个工程师？** 厂商付薪 = vendor-embedded；甲方付薪 = in-house；按人天计费 = 外包。
2. **他的 KPI 是交付物还是业务指标？** "完成 12 个需求"是外包；"把排产响应从 3 天压到 1 天"是 FDE。
3. **他走了以后客户还剩什么？** 只剩一套系统 = 外包；留下可复用的组件、剧本、评测集 = FDE。
4. **他的现场发现有没有改变产品？** FDE 的定义性特征是"双向"：既把产品带进客户，也把客户的问题带回产品路线图。OpenAI 的岗位描述里，这一条写作 "codify working patterns into tools, playbooks, or building blocks"。
5. **有没有"退场机制"？** 高盛 CIO Marco Argenti 的说法最准确："It's not the classic consultant. This is a specific kind of engagement whose job is to become unnecessary in the shortest time possible."

第 5 条是最好的照妖镜：**真 FDE 的目标是让自己尽快失业。**

---

## 四、FDE 模式的三个结构性代价

写正面案例容易，但这条路径有明显成本，必须一起写：

| 代价 | 具体表现 | 谁在承受 |
|---|---|---|
| **不可线性扩张** | 每个大客户要 6–18 个月驻场周期，人力是硬约束。Palantir 约 4,400 名员工撑起数百亿美元收入，人均创收极高，但客户数增长受限 | 厂商 |
| **毛利被拉低** | 服务收入占比上升会稀释软件毛利。Palantir 的应对是把服务当获客成本，靠后续 license 回收 | 厂商 |
| **知识不转移** | 客户过度依赖驻场团队，团队撤走后无法自主迭代。这是 si-partner 形态最常见的失败 | 客户 |

**这就是为什么"AI 化的 FDE"会出现**：Palantir CTO 称其 AI FDE 已能在两周内完成原本数年的 SAP ECC→S/4HANA 迁移。如果这个方向成立，FDE 的瓶颈会从"人不够"变成"人做什么"。

---

## 五、本专题的文件

| 文件 | 主题 | 证据等级 |
|---|---|---|
| [`openai-fde.md`](openai-fde.md) | 模型厂商把 FDE 做成正式职级：2025 年初成立的团队、考核口径、地理分布 | A（官方博客 + 招聘页） |
| [`anthropic-applied-ai.md`](anthropic-applied-ai.md) | Anthropic 的 FDE 仍在组建期；与 Palantir 的合作被误读成"已进五角大楼" | A（JD/公告）/ 无（成效） |
| [`anthropic-goldman-jv.md`](anthropic-goldman-jv.md) | FDE 被资本化：15 亿美元合资公司，瞄准 PE 旗下中型企业 | A（官方新闻稿） |
| [`palantir-bootcamp.md`](palantir-bootcamp.md) | FDE 的原始形态：Bootcamp 把 POC 压到 5 天；转化率溯源失败 | B（官方）/ 无（转化率） |
| [`china-fde.md`](china-fde.md) | 中国路径：运营商、集成商、地方政府、软件谷联盟 | B/C（官媒 + 企业自述） |

### 已经写进案例库的 FDE 客户案例

上面五篇是"模式笔记"。真正落到客户、带成效数字的条目在 `cases/` 下，用 `fde_involved` 字段标记：

| 案例 | 客户 | 供应商 | FDE 形态 | 证据 |
|---|---|---|---|---|
| [Tampa General](../cases/healthcare/tampa-general-palantir.md) | 学术医疗中心 | Palantir | **vendor-embedded**（原文有 "embedded themselves" 与 "forward-deployed engineers"） | B |
| [Cleveland Clinic](../cases/healthcare/cleveland-clinic-palantir.md) | 学术医疗中心 | Palantir | vendor-embedded（共创，非驻场接需求） | B |
| [Wendy's / QSCC](../cases/retail/wendys-qscc-palantir.md) | 快餐供应链合作社 | Palantir | unknown（官方无 FDE 表述） | C |
| [英国 NHS FDP](../cases/public-sector/nhs-fdp-palantir.md) | 公共医疗 | Palantir 联合体 | unknown | A（含监管否定） |
| [美国国防部 Maven](../cases/public-sector/dod-maven-smart-system.md) | 国防 | Palantir USG | vendor-embedded（证据弱于商业侧） | A（合同文件） |
| [BBVA](../cases/finance/bbva-openai-enterprise.md) | 银行 | OpenAI | unknown（客户未确认 FDE 参与） | B |
| [T-Mobile](../cases/telecom/tmobile-intentcx.md) | 电信 | OpenAI | vendor-embedded（仅供应商侧表述） | B |
| [Lowe's](../cases/retail/lowes-mylow.md) | 零售 | OpenAI | unknown | A（财报电话会） |
| [ADT](../cases/finance/adt-sierra-agent.md) | 安防 | Sierra + Google | vendor-embedded（陪跑，无驻场条款） | A（财报电话会） |
| [North Highland](../cases/professional-services/north-highland-claude.md) | 咨询 | Anthropic | unknown（客户自采） | B |

**这张表最重要的一点**：十家里只有 Palantir 的条目能拿出"工程师常驻客户现场"的公开表述，其余全部是 `unknown` 或仅供应商单方说法。所谓"FDE 已成标准交付形态"，目前更多是叙事，不是可核验的普遍事实。

---

## 六、写这个专题时的常见错误

1. **把 FDE 等同于"驻场"。** 驻场只是形式。核心是责任归属与知识回流。
2. **用 Palantir 的转化率当行业基准。** 公开转述有 30–40%、70%、75% 三个互斥版本，全部溯源失败；官方唯一可引的是 Q1 2024 单季 660+ 场 bootcamp。
3. **忽略 in-house 形态。** 中国的 FDE 讨论大量发生在甲方内部（联通软研院、美的），只盯厂商会漏掉一半。
4. **把"AI FDE"当成已实现。** 目前只有厂商高管的公开表述，没有独立验证的交付记录。
5. **不写代价。** 只写"FDE 让 AI 落地更快"，不写"FDE 让毛利更低、扩张更慢"，是不完整的。
6. **把客户案例默认算成 FDE 项目。** BBVA、Lowe's、T-Mobile 都出现在 OpenAI 的 FDE 页面上，但三家客户自己的材料都没这么说。除非有客户方或合同证据，一律记 `unknown`。
