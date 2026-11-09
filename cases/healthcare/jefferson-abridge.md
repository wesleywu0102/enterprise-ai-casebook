---
id: "healthcare-jefferson-abridge"
title: "Jefferson Health：5,234 名临床医生的门诊文书助手"
company: "Jefferson Health"
company_hq: "US"
industry: "healthcare"
sub_industry: "hospital-system"
scenario: ["clinical-documentation"]
deployment_model: "vendor-copilot"
fde_involved: "none"
ai_tech: ["ASR", "LLM"]
vendor: ["Abridge"]
scale: "5,234 名配置账号的临床医生；283,028 次门诊；1,802 名活跃使用者"
start_date: "2025"
status: "scaled"
evidence_grade: "A"
last_verified: "2026-11-09"
metrics:
  - name: "现病史与评估计划段落的书写投入"
    value: "-84%"
    unit: "%"
    baseline: "部署前同一批医生的同类段落书写工作量"
    method: "平台内工作量评分（effort），1,802 名活跃使用者；单次就诊平均录音 14.9 分钟"
    window: "2025-07-01 ~ 2025-12-31"
    direction: "effort-down"
  - name: "下班后文书时间（pajama time）"
    value: "-8.9% / -16.6%"
    unit: "%"
    baseline: "部署前同队列的 Epic Signal 基线"
    method: "Epic Signal 系统日志，两个实施批次分别统计（对应两套遗留 EHR 实例）"
    window: "2025-07-01 ~ 2025-12-31"
    direction: "time-down"
  - name: "每次预约的文书时长"
    value: "-10.5% / -17.3%"
    unit: "%"
    baseline: "同上"
    method: "Epic Signal，两批次分别统计"
    window: "2025-07-01 ~ 2025-12-31"
    direction: "time-down"
  - name: "病历关闭时长"
    value: "-25.3% / -39.3%"
    unit: "%"
    baseline: "同上"
    method: "Epic Signal，两批次分别统计"
    window: "2025-07-01 ~ 2025-12-31"
    direction: "time-down"
  - name: "高级实践护士（APC）与医生的日文书时间差"
    value: "APC -9.9 分钟/天；医生 -3.8 分钟/天"
    unit: "min/day"
    baseline: "各自部署前的日文书时间"
    method: "两组对比，P<0.001；APC 降幅约为医生的 2.5 倍"
    window: "2025-07-01 ~ 2025-12-31"
    direction: "time-down"
sources:
  - id: "src-nejm-cat-26-0269"
    type: "peer-reviewed"
    grade: "A"
    url: "https://catalyst.nejm.org/doi/full/10.1056/CAT.26.0269"
    publisher: "NEJM Catalyst Innovations in Care Delivery"
    published: "2026"
    accessed: "2026-11-09"
    note: "作者披露：Jefferson Health 按标准商业合同采购 Abridge，Abridge 未参与设计、分析、解读与写作，未提供资金/数据/技术支持；研究无外部资助"
tags: ["human-review", "floor-raising", "regulated-industry", "evals-in-production"]
replicability: 4
human_in_loop: "review-before-send"
confidence_notes: "单家医疗系统的观察性研究，无随机对照；患者体验的组间差异在院内比较后大多不显著，存在医生自选择"
---

## 1. 一句话摘要

一家拥有 5,234 名配置账号的医疗系统，在门诊全面铺开环境录音式文书助手后，病历书写投入下降 84%、下班后文书时间下降 9%–17%，且增益集中在原本文书负担最重的群体。

## 2. 业务痛点

美国门诊医生的电子病历（EHR）文书工作长期侵占诊疗与休息时间：

- 每次门诊结束后要手工整理现病史（HPI）与评估计划（A&P），单次就诊的文书时间以十分钟计
- 大量文书被推到下班后完成，即业内所称 "pajama time"（睡衣时间）
- 病历关闭（chart closure）延迟数天，影响随访、计费与合规
- Jefferson Health 在一年前刚完成组织合并，同时运行两套遗留 EHR 实例，文书流程本身不统一

这意味着部署前不存在"统一的基线"，两个实施批次必须分开统计——这也是本案例统计上最值得注意的地方。

## 3. AI 应用场景

```
输入：医患门诊对话的实时录音（单次平均 14.9 分钟）
  ↓
处理：ASR 转写 → LLM 按病历结构起草 HPI 与 A&P → 写入 EHR 草稿
  ↓
输出：结构化病历草稿，医生在 EHR 内编辑
  ↓
人工动作：医生逐份审阅、修改、签字（系统不允许直接提交）
```

人机分工是"AI 起草 + 医生定稿"，医生不能跳过审阅。这是医疗场景的硬约束，也是这条案例 `replicability` 没有给满分的原因之一。

## 4. 落地方式

- **交付方**：Abridge 作为 SaaS 供应商，按标准商业合同供货；无 FDE 驻场记录
- **推广方式**：自愿使用（voluntary, clinician-centered adoption），不做强制配额
- **统计口径**：以"≥50 次环境录音就诊且使用率≥10%"定义活跃使用者，最终进入效率分析的队列为 637 名医生
- **治理**：以明确的组织目的 + 高管赞助 + EHR 原生计量（Epic Signal）为三大支柱
- **周期**：部署满 1 年后开展评估，取 6 个月窗口数据

值得注意的组织选择：**没有把使用率当 KPI**。研究把"自愿采用"写进方法论，因为这直接决定了后面看到的效应是不是自选择造成的。

## 5. 可验证成效

| 指标 | 数值 | 口径与基线 | 来源 |
|---|---|---|---|
| 病历书写投入（HPI+A&P） | -84%（均值） | 平台内工作量评分，1,802 名活跃使用者 | NEJM Catalyst |
| 下班后文书时间 | -8.9% / -16.6% | Epic Signal，两批次分列 | 同上 |
| 每次预约文书时长 | -10.5% / -17.3% | Epic Signal，两批次分列 | 同上 |
| 病历关闭时长 | -25.3% / -39.3% | Epic Signal，两批次分列 | 同上 |
| 改善最快四分位 | 每排班日回补近 17 分钟 pajama time；关闭时长缩短 >36 小时 | 分组分析 | 同上 |
| APC vs 医生 | -9.9 vs -3.8 分钟/天 | P<0.001，剂量-反应关系显著 | 同上 |
| 患者体验 | 各维度等于或优于未使用者 | 两套问卷工具；院内比较后大多不显著 | 同上 |

## 6. 不可验证或存疑之处

1. **观察性研究，无随机对照。** 自愿采用意味着使用者本身可能更年轻、更熟悉技术、文书负担更重。作者用院内比较（within-provider）处理了这一点，但院内比较后患者体验差异大多不显著——说明部分"患者体验更好"的结论站不住。
2. **84% 是"投入（effort）"而非"时间"。** 这是平台内的工作量评分，不是分钟数。把它写成"节省 84% 时间"是错的，也是最常见的转述错误。
3. **时间节省的绝对值不大。** 每次预约文书时长只降 10%–17%，pajama time 降 9%–17%。同期的 JAMA 述评明确指出：如果把审阅和编辑时间算进去，每班净节省有限，主要收益是**认知负荷下降**而非工时。
4. **两个批次数字并列，不能取平均。** 两个批次对应两套遗留 EHR 和历史文书项目经验，直接平均会掩盖实施差异。
5. **单一医疗系统，且刚刚合并。** 合并期的流程重组本身就可能改善文书指标，无法完全归因于 AI。

## 7. 可复用要点

1. **先量测，再推广。** 用 EHR 自带的日志（Epic Signal）做基线，而不是发问卷问"你觉得省了多少时间"。
2. **不要用使用率考核。** 强制配额会污染效果评估，也会招致临床反弹。
3. **预期收益是"抬高下限"。** 负担最重的人（APC、住院医、女性医生、基层与内科）获益最大。若管理层期待"人人都省一小时"，落地后一定失望。
4. **保留医生签字环节。** 病历是法律文件，AI 只能起草。
5. **把评估窗口设成 6 个月以上。** 上线首月的数据受新奇效应影响，通常高估。

## 8. 引用边界

✅ 可以说：
- "Jefferson Health 的环境 AI 文书助手使病历书写投入下降 84%，下班后文书时间下降 9%–17%（NEJM Catalyst，2026）"
- "增益集中在文书负担最重的群体，是一种'抬高下限'的效应"

❌ 不能说：
- "AI 让医生节省了 84% 的时间"（偷换 effort 与 time）
- "AI 减少了医生 84% 的工作量"（口径错误）
- "患者体验显著改善"（院内比较后大多不显著）
- "证明 AI 文书助手能缓解医生短缺"（论文未涉及人力供给）

## 9. 来源

- NEJM Catalyst, *Ambient AI as a Tool for Returning Time to Care*, 2026. DOI: 10.1056/CAT.26.0269
  关键句："the platform delivered an 84% mean effort reduction in completion of history of present illness and assessment and plan note sections"
  利益冲突："Abridge had no role in the design, analysis, interpretation, or writing of the manuscript"
- 同期述评：JAMA, *Ambient AI Scribes and the Quintuple Aim: What Is Counted—and What Matters*, 2026;335(16):1393-1395
