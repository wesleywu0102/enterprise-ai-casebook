#!/usr/bin/env python3
"""写稿前查一句：这个数字在库里能不能用。

    python scripts/check_claim.py 35%
    python scripts/check_claim.py 西门子
    python scripts/check_claim.py --stats

先查 index/watchlist.md 里的「不收」清单，再查 data/claims.csv。
只输出能核实的部分；查不到就明说查不到，不猜。
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CLAIMS = ROOT / "data" / "claims.csv"
WATCHLIST = ROOT / "index" / "watchlist.md"


def load():
    if not CLAIMS.exists():
        sys.exit("先跑 python scripts/export_claims.py 生成 data/claims.csv")
    return list(csv.DictReader(CLAIMS.open(encoding="utf-8")))


def watch_hits(kw: str) -> list[str]:
    text = WATCHLIST.read_text(encoding="utf-8").splitlines()
    out = []
    for i, line in enumerate(text):
        if kw in line and line.strip().startswith(("-", "|", "#")):
            out.append(line.strip())
        elif kw in line and i and text[i - 1].strip().startswith("###"):
            out.append(f"{text[i-1].strip()}  →  {line.strip()}")
    return out[:8]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("keyword", nargs="?", help="数字、企业名或关键词")
    ap.add_argument("--stats", action="store_true", help="只打印口径统计")
    a = ap.parse_args()
    rows = load()

    if a.stats:
        n = len(rows)
        no_base = sum(1 for r in rows if r["baseline_status"] != "stated")
        ok = sum(1 for r in rows if r["recomputable"] == "yes")
        print(f"{n} 条宣称｜无基线 {no_base} ({no_base/n:.0%})｜可独立复算 {ok} ({ok/n:.0%})")
        print("判定规则见 scripts/export_claims.py；为什么这两个比例不等于「效果真假」，见 findings/01")
        return

    if not a.keyword:
        ap.print_help()
        return

    kw = a.keyword
    w = watch_hits(kw)
    if w:
        print(f"⚠ 「{kw}」出现在待回溯/不收清单里：")
        for line in w:
            print("   ", line)
        print("   → 详见 index/watchlist.md\n")

    hit = [r for r in rows if any(kw in str(v) for v in r.values())]
    # 关键词可能只出现在正文或厂商名里，claims.csv 没收录这些列 —— 再查一遍案例原文
    case_hits = []
    for p in sorted((ROOT / "cases").rglob("*.md")):
        if p.name == "_TEMPLATE.md":
            continue
        if kw in p.read_text(encoding="utf-8"):
            case_hits.append(str(p.relative_to(ROOT)).replace("\\", "/"))
    if not hit and case_hits:
        print(f"「{kw}」不在成效数字里，但出现在这些案例中：")
        for c in case_hits[:8]:
            print("   ", c)
        print("案例正文里的数字未必是成效宣称，翻 §5 和 §8 再决定。\n")
        return
    if not hit:
        print(f"库里没有「{kw}」这条宣称。")
        print("不代表它是假的，只代表本库没有核实过它 —— 别引。")
        return

    print(f"库里有 {len(hit)} 条相关宣称：\n")
    for r in hit[:12]:
        flag = "可复算" if r["recomputable"] == "yes" else "不可复算"
        print(f"  {r['company']}｜{r['metric']}：{r['value']}")
        print(f"    {flag}｜证据 {r['evidence_grade']}｜基线 {r['baseline'] or '未披露'}")
        print(f"    口径：{r['method']}")
        print(f"    {r['case_file']}  →  {r['source_url']}\n")
    print("引用前翻该案例的 §8 引用边界。")


if __name__ == "__main__":
    main()
