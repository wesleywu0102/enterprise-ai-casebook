# 贡献指南

## 一、什么能进，什么不能进

### 可以进

- 已在生产环境运行 ≥ 3 个月的企业 AI 应用
- 有至少 1 个 A 或 B 级一手来源
- 能说清"部署前是什么样"（有基线或有流程描述）

### 不能进

| 情况 | 原因 | 去处 |
|---|---|---|
| 只有发布会/PPT，无生产运行证据 | 无法验证 | `index/watchlist.md` |
| 只有厂商案例页，客户未具名 | C 级，不可引用 | 可入库，标 C，正文注明"仅作线索" |
| 只有二手转述 | 数字已失真 | `index/watchlist.md`，待回溯 |
| "某企业"匿名案例 | 无法核查主体 | 不收 |
| 内部消息/未公开信息 | 合规风险 | 不收 |
| 纯技术 demo、benchmark | 不是企业落地 | 不收 |

---

## 二、提交前检查清单

复制下面这段到 PR 描述里逐项打勾：

```markdown
- [ ] front-matter 通过 `python scripts/validate.py`
- [ ] 每个 metric 都填了 baseline 和 method（无基线写"未披露"）
- [ ] 每个 source 的 URL 我都亲自打开过，且能访问
- [ ] 数字来自一手来源，不是二手博客转述
- [ ] 第 6 节写了至少 2 个具体存疑点
- [ ] 第 8 节写了"不能说的话"
- [ ] 如果引用了厂商测算的数字，method 里写明了"厂商测算"
- [ ] 已在 `sources/registry.yml` 登记新增来源
- [ ] 运行 `python scripts/build_index.py` 并提交 index 变更
```

---

## 三、评审规则

### 会被直接拒的

1. `baseline: "N/A"` 或留空 —— 无基线是允许的，隐瞒不是
2. `method` 写成"官方数据""据测算" —— 必须说明测算方
3. 把厂商案例页的 ROI 当成事实陈述
4. 同一案例重复建档（先搜 `id` 和 `company`）
5. 删除已存在的数字而不留修正记录

### 会被要求修改的

1. 标题带形容词（"革命性""颠覆性"）
2. 第 7 节写成了方法论空话（"要重视数据治理"）
3. 一个案例塞了 5 个场景，每个都没写清
4. `replicability` 给 5 分但案例依赖专有数据

---

## 四、修正与回撤

### 修正数字

不要覆盖。在该案例 `## 6. 不可验证或存疑之处` 末尾追加：

```markdown
**修正记录**
- 2026-11-09：原记"降本 7 亿元"，经核对 2025 年报原文为"提效超 1500 万小时、降本 7 亿元"，
  但同年另一场业绩说明会口径为 7.7 亿元。两个数字并存，以年报为准，差异原因未披露。
```

### 回撤整个案例

```bash
git mv cases/finance/xxx.md cases/retracted/xxx.md
```

然后：
- `evidence_grade: "X"`，`status: "retracted"`
- 正文加 `## 回撤时间线` 表格
- 保留全部原始数字与原始来源链接

---

## 五、周期性维护

| 频率 | 动作 |
|---|---|
| 每季度 | 复核 `last_verified` 超过 12 个月的案例，更新或标 `stale` |
| 每半年 | 检查 A 级来源是否被后续财报修正（重点看已披露的降本金额） |
| 每年 | 重跑 `build_index.py`，清理 `watchlist` 中已确认无法回溯的条目 |

---

## 六、commit 约定

```
feat(case): add <company> <scene>
fix(case): correct <metric> in <case-id>
retract(case): move <case-id> to retracted
taxonomy: add <term>
docs: <what>
```
