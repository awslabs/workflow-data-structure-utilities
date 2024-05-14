#!/bin/bash
set -eo pipefail
cd "$(dirname "$0")"
root="$(pwd)"

for i in src/*; do
  if [[ ! -d "$i" ]]; then
    echo "${i} is not a directory!"
  fi
  echo "=== Testing ${i} ==="
  python3 -m coverage run -p -m pytest "${root}/${i}/tests.py"

done