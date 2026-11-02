# Polymarket List series API: pricing, parameters and code examples

`polymarket/series` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00044 per call (free daily quota) · **Modes:** sync

List series from Polymarket. Returns the official Polymarket API response unchanged.

## Pricing

- **$0.00044 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/series"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/series', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/series", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/series", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/polymarket/series` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `slug` | array |  | slug  |
| `limit` | integer |  | limit range 0– |
| `order` | string |  | Comma-separated list of fields to order by  |
| `closed` | boolean |  | closed  |
| `offset` | integer |  | offset range 0– |
| `ascending` | boolean |  | ascending  |
| `recurrence` | string |  | recurrence  |
| `include_chat` | boolean |  | include_chat  |
| `categories_ids` | array |  | categories_ids  |
| `exclude_events` | boolean |  | exclude_events  |
| `categories_labels` | array |  | categories_labels  |

## Details

List series from Polymarket. Returns the official Polymarket API response unchanged.

The response is the official Polymarket API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/series" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": 1}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `ascending` | boolean | No | ascending |
| `categories_ids` | array | No | categories_ids |
| `categories_labels` | array | No | categories_labels |
| `closed` | boolean | No | closed |
| `exclude_events` | boolean | No | exclude_events |
| `include_chat` | boolean | No | include_chat |
| `limit` | integer | No | limit |
| `offset` | integer | No | offset |
| `order` | string | No | Comma-separated list of fields to order by |
| `recurrence` | string | No | recurrence |
| `slug` | array | No | slug |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/polymarket/series.json`](../../../catalog/models/polymarket/series.json) · Store page: https://www.sandbase.ai/model/polymarket/series
