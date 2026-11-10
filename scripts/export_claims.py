#!/usr/bin/env python3
"""把 cases/ 里的每个「宣称」拍平成一列可查询的记录。

输出 data/claims.csv —— 本仓库唯一被设计成「给别人拿去用」的资产。
别人可以用它做自己的统计、画图、找选题，不必同意本库的任何结论。

用法:
    python scripts/export_claims.py
"""
from __future__ import annotations

import csv
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CASES = ROOT / "cases"
OUT = ROOT / "data" / "claims.csv"

FIELDS = [
    "case_id", "company", "industry", "pattern", "evidence_grade",
    "metric", "value", "unit", "baseline", "baseline_status",
    "method", "window", "window_status", "direction", "claim_class",
    "recomputable", "top_source_grade", "source_url", "case_file",
]

# 判定口径（写在 CSV 之外的唯一理由：让判定规则可被质疑）
UNDISCLOSED = ("未披露", "不适用", "同上", "unknown", "")
EFFECT_DIRS = {
    "effort-down", "time-down", "cost-down", "quality-up", "volume-down",
    "time-up", "cost-up",
}
ADOPTION_DIRS = {"adoption", "coverage", "scale"}


def baseline_status(raw: str) -> str:
    s = str(raw or "").strip()
    if not s or any(k in s for k in UNDISCLOSED if k):
        return "undisclosed"
    return "stated"


def window_status(raw: str) -> str:
    s = str(raw or "").strip()
    if not s or any(k in s for k in UNDISCLOSED if k):
        return "undisclosed"
    return "stated"


# 方法说明里出现这些词，等于作者自己承认口径没定义清楚 —— 不能算「可复算」
WEAK_METHOD = (
    "未定义", "未披露", "未说明", "未公开", "无法核验", "无法复核",
    "口径存疑", "定性表述", "存疑", "未给出", "无基线", "无对照",
)


def is_recomputable(bs: str, ws: str, method: str) -> str:
    if bs != "stated" or ws != "stated" or not method:
        return "no"
    if any(k in method for k in WEAK_METHOD):
        return "no"
    return "yes"


def claim_class(m: dict) -> str:
    """区分「规模」「效应」「能力描述」「金额」——这四类不能混在一个百分比里谈。"""
    v = str(m.get("value", ""))
    d = str(m.get("direction", ""))
    n = str(m.get("name", ""))
    if any(k in n for k in ("合同", "降本", "收益", "成本", "价格", "费用")):
        return "money"
    if "%" in v or d in EFFECT_DIRS:
        return "effect"
    if re.search(r"\d", v) and (d in ADOPTION_DIRS or any(k in n for k in ("数", "率", "规模", "覆盖", "门店", "员工", "用户"))):
        return "scale"
    return "capability"


def main() -> None:
    rows = []
    for p in sorted(CASES.rglob("*.md")):
        if p.name == "_TEMPLATE.md":
            continue
        text = p.read_text(encoding="utf-8")
        if not text.startswith("---"):
            continue
        d = yaml.safe_load(text.split("---", 2)[1]) or {}
        srcs = [s for s in (d.get("sources") or []) if isinstance(s, dict)]
        grades = [str(s.get("grade", "")) for s in srcs]
        top = min(grades, key=lambda g: "ABCDX".index(g) if g in "ABCDX" else 9) if grades else ""
        url = next((str(s.get("url", "")) for s in srcs if str(s.get("grade")) == "A"), "")
        if not url and srcs:
            url = str(srcs[0].get("url", ""))

        last_window = ""
        for m in (d.get("metrics") or []):
            if not isinstance(m, dict):
                continue
            w = str(m.get("window", "")).strip()
            if w and w not in ("同上", "未披露"):
                last_window = w
            elif w == "同上":
                w = last_window
            b = str(m.get("baseline", "")).strip()
            bs = baseline_status(b)
            ws = window_status(w)
            rows.append({
                "case_id": d.get("id", ""),
                "company": d.get("company", ""),
                "industry": d.get("industry", ""),
                "pattern": ", ".join(d.get("pattern") or []),
                "evidence_grade": d.get("evidence_grade", ""),
                "metric": m.get("name", ""),
                "value": m.get("value", ""),
                "unit": m.get("unit", ""),
                "baseline": b,
                "baseline_status": bs,
                "method": str(m.get("method", "")).strip(),
                "window": w,
                "window_status": ws,
                "direction": m.get("direction", ""),
                "claim_class": claim_class(m),
                "recomputable": is_recomputable(bs, ws, str(m.get("method", "")).strip()),
                "top_source_grade": top,
                "source_url": url,
                "case_file": str(p.relative_to(ROOT)).replace("\\", "/"),
            })

    OUT.parent.mkdir(exist_ok=True)
    with OUT.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows)

    n = len(rows)
    no_base = sum(1 for r in rows if r["baseline_status"] == "undisclosed")
    recomputable = sum(1 for r in rows if r["recomputable"] == "yes")
    print(f"已导出 {n} 条宣称 -> {OUT.relative_to(ROOT)}")
    print(f"  无基线 {no_base} ({no_base / n:.1%})")
    print(f"  可复算（基线+时间窗+方法齐备）{recomputable} ({recomputable / n:.1%})")


if __name__ == "__main__":
    main()
