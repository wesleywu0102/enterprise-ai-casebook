---
id: "healthcare-providence-dragon-copilot"
title: "Providence：1,547 名医生的环境录音助手，效应量只有这么点"
company: "Providence"
company_hq: "US"
industry: "healthcare"
sub_industry: "hospital-system"
scenario: ["clinical-documentation"]
pattern: ["ambient-documentation"]
deployment_model: "vendor-copilot"
fde_involved: "none"
ai_tech: ["ASR", "LLM"]
vendor: ["Microsoft (Nuance Dragon Copilot)"]
scale: "1,547 名活跃使用者；16,149 个观察月；覆盖 7 个州"
start_date: "2023-07"
status: "scaled"
evidence_grade: "A"
last_verified: "2026-11-09"
metrics:
  - name: "每次预约的文书时间"
    value: "7.1 → 6.1 分钟（中位数）"
    unit: "min"
    baseline: "使用者启用前的自身基线"
    method: "EHR 元数据；即时效应 β=-0.26 分钟（95%CI -0.41~-0.11），持续效应 β=-0.04（-0.08~0.00，跨零）"
    window: "2023-07 ~ 2025-03"
    direction: "time-down"
  - name: "下班后文书时间"
    value: "22.0 → 20.6 分钟（中位数）"
    unit: "min"
    baseline: "同上"
    method: "即时效应不显著（β=0.15，跨零）；持续效应 β=-0.38 分钟（-0.69~-0.07）"
    window: "2023-07 ~ 2025-03"
    direction: "time-down"
  - name: "相对价值单位（RVU）"
    value: "+7.40（即时）"
    unit: "RVU"
    baseline: "同上"
    method: "即时 β=7.40（0.80~14.0）；持续效应跨零。门诊量未见增加"
    window: "2023-07 ~ 2025-03"
    direction: "volume-up"
sources:
  - id: "src-jama-netw-open-2026"
    type: "peer-reviewed"
    grade: "A"
    url: "https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2849634"
    publisher: "JAMA Network Open 2026;9(5):e2615762"
    published: "2026-05"
    accessed: "2026-11-09"
    note: "观察性研究，1,547 名活跃使用者、16,149 观察月；同时段无未使用者对照组，采用使用者自身前后对比"
  - id: "src-providence-blog"
    type: "company-blog"
    grade: "B"
    url: "https://blog.providence.org/national-news/providence-study-finds-ai-ambient-listening-tool-modestly-reduces-documentation-burden-improves-provider-efficiency"
    publisher: "Providence"
    published: "2026-05-29"
    accessed: "2026-11-09"
    note: "机构自述，用词为 modest（温和），未夸大"
tags: ["human-review", "novelty-decay", "regulated-industry"]
replicability: 4
human_in_loop: "review-before-send"
confidence_notes: "无同期对照组，前后对比可能混入季节性、人员结构变化；效应量小，单看数字容易被解读为'没用'"
---

## 1. 一句话摘要

同为大尺度环境 AI 文书部署，Providence 用 1,547 名医生、16,149 个观察月算出的结论是：每次预约省 1 分钟，下班后文书时间基本没变——一个故意保留的"效应量反例"。

## 2. 业务痛点

与所有美国医疗系统相同：文书占用诊疗时间、下班后补病历、病历关闭延迟。Providence 是一家社区型医疗系统（非学术医学中心），资源与流程标准化程度都低于学术系统，这类机构在美国占多数，但既往研究大多在学术中心做。

## 3. AI 应用场景

```
输入：门诊对话（环境录音）
  ↓
处理：Dragon Copilot 转写并按模板生成病历草稿
  ↓
输出：EHR 内草稿
  ↓
人工动作：医生逐份编辑、签字
```

与 Jefferson Health 案例形态一致，差别在于供应商（Microsoft/Nuance）和实施环境。

## 4. 落地方式

- 供应商 SaaS + EHR 内嵌，无 FDE 驻场
- 覆盖 7 个州、多个专科，以基层医疗为主（近三分之二）
- 采用完全自愿使用；"活跃使用者"定义为当月使用 ≥25 次接诊
- 用 EHR 元数据（而非自报问卷）做前后对比

## 5. 可验证成效

| 指标 | 数值 | 口径与基线 | 来源 |
|---|---|---|---|
| 每次预约文书时间 | 中位数 7.1 → 6.1 分钟 | 使用者自身前后；即时 β=-0.26 分钟 | JAMA Netw Open |
| 下班后文书时间 | 中位数 22.0 → 20.6 分钟 | 即时效应不显著；持续 β=-0.38 分钟 | 同上 |
| RVU | 即时 +7.40，持续不显著 | 门诊量未增加，增量来自单次接诊计费 | 同上 |
| 机构定性结论 | "improvements were modest" | 原文用 modest 一词 | Providence 官方博客 |

## 6. 不可验证或存疑之处

1. **没有同期对照组。** 前后对比无法排除季节性（冬季门诊量高、文书时间长）与人员结构变化。
2. **持续效应几乎全部跨零。** 除下班后文书时间外，多数指标的持续效应置信区间包含 0。也就是说，好处主要出现在刚启用时，随后衰减——这与"新奇效应"一致。
3. **不能与 Jefferson 的数字直接对比。** 两家的基线、专科结构、EHR 实例、活跃使用者定义都不同。把它们放在一张图里比较，是典型的跨案例误用。
4. **RVU 上升不等于效率提升。** 门诊量没增加，RVU 上升可能只是因为病历写得更完整、编码更充分——这是收入效应，不是时间效应。

## 7. 可复用要点

1. **先想清楚"要省时间还是要省心力"。** 这条案例支持后者：时间只省 1 分钟，但机构强调的是认知负荷。
2. **上线 3 个月和上线 18 个月的数据要分开报。** 否则会把新奇效应当成长期收益。
3. **社区医院的结论未必能套到学术中心，反之亦然。** 选参照对象时先对齐机构类型。
4. **用元数据，不用自报。** 自报的"每天省 2 小时"在日志数据面前普遍缩水 60% 以上。

## 8. 引用边界

✅ 可以说：
- "在 Providence 的 1,547 名使用者中，环境 AI 使每次预约文书时间从 7.1 分钟降到 6.1 分钟，下班后文书时间基本持平（JAMA Netw Open，2026）"
- "大样本真实世界研究显示的效应量，普遍小于厂商案例页宣传的量级"

❌ 不能说：
- "AI 文书助手没用"（有统计显著的改善，只是幅度小）
- "AI 让医生每天省 1 小时"
- "Jefferson 的 84% 和 Providence 的 1 分钟互相矛盾，说明其中一家在造假"（口径与场景不同，不可比）

## 9. 来源

- JAMA Network Open, *Ambient Artificial Intelligence Use and Clinician Documentation Burden, Productivity, and Efficiency*, 2026;9(5):e2615762. DOI: 10.1001/jamanetworkopen.2026.15762
- Providence 官方博客，2026-05-29，含第一作者 Robyn Husa 与 PI Canada Parrish 的引语
