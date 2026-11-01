#!/usr/bin/env bash
# Run any SandBase capability with curl + jq and wait for the result (sync or async).
#
#   export SANDBASE_API_KEY=sk-...
#   ./run.sh exa/search '{"query":"AI agents","numResults":3}'
#   ./run.sh app-store/search '{"term":"notes"}'
set -euo pipefail
MODEL="${1:?usage: run.sh <model> '<json params>'}"
PARAMS="${2:-{\}}"
BASE="${SANDBASE_BASE_URL:-https://api.sandbase.ai}"
AUTH="Authorization: Bearer ${SANDBASE_API_KEY:?set SANDBASE_API_KEY}"

body=$(jq -cn --arg m "$MODEL" --argjson p "$PARAMS" '$p + {model: $m}')
run=$(curl -sS --fail-with-body "$BASE/v1/run" -H "$AUTH" -H 'Content-Type: application/json' -d "$body")
status=$(jq -r .status <<<"$run")
id=$(jq -r .id <<<"$run")

delay=2
while [[ "$status" != "completed" && "$status" != "failed" && "$status" != "cancelled" ]]; do
  sleep "$delay"; [[ $delay -lt 15 ]] && delay=$((delay * 3 / 2))
  run=$(curl -sS --fail-with-body "$BASE/v1/run/$id" -H "$AUTH")
  status=$(jq -r .status <<<"$run")
  echo "… $status" >&2
done

jq . <<<"$run"
[[ "$status" == "completed" ]]
