---
id: "public-sector-nhs-fdp-palantir"
title: "英国 NHS 联邦数据平台：3.3 亿英镑买来的争议"
company: "NHS England"
company_hq: "UK"
industry: "public-sector"
sub_industry: "healthcare-administration"
scenario: ["scheduling-optimization", "data-analysis"]
deployment_model: "platform-build"
fde_involved: "unknown"
ai_tech: ["digital-twin", "predictive-ml"]
vendor: ["Palantir Technologies UK（联合体：Accenture、PwC、NECS、Carnall Farrar）"]
scale: "覆盖最多 240 家 NHS 机构；截至 2026-06 有 168 家信托签约"
start_date: "2024"
status: "production"
evidence_grade: "A"
last_verified: "2026-11-10"
metrics:
  - name: "七年合同上限"
    value: "3.3 亿英镑"
    unit: "GBP"
    baseline: "不适用"
    method: "英国卫生部书面声明 HCWS57；首年投入至少 2,560 万英镑。上限非已支出"
    window: "2023-11 ~ 2031-03"
    direction: "cost-down"
  - name: "额外完成手术的患者数"
    value: "10 万+ / 110,078 / 111,589 / 117,539"
    unit: "人"
    baseline: "2024-03 起累计"
    method: "四个数字来自四个官方/半官方渠道，时点不同；同一指标在 12 个月内出现四个版本"
    window: "2024-03 ~ 2026"
    direction: "volume-up"
  - name: "出院延迟下降"
    value: "14% / 约 15%"
    unit: "%"
    baseline: "未设对照组"
    method: "部长答询写 14%，Palantir 博客写约 15%；NHS England 2026-06 自行加注「无法就因果下结论」"
    window: "2024-03 ~ 2026"
    direction: "time-down"
  - name: "28 天内获得癌症检查结果的比例"
    value: "+6.8% / +7%"
    unit: "%"
    baseline: "未披露"
    method: "同上，两个渠道口径略有差异；无对照"
    window: "截至 2026-06"
    direction: "quality-up"
sources:
  - id: "src-uk-hcws57-fdp"
    type: "regulatory-filing"
    grade: "A"
    url: "https://questions-statements.parliament.uk/written-statements/detail/2023-11-21/hcws57"
    publisher: "UK Parliament / DHSC"
    published: "2023-11-21"
    accessed: "2026-11-10"
    note: "合同金额原始出处：七年最多 3.3 亿英镑，首年至少 2,560 万英镑。"
  - id: "src-nhs-fdp-contract"
    type: "official-press-release"
    grade: "B"
    url: "https://www.england.nhs.uk/digitaltechnology/nhs-federated-data-platform/security-privacy/contract-explainer/"
    publisher: "NHS England"
    published: "unknown"
    accessed: "2026-11-10"
    note: "合同说明：仅承诺三年，可延两次两年再延两次一年，潜在结束日 2031-03；覆盖最多 240 家机构。"
  - id: "src-osr-fdp-2026"
    type: "regulatory-filing"
    grade: "A"
    url: "https://osr.statisticsauthority.gov.uk/news/nhs-england-federated-data-platform-fdp-presentation-and-communication-of-information-and-performance-metrics/"
    publisher: "UK Office for Statistics Regulation"
    published: "2026-07-22"
    accessed: "2026-11-10"
    note: "监管结论：NHS England 于 2026-06-06 加入「无法就因果下结论」的限定；要求部长引用数字时清晰准确。本案例最强的一手负面证据。"
  - id: "src-palantir-fdp-blog"
    type: "company-blog"
    grade: "C"
    url: "https://blog.palantir.com/ready-set-build-with-the-nhs-federated-data-platform-41405fa4c226"
    publisher: "Palantir"
    published: "2026-04-30"
    accessed: "2026-11-10"
    note: "厂商博客，注明 data as of end of December 2025；给 110,078 / 297,943 / 约 15% / 6.8%。"
  - id: "src-commons-scitech-2026"
    type: "regulatory-filing"
    grade: "A"
    url: "https://publications.parliament.uk/pa/cm5902/cmselect/cmsctech/61/report.html"
    publisher: "UK House of Commons Science, Innovation and Technology Committee（HC 61）"
    published: "2026-06-03"
    accessed: "2026-11-10"
    note: "建议行使 2027-02 解约条款、12 月底前拿出 fully costed exit plan；记录 Palantir 人员数据访问证词。"
  - id: "src-parliament-wq-3927"
    type: "regulatory-filing"
    grade: "A"
    url: "https://questions-statements.parliament.uk/written-questions/detail/2026-05-21/3927/"
    publisher: "UK Parliament（答询日 2026-06-16）"
    published: "2026-06-16"
    accessed: "2026-11-10"
    note: "部长给成效：10 万+ 额外手术、近 9.4 万癌症路径、出院延迟 -14%、168 家信托签约。"
tags: ["regulated-industry", "metric-definition-war", "data-sovereignty", "vendor-sourced-number", "human-review"]
replicability: 2
human_in_loop: "sampling-audit"
confidence_notes: "金额与合同期限有硬来源，但成效数字既无对照、又被英国统计监管机构认定不能归因；同一指标在 12 个月内出现四个版本"
---

## 1. 一句话摘要

Palantir 领衔的联合体拿下英国 NHS 七年最多 3.3 亿英镑的联邦数据平台合同，官方宣称加快了手术、出院与癌症路径——随后英国统计监管机构要求 NHS 在页面上加注"无法就因果下结论"。

## 2. 业务痛点

NHS England 面对的是全球最庞杂的公共医疗体系之一：

- 各信托（trust）用不同厂商的 EHR，数据无法跨机构流动
- 择期手术等待名单、床位、出院协调、癌症路径各有一套表格
- 出院延迟（delayed discharge）长期占用床位，是系统性瓶颈
- 疫情期间临时建的数据平台证明了"集中看数"有用，但也引发了隐私争议

真正的痛点是：**同一个患者的状态散落在多个机构里，没有一个共同的视图**。

## 3. AI 应用场景

严格说，FDP 的主体**不是生成式 AI**，而是数据平台（Foundry）：

```
输入：各信托的 EHR、等待名单、床位、出院评估、癌症转诊记录
  ↓
处理：统一身份与数据模型 → 跨机构视图 → 在应用层做
      手术室利用率优化、出院协调（OPTICA）、癌症路径追踪
  ↓
输出：可执行的待办清单（哪些患者可以出院、哪台手术室可加台）
  ↓
人工动作：临床与运营团队评估后执行；隐私增强技术环节由另一供应商负责
```

把它写成"AI 平台"会失真。它是**数据基础设施 + 应用层优化**，其中部分组件用到模型，但核心价值在整合。

## 4. 落地方式

- **供应商**：Palantir Technologies UK 领衔的联合体（Accenture、PwC、NECS、Carnall Farrar）；隐私增强技术由 IQVIA 单独中标
- **合同结构**：7 年最多 3.3 亿英镑；但只承诺 3 年，可延 2 年 + 2 年 + 1 年，潜在结束日 2031-03
- **交付形态：未见 FDE 官方表述。** 官方描述是供应商按 NHS England 指示提供平台服务。本库按 `unknown` 处理——这是本案例与 Palantir 商业侧案例的重要区别
- **上线节奏**：2023-11 中标与授标，2024-03 正式生效，2024 年 3–7 月首批迁移
- **治理争议**：涉及患者可识别数据的访问权限，议会专门记录了 Palantir 人员的访问范围证词（"a specific technical permission inside one staging environment"，涉及"fewer than five"员工）

## 5. 可验证成效

| 指标 | 数值 | 口径与基线 | 来源 |
|---|---|---|---|
| 合同上限 | 3.3 亿英镑 / 7 年 | 上限，非支出；首年 ≥2,560 万英镑 | 议会书面声明 HCWS57 |
| 额外完成手术 | 10 万+ | 部长答询，2024-03 起累计 | 议会答询 2026-06-16 |
| 同上（另一版本） | 110,078 | 厂商博客，数据截至 2025-12 | Palantir blog |
| 同上（第三版本） | 111,589 | NHS England 成效页原文 | 经 OSR 与 Foxglove 引用 |
| 出院延迟 | -14% / 约 -15% | 无对照；NHS 自行加注不能归因 | 议会答询 / 厂商博客 |
| 28 天内癌症结果 | +6.8% / +7% | 无对照 | 同上 |
| 签约机构 | 168 家信托 / 24 个 ICB 集群 | 覆盖最多 240 家 | 议会答询 |
| 安全出院人数 | 297,943 | 厂商博客，截至 2025-12 | Palantir blog |

**这一格最重要的不是数字，而是数字旁边的限定语。** NHS England 在 2026-06-06 自行加入："We cannot therefore draw conclusions about cause and effect as other variables have not been controlled for."

## 6. 不可验证或存疑之处

1. **因果性被监管机构正式否定。** 英国统计监管办公室（OSR）2026-07-22 的结案声明记录了 NHS England 加注"无法就因果下结论"，并要求"部长或官方简报引用 FDP 数字时必须清晰准确"。这是本库收录的**最强一手负面证据**。
2. **同一指标四个版本。** "额外手术例数"在 12 个月里出现 10 万+、110,078、111,589、117,539 四个数。它们是不同时点的累计值，跨期拼接会得出不可辩护的结论。
3. **我原本以为 NAO 有专项报告，核实后不存在。** NAO 站内只有一个在研课题（患者记录整合，预计 2026/27 冬季），没有 FDP 专项审计。指出问题的是 OSR，不是 NAO。这一点必须纠正，否则是事实错误。
4. **合同期限两个官方说法不一致。** 议会报告写初始三年期"ends on 15 February 2027"，NHS England 自己的合同说明写"comes up in March 2027"。不要写死某一天。
5. **信托层面的反证。** 有 FOI 调查称，29 家被 NHS England 列为"已实现效益"的信托表示平台未上线或未使用其应用；NHS England 回应称部分仅为后台数据提交。此为我读到的媒体转述，未取得原始 FOI 文件。
6. **决策早于证据。** 独立评估（Imperial College，2026-02 委托）预计在续约决定之后才发布，而政府须在 2026-12 前知会是否续约。
7. **它不是生成式 AI。** 用这条案例论证"LLM 在企业落地"是错的；它属于数据平台与运营优化。

## 7. 可复用要点

1. **公共部门项目要把"合同"与"成效"分开审计。** 金额可以精确到英镑，成效却可能连因果都立不住。写文章时这两件事必须分节。
2. **看监管机构，不看新闻稿。** OSR 的一页声明，比十篇宣传稿有信息量。
3. **指标会漂移，引用必须带截止日。** 同一指标四个版本，是因为季度更新 + 口径微调。
4. **解约条款是项目健康度的晴雨表。** 议会建议行使解约权、要求 12 月底前拿出退出成本方案——这比任何满意度调查都真实。
5. **数据访问权限是这类项目的真正战场。** 技术上线容易，谁能在什么权限下看到什么数据，才是争议核心。

## 8. 引用边界

✅ 可以说：
- "英国 NHS England 与 Palantir 领衔的联合体签订七年最多 3.3 亿英镑的联邦数据平台合同，仅承诺三年，潜在结束日 2031 年 3 月"
- "官方称 2024 年 3 月以来额外完成逾 10 万台手术、出院延迟下降约 14%（截至 2026-06，无对照）"
- "英国统计监管办公室 2026 年 7 月指出，NHS England 已在成效页加注'无法就因果下结论'，并要求官方引用数字时清晰准确"
- "英国下议院科技委员会建议行使 2027 年 2 月的解约条款"

❌ 不能说：
- "英国国家审计署（NAO）认定 FDP 效益未量化"（NAO 没有发布 FDP 专项报告，这是 OSR 的结论）
- "AI 让 NHS 多做了 10 万台手术"（无对照，监管机构明确否定因果）
- "Palantir 已从 NHS 赚走 3.3 亿英镑"（是七年上限，实际支出远低于此）
- 把 FDP 当作生成式 AI 案例

## 9. 来源

- UK Parliament, *NHS Federated Data Platform: Contract Award (HCWS57)*, 2023-11-21
- NHS England, *Contract explainer*（无发布日期，内容更新至 2026）
- Office for Statistics Regulation, *NHS England FDP – presentation and communication of information and performance metrics*, 2026-07-22
  关键句："We cannot therefore draw conclusions about cause and effect as other variables have not been controlled for"
- UK Parliament, *Written Question 3927*（答询 2026-06-16）
- Palantir Blog, *Ready, Set, Build with the NHS Federated Data Platform*, 2026-04-30
- House of Commons Science, Innovation and Technology Committee, *Rewiring the state: Delivering digital government (HC 61)*, 2026-06-03
- National Audit Office, *Integrating patient records*（在研课题，预计 Winter 2026/27，非 FDP 专项报告）
