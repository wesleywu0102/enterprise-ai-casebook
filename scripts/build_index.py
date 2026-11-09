#!/usr/bin/env python3
"""从 cases/ 自动重建 index/ 下的三个索引页。

用法:
    python scripts/build_index.py
"""
from __future__ import annotations

from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CASES = ROOT / "cases"
INDEX = ROOT / "index"

GRADE_LABEL = {
    "A": "A 法定披露/同行评审",
    "B": "B 官方+数字",
    "C": "C 单方证言",
    "D": "D 二手",
    "X": "X 已回撤",
}


def load_cases() -> list[dict]:
    out = []
    for p in sorted(CASES.rglob("*.md")):
        if p.name == "_TEMPLATE.md":
            continue
        text = p.read_text(encoding="utf-8")
        if not text.startswith("---"):
            continue
        raw = text.split("---", 2)[1]
        data = yaml.safe_load(raw) or {}
        data["_path"] = str(p.relative_to(ROOT)).replace("\\", "/")
        out.append(data)
    return out


def table(rows: list[dict], group_key: str, title: str, intro: str) -> str:
    buckets: dict[str, list[dict]] = defaultdict(list)
    for c in rows:
        key = c.get(group_key)
        if isinstance(key, list):
            for k in key:
                buckets[str(k)].append(c)
        else:
            buckets[str(key)].append(c)

    lines = [f"# {title}", "", intro, "", f"> 由 `scripts/build_index.py` 自动生成，请勿手工编辑。共 {len(rows)} 条案例。", ""]
    for key in sorted(buckets):
        lines.append(f"## {key}（{len(buckets[key])}）")
        lines.append("")
        lines.append("| 案例 | 企业 | 场景 | 证据 | 状态 | 交付 |")
        lines.append("|---|---|---|---|---|---|")
        for c in sorted(buckets[key], key=lambda x: str(x.get("company"))):
            link = f"[{c.get('title')}](../{c.get('_path')})"
            scene = ", ".join(c.get("scenario") or [])
            lines.append(
                f"| {link} | {c.get('company')} | {scene} | "
                f"{c.get('evidence_grade')} | {c.get('status')} | {c.get('deployment_model')} |"
            )
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    INDEX.mkdir(exist_ok=True)
    cases = load_cases()

    (INDEX / "by-industry.md").write_text(
        table(cases, "industry", "按行业索引", "行业是第一检索维度。点开任一案例查看完整记录。"),
        encoding="utf-8",
    )
    (INDEX / "by-scenario.md").write_text(
        table(cases, "scenario", "按场景索引", "同一场景下横向对比不同企业的做法，比纵向看单个案例更有信息量。"),
        encoding="utf-8",
    )
    (INDEX / "by-evidence.md").write_text(
        table(cases, "evidence_grade", "按证据等级索引",
              "写文章引用前，先确认案例在同行业中的证据等级。" + "；".join(f"{k}={v}" for k, v in GRADE_LABEL.items())),
        encoding="utf-8",
    )

    # 纯文本统计
    print(f"已重建 3 个索引，共 {len(cases)} 条案例")
    for g in ("A", "B", "C", "D", "X"):
        n = sum(1 for c in cases if c.get("evidence_grade") == g)
        if n:
            print(f"  {GRADE_LABEL[g]}: {n}")


if __name__ == "__main__":
    main()
