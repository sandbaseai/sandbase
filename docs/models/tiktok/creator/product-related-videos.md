# TikTok Product Related Videos

`tiktok/creator/product-related-videos` · api · TikTok

Returns videos linked to a specified product alongside interaction metrics like counts for likes, comments, and shares. Supports date-based filtering using product and video identifiers.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/creator/product-related-videos", "item_id": "7350810998023949599", "product_id": "1732108663255959373"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/creator/product-related-videos', {'item_id': '7350810998023949599', 'product_id': '1732108663255959373'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/creator/product-related-videos", {
  "item_id": "7350810998023949599",
  "product_id": "1732108663255959373"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/creator/product-related-videos", sandbase.Params{
	"item_id": "7350810998023949599",
	"product_id": "1732108663255959373",
})
```

Same call via the path form: `POST /v1/api/tiktok/creator/product-related-videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `proxy` |  |  | Optional HTTP Proxy Address  |
| `item_id` | string | yes | Video ID  |
| `product_id` | string | yes | Product ID  |
| `start_date` | string |  | Query Start Date, e.g. '04-01-2025'  |

## Details

Retrieve all videos linked to a specific product by supplying `product_id` and `item_id`. You can also filter results by calendar month using `start_date`.

### Use cases

- Analyze promotional effectiveness across creator videos featuring the same product.
- Monitor engagement metrics such as likes, comments, and shares on sponsored videos.
- Compare performance differences across creator campaigns for a specific item.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/creator/product-related-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"item_id": "7350810998023949599", "product_id": "1732108663255959373"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `item_id` | string | Yes | Video ID |
| `product_id` | string | Yes | Product ID |
| `proxy` | string | No | Optional HTTP Proxy Address |
| `start_date` | string | No | Query Start Date, e.g. '04-01-2025' |

### Notes

- `start_date` expects a date formatted like '04-01-2025' and defaults to that calendar month.
- Both `product_id` and `item_id` are required to query related video data.
- An optional HTTP proxy can be configured via `proxy`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Creator Account Health Status](/model/tiktok/creator/account-health-status): Returns the health status of a TikTok Shop creator account.
- [TikTok Creator Account Insights Overview](/model/tiktok/creator/account-insights-overview): Retrieves performance metrics for a TikTok Shop creator account, including revenue, exposure, clicks, and orders for the specified month.
- [TikTok Creator Account Violations](/model/tiktok/creator/account-violation-list): Returns the violation history and enforcement actions for a TikTok Shop creator account.

---
Machine-readable: [`catalog/models/tiktok/creator/product-related-videos.json`](../../../../catalog/models/tiktok/creator/product-related-videos.json) · Store page: https://www.sandbase.ai/model/tiktok/creator/product-related-videos
