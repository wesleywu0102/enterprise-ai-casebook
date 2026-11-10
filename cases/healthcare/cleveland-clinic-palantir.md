---
id: "healthcare-cleveland-clinic-palantir"
title: "Cleveland Clinic：虚拟指挥中心，四条数字都来自厂商"
company: "Cleveland Clinic"
company_hq: "US"
industry: "healthcare"
sub_industry: "academic-medical-center"
scenario: ["scheduling-optimization"]
pattern: ["ops-orchestration"]
deployment_model: "platform-build"
fde_involved: "vendor-embedded"
ai_tech: ["digital-twin", "predictive-ml"]
vendor: ["Palantir"]
scale: "主院区 + Hillcrest、South Pointe、Euclid 三家区域医院；三个模块（Hospital 360、Staffing Matrix、OR Stewardship）"
start_date: "2023"
status: "production"
evidence_grade: "B"
last_verified: "2026-11-10"
metrics:
  - name: "床位容量测算耗时"
    value: "-75%"
    unit: "%"
    baseline: "未披露"
    method: "厂商 case study 引用客户数据；未给统计期、样本量与基线定义"
    window: "未披露"
    direction: "time-down"
  - name: "日均转院收治量"
    value: "+10% 以上"
    unit: "%"
    baseline: "未披露"
    method: "同上。注意二手榜单另给 7.6%，与厂商页不一致"
    window: "未披露"
    direction: "volume-up"
  - name: "转院后分床效率"
    value: "+20%"
    unit: "%"
    baseline: "未披露"
    method: "厂商 case study 引用客户数据；同一页面给了四个数字，但只有这一条附了客户高管引语"
    window: "未披露"
    direction: "time-down"
  - name: "每名患者日均急诊滞留"
    value: "约 -1 小时"
    unit: "小时/人/天"
    baseline: "未披露"
    method: "同上；这是四个数字里唯一带绝对值的，可信度相对高"
    window: "未披露"
    direction: "time-down"
  - name: "护理排班预测滚动窗口"
    value: "6 周"
    unit: "周"
    baseline: "不适用"
    method: "护理总监引语；这是规划前置期，不是模型精度"
    window: "2023"
    direction: "adoption"
sources:
  - id: "src-palantir-cleveland-2023"
    type: "official-press-release"
    grade: "B"
    url: "https://investors.palantir.com/news-details/2023/Cleveland-Clinic-and-Palantir-Technologies-Partner-to-Improve-Hospital-Performance-Through-Virtual-Command-Center/"
    publisher: "Palantir IR / PRNewswire"
    published: "2023-01-19"
    accessed: "2026-11-10"
    note: "多年合作公告，明确系统基于 Foundry 而非 AIP，并称已在用（is in use today）。"
  - id: "src-palantir-impact-cleveland"
    type: "official-case-study"
    grade: "C"
    url: "https://www.palantir.com/impact/cleveland-clinic"
    publisher: "Palantir"
    published: "unknown"
    accessed: "2026-11-10"
    note: "厂商 impact 页，四条数字的唯一出处；含客户高管署名引语与 AIPCon 2023 表述。"
tags: ["fde-model", "vendor-sourced-number", "co-delivery", "regulated-industry"]
replicability: 3
human_in_loop: "escalation-only"
confidence_notes: "四条成效数字只有厂商页面一个出处，客户官网与年报均无对应披露；且常被误标为 AIP 案例，实际是 Foundry"
---

## 1. 一句话摘要

Cleveland Clinic 与 Palantir 共建"虚拟指挥中心"，把床位、转院、急诊滞留和护理排班放进一个指挥台，床位测算耗时降 75%——四条数字全部出自 Palantir 自己的案例页。

## 2. 业务痛点

大型医疗系统的容量管理是典型的"多点同时决策"问题：

- 转院患者从申请到真正有床位，中间要经过多次电话确认
- 急诊滞留（ED hold）让急诊床位无法周转，救护车开始排队
- 护理排班按周做，需求预测靠护士长经验
- 手术室利用率不均，骨科等科室存在空台

Cleveland Clinic 的说法是：问题不在缺数据，而在"没有一个地方能同时看到全院状态"。

## 3. AI 应用场景

```
输入：EHR 床位状态、转院申请、急诊登记、手术排程、护理需求历史
  ↓
处理：Foundry 上做统一数据模型 → 容量测算、转院优先级排序、
      按单元逐周护理需求预测
  ↓
输出：床位分配建议、转院收治清单、排班建议、手术室调配建议
  ↓
人工动作：指挥中心调度员与护士长确认执行
```

三个模块分工：Hospital 360（全院容量与转院）、Staffing Matrix（护理排班）、OR Stewardship（手术室使用）。

## 4. 落地方式

- **供应商**：Palantir，**基于 Foundry**（新闻稿原文："Built on the Palantir Foundry, the Virtual Command Center…"）。**不是 AIP**
- **交付形态**：联合开发。医院提供业务专家参与产品设计，Palantir 团队与其 side-by-side 工作（其首席数据官在 AIPCon 2023 的表述）。本库判为 `vendor-embedded`，但严格说这是"共创"，不是"厂商派人驻场接需求"
- **上线范围**：2023-01 宣布多年合作时，Hospital 360 与 Staffing Matrix 已在主院区及 Hillcrest、South Pointe、Euclid 使用；OR Stewardship 在俄亥俄州骨科与头颈科室使用
- **注意**：Cleveland Clinic 后来另有环境记录等临床 AI 项目，与这个指挥中心不是一回事，不要混为一谈

## 5. 可验证成效

| 指标 | 数值 | 口径与基线 | 来源 |
|---|---|---|---|
| 床位容量测算耗时 | -75% | 厂商页，无基线无统计期 | Palantir impact |
| 日均转院收治 | +10% 以上 | 同上 | 同上 |
| 转院后分床效率 | +20% | 同上 | 同上 |
| 每人日均急诊滞留 | 约 -1 小时 | 同上 | 同上 |
| 护理排班预测窗口 | 6 周 | 客户高管引语，规划前置期 | 同上 |

**这一格必须配上警告**：四条数字只有厂商一个出处。我没有找到 Cleveland Clinic 新闻室或年报里的对应披露。

## 6. 不可验证或存疑之处

1. **单一来源。** 四条数字全部来自 Palantir 的 impact 页。虽然页面附了客户高管署名引语，但客户自己从未公开发布过这些数字。
2. **二手数字打架。** 有行业榜单（Becker's）另给一组数："转院量 +7.6%"、"骨科空台时间 -40%"。与厂商页的"+10% 转院收治"数值和口径都不一致，未经一手确认，本库不采用。
3. **无对照组、无统计期。** 四条都是"改善了多少"，但不说改善前后各是多少、统计了几个月。
4. **常被误标为 AIP。** 这是 Foundry 项目。把 2023 年的 Foundry 案例写成"Palantir AIP 的生成式 AI 落地"是常见错误。
5. **急诊滞留"1 小时"要看分母。** 如果分母是全院每天几百名患者，1 小时/人的累计效应可观；但这仍是厂商给的单点值。

## 7. 可复用要点

1. **指挥中心模式的前提是"先有一个院子"。** 多院区、多系统的机构收益最大；单院区小医院做同样的东西，复杂度收益比不划算。
2. **让业务专家进产品设计。** Cleveland Clinic 派了运营与护理专家参与共创，这比"提需求—等交付"有效得多。
3. **排班预测的价值在"提前量"，不在"精度"。** 6 周滚动窗口让护士长能提前换班，这比把预测误差从 8% 降到 6% 更有用。
4. **FDE 团队要有退场机制。** 联合开发的终点是客户自己能改，否则就是长期外包。

## 8. 引用边界

✅ 可以说：
- "Cleveland Clinic 与 Palantir 共建基于 Foundry 的虚拟指挥中心，据 Palantir 案例页，床位容量测算耗时下降 75%、日均转院收治增加 10% 以上、每人日均急诊滞留减少约 1 小时"
- "该系统 2023 年 1 月宣布时已在主院区及三家区域医院使用"

❌ 不能说：
- "Cleveland Clinic 官方确认这些数字"（客户官网无对应披露）
- "这是 Palantir AIP 的生成式 AI 案例"（是 Foundry）
- "急诊滞留下降 1 小时意味着急诊拥挤缓解"（单指标，未涉及救护车排队等结果）
- "骨科空台时间下降 40%"（二手数字，与本库采用的口径不一致）

## 9. 来源

- Palantir IR / PRNewswire, *Cleveland Clinic and Palantir Technologies Partner to Improve Hospital Performance Through Virtual Command Center*, 2023-01-19
  关键句："Built on the Palantir Foundry, the Virtual Command Center…"，并称系统 "is in use today"
- Palantir impact 页（无发布日期）：四条成效数字与客户高管引语
  关键句："75% reduction in time spent calculating bed capacity" / ">10% increase in daily hospital transfer admissions"
