# Artificial Analysis API: 4 endpoints with pricing and code examples

Call 4 Artificial Analysis endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`artificial-analysis/cost-per-task`](../models/artificial-analysis/cost-per-task.md) | Get per-model cost-per-task data from the Artificial Analysis homepage. Returns Intelligence Index score, cost per task (USD) with… | $0.05 per call |
| [`artificial-analysis/llm-providers-leaderboard`](../models/artificial-analysis/llm-providers-leaderboard.md) | Get the main LLM API Providers Leaderboard data, including all model endpoints and their performance metrics (speed, latency, price,… | $0.01 per call (free daily quota) |
| [`artificial-analysis/models-list`](../models/artificial-analysis/models-list.md) | Get a list of all LLM models (one row per model variant, e.g. each effort level) with slug, display name, the release it belongs to… | $0.02 per call |
| [`artificial-analysis/search-models`](../models/artificial-analysis/search-models.md) | Search for models by name or slug. Performs client-side filtering against the full models list, matching the query string against model… | $0.01 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "artificial-analysis/cost-per-task"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
