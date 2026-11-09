# 字段规范

每条案例的 front-matter 必须包含下列字段。`必填` 为 `是` 的字段缺失会导致 `validate.py` 失败。

## 标识与分类

| 字段 | 必填 | 类型 | 说明 | 常见错误 |
|---|---|---|---|---|
| `id` | 是 | string | 全局唯一。格式 `{industry}-{company-slug}-{scene-slug}`，全小写、连字符 | 用中文；用空格；同一企业多个场景未加区分 |
| `title` | 是 | string | 一句话标题，含企业名 + 场景，不超过 30 字 | 写成"某集团数字化转型实践"这种无信息量标题 |
| `company` | 是 | string | 落地企业（甲方）名称，用公开全称 | 填成厂商名（厂商应填 `vendor`） |
| `company_hq` | 否 | string | 总部所在国家/地区，ISO 风格 | — |
| `industry` | 是 | enum | 必须取自 `taxonomy/industries.yml` | 自造行业名 |
| `sub_industry` | 否 | string | 更细的行业标签，自由文本 | — |
| `scenario` | 是 | array | 1–3 个，取自 `taxonomy/scenarios.yml` | 填 6 个以上，等于没分类 |

## 落地方式

| 字段 | 必填 | 类型 | 说明 |
|---|---|---|---|
| `deployment_model` | 是 | enum | 取自 `taxonomy/deployment.yml`：`vendor-saas` / `vendor-copilot` / `platform-build` / `in-house` / `si-delivery` |
| `fde_involved` | 是 | enum | `none`（无驻场）/ `vendor-embedded`（厂商 FDE 驻场）/ `si-partner`（集成商驻场）/ `in-house`（自建前线团队）/ `unknown`（未披露） |
| `ai_tech` | 是 | array | 受控词：`LLM` `RAG` `ASR` `CV` `agent` `predictive-ml` `rules` |
| `vendor` | 否 | array | 供应商/模型提供方 |
| `scale` | 是 | string | 覆盖范围，写"人数/门店数/产线数/月会话量"等具体量，不写"全集团" |
| `start_date` | 是 | string | 首次进入生产的时间（`YYYY` 或 `YYYY-MM`）。不确定写 `unknown` 并在正文说明 |
| `status` | 是 | enum | `pilot` / `production` / `scaled` / `paused` / `retracted` |

## 证据

| 字段 | 必填 | 类型 | 说明 |
|---|---|---|---|
| `evidence_grade` | 是 | enum | `A` `B` `C` `D` `X`，定义见 `taxonomy/evidence.md` |
| `last_verified` | 是 | date | 最后一次人工核对来源的日期 `YYYY-MM-DD`。超过 12 个月会被标记 stale |
| `metrics` | 是 | array | 至少 1 条。结构见下 |
| `sources` | 是 | array | 至少 1 条。结构见下 |
| `confidence_notes` | 是 | string | 一句话说明这条案例最脆弱的地方（无则写"无重大不确定性"） |

### metrics 条目

```yaml
metrics:
  - name: "病历书写投入（HPI 与 A&P）"
    value: "-84%"
    unit: "%"
    baseline: "部署前同科室均值"
    method: "平台内工作量评分；1,802 名活跃使用者"
    window: "2025-07-01 ~ 2025-12-31"
    direction: "effort-down"
```

| 子字段 | 必填 | 说明 |
|---|---|---|
| `name` | 是 | 指标名，用业务语言（"排产响应时间"而非"效率"） |
| `value` | 是 | 数值或带箭头的区间（`"20% → 80%"`） |
| `unit` | 否 | 单位。无量纲写 `"ratio"` |
| `baseline` | **是** | 对照组或基线。**没有基线就写 `"未披露"`，不许省略** |
| `method` | **是** | 怎么算的、谁算的、样本量。这是本库最核心的字段 |
| `window` | 否 | 统计时间窗 |
| `direction` | 是 | `cost-down` / `effort-down` / `time-down` / `volume-up` / `revenue-up` / `quality-up` / `adoption` / `risk-down` |

**红线**：`method` 里出现"官方称""据测算"而不说明测算方，视为未填写。

### sources 条目

```yaml
sources:
  - id: "src-nejm-cat-26-0269"
    type: "peer-reviewed"
    grade: "A"
    url: "https://catalyst.nejm.org/doi/full/10.1056/CAT.26.0269"
    publisher: "NEJM Catalyst"
    published: "2026"
    accessed: "2026-11-09"
    note: "作者披露：Abridge 提供商业合同但未参与设计/分析/写作，未提供资金"
```

`type` 受控值：`annual-report`（年报/10-K）、`earnings-call`、`regulatory-filing`、`peer-reviewed`、`official-press-release`、`official-case-study`、`official-careers-page`、`company-blog`、`conference-talk`、`media-report`、`aggregator`。

**每个 URL 必须真实抓取过**，并在 `sources/registry.yml` 登记。没有抓取过的链接不允许写进 `url`。

## 评估与标签

| 字段 | 必填 | 类型 | 说明 |
|---|---|---|---|
| `tags` | 是 | array | 自由标签，建议复用已有标签；新增标签需在 `taxonomy/tags.yml` 追加 |
| `replicability` | 是 | int 1–5 | 中小企业/异构 IT 环境下复制的难度。1=几乎不可复制（依赖专有数据/超大规模），5=可直接照搬流程 |
| `human_in_loop` | 是 | enum | `none` / `review-before-send` / `escalation-only` / `sampling-audit`——人机分工是案例能否成立的关键 |

## 正文九节

`validate.py` 会检查下列二级标题存在且顺序正确：

```
## 1. 一句话摘要
## 2. 业务痛点
## 3. AI 应用场景
## 4. 落地方式
## 5. 可验证成效
## 6. 不可验证或存疑之处
## 7. 可复用要点
## 8. 引用边界
## 9. 来源
```

第 6、8 节内容为空（或只有"无"一个字）时校验失败——这两节是本库的信用来源，必须写出具体的存疑点与不可引用范围。
