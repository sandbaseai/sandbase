# TikTok Creative Center Ad Search

`tiktok/ads/search-ads` · api · TikTok

Searches ad materials in the TikTok Creative Center using filters such as keyword, industry, country, and performance metrics. Returns ad titles, brand names, IDs, and video metadata.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/ads/search-ads"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/ads/search-ads', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/ads/search-ads", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/ads/search-ads", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok/ads/search-ads` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `like` | integer |  | Like count filter, 1=All  |
| `page` | integer |  | Page number, default 1  |
| `limit` | integer |  | Items per page, default 20, max 50  |
| `period` | integer |  | Time period in days, e.g., 7, 30, 120, 180 days  |
| `keyword` | string |  | Search keyword, optional, returns all ads if empty  |
| `duration` |  |  | 视频时长筛选值（可选）/Video duration filter value (optional)  |
| `industry` | string |  | Industry ID list, multiple IDs separated by commas.  |
| `order_by` | string |  | Sort method, "for_you"=Recommended, "likes"=Sort by likes  |
| `ad_format` | integer |  | Ad format, 1=Video ads  |
| `objective` | integer |  | Ad objective, 1=All  |
| `search_id` | string |  | Search ID (optional)  |
| `ad_language` | string |  | Ad language code, e.g., en, zh  |
| `country_code` | string |  | Country code, e.g., US, UK, JP  |
| `pattern_label` |  |  | 创意趋势标签（可选）/Creative pattern label (optional)  |

## Details

Query TikTok Creative Center ad cases using parameters like `keyword`, `industry`, and `country_code`. Returns matching ad materials along with engagement metrics and video details.

### Use cases

- Discover top-performing video ad campaigns across specific industries.
- Analyze competitive creative strategies by keyword and country.
- Benchmark ad performance metrics such as like counts and video durations.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/ads/search-ads" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `like` | integer | No | Like count filter, 1=All |
| `page` | integer | No | Page number, default 1 |
| `limit` | integer | No | Items per page, default 20, max 50 |
| `period` | integer | No | Time period in days, e.g., 7, 30, 120, 180 days |
| `keyword` | string | No | Search keyword, optional, returns all ads if empty |
| `duration` | string | No | 视频时长筛选值（可选）/Video duration filter value (optional) |
| `industry` | string | No | Industry ID list, multiple IDs separated by commas. |
| `order_by` | string | No | Sort method, "for_you"=Recommended, "likes"=Sort by likes |
| `ad_format` | integer | No | Ad format, 1=Video ads |
| `objective` | integer | No | Ad objective, 1=All |
| `search_id` | string | No | Search ID (optional) |
| `ad_language` | string | No | Ad language code, e.g., en, zh |
| `country_code` | string | No | Country code, e.g., US, UK, JP |
| `pattern_label` | string | No | 创意趋势标签（可选）/Creative pattern label (optional) |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "materials": [
      {
        "ad_title": "Upgrade your dog's gear",
        "brand_name": "Tactipup",
        "id": "7172587525965332482",
        "like": 69817,
        "video_info": {
          "duration": 29.92
        }
      }
    ]
  }
}
```

### Notes

- Use `limit` (max 50, default 20) and `page` (default 1) for pagination.
- `order_by` accepts `for_you` for recommendations or `likes` to sort by engagement.
- `industry` accepts a comma-separated list of industry IDs.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Ad Interactive Analysis](/model/tiktok/ads/ad-interactive-analysis): Returns audience retention and interaction analytics across video timestamps for a specified ad creative.
- [TikTok Ad Keyframe Analysis](/model/tiktok/ads/ad-keyframe-analysis): Returns keyframe performance metrics across video ad timestamps for a specified material ID, including retention and conversion figures.
- [TikTok Ad Material Percentile Rankings](/model/tiktok/ads/ad-percentile): Returns ad performance percentile rankings within the industry for a specific ad material.

---
Machine-readable: [`catalog/models/tiktok/ads/search-ads.json`](../../../../catalog/models/tiktok/ads/search-ads.json) · Store page: https://www.sandbase.ai/model/tiktok/ads/search-ads
