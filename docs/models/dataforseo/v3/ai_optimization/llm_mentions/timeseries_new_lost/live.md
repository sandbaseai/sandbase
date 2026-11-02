# DataForSEO LLM Mentions New and Lost API: pricing, parameters and code examples

`dataforseo/v3/ai_optimization/llm_mentions/timeseries_new_lost/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.104 per call · **Modes:** sync

New and lost mentions of a domain or keyword in AI answers per period.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.104**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/ai_optimization/llm_mentions/timeseries_new_lost/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/ai_optimization/llm_mentions/timeseries_new_lost/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/ai_optimization/llm_mentions/timeseries_new_lost/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/ai_optimization/llm_mentions/timeseries_new_lost/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/ai_optimization/llm_mentions/timeseries_new_lost/live` with the body above minus `model`.

## Details

New and lost mentions of a domain or keyword in AI answers per period.

Request fields follow the official DataForSEO `/v3/ai_optimization/llm_mentions/timeseries_new_lost/live` task schema (one task per call). The response is DataForSEO's original JSON; results are in `tasks[].result`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/ai_optimization/llm_mentions/timeseries_new_lost/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"target": [{"domain": "nike.com"}], "date_from": "2026-07-01", "date_to": "2026-10-01", "group_range": "month"}'
```

### Parameters

The JSON body is forwarded to the upstream endpoint. Main fields:

| Name | Description |
|---|---|
| `target` | Array of up to 10 entities, each with one `domain` or one `keyword` (optional `search_filter`, `search_scope`, `match_type`). |
| `date_from` | Start date, "yyyy-mm-dd" (from 2025-08-01). |
| `date_to` | End date, "yyyy-mm-dd". |
| `group_range` | "day", "week", "month" or "year". |
| `location_code` | Location code; default 2840 (United States). |
| `language_code` | Language code; default "en". |
| `platform` | Optional: "google" (AI Overviews) or "chat_gpt". Omit for both. |

### Reference

- Official docs: https://docs.dataforseo.com/v3/ai_optimization/llm_mentions/timeseries_new_lost/live/

### Pricing

Billed at the actual cost of each call, about $0.104 for the request above. The cost grows with the number of rows, targets or tokens a call returns. Failed calls are not charged. Searches with no results are billed at their actual cost.

---
Machine-readable: [`catalog/models/dataforseo/v3/ai_optimization/llm_mentions/timeseries_new_lost/live.json`](../../../../../../../catalog/models/dataforseo/v3/ai_optimization/llm_mentions/timeseries_new_lost/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/ai_optimization/llm_mentions/timeseries_new_lost/live
