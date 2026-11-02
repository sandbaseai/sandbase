# TikTok Top contents list API: pricing, parameters and code examples

`tiktok/ads/top-contents-list` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get top contents list on TikTok. Returns the platform data as structured JSON.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/ads/top-contents-list", "period_end_timestamp": 1793318400}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/ads/top-contents-list', {'period_end_timestamp': 1793318400})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/ads/top-contents-list", {
  "period_end_timestamp": 1793318400
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/ads/top-contents-list", sandbase.Params{
	"period_end_timestamp": 1793318400,
})
```

Same call via the path form: `POST /v1/api/tiktok/ads/top-contents-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number default `1` |
| `limit` | integer |  | Items per page, max 100 default `20` |
| `cookie` | string |  | Custom Cookie string (optional)  |
| `country_code` | string |  | Country code default `"US"` |
| `organic_only` | boolean |  | Organic content only default `false` |
| `order_by_metric` | integer |  | Order by metric default `1` |
| `period_dimension` | integer |  | 3/5 /Period dimension default `3` |
| `content_label_ids` | string |  | Content label IDs, comma separated  |
| `period_end_timestamp` | integer | yes | The caller must generate this 10-digit Unix timestamp in seconds from the target ranking date, for example 1785024000; do not pass 0 because it returns an empty result  |

## Details

Get top contents list on TikTok. Returns the platform data as structured JSON.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/ads/top-contents-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"period_end_timestamp": 1793318400, "period_dimension": 3, "country_code": "US", "order_by_metric": 1, "page": 1, "limit": 20}'
```

The result is returned in `outputs[0].data`. `period_end_timestamp` is the Unix time (seconds, UTC midnight) of a recent ranking day. Older days, and regions outside US, TH, JP, ID and VN, return an empty `entityInfos`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `period_end_timestamp` | integer | Yes | The caller must generate this 10-digit Unix timestamp in seconds from the target ranking date, for example 1785024000; do not pass 0 because it returns an empty result |
| `content_label_ids` | string | No | Content label IDs, comma separated |
| `cookie` | string | No | Custom Cookie string (optional) |
| `country_code` | string | No | Country code |
| `limit` | integer | No | Items per page, max 100 |
| `order_by_metric` | integer | No | Order by metric |
| `organic_only` | boolean | No | Organic content only |
| `page` | integer | No | Page number |
| `period_dimension` | integer | No | 3/5 /Period dimension |

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

---
Machine-readable: [`catalog/models/tiktok/ads/top-contents-list.json`](../../../../catalog/models/tiktok/ads/top-contents-list.json) · Store page: https://www.sandbase.ai/model/tiktok/ads/top-contents-list
