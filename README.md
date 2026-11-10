# Enterprise AI Casebook

「提效 35%」这句话，西门子自己发过的三份通稿里都没有。我在中文文章里找到它几十次，没有一次给出处。

这类数字不是测量结果。**给出基线，等于同意被对照检验**；而一个不能被证伪的百分比，转发起来方便得多。这个库里 73 条公开成效宣称，能被第三方独立复算的只有 17 条。我数了两遍，得到两个不同的结果——差别全在"什么叫没有基线"要人判一次。这件事没被当成误差抹掉，写在第一篇里。

所以这个仓库不是案例合集。20 条案例、6 个架构方案、73 条原始数据都只是下面四个判断的证据。

---

## 四个判断

**一、[「提效 35%」不是测量结果，是一份不想被复算的声明](findings/01-claims-are-not-measurements.md)**
缺口径不是疏漏，是发布方在约束下的理性选择。顺带承认一件事：我这套 A/B/C 证据分级把法定披露和同行评审放在同一档，是错的——30 条 A 级宣称里只有 8 条可复算。
*推翻它*：若出现强制披露模板，无基线比例应在被监管行业明显下降，其他行业不变。

**二、[厂商测动作，独立研究测产出，所以差 80 倍不奇怪](findings/02-action-vs-output.md)**
Jefferson 的 -84% 是"书写投入评分"，Providence 的 1 分钟是"每次预约实际耗时"。不是数据打架，是问题定义不同。任何"AI 提效 X%"的争论，先问测的是动作还是产出。
*推翻它*：若哪天出现动作 -80%、产出也 -80% 的独立研究，这个框架就该扔。

**三、[FDE 是毛利结构，不是交付模式](findings/03-fde-is-a-margin-structure.md)**
模型还不能写进标准合同定价，只能靠人把价值做出来再收钱。所以 FDE 密度和软件产品化程度负相关，「FDE 越多越成熟」是反的。
*推翻它*：哪天有厂商敢在公开价目表里写"未达标赔付"，它的 FDE 招聘量应当同季下降。

**四、[按结果收费的 AI，裁判和收款方是同一个人](findings/04-who-defines-resolved.md)**
Intercom 改分母那天明写 "Resolution Rate: Will increase"，还给了 33%→50% 的算例。这不是操守问题，是结构。谈这类合同，第一件事不是谈单价，是争"解决"的判定权。
*推翻它*：若出现通行第三方审计，各家解决率会集体下调并收敛。

每篇末尾都写了基于什么、哪里可能错、什么观察会让我作废它。**第三篇推翻的是我上一版在这个库里写下的结论**，改掉了，没另写文章打圆场。

---

## 写稿前的 10 秒

```bash
python scripts/check_claim.py 35%
```

```
⚠ 「35%」出现在待回溯/不收清单里：
    ### 2. 西门子 / 舍弗勒："工程工时减少 35%"
    - **已核**：两份官方通稿 + 舍弗勒官方故事页，全文无此数字
```

```bash
python scripts/check_claim.py 西门子       # 查企业，顺带列出相关案例
python scripts/check_claim.py --stats      # 口径统计
python scripts/export_claims.py            # 重新生成 data/claims.csv
```

数据层是 [`data/claims.csv`](data/claims.csv)：73 条宣称拍平成一行一条，含基线状态、时间窗、测算方法、是否可复算、来源链接。判定规则写在 `export_claims.py` 里，可以质疑、可以改。拿去做你自己的统计，不必同意这里任何一句结论。

---

## 其余的东西

| 想要什么 | 去哪 |
|---|---|
| 20 条案例，每条带痛点 / 场景 / 落地方式 / 成效 / **存疑之处** / **引用边界** | [`index/by-industry.md`](index/by-industry.md) |
| 按场景、证据等级、FDE 交付形态、方案模式切片 | [`index/`](index/) |
| 6 个架构模式（参考架构、组件选型、集成点、失败模式） | [`solutions/`](solutions/) |
| 8 个流传很广但**不能用**的数字，以及 10 个被主动排除的著名案例 | [`index/watchlist.md`](index/watchlist.md) |
| FDE 专题、原始来源登记 | [`fde/`](fde/)、[`sources/registry.yml`](sources/registry.yml) |

案例正文固定九节，其中「不可验证或存疑之处」和「引用边界」不许为空。这两节是它和客户成功故事的区别。

---

## 不做什么

不收没有一手来源的数字，不把合作公告写成已落地，不清洗掉自相矛盾的口径——摩根大通同一年给出 20 万和 32 万两套员工数，美的给出 7 亿和 7.7 亿两套降本，都照原样留着。**信息本来就不整齐，把它摆整齐反而是失真。**

也不打算让这个库看起来很全。20 条，能查到这儿就到这儿；查不到的写在 `watchlist.md`，标清楚缺什么。

---

## 贡献与许可

复制 [`cases/_TEMPLATE.md`](cases/_TEMPLATE.md)，写满九节，`python scripts/validate.py --strict`，提 PR。CI 会校验字段、章节顺序和索引是否同步。评审清单在 [`CONTRIBUTING.md`](CONTRIBUTING.md)。

案例正文 CC BY 4.0，脚本 MIT。引用保留仓库链接与证据级别。

<details>
<summary>English TL;DR</summary>

Not a case-study roundup. Four falsifiable arguments about how enterprise AI results are reported, built on 20 production deployments, 73 individual claims, and a flat CSV you can re-analyse yourself.

The core one: public efficiency numbers are mostly **statements, not measurements** — only 17 of 73 claims are independently recomputable. Each argument ends with what would make me withdraw it.

</details>
