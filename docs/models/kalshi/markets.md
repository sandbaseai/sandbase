# Kalshi Get Kalshi Markets API: pricing, parameters and code examples

`kalshi/markets` · data API · Kalshi · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Get Kalshi Markets from Kalshi. Returns the official Kalshi API response unchanged.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kalshi/markets"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kalshi/markets', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kalshi/markets", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kalshi/markets", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/kalshi/markets` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Number of results per page. Defaults to 100. Maximum value is 1000. default `100`; range 0–1000 |
| `cursor` | string |  | Pagination cursor. Use the cursor value returned from the previous response to get the next page of results. Leave empty for the first page.  |
| `status` | string |  | Filter by market status. Leave empty to return markets with any status. one of: `unopened`, `open`, `paused`, `closed`, `settled` |
| `tickers` | string |  | Filter by specific market tickers. Comma-separated list of market tickers to retrieve.  |
| `mve_filter` | string |  | Filter by multivariate events (combos). 'only' returns only multivariate events, 'exclude' excludes multivariate events. one of: `only`, `exclude` |
| `event_ticker` | string |  | Event ticker to filter by. Only a single event ticker is supported.  |
| `max_close_ts` | integer |  | Filter items that close before this Unix timestamp  |
| `min_close_ts` | integer |  | Filter items that close after this Unix timestamp  |
| `series_ticker` | string |  | Filter by series ticker  |
| `max_created_ts` | integer |  | Filter items that created before this Unix timestamp  |
| `max_settled_ts` | integer |  | Filter items that settled before this Unix timestamp  |
| `max_updated_ts` | integer |  | Return markets with metadata updated at or before this Unix timestamp (in seconds). Tracks non-trading changes only. May be combined with min_updated_ts and mve_filter=exclude. May also be combined with series_ticker,…  |
| `min_created_ts` | integer |  | Filter items that created after this Unix timestamp  |
| `min_settled_ts` | integer |  | Filter items that settled after this Unix timestamp  |
| `min_updated_ts` | integer |  | Return markets with metadata updated later than this Unix timestamp (in seconds). Tracks non-trading changes only. May be combined with max_updated_ts and mve_filter=exclude. May also be combined with series_ticker,…  |

## Details

Get Kalshi Markets from Kalshi. Returns the official Kalshi API response unchanged.

The response is the official Kalshi API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kalshi/markets" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | string | No | Pagination cursor. Use the cursor value returned from the previous response to get the next page of results. Leave empty for the first page. |
| `event_ticker` | string | No | Event ticker to filter by. Only a single event ticker is supported. |
| `limit` | integer | No | Number of results per page. Defaults to 100. Maximum value is 1000. |
| `max_close_ts` | integer | No | Filter items that close before this Unix timestamp |
| `max_created_ts` | integer | No | Filter items that created before this Unix timestamp |
| `max_settled_ts` | integer | No | Filter items that settled before this Unix timestamp |
| `max_updated_ts` | integer | No | Return markets with metadata updated at or before this Unix timestamp (in seconds). Tracks non-trading changes only. May be combined with min_updated_ts and mve |
| `min_close_ts` | integer | No | Filter items that close after this Unix timestamp |
| `min_created_ts` | integer | No | Filter items that created after this Unix timestamp |
| `min_settled_ts` | integer | No | Filter items that settled after this Unix timestamp |
| `min_updated_ts` | integer | No | Return markets with metadata updated later than this Unix timestamp (in seconds). Tracks non-trading changes only. May be combined with max_updated_ts and mve_f |
| `mve_filter` | string | No | Filter by multivariate events (combos). 'only' returns only multivariate events, 'exclude' excludes multivariate events. |
| `series_ticker` | string | No | Filter by series ticker |
| `status` | string | No | Filter by market status. Leave empty to return markets with any status. |
| `tickers` | string | No | Filter by specific market tickers. Comma-separated list of market tickers to retrieve. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/kalshi/markets.json`](../../../catalog/models/kalshi/markets.json) · Store page: https://www.sandbase.ai/model/kalshi/markets
