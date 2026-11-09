# Enterprise AI Casebook / 企业级 AI 落地案例库

> 只收录**已经进入生产环境**、且**能追溯到可核查来源**的企业 AI 应用。不收录演示、PoC、发布会宣称、以及无法追溯到一手来源的"据称节省 XX%"。

本项目面向三类使用者：

1. **写作者 / 研究者**：需要能公开引用的案例，且必须知道自己引用的数字站在什么证据上。
2. **企业决策者**：想知道"同类企业到底怎么落地的、花了多久、谁交付的、哪些环节最容易翻车"。
3. **FDE / 交付工程师**：想积累可复用的交付模式，而不是背客户成功故事。

---

## 一、这个库的立场

企业 AI 案例的公开信息存在系统性污染，主要来自四个方向：

| 污染类型 | 具体表现 | 本库的处理方式 |
|---|---|---|
| **来源转述失真** | 官方通稿里没有数字，二手博客补上"提效 35%"，第三手再引用博客 | 每个数字必须挂到**一手**来源；通稿无数字时明确写"官方未披露" |
| **口径缺失** | "效率提升 30%" 未说明基线、时间窗、样本量、是否减对照组 | 强制填写 `baseline` / `method` / `window` 三个字段 |
| **供应商自述** | 厂商案例页的 ROI 由厂商自己算，客户只署名不核数 | 按证据分级标注，C 级不可作为论据引用 |
| **事后回撤** | 2024 年高调宣布的数字，2025 年被 CEO 自己推翻 | 保留在 `cases/retracted/`，记录"宣称—修正—现状"三段 |

因此本库**刻意保留了失败与被修正的案例**。一个只有成功故事的案例库，本身就不值得引用。

---

## 二、证据分级（最重要的规则）

每条案例必须标注 `evidence_grade`，含义如下：

| 级别 | 定义 | 典型来源 | 可否公开引用 |
|---|---|---|---|
| **A** | 法定披露或同行评审 | 年报/10-K、财报电话会、监管文件、NEJM/JAMA/Nature 等 | ✅ 可直接引用，仍需带口径 |
| **B** | 企业官方发布 + 含可核查数字 | 官方新闻稿、官方案例页、技术博客 | ✅ 可引用，须注明"企业自述" |
| **C** | 单方证言，无口径无基线 | 厂商网站客户引语、销售物料、大会演讲 | ⚠️ 仅可作线索，不可作论据 |
| **D** | 二手报道 / 聚合站 | 媒体转述、行业报告汇编、榜单 | ❌ 仅用于发现线索，须回溯一手来源 |
| **X** | 已被回撤或重大修正 | 企业公开承认、后续财报修正 | ✅ 但必须同时给出修正后的说法 |

细则见 [`taxonomy/evidence.md`](taxonomy/evidence.md)。

**一条硬规则**：D 级来源不得直接生成案例。任何案例至少要有 1 个 A 或 B 级来源，否则只能进 `index/watchlist.md`。

---

## 三、目录结构

```
.
├── README.md                  # 本文件：定位、方法论、使用方式
├── CONTRIBUTING.md            # 增补流程、评审清单、拒收标准
├── schema/
│   ├── case.schema.json       # 案例条目的机器可校验 schema
│   └── fields.md              # 每个字段的填写规范与常见错误
├── taxonomy/
│   ├── industries.yml         # 受控行业词表
│   ├── scenarios.yml          # 受控场景词表
│   ├── deployment.yml         # 交付模式词表（含 FDE 五种形态）
│   └── evidence.md            # 证据分级细则
├── cases/
│   ├── _TEMPLATE.md           # 新建案例从这里复制
│   ├── finance/               # 按行业分目录
│   ├── healthcare/
│   ├── manufacturing/
│   ├── retail/
│   ├── software/
│   └── retracted/             # 被回撤/修正的案例（保留，不删除）
├── fde/                       # FDE（前沿部署工程师）专题
│   ├── README.md              # FDE 是什么、五种形态、如何评估
│   ├── openai-fde.md          # 模型厂商自建 FDE 团队
│   ├── anthropic-goldman-jv.md# FDE 被资本化：15 亿美元交付公司
│   ├── palantir-bootcamp.md   # FDE 的原始形态：Bootcamp 压缩销售周期
│   └── china-fde.md           # 中国 FDE：运营商、集成商、地方政府
├── index/
│   ├── by-industry.md         # 自动生成
│   ├── by-scenario.md         # 自动生成
│   ├── by-evidence.md         # 自动生成
│   └── watchlist.md           # 待核实线索（D 级，不进正式案例）
├── sources/
│   └── registry.yml           # 来源登记表：URL、类型、抓取日期、可信度
└── scripts/
    ├── validate.py            # 校验 front-matter 与必填章节
    └── build_index.py         # 从案例自动重建 index/
```

**为什么按行业分目录而不是按厂商**：案例的使用场景是"我在 X 行业，别人怎么做的"，行业是第一检索维度；厂商维度用 `vendor` 字段和 `index/` 解决。

---

## 四、一条案例长什么样

案例是**带 YAML front-matter 的 Markdown**。这样既能被脚本解析成索引/JSON，又能直接当文章素材读。

```yaml
---
id: "healthcare-jefferson-abridge"
title: "Jefferson Health：5,234 名临床医生的门诊文书助手"
company: "Jefferson Health"
industry: "healthcare"
scenario: ["clinical-documentation"]
deployment_model: "vendor-saas"
fde_involved: "none"
evidence_grade: "A"
status: "scaled"
metrics:
  - name: "病历书写投入（HPI 与 A&P 部分）"
    value: "-84%"
    unit: "%"
    baseline: "部署前同科室均值"
    method: "平台内工作量评分，1,802 名活跃使用者"
    direction: "effort-down"
---
```

正文固定 9 个小节，顺序不可变（脚本会检查）：

1. 一句话摘要
2. 业务痛点（部署前的流程、成本、瓶颈）
3. AI 应用场景（输入 / 输出 / 人机分工）
4. 落地方式（谁交付、什么技术栈、多长周期、组织配套）
5. 可验证成效（表格：指标 / 数值 / 口径 / 来源）
6. 不可验证或存疑之处
7. 可复用要点
8. 引用边界（哪些话可以说，哪些不能说）
9. 来源

第 6 和第 8 节是本库和"客户成功故事"的分界线，不允许为空。

---

## 五、如何使用

### 写文章时

```bash
# 找某行业全部 A/B 级案例
grep -rl 'evidence_grade: "A"' cases/healthcare/

# 找所有涉及 FDE 交付的案例
grep -rl 'fde_involved: "vendor-embedded"' cases/
```

### 引用时的最小标注格式

> 摩根士丹利称其财富管理条线超过 98% 的顾问团队在使用内部 AI 助手（来源：OpenAI 客户案例，B 级，企业自述，未披露统计分母）。

**必须包含四要素**：数字 + 来源 + 证据级别 + 口径限制。缺任何一项，都会在评论区被拆。

### 维护时

```bash
python scripts/validate.py          # 提交前必跑
python scripts/build_index.py       # 增删案例后重建索引
```

---

## 六、增补机制

- **新增案例**：复制 `cases/_TEMPLATE.md` → 填 front-matter → 写满 9 节 → 跑 `validate.py` → 提 PR。
- **修正数字**：不覆盖原值，在 `## 6. 不可验证或存疑之处` 里追加"修正记录（日期 / 原值 / 新值 / 依据）"。
- **发现回撤**：把文件 `git mv` 到 `cases/retracted/`，`evidence_grade` 改 `X`，`status` 改 `retracted`，补写"回撤时间线"。
- **只有线索没证据**：写进 `index/watchlist.md`，不要建案例文件。

PR 评审清单见 [`CONTRIBUTING.md`](CONTRIBUTING.md)。

---

## 七、已知局限

- **幸存者偏差**：能公开查到细节的案例，本身就是"愿意公开"的少数；失败案例几乎不可见，本库只能靠回撤记录部分补偿。
- **效应量不可比**：不同企业的"提效 30%"口径互不相通，本库只保证口径被记录，不保证可比。
- **时间衰减**：模型能力每季度变化，2023 年的部署结论未必适用于 2026 年。每条案例有 `last_verified` 字段，超过 12 个月未复核会进 `index/stale.md`。
- **语言偏斜**：英文一手来源更易获得，中文案例多依赖官媒转述，证据等级普遍偏低。这是结构性缺陷，不做美化。

---

## 八、许可

案例正文采用 CC BY 4.0；脚本采用 MIT。引用时请保留本仓库链接与证据等级标注。
