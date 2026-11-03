# TikTok Top Ads Spotlight API: pricing, parameters and code examples

`tiktok/ads/top-ads-spotlight` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns top spotlight ad cases, highlights, and performance metrics across industries or filtered by a specific industry ID. Supports pagination via page and limit parameters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/ads/top-ads-spotlight"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/ads/top-ads-spotlight', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/ads/top-ads-spotlight", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/ads/top-ads-spotlight", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok/ads/top-ads-spotlight` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number, default 1  |
| `limit` | integer |  | Items per page, default 20  |
| `industry` | string |  | Industry ID, optional, returns cross-industry list if omitted, e.g., Education: 25000000000  |

## Details

Look up top-performing TikTok ad showcases and creative highlights. Filter results by `industry` or paginate through cross-industry cases using `page` and `limit`.

### Use cases

- Analyze high-performing video ad creative formats and hooks within specific industries.
- Gather creative inspiration and benchmark engagement metrics for campaign planning.
- Track top ad trends and spotlight examples across multiple business sectors.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/ads/top-ads-spotlight" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `page` | integer | No | Page number, default 1 |
| `limit` | integer | No | Items per page, default 20 |
| `industry` | string | No | Industry ID, optional, returns cross-industry list if omitted, e.g., Education: 25000000000 |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "materials": [
      {
        "highlight": "Showcase a real-time comparison between products, while communicating your product's valu…",
        "id": "7182310470102122497",
        "like": 33506,
        "video_info": {
          "duration": 43.542
        }
      }
    ]
  }
}
```

### Notes

- Omitting `industry` returns a cross-industry list of spotlight ads.
- Default pagination settings are `page` 1 and `limit` 20.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Ad Interactive Analysis](/apis/tiktok/ads/ad-interactive-analysis): Returns audience retention and interaction analytics across video timestamps for a specified ad creative.
- [TikTok Ad Keyframe Analysis](/apis/tiktok/ads/ad-keyframe-analysis): Returns keyframe performance metrics across video ad timestamps for a specified material ID, including retention and conversion figures.
- [TikTok Ad Material Percentile Rankings](/apis/tiktok/ads/ad-percentile): Returns ad performance percentile rankings within the industry for a specific ad material.

---
Machine-readable: [`catalog/models/tiktok/ads/top-ads-spotlight.json`](../../../../catalog/models/tiktok/ads/top-ads-spotlight.json) · Store page: https://www.sandbase.ai/model/tiktok/ads/top-ads-spotlight
