---
id: "industry-company-scene"
title: "企业名：一句话说清场景（不超过 30 字）"
company: "企业公开全称"
company_hq: "US"
industry: "financial-services"
sub_industry: "wealth-management"
scenario: ["knowledge-retrieval"]
deployment_model: "vendor-copilot"
fde_involved: "none"
ai_tech: ["LLM", "RAG"]
vendor: ["供应商名"]
scale: "写具体量：X 名员工 / X 家门店 / X 条产线"
start_date: "2024"
status: "production"
evidence_grade: "B"
last_verified: "2026-11-09"
metrics:
  - name: "指标名（用业务语言）"
    value: ">98%"
    unit: "%"
    baseline: "未披露"
    method: "谁算的、怎么算的、样本量"
    window: "统计时间窗"
    direction: "adoption"
sources:
  - id: "src-xxx"
    type: "official-case-study"
    grade: "B"
    url: "https://example.com"
    publisher: "发布方"
    published: "2026"
    accessed: "2026-11-09"
    note: "这条来源的性质与局限"
tags: ["RAG", "regulated-industry", "human-review"]
replicability: 4
human_in_loop: "review-before-send"
confidence_notes: "一句话说明这条案例最脆弱的地方"
---

## 1. 一句话摘要

<!-- 30–60 字。包含：谁、在什么流程上、用什么方式、改变了什么指标。不要写"赋能""抓手""闭环"。 -->

## 2. 业务痛点

<!-- 部署前的流程长什么样？卡在哪一步？成本/时长/人力是多少？
     必须给出"部署前"的具体数字或具体动作序列，否则读者无法判断改善是否真实。 -->

## 3. AI 应用场景

<!-- 输入是什么、输出是什么、输出交给谁、人还需要做什么。
     建议写成"输入 → 处理 → 输出 → 人工动作"四段。 -->

## 4. 落地方式

<!-- 谁交付（厂商 FDE / 集成商 / 自建）；技术栈；从立项到生产多久；
     组织上做了什么配套（培训、激励、责任归属、验收口径）。 -->

## 5. 可验证成效

| 指标 | 数值 | 口径与基线 | 来源 |
|---|---|---|---|
|  |  |  |  |

<!-- 每个数字都要能追到 sources 里的某一条。口径不明的写"未披露"。 -->

## 6. 不可验证或存疑之处

<!-- 必填。至少写两点：
     1) 哪些数字无法核对（口径缺失/厂商测算/样本太小）
     2) 哪些因果无法排除（同期业务变化、幸存者偏差、新奇效应） -->

## 7. 可复用要点

<!-- 3–5 条，写给"想复制的人"，不是写给"想膜拜的人"。
     要具体到可以执行：先做什么、不要做什么、什么条件下不适用。 -->

## 8. 引用边界

<!-- 必填。明确列出：
     ✅ 可以说的话（带口径）
     ❌ 不可以说的话（容易被拆的引申）
     这是防止自己写文章时翻车的一节。 -->

## 9. 来源

<!-- 与 front-matter 的 sources 对应，补上访问日期与关键原文摘句。 -->
