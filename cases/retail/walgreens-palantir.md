---
id: "retail-walgreens-palantir"
title: "Walgreens：8 个月从 10 家店到 4,000 家店"
company: "Walgreens"
company_hq: "US"
industry: "retail"
sub_industry: "pharmacy-retail"
scenario: ["scheduling-optimization", "supply-chain"]
pattern: ["ops-orchestration"]
deployment_model: "platform-build"
fde_involved: "vendor-embedded"
ai_tech: ["agent", "predictive-ml", "rules"]
vendor: ["Palantir"]
scale: "约 4,000 家门店（原计划 6 个月试点 10 家）"
start_date: "2025"
status: "scaled"
evidence_grade: "C"
last_verified: "2026-11-09"
metrics:
  - name: "部署门店数"
    value: "10 家（计划）→ 约 4,000 家（8 个月）"
    unit: "店"
    baseline: "原计划 6 个月试点 10 家"
    method: "客户高管在厂商大会上的口头表述，无门店清单、无时间戳核验"
    window: "约 8 个月"
    direction: "adoption"
sources:
  - id: "src-palantir-walgreens-quote"
    type: "official-case-study"
    grade: "C"
    url: "https://www.palantir.com/"
    publisher: "Palantir（首页客户证言）"
    published: "unknown"
    accessed: "2026-11-09"
    note: "Jeff Hoffman（Walgreens 药品副总裁）在 Palantir 大会/官网的引语；属单方证言，无口径、无基线、无第三方核验"
  - id: "src-palantir-aipcon"
    type: "conference-talk"
    grade: "C"
    url: "https://www.palantir.com/"
    publisher: "AIPCon"
    published: "2026"
    accessed: "2026-11-09"
    note: "同一位高管另有一句「如果全靠人，每天要处理约 3,840 亿个决策」——修辞性表述，不可作为事实引用"
tags: ["agent-orchestration", "fde-model", "bootcamp-model"]
replicability: 2
human_in_loop: "sampling-audit"
confidence_notes: "唯一来源是客户高管在厂商活动上的口头引语，C 级；门店数与时间窗均未独立核实，仅可作线索"
---

## 1. 一句话摘要

Walgreens 原计划 6 个月试点 10 家店，实际 8 个月铺到约 4,000 家——这是"平台 + 驻场工程师"模式下扩散速度的极端样本，但全部数字都出自一场厂商大会。

## 2. 业务痛点

连锁药房的运营是典型的"高决策密度、低单笔价值"结构：

- 每家店每天要处理补货、效期、处方流转、人员排班等大量例行决策
- 单店决策量不足以支撑专职分析岗，但累计起来规模惊人
- 传统做法靠区域经理巡店 + 总部报表，响应滞后
- 并购整合后系统不统一，数据口径混乱

## 3. AI 应用场景

Palantir 的定位不是"生成内容"，而是**把决策逻辑编码成可执行的编排**：

```
输入：门店库存、处方流、客流、人员排班数据
  ↓
处理：Ontology 层把业务对象（门店、SKU、处方、员工）建模为可操作实体，
      在其上编排 AI 驱动的端到端工作流
  ↓
输出：补货建议、调拨指令、排班调整、异常工单
  ↓
人工动作：店长/区域经理处理例外与例外授权
```

客户表述中"每天 3,840 亿个决策"是修辞（全球门店 × 每店每日决策项的理论上限），不要当真实数据。

## 4. 落地方式

- **交付方**：Palantir 的 FDE 模式——工程师驻场，与客户团队在真实数据上共建工作流
- **销售形态**：AIP Bootcamp，3–5 天驻场工作坊，把原本数月的 POC 压缩到几天；Palantir 披露 bootcamp 到付费部署的转化率在不同季度为 21%–75%（口径随时间变化，见 `fde/palantir-bootcamp.md`）
- **扩散路径**：先做 10 家店的试点，验证工作流可复用后，把同一套编排复制到数千家店
- **关键前提**：门店数据必须已在同一平台上（Palantir Foundry），否则复制的是代码而不是能力

## 5. 可验证成效

| 指标 | 数值 | 口径与基线 | 来源 |
|---|---|---|---|
| 门店覆盖 | 约 4,000 家 / 8 个月 | 客户高管口述，无清单核验 | Palantir 官网证言 |
| 原计划 | 10 家 / 6 个月 | 同上 | 同上 |
| 财务影响 | 未披露 | — | — |

## 6. 不可验证或存疑之处

1. **C 级证据，不能作为论据。** 唯一来源是客户高管在厂商大会上的引语。没有门店清单、没有上线时间戳、没有第三方审计。
2. **"4,000 家店"不等于"4,000 家店都在用"。** 开通 license 与日常使用是两件事，公开信息无法区分。
3. **没有效益指标。** 没有缺货率、周转天数、单店人力成本的任何变化数据。速度故事讲得很足，价值故事缺失。
4. **Palantir 的转化率数字自身在漂移。** 不同季度披露的 bootcamp 转化率有 21%、34%、70%+、75% 多个版本，说明其口径未统一，引用时必须带时间点。
5. **并购背景被忽略。** Walgreens 当时正处于门店整合与关店周期，铺开速度可能部分来自"本来就要重做流程"。

## 7. 可复用要点

1. **先在 10 家店把工作流跑通，再复制。** 复制的对象是"编排逻辑"，不是"模型"。
2. **决策类 AI 的瓶颈在数据建模，不在模型。** 没有统一的业务对象模型，agent 无法执行动作。
3. **驻场工程师的作用是"把客户的隐式规则写成显式流程"。** 这是 FDE 与外包的本质区别。
4. **不要用覆盖率当成果指标。** 上线门店数是过程指标。

## 8. 引用边界

✅ 可以说：
- "Walgreens 的一位副总裁在 Palantir 活动上表示，公司原计划 6 个月试点 10 家店，实际 8 个月铺到约 4,000 家店"
- "该案例的数字来自厂商大会的单方表述，未经独立核实"

❌ 不能说：
- "Walgreens 4,000 家店已全面由 AI 运营"（覆盖≠使用≠生效）
- "AI 帮 Walgreens 每天处理 3,840 亿个决策"（修辞，非实测）
- "Palantir 的 bootcamp 转化率是 75%"（不同季度口径不同，须注明时间）
- 任何关于降本增效的具体数字（不存在）

## 9. 来源

- Palantir 官网首页客户证言，Jeff Hoffman（Walgreens, VP, Product Pharmacy）：
  "We started with the goal of piloting 10 stores within about six months. However, leveraging Foundry and AIP, we began to see real promise quickly… allowed us to get to about 4000 stores within eight months."
- AIPCon 相关表述：同上（含"3,840 亿决策"的修辞）
