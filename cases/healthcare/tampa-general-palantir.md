---
id: "healthcare-tampa-general-palantir"
title: "Tampa General：把床位调度交给 Palantir 驻场团队"
company: "Tampa General Hospital"
company_hq: "US"
industry: "healthcare"
sub_industry: "academic-medical-center"
scenario: ["scheduling-optimization", "clinical-decision"]
deployment_model: "platform-build"
fde_involved: "vendor-embedded"
ai_tech: ["digital-twin", "agent", "predictive-ml"]
vendor: ["Palantir"]
scale: "单个学术医疗中心；2022 年起覆盖院内床位/转院调度，2024 年扩至 AIP；床位数未披露"
start_date: "2021"
status: "scaled"
evidence_grade: "B"
last_verified: "2026-11-10"
metrics:
  - name: "患者安置（patient placement）耗时"
    value: "-83%"
    unit: "%"
    baseline: "未披露（无部署前后同口径时间序列）"
    method: "医院与 Palantir 联合新闻稿给出的实测值；未说明统计期、样本量与计算方式"
    window: "截至 2024-06"
    direction: "time-down"
  - name: "PACU（麻醉复苏室）滞留"
    value: "-28%"
    unit: "%"
    baseline: "未披露"
    method: "同上，联合新闻稿口径；无对照组"
    window: "截至 2024-06"
    direction: "time-down"
  - name: "脓毒症患者平均住院日"
    value: "-30%"
    unit: "%"
    baseline: "未披露"
    method: "联合新闻稿口径；注意同一家厂商的另一页面把「30%」写成护理人力配比改善，指标名不一致"
    window: "截至 2024-06"
    direction: "time-down"
  - name: "48 小时脓毒症死亡率"
    value: "近 -68%"
    unit: "%"
    baseline: "2022 年项目启动前"
    method: "医院官网自报的运营统计，非对照试验；同一页面称累计「挽救逾 1,000 条生命」"
    window: "2022 ~ 2026-10"
    direction: "quality-up"
  - name: "MRI 检查周转时间"
    value: "+30%"
    unit: "%"
    baseline: "未披露"
    method: "院方高管在 2025-07 接受行业媒体采访时口述；非书面披露"
    window: "2025-07"
    direction: "time-down"
sources:
  - id: "src-palantir-tgh-2024"
    type: "official-press-release"
    grade: "B"
    url: "https://investors.palantir.com/news-details/2024/Tampa-General-Hospital-Selects-Palantirs-AI-Software-to-Power-Connected-Care-Coordination-Extending-Long-Term-Partnership/"
    publisher: "Palantir Technologies / Business Wire"
    published: "2024-06-05"
    accessed: "2026-11-10"
    note: "联合新闻稿（客户署名）。给出 83%/28%/30% 三个数字，均无基线、无统计口径。"
  - id: "src-tgh-newsroom-2026"
    type: "official-press-release"
    grade: "B"
    url: "https://www.tgh.org/news/tgh-press-releases/2026/october/tampa-general-hospital-recognized-among-worlds-best-smart-hospitals-for-2027-by-newsweek"
    publisher: "Tampa General Hospital"
    published: "2026-10-22"
    accessed: "2026-11-10"
    note: "客户官网自述：2022 年以来逾 1,000 条生命、48 小时脓毒症死亡率近 -68%。是累计计数而非比率。"
  - id: "src-palantir-impact-tgh"
    type: "official-case-study"
    grade: "C"
    url: "https://www.palantir.com/impact/tampa-general-hospital/"
    publisher: "Palantir"
    published: "unknown"
    accessed: "2026-11-10"
    note: "厂商 impact 页；把 30% 描述为 nurse staffing ratio 改善，与联合新闻稿的「脓毒症住院日」不是同一指标。"
  - id: "src-hitnews-tgh-2025"
    type: "media-report"
    grade: "D"
    url: "https://www.healthcareitnews.com/news/tampa-generals-investment-ai-enabled-care-coordination-software-saves-nearly-600-lives"
    publisher: "Healthcare IT News"
    published: "2025-07-15"
    accessed: "2026-11-10"
    note: "转述院方高管：累计近 600 条生命、MRI 周转 +30%；并披露上一代脓毒症工具曾被 FDA 判定为受监管器械而停用。"
tags: ["fde-model", "co-delivery", "regulated-industry", "human-review", "exec-sponsorship"]
replicability: 3
human_in_loop: "review-before-send"
confidence_notes: "所有成效均为单院前后对比、无同期对照；且「30%」在客户与厂商两个官方渠道指向不同指标，是本案例最容易被拆的地方"
---

## 1. 一句话摘要

一家美国学术医疗中心让 Palantir 的工程师常驻院内，把床位、转院、手术排程和脓毒症预警搬进同一个数据平台，患者安置耗时降 83%、脓毒症住院日降 30%——但所有数字都没有基线。

## 2. 业务痛点

Tampa General 是佛罗里达州的大型学术医疗中心，也是当地唯一的一级创伤中心，常年承接大量转院。部署前的状态是典型的"系统各自为政"：

- 床位、转院、手术、护理排班分散在不同系统，靠电话和人工表格协调
- 转院请求要在多个科室之间来回确认，患者在各环节之间"悬空"
- 脓毒症识别依赖护士按流程定时筛查，发现晚、启动抗生素晚
- 容量压力在飓风季等突发事件时集中爆发

这类问题在学术医疗中心很常见，真正的瓶颈往往不是模型精度，而是**没有一张全院的实时状态图**。

## 3. AI 应用场景

```
输入：EHR、床位管理、转院请求、手术排程、监护数据
  ↓
处理：统一到 Foundry 做数据整合（2021 起）→ 2024 年叠加 AIP 做
      床位/转院决策建议、脓毒症风险评分、护理需求预测
  ↓
输出：待安置患者清单 + 建议去向、脓毒症预警、排班建议
  ↓
人工动作：床位协调员确认并执行；临床团队复核预警后启动治疗
```

关键在于输出不是"报告"，而是**排进当天工作清单的待办**。院方的说法是：以前只能当天临时排班，现在可以提前数天甚至数周规划。

## 4. 落地方式

- **供应商**：Palantir。2021 年起用 Foundry 做数据底座，2024-06 宣布扩到 AIP，命名为 "Care Coordination Operating System"
- **交付形态：FDE 驻场。** 这是本案例入库的核心原因——TGH 的数字与创新官在公开表述里说 Palantir 团队 "embedded themselves within our organization"；行业媒体报道时直接使用了 "Palantir's forward-deployed engineers" 这一说法
- **组织配套**：医院侧建了专门的运营指挥团队（CareComm），把床位协调员、护理管理、数据分析放在同一个物理空间
- **应急场景的验证**：2022 年飓风 Ian 期间，团队在灾后 24 小时内交付了一个应急调度应用——这是"平台+驻场"组合相对纯采购的最大差别

## 5. 可验证成效

| 指标 | 数值 | 口径与基线 | 来源 |
|---|---|---|---|
| 患者安置耗时 | -83% | 联合新闻稿，无基线、无统计期 | Palantir IR 2024-06-05 |
| PACU 滞留 | -28% | 同上 | 同上 |
| 脓毒症平均住院日 | -30% | 同上 | 同上 |
| 48 小时脓毒症死亡率 | 近 -68% | 院方自报，无对照 | TGH 新闻室 2026-10-22 |
| 累计"挽救生命" | 逾 1,000 条 | 累计计数，非比率 | 同上 |
| MRI 周转 | +30% | 院方高管口头表述 | Healthcare IT News 2025-07 |

累计数的时间序列本身值得记一笔：2025-07 是"近 600 例"，2025-12 是"over 700"，2026-10 是"more than 1,000"。这是随装机范围扩大而增长的计数，不是疗效持续改善的证据。

## 6. 不可验证或存疑之处

1. **83% 没有基线。** 联合新闻稿只给结果值，不说部署前是多少分钟、统计了多少例、用什么方法测。这类数字可以引用，但只能标"医院与厂商联合披露"，不能当独立验证。
2. **"30%" 在同两个官方渠道指向不同指标。** 联合新闻稿与 TGH 官网说 30% 是脓毒症住院日；Palantir 的 impact 页说 30% 是护理人力配比改善。两个都对不了，引用时必须写明版本。
3. **"挽救 1,000 条生命"是累计计数。** 它随时间自然增长，且"挽救"的判定标准（预期死亡风险 vs 实际死亡）未公开。把它写成"死亡率下降"是偷换。
4. **无同期对照。** 单院前后对比无法排除：同期医院合并、转院政策变化、脓毒症诊疗指南更新、护理人力增加。
5. **监管反复。** 院方在 2025-07 的采访中自述，其上一代脓毒症工具曾因被 FDA 判定为受监管医疗器械而被迫停用。这说明同类临床 AI 的合规路径并不稳定。
6. **FDE 驻场的成本未披露。** 合同金额、驻场人数、驻场时长都没有公开，无法判断这套模式对中等规模医院是否可负担。

## 7. 可复用要点

1. **FDE 的价值在"把系统缝起来"，不在模型。** 这家医院的瓶颈是跨系统协调，不是预测精度。想复制的话，先问"我有没有一张全院实时状态图"，而不是"我要用哪个模型"。
2. **先做数据底座，再做 AI。** Foundry 2021 年进场、AIP 2024 年才上，中间隔了三年。跳过这一步直接上 agent，通常得到的是一个能聊天但不敢用的东西。
3. **让输出进入班次清单。** 预警如果只发到邮箱，一周内就没人看了。
4. **应急场景是最好的验收测试。** 飓风季的真实压力测试，比任何 demo 都能暴露系统边界。
5. **临床部分必须留人复核。** 脓毒症预警涉及用药，属于高风险决策。

## 8. 引用边界

✅ 可以说：
- "Tampa General 与 Palantir 联合披露：患者安置耗时下降 83%、PACU 滞留下降 28%、脓毒症患者住院日下降 30%（2024-06，未公开基线）"
- "该院官网称 2022 年以来累计挽救逾 1,000 条生命、48 小时脓毒症死亡率下降近 68%"
- "Palantir 工程师以常驻方式参与院内系统改造，属于典型的 FDE 交付"

❌ 不能说：
- "AI 让床位周转效率提升 83%"（原文是"安置耗时"，不是周转率）
- "AI 使脓毒症死亡率下降 68%"（原文限定 48 小时窗口，且是院方自报）
- "证明了 Palantir FDE 模式可复制到医院"（单案例，无成本数据）
- "这家的 AI 通过了 FDA 认证"（院方明确说过上一代工具因监管问题停用）

## 9. 来源

- Palantir IR / Business Wire, *Tampa General Hospital Selects Palantir's AI Software to Power Connected Care Coordination*, 2024-06-05
  关键句："Tampa General cut by 83% the amount of time required to place patients and post anesthesia care unit (PACU) holds declined 28%."
- TGH 新闻室, *Tampa General Hospital Recognized Among World's Best Smart Hospitals for 2027*, 2026-10-22
  关键句："helped save more than 1,000 lives, reduced 48-hour sepsis mortality by nearly 68%"
- Palantir impact 页（无日期）：同一数字被表述为护理配比改善，需与上条区分
- Healthcare IT News, *Tampa General's investment in AI-enabled care coordination software saves nearly 600 lives*, 2025-07-15
