# Polymarket Search markets, events, and profiles API: pricing, parameters and code examples

`polymarket/public-search` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.012 per call (free daily quota) · **Modes:** sync

Search markets, events, and profiles from Polymarket. Returns the official Polymarket API response unchanged.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/public-search", "q": "election"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/public-search', {'q': 'election'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/public-search", {
  "q": "election"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/public-search", sandbase.Params{
	"q": "election",
})
```

Same call via the path form: `POST /v1/api/polymarket/public-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string | yes | q  |
| `page` | integer |  | page  |
| `sort` | string |  | sort  |
| `cache` | boolean |  | cache  |
| `ascending` | boolean |  | ascending  |
| `optimized` | boolean |  | optimized  |
| `events_tag` | array |  | events_tag  |
| `recurrence` | string |  | recurrence  |
| `search_tags` | boolean |  | search_tags  |
| `events_status` | string |  | events_status  |
| `exclude_tag_id` | array |  | exclude_tag_id  |
| `limit_per_type` | integer |  | limit_per_type  |
| `search_profiles` | boolean |  | search_profiles  |
| `keep_closed_markets` | integer |  | keep_closed_markets  |

## Details

Search markets, events, and profiles from Polymarket. Returns the official Polymarket API response unchanged.

The response is the official Polymarket API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/public-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "election"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `ascending` | boolean | No | ascending |
| `cache` | boolean | No | cache |
| `events_status` | string | No | events_status |
| `events_tag` | array | No | events_tag |
| `exclude_tag_id` | array | No | exclude_tag_id |
| `keep_closed_markets` | integer | No | keep_closed_markets |
| `limit_per_type` | integer | No | limit_per_type |
| `optimized` | boolean | No | optimized |
| `page` | integer | No | page |
| `q` | string | Yes | q |
| `recurrence` | string | No | recurrence |
| `search_profiles` | boolean | No | search_profiles |
| `search_tags` | boolean | No | search_tags |
| `sort` | string | No | sort |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/polymarket/public-search.json`](../../../catalog/models/polymarket/public-search.json) · Store page: https://www.sandbase.ai/model/polymarket/public-search
