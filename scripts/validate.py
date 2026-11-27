#!/usr/bin/env python3
"""تحقق من سلامة ملفات محرر: YAML، والمخطط، والمعرفات، وعدد القواعد، وتغطية الاختبارات.

الاستخدام: python3 scripts/validate.py
يتطلب: pyyaml وjsonschema
"""
import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent.parent
errors = []


def load_yaml(rel):
    try:
        return yaml.safe_load((ROOT / rel).read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        errors.append(f"{rel}: تعذرت قراءة YAML: {exc}")
        return None


core = load_yaml("rules/core.yml")
reviewed = load_yaml("tests/reviewed-examples.yml")
nochange = load_yaml("tests/must-not-change.yml")
load_yaml("optional/basic-proofreading.yml")

schema = json.loads((ROOT / "schema/rule.schema.json").read_text(encoding="utf-8"))
validator = Draft202012Validator(schema)

if core:
    rules = core.get("rules", [])
    ids = [r.get("id") for r in rules]
    for rule in rules:
        for err in validator.iter_errors(rule):
            errors.append(f"{rule.get('id')}: {err.message}")
    dupes = {i for i in ids if ids.count(i) > 1}
    if dupes:
        errors.append(f"معرفات مكررة: {sorted(dupes)}")
    if core.get("rule_count") != len(rules):
        errors.append(f"rule_count = {core.get('rule_count')} والعدد الفعلي {len(rules)}")

    tested = {t.get("rule") for t in (reviewed or {}).get("tests", [])}
    for t in (reviewed or {}).get("tests", []):
        tested.update(t.get("related_rules", []))
    guarded = {t.get("related_rule") for t in (nochange or {}).get("tests", [])}
    for rule in rules:
        rid = rule["id"]
        if rid >= "MHR-C036" and rid not in tested:
            errors.append(f"{rid}: لا توجد حالة في reviewed-examples.yml")
        if rid >= "MHR-C036" and rule["examples"]["must_not_change"] and rid not in guarded:
            errors.append(f"{rid}: له مثال must_not_change ولا توجد حالة في must-not-change.yml")

    for name, data in (("reviewed-examples", reviewed), ("must-not-change", nochange)):
        tids = [t.get("id") for t in (data or {}).get("tests", [])]
        if len(tids) != len(set(tids)):
            errors.append(f"{name}: معرفات اختبار مكررة")
        if data and data.get("version") != core.get("version"):
            errors.append(f"{name}: الإصدار {data.get('version')} لا يطابق {core.get('version')}")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"سليم: {core['rule_count']} قاعدة، {len(reviewed['tests'])} حالة مراجعة، {len(nochange['tests'])} حالة يجب ألا تتغير.")
