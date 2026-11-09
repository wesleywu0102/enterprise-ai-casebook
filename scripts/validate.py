#!/usr/bin/env python3
"""校验 cases/ 下所有案例的 front-matter 与正文结构。

用法:
    python scripts/validate.py            # 校验全部
    python scripts/validate.py --strict    # 额外检查来源是否在 registry 登记

依赖: PyYAML（必需）、jsonschema（可选，缺失时用内置规则）
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CASES = ROOT / "cases"
SCHEMA = ROOT / "schema" / "case.schema.json"
REGISTRY = ROOT / "sources" / "registry.yml"

REQUIRED_HEADINGS = [
    "## 1. 一句话摘要",
    "## 2. 业务痛点",
    "## 3. AI 应用场景",
    "## 4. 落地方式",
    "## 5. 可验证成效",
    "## 6. 不可验证或存疑之处",
    "## 7. 可复用要点",
    "## 8. 引用边界",
    "## 9. 来源",
]

REQUIRED_FIELDS = [
    "id", "title", "company", "industry", "scenario",
    "deployment_model", "fde_involved", "ai_tech", "scale",
    "start_date", "status", "evidence_grade", "last_verified",
    "metrics", "sources", "confidence_notes",
    "tags", "replicability", "human_in_loop",
]

GRADES = {"A", "B", "C", "D", "X"}
STATUSES = {"pilot", "production", "scaled", "paused", "retracted"}
FDE = {"none", "vendor-embedded", "si-partner", "in-house", "unknown"}
HIL = {"none", "review-before-send", "escalation-only", "sampling-audit"}
METRIC_DIRECTIONS = {
    "cost-down", "effort-down", "time-down", "volume-up",
    "revenue-up", "quality-up", "adoption", "risk-down",
}


def split_front_matter(text: str) -> tuple[dict | None, str, str | None]:
    if not text.startswith("---"):
        return None, text, "文件未以 --- 开头，缺少 front-matter"
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, text, "front-matter 未闭合"
    raw, body = parts[1], parts[2]
    try:
        data = yaml.safe_load(raw)
    except yaml.YAMLError as exc:
        return None, body, f"YAML 解析失败: {exc}"
    if not isinstance(data, dict):
        return None, body, "front-matter 不是映射结构"
    return data, body, None


def check_body(body: str) -> list[str]:
    errs: list[str] = []
    positions = []
    for heading in REQUIRED_HEADINGS:
        idx = body.find(heading)
        if idx < 0:
            errs.append(f"缺少章节: {heading}")
        else:
            positions.append((idx, heading))
    if len(positions) == len(REQUIRED_HEADINGS):
        if positions != sorted(positions):
            errs.append("章节顺序与模板不一致")

    # 第 6 / 8 节不允许为空或仅写"无"
    for heading, minimum in (("## 6. 不可验证或存疑之处", 30), ("## 8. 引用边界", 20)):
        start = body.find(heading)
        if start < 0:
            continue
        nxt = body.find("\n## ", start + len(heading))
        section = body[start + len(heading): nxt if nxt > 0 else len(body)]
        cleaned = re.sub(r"<!--.*?-->", "", section, flags=re.S).strip()
        if len(cleaned) < minimum:
            errs.append(f"{heading} 内容过短（{len(cleaned)} 字符），必须写出具体存疑点/引用边界")
    return errs


def check_metrics(data: dict) -> list[str]:
    errs: list[str] = []
    metrics = data.get("metrics") or []
    if not isinstance(metrics, list) or not metrics:
        return ["metrics 为空"]
    for i, m in enumerate(metrics):
        if not isinstance(m, dict):
            errs.append(f"metrics[{i}] 不是映射")
            continue
        for key in ("name", "value", "baseline", "method", "direction"):
            if key not in m or str(m.get(key, "")).strip() == "":
                errs.append(f"metrics[{i}] 缺少 {key}")
        baseline = str(m.get("baseline", "")).strip()
        if baseline in {"N/A", "n/a", "NA", "-", "无"}:
            errs.append(f"metrics[{i}] baseline 写成了 {baseline}；没有基线请写「未披露」")
        method = str(m.get("method", ""))
        if method and len(method) < 8:
            errs.append(f"metrics[{i}] method 过短，需说明谁算的/怎么算/样本量")
        for bad in ("官方称", "据测算", "官方数据"):
            if method == bad:
                errs.append(f"metrics[{i}] method 只写了「{bad}」，需说明测算方")
        if m.get("direction") not in METRIC_DIRECTIONS:
            errs.append(f"metrics[{i}] direction 非法: {m.get('direction')}")
    return errs


def check_sources(data: dict) -> list[str]:
    errs: list[str] = []
    sources = data.get("sources") or []
    if not isinstance(sources, list) or not sources:
        return ["sources 为空"]
    if not any(s.get("grade") in {"A", "B"} for s in sources if isinstance(s, dict)):
        # C 级案例允许全部来源为单方证言（前提是案例自身标注为 C）
        # A/B/X 级案例若没有 A/B 来源，属于等级虚高，必须报错
        if data.get("evidence_grade") in {"A", "B", "X"}:
            errs.append("标注为 A/B/X 但没有任何 A 或 B 级来源（等级虚高）")
    for i, s in enumerate(sources):
        if not isinstance(s, dict):
            errs.append(f"sources[{i}] 不是映射")
            continue
        for key in ("id", "type", "grade", "url", "accessed"):
            if key not in s:
                errs.append(f"sources[{i}] 缺少 {key}")
        url = str(s.get("url", ""))
        if not url.startswith(("http://", "https://")):
            errs.append(f"sources[{i}] url 不合法: {url}")
        if s.get("grade") not in {"A", "B", "C", "D"}:
            errs.append(f"sources[{i}] grade 非法")
    return errs


def check_scalar(data: dict) -> list[str]:
    errs: list[str] = []
    for key in REQUIRED_FIELDS:
        if key not in data:
            errs.append(f"缺少字段: {key}")
    if data.get("evidence_grade") not in GRADES:
        errs.append(f"evidence_grade 非法: {data.get('evidence_grade')}")
    if data.get("status") not in STATUSES:
        errs.append(f"status 非法: {data.get('status')}")
    if data.get("fde_involved") not in FDE:
        errs.append(f"fde_involved 非法: {data.get('fde_involved')}")
    if data.get("human_in_loop") not in HIL:
        errs.append(f"human_in_loop 非法: {data.get('human_in_loop')}")
    rep = data.get("replicability")
    if not isinstance(rep, int) or not 1 <= rep <= 5:
        errs.append(f"replicability 需为 1-5 的整数: {rep}")
    cid = str(data.get("id", ""))
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+){2,}", cid):
        errs.append(f"id 格式不合法（需 industry-company-scene 形式）: {cid}")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(data.get("last_verified", ""))):
        errs.append("last_verified 需为 YYYY-MM-DD")
    # 回撤案例一致性
    path_is_retracted = "retracted" in str(data.get("_path", ""))
    if data.get("status") == "retracted" and data.get("evidence_grade") != "X":
        errs.append("status=retracted 时 evidence_grade 必须为 X")
    if data.get("evidence_grade") == "X" and not path_is_retracted:
        errs.append("evidence_grade=X 的案例应放在 cases/retracted/")
    return errs


def json_schema_check(data: dict) -> list[str]:
    try:
        import jsonschema  # type: ignore
    except ImportError:
        return []
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    payload = {k: v for k, v in data.items() if not k.startswith("_")}
    validator = jsonschema.Draft202012Validator(schema)
    return [
        f"schema: {e.message} (at {list(e.absolute_path)})"
        for e in sorted(validator.iter_errors(payload), key=lambda e: e.path)
    ]


def load_registry(strict: bool) -> set[str]:
    if not strict or not REGISTRY.exists():
        return set()
    try:
        reg = yaml.safe_load(REGISTRY.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError:
        return set()
    urls: set[str] = set()
    for item in reg.get("sources", []) or []:
        if isinstance(item, dict) and item.get("url"):
            urls.add(str(item["url"]).rstrip("/"))
    return urls


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true", help="额外检查来源是否在 registry 登记")
    args = parser.parse_args()

    files = sorted(p for p in CASES.rglob("*.md") if p.name != "_TEMPLATE.md")
    if not files:
        print("未找到任何案例文件")
        return 1

    registry = load_registry(args.strict)
    total_errors = 0
    seen_ids: dict[str, Path] = {}

    for path in files:
        rel = path.relative_to(ROOT)
        errs: list[str] = []
        text = path.read_text(encoding="utf-8")
        data, body, fm_err = split_front_matter(text)
        if fm_err:
            print(f"✗ {rel}\n    {fm_err}")
            total_errors += 1
            continue

        data["_path"] = str(path)
        errs += check_scalar(data)
        errs += check_metrics(data)
        errs += check_sources(data)
        errs += check_body(body)
        errs += json_schema_check(data)

        cid = str(data.get("id", ""))
        if cid in seen_ids:
            errs.append(f"id 重复，与 {seen_ids[cid].relative_to(ROOT)} 冲突")
        else:
            seen_ids[cid] = path

        if registry:
            for s in data.get("sources", []) or []:
                if isinstance(s, dict):
                    u = str(s.get("url", "")).rstrip("/")
                    if u and u not in registry:
                        errs.append(f"来源未在 registry.yml 登记: {u}")

        if errs:
            total_errors += len(errs)
            print(f"✗ {rel}")
            for e in errs:
                print(f"    - {e}")
        else:
            print(f"✓ {rel}  [{data.get('evidence_grade')}] {data.get('title')}")

    print()
    print(f"共 {len(files)} 个案例，{total_errors} 个问题")
    return 1 if total_errors else 0


if __name__ == "__main__":
    sys.exit(main())
