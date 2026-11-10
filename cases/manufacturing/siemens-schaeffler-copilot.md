---
id: "manufacturing-siemens-schaeffler-copilot"
title: "西门子 × 舍弗勒：被二手文章编出「35%」的工业 Copilot"
company: "Schaeffler（舍弗勒）"
company_hq: "DE"
industry: "manufacturing"
sub_industry: "automotive"
scenario: ["manufacturing-quality", "software-engineering"]
pattern: ["embedded-codegen"]
deployment_model: "vendor-copilot"
fde_involved: "unknown"
ai_tech: ["LLM"]
vendor: ["Siemens", "Microsoft Azure OpenAI"]
scale: "首台搭载 Industrial Copilot 的量产设备（2023 SPS 展）；舍弗勒自动化工程团队"
start_date: "2023-11"
status: "production"
evidence_grade: "B"
last_verified: "2026-11-09"
metrics:
  - name: "自动化任务耗时"
    value: "「数周」→「数分钟」"
    unit: "qualitative"
    baseline: "此前的仿真/代码准备流程"
    method: "厂商通稿表述；未说明具体任务、样本量、对照方式，无法核验"
    window: "2023-11"
    direction: "time-down"
sources:
  - id: "src-siemens-pr-2023-11"
    type: "official-press-release"
    grade: "B"
    url: "https://press.siemens.com/global/en/pressrelease/ai-industry-schaeffler-and-siemens-bring-industrial-copilot-shopfloor"
    publisher: "Siemens"
    published: "2023-11"
    accessed: "2026-11-09"
    note: "官方通稿：首台集成 Industrial Copilot 的生产设备；全文无任何百分比数字，仅「数周→数分钟」的定性表述"
  - id: "src-siemens-ms-2023-10"
    type: "official-press-release"
    grade: "B"
    url: "https://assets.new.siemens.com/siemens/assets/api/uuid:89b84c68-fcea-4d6d-8180-678d4663e55b/HQCOPR202310306800EN.pdf"
    publisher: "Siemens / Microsoft"
    published: "2023-10-30"
    accessed: "2026-11-09"
    note: "联合发布：Industrial Copilot 基于 Azure OpenAI；客户数据不用于训练模型；原文「reduce a task that previously took weeks to minutes」"
  - id: "src-schaeffler-story"
    type: "official-case-study"
    grade: "B"
    url: "https://www.schaeffler.com/en/media/stories/digitalization-stories/ai-in-industry/"
    publisher: "Schaeffler"
    published: "2023-11"
    accessed: "2026-11-09"
    note: "舍弗勒官方故事页：通过 TIA Portal Openness 接入，用自然语言生成 PLC 代码；无量化数字"
tags: ["metric-definition-war", "vendor-sourced-number", "human-review"]
replicability: 3
human_in_loop: "review-before-send"
confidence_notes: "官方来源全部无百分比数字；广泛流传的「工程工时减少 35%」在西门子与舍弗勒的一手材料中均不存在"
---

## 1. 一句话摘要

这是被引用最多的工业 AI 案例之一，也是最典型的"数字在转述中长出来"的案例：官方通稿里一个百分比都没有，二手文章却普遍写着"工程工时减少 35%"。

## 2. 业务痛点

PLC（可编程逻辑控制器）是工厂设备的"大脑"，其代码编写高度依赖资深自动化工程师：

- 一个中等复杂度的产线改造，PLC 代码编写与调试可能耗时数周
- 代码错误导致设备停机，排查要靠翻手册、查文档、凭经验
- 资深自动化工程师供给不足，欧美制造业普遍面临这一缺口
- 新人成长周期长，车间员工难以转入工程岗

## 3. AI 应用场景

```
输入：工程师的自然语言描述（"这段输送带要…"）+ 设备文档/手册
  ↓
处理：Industrial Copilot 经 TIA Portal Openness 接口生成 PLC 代码；
      或检索设备文档，定位故障并给出分步处置建议
  ↓
输出：S7 代码草稿 / 故障处置步骤
  ↓
人工动作：工程师审阅、编译、仿真、下装到设备
```

两个场景：**代码生成**（工程阶段）与**故障诊断**（运维阶段）。

## 4. 落地方式

- **技术栈**：Siemens Industrial Copilot + Microsoft Azure OpenAI Service，通过开放 API 接入 TIA Portal
- **数据边界**：客户数据不用于训练底层模型（联合通稿明确）
- **形态**：嵌入现有工程框架，而非独立应用——这是它能被工程师接受的关键
- **公开程度**：2023 年 SPS 展会上展示首台搭载该 Copilot 的生产设备；此后西门子持续扩展 Industrial Copilot 产品线，但舍弗勒侧的具体推广规模未公开
- **交付方**：厂商（西门子）主导，是否有驻场工程师未披露，标 unknown

## 5. 可验证成效

| 指标 | 数值 | 口径与基线 | 来源 |
|---|---|---|---|
| 自动化任务耗时 | "数周 → 数分钟" | 厂商通稿定性表述，无任务定义、无样本 | Siemens/Microsoft 通稿 |
| PLC 代码生成方式 | 自然语言输入 | 功能描述，非效益指标 | Siemens / Schaeffler 官方 |
| 工程工时降幅 | **官方未披露** | — | 两份官方通稿均无百分比 |

## 6. 不可验证或存疑之处

**这一节是本案例存在的理由。**

1. **"35% 工程工时减少"在一手来源中不存在。** 西门子 2023-10 的联合通稿、西门子 2023-11 的舍弗勒新闻稿、舍弗勒官方故事页，三份材料全文都没有这个数字。它出现在大量二手聚合文章里，通常不给出处。
2. **"数周→数分钟"没有任务定义。** 是仿真时间、代码生成时间、还是整条产线调试时间？三种口径差异巨大。
3. **展示 ≠ 规模部署。** 2023 年 SPS 上展示的是"首台"设备，属于产线级示范，不等于舍弗勒全球工厂已规模化使用。
4. **没有质量数据。** 生成代码的编译通过率、返工率、上线后缺陷率，官方均未披露。工业场景里，这是比"快多少"更重要的指标。
5. **案例已过去三年，产品形态已变。** 2023 年的 Industrial Copilot 与 2026 年的产品能力不可直接类比，旧结论会过期。

## 7. 可复用要点

1. **嵌进原有工程工具，而不是新建一个聊天窗口。** TIA Portal 是工程师每天用的界面，Copilot 在里面才有使用率。
2. **优先做"查文档 + 生成草稿"，不要做"自动下装"。** 工业控制的容错空间极小，人必须在下装前签字。
3. **把编译通过率当第一指标。** 而不是"生成速度"。
4. **数据不进训练集是采购硬条件。** 工艺参数是核心资产。

## 8. 引用边界

✅ 可以说：
- "西门子与舍弗勒在 2023 年 SPS 展会上展示了首台集成 Industrial Copilot 的生产设备，可用自然语言生成 PLC 代码"
- "西门子称该工具可将此前需要数周的自动化任务缩短到数分钟（未披露具体任务与测算方式）"
- "该案例的官方材料中没有任何百分比形式的效益数据"

❌ 不能说：
- "舍弗勒用 AI 把工程工时减少了 35%"（无一手来源）
- "西门子 Industrial Copilot 已在舍弗勒全球工厂规模化部署"（公开信息只到首台设备/试点）
- "工业 AI 平均可提效 35%"（把单案例当行业基准，且数字本身无来源）

## 9. 来源

- Siemens 新闻稿，2023-11：*AI for industry: Schaeffler and Siemens bring Industrial Copilot to shopfloor*
- Siemens / Microsoft 联合新闻稿，2023-10-30：*Siemens and Microsoft partner to drive cross-industry AI adoption*（含 "reduce a task that previously took weeks to minutes"）
- Schaeffler 官方故事页：*AI for industry: Schaeffler and Siemens bring Industrial Copilot to shop floor*
- 西门子中国新闻稿（中文版）：同上内容
