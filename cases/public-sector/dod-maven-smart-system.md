---
id: "public-sector-dod-maven-smart-system"
title: "美国国防部 Maven：13 亿美元、2 万用户的军事 AI"
company: "U.S. Department of Defense (Maven Smart System)"
company_hq: "US"
industry: "public-sector"
sub_industry: "defense"
scenario: ["data-analysis", "risk-compliance"]
deployment_model: "platform-build"
fde_involved: "vendor-embedded"
ai_tech: ["CV", "LLM", "agent"]
vendor: ["Palantir USG"]
scale: "2 万+ 活跃用户、35+ 软件工具，覆盖 5 个作战司令部与联合参谋部"
start_date: "2024"
status: "scaled"
evidence_grade: "A"
last_verified: "2026-11-10"
metrics:
  - name: "合同上限（累计）"
    value: "约 12.75 亿美元"
    unit: "USD"
    baseline: "不适用"
    method: "两份国防部合同公告相加：2024-05 授予 4.8 亿美元原型合同 + 2025-05 追加 7.95 亿美元修改。均为上限，非已支付额"
    window: "2024-05 ~ 2025-05"
    direction: "cost-down"
  - name: "活跃用户数"
    value: "2 万+"
    unit: "人"
    baseline: "2024-03 时为当前的 1/4（原话 quadrupled）"
    method: "美国国家地理空间情报局（NGA）局长在 GEOINT 研讨会的公开讲话；政府官员口径，非审计数据"
    window: "截至 2025-05"
    direction: "adoption"
  - name: "覆盖工具数"
    value: "35+"
    unit: "个"
    baseline: "未披露"
    method: "同上，政府官员讲话"
    window: "截至 2025-05"
    direction: "adoption"
sources:
  - id: "src-dod-contract-2024-05-29"
    type: "regulatory-filing"
    grade: "A"
    url: "https://www.defense.gov/News/Contracts/Contract/Article/3790490/"
    publisher: "U.S. Department of Defense"
    published: "2024-05-29"
    accessed: "2026-11-10"
    note: "Maven Smart System 原型合同 4.8 亿美元，单一投标，履约期至 2029-05-28。"
  - id: "src-dod-contract-2025-05-21"
    type: "regulatory-filing"
    grade: "A"
    url: "https://www.defense.gov/News/Contracts/Contract/Article/4194643/"
    publisher: "U.S. Department of Defense"
    published: "2025-05-21"
    accessed: "2026-11-10"
    note: "对同一合同的 7.95 亿美元修改（P00005），标的是软件许可。"
  - id: "src-defensenews-maven-2024"
    type: "media-report"
    grade: "D"
    url: "https://www.defensenews.com/artificial-intelligence/2024/05/30/palantir-wins-contract-to-expand-access-to-project-maven-ai-tools/"
    publisher: "Defense News"
    published: "2024-05-30"
    accessed: "2026-11-10"
    note: "生产化定性、五个作战司令部范围、以及「自动识别潜在目标」的功能描述。"
  - id: "src-meritalk-nga-2025"
    type: "conference-talk"
    grade: "B"
    url: "https://www.meritalk.com/articles/nga-expands-maven-ai-system-in-year-of-ai-whitworth-says/"
    publisher: "MeriTalk（转述 NGA 局长 GEOINT 讲话）"
    published: "2025-05-27"
    accessed: "2026-11-10"
    note: "2 万用户、35+ 工具、自 2024-03 翻两番的口径来源。"
tags: ["regulated-industry", "data-sovereignty", "metric-definition-war", "fde-model"]
replicability: 2
human_in_loop: "review-before-send"
confidence_notes: "金额与用户规模有硬来源，但「成效」没有任何可核验的作战效能数据；且系统功能涉及目标识别，政治与伦理争议大"
---

## 1. 一句话摘要

美国国防部把多源情报融合与目标识别交给 Palantir 的 Maven Smart System，累计合同上限约 12.75 亿美元、用户从数千扩到 2 万以上——但公开材料里没有一个字说明它让作战效能提升了多少。

## 2. 业务痛点

军事指挥决策的输入是"人看不完的数据"：

- 卫星图像、无人机视频、信号情报、地理定位数据分属不同系统与密级
- 分析师在多个终端之间切换，靠人工把同一目标的线索拼起来
- 从发现到决策的链路长，跨军种协同需要反复确认
- 五个作战司令部各自建设，导致工具与标准不统一

Project Maven 的初衷就是把计算机视觉用于无人机影像的自动标注，减少分析师逐帧看的负担。

## 3. AI 应用场景

```
输入：卫星图像、全动态视频、信号情报、地理定位、后勤数据
  ↓
处理：多源融合 + 计算机视觉识别 + 目标关联，在统一界面上呈现战场态势；
      系统可"自动检测潜在目标"（Defense News 原文表述）
  ↓
输出：态势图、目标候选清单、火力与后勤建议
  ↓
人工动作：情报与作战人员复核、按交战规则决策
```

必须说清楚：这是一个**进入杀伤链上游的系统**，不是"数据分析工具"。Defense News 的原文用了 "automatically detect potential targets"。

## 4. 落地方式

- **供应商**：Palantir USG，合同标的写作 "Maven Smart System prototype" 与后续软件许可
- **不是商业 AIP**：这是政府产品栈（Gotham 系）的定制版本，运行在国防部环境内
- **交付形态**：Palantir 人员深度参与部署与扩展，但其国防业务负责人对媒体的表述集中在交付范围，未见官方使用 "forward deployed engineer" 这一称谓。本库标为 `vendor-embedded` 但在正文注明证据强度弱于 Palantir 商业侧的 FDE 表述
- **合同结构**：2024-05 授予原型合同（单一投标），2025-05 追加软件许可修改，履约期至 2029 年
- **扩散方式**：先在几个司令部试点，再横向扩到五个作战司令部与联合参谋部

## 5. 可验证成效

| 指标 | 数值 | 口径与基线 | 来源 |
|---|---|---|---|
| 原型合同金额 | 4.8 亿美元 | 国防部公告，firm-fixed-price，至 2029-05-28 | DoD 2024-05-29 |
| 追加修改 | 7.95 亿美元 | 同一合同 P00005，软件许可 | DoD 2025-05-21 |
| 累计上限 | 约 12.75 亿美元 | 两项相加，非已支付 | 计算 |
| 活跃用户 | 2 万+ | 政府官员讲话，含各军种与司令部 | MeriTalk 2025-05 |
| 覆盖工具 | 35+ | 同上 | 同上 |

**没有任何作战效能数字。** 没有"目标识别准确率"、没有"决策时间缩短"、没有"分析师人时节省"。这一点必须诚实写出来——公开材料到这个层级就断了。

## 6. 不可验证或存疑之处

1. **金额口径极容易错。** 4.8 亿（2024 授予）、7.95 亿（2025 修改）、约 12.75 亿（累计上限）、媒体常写的"近 13 亿"，四个数字都不是"已支付额"。我最初也把 4.8 亿记成 2025 年 5 月的合同，实际是 2024 年 5 月。
2. **用户数 ≠ 使用强度。** 2 万活跃用户是账号层面的统计，不代表作战使用频次或依赖程度。
3. **无成效披露是结构性的。** 军事系统的效能数据通常涉密，这既不是厂商隐瞒，也不代表效果好。把"没有负面消息"当"效果很好"是错的。
4. **单一投标，无竞争。** 国防部公告原文写明 "One bid was solicited via the internet with one received"。这在美国政府采购里属于异常，是争议点之一。
5. **政治与伦理争议必须标注。** 系统功能包含自动检测潜在目标；英国下议院科技委员会 2026-06 的报告曾直接点名 Palantir 为美国军方与移民部门供货、支持"highly controversial policies and activities"。
6. **合同可继续修改。** 2029 年到期前仍可能追加，当前上限不是终值。

## 7. 可复用要点

1. **政府场景的"落地"要看合同，不看新闻稿。** 公告里的合同号、履约期、投标方式，比任何 case study 都可靠。
2. **区分"原型"与"生产"。** 这份合同标的写的是 prototype，虽然 Palantir 高管称已进入生产，但合同语言与产品语言不是一回事。
3. **涉密场景不存在外部验证。** 引用这类案例时，唯一诚实的方式是只报金额与规模，不评价效果。
4. **单一供应商风险。** 一个平台承载五个司令部的工具，替换成本极高。

## 8. 引用边界

✅ 可以说：
- "美国国防部 2024 年 5 月授予 Palantir 4.8 亿美元的 Maven Smart System 原型合同，2025 年 5 月又追加 7.95 亿美元的软件许可修改，累计上限约 12.75 亿美元（国防部合同公告）"
- "据 NGA 局长 2025 年 5 月的公开讲话，Maven 已有 2 万以上活跃用户、覆盖 35 种以上工具"
- "该系统包含自动检测潜在目标的功能，属于进入杀伤链上游的军事 AI"

❌ 不能说：
- "Maven 让美军决策速度快了 X 倍"（无任何公开数据）
- "Palantir 从这份合同赚了 12.75 亿美元"（是上限，不是收入）
- "这是企业级 AI 的最佳实践"（涉密、单一供应商、无成效披露，不能作为商业案例范本）
- 把它当作"数据分析工具"淡化军事属性

## 9. 来源

- U.S. DoD, *Contracts For May 29, 2024*, 2024-05-29
  关键句："awarded a $480,000,000 firm-fixed-price contract for the Maven Smart System prototype. One bid was solicited via the internet with one received."
- U.S. DoD, *Contracts For May 21, 2025*, 2025-05-21
  关键句："a $795,000,000 modification (P00005) ... for Maven Smart System software licenses"
- Defense News, *Palantir wins contract to expand access to Project Maven AI tools*, 2024-05-30
- MeriTalk, *NGA Expands Maven AI System in 'Year of AI,' Whitworth Says*, 2025-05-27
  关键句："Maven now supports over 20,000 active users across more than 35 software tools"
