#!/usr/bin/env bash
# يبني حزمة المهارة dist/muharrir-<version>.zip من الملفات المتتبعة في git،
# ثم يتأكد أن الحزمة تتضمن SKILL.md ومجلدات rules وreferences وtests.
set -euo pipefail
cd "$(dirname "$0")/.."

version=$(sed -n 's/^version: //p' rules/core.yml)
out="dist/muharrir-${version}.zip"
mkdir -p dist
git archive --format=zip --prefix=muharrir/ -o "$out" HEAD

for required in SKILL.md rules/core.yml references/ tests/ optional/ schema/; do
  if ! unzip -Z1 "$out" | grep -q "^muharrir/${required}"; then
    echo "الحزمة لا تتضمن ${required}" >&2
    exit 1
  fi
done
echo "$out"
