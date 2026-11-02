# TikTok Top contents item detail API: pricing, parameters and code examples

`tiktok/ads/top-contents-item-detail` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get top contents item detail on TikTok. Returns the platform data as structured JSON.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/ads/top-contents-item-detail", "item_id": "7684011124739656991", "period_end_timestamp": 1793318400}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/ads/top-contents-item-detail', {'item_id': '7684011124739656991', 'period_end_timestamp': 1793318400})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/ads/top-contents-item-detail", {
  "item_id": "7684011124739656991",
  "period_end_timestamp": 1793318400
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/ads/top-contents-item-detail", sandbase.Params{
	"item_id": "7684011124739656991",
	"period_end_timestamp": 1793318400,
})
```

Same call via the path form: `POST /v1/api/tiktok/ads/top-contents-item-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cookie` | string |  | Custom Cookie string (optional)  |
| `item_id` | string | yes | Video item ID  |
| `country_code` | string |  | Country code of the ranking default `"US"` |
| `period_dimension` | integer |  | 3/5 /Period dimension default `3` |
| `period_end_timestamp` | integer | yes | The caller must generate this 10-digit Unix timestamp in seconds from the target ranking date, for example 1785024000; do not pass 0 because it returns an empty result  |

## Details

Get top contents item detail on TikTok. Returns the platform data as structured JSON.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/ads/top-contents-item-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"item_id": "7684011124739656991", "period_end_timestamp": 1793318400, "period_dimension": 3, "country_code": "US"}'
```

The result is returned in `outputs[0].data`. Use an `itemID` from Top Contents List with the same `period_end_timestamp` and `country_code`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `item_id` | string | Yes | Video item ID |
| `period_end_timestamp` | integer | Yes | The caller must generate this 10-digit Unix timestamp in seconds from the target ranking date, for example 1785024000; do not pass 0 because it returns an empty result |
| `cookie` | string | No | Custom Cookie string (optional) |
| `country_code` | string | No | Country code of the ranking |
| `period_dimension` | integer | No | 3/5 /Period dimension |

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

---
Machine-readable: [`catalog/models/tiktok/ads/top-contents-item-detail.json`](../../../../catalog/models/tiktok/ads/top-contents-item-detail.json) · Store page: https://www.sandbase.ai/model/tiktok/ads/top-contents-item-detail
