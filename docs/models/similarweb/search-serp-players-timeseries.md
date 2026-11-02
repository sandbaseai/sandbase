# Similarweb SERP Players - Clicks over time API: pricing, parameters and code examples

`similarweb/search-serp-players-timeseries` · data API · Similarweb · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.075 per call · **Modes:** sync

Get month-by-month clicks for the websites that appear on search results for given keywords.

## Pricing

- Depends on parameters (`params.limit`).

Formula: `0.075 * Math.max(1.0, Math.ceil(Math.min(20.0, (output.data?.data != nil ? len(output.data.data) : (params.limit ?? 20)) * 1.0) * 20000.0 / 1000000.0))`

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "similarweb/search-serp-players-timeseries", "end_date": "2026-09", "keywords": "running shoes", "limit": 1, "start_date": "2026-09"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('similarweb/search-serp-players-timeseries', {'end_date': '2026-09', 'keywords': 'running shoes', 'limit': 1, 'start_date': '2026-09'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("similarweb/search-serp-players-timeseries", {
  "end_date": "2026-09",
  "keywords": "running shoes",
  "limit": 1,
  "start_date": "2026-09"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "similarweb/search-serp-players-timeseries", sandbase.Params{
	"end_date": "2026-09",
	"keywords": "running shoes",
	"limit": 1,
	"start_date": "2026-09",
})
```

Same call via the path form: `POST /v1/api/similarweb/search-serp-players-timeseries` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer | yes | limit range 1–20 |
| `offset` | integer |  | offset range 0–100000 |
| `country` | string |  | Worldwide data only; values are case-insensitive. one of: `ww`; default `"ww"` |
| `end_date` | string | yes | end_date  |
| `keywords` | string | yes | keywords  |
| `start_date` | string | yes | start_date  |
| `granularity` | string |  | granularity one of: `monthly` |

## Details

Get month-by-month clicks for the websites that appear on search results for given keywords.

The response is the official Similarweb API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/similarweb/search-serp-players-timeseries" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"start_date": "2026-09", "end_date": "2026-09", "country": "ww", "keywords": "running shoes", "limit": 1}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `country` | string | No | Worldwide data only; values are case-insensitive. |
| `end_date` | string | Yes | end_date |
| `granularity` | string | No | granularity |
| `keywords` | string | Yes | keywords |
| `limit` | integer | Yes | limit |
| `offset` | integer | No | offset |
| `start_date` | string | Yes | start_date |

### Pricing

$0.075 per Similarweb credit; 0.02 credit per returned row, rounded up to whole credits. Failed calls are not charged.

---
Machine-readable: [`catalog/models/similarweb/search-serp-players-timeseries.json`](../../../catalog/models/similarweb/search-serp-players-timeseries.json) · Store page: https://www.sandbase.ai/model/similarweb/search-serp-players-timeseries
