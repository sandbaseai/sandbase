# TikTok Creative Center Ad Search API: pricing, parameters and code examples

`tiktok/ads/search-ads` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Searches ad materials in the TikTok Creative Center using filters such as keyword, industry, country, and performance metrics. Returns ad titles, brand names, IDs, and video metadata.

## Pricing

- **$0.001 per call** (USD)
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

Searches TikTok Creative Center ad materials and returns a page of matching ads with titles, brand names, like counts, click-through rates and video details. No input is required. You can narrow results with `keyword`, `industry`, `country_code`, `period` and other filters.

### Use cases

- Find the most liked video ads in one industry for a given country.
- Search a keyword to see how competing brands word their ad titles.
- Collect cover images and video files of ads for a creative swipe file.
- Compare `ctr` and `like` across ads with different campaign objectives.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/ads/search-ads" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `ad_format` | integer | No | Ad format, 1=Video ads |
| `ad_language` | string | No | Ad language code, e.g., en, zh |
| `country_code` | string | No | Country code, e.g., US, UK, JP |
| `duration` | string | No | 视频时长筛选值（可选）/Video duration filter value (optional) |
| `industry` | string | No | Industry ID list, multiple IDs separated by commas. |
| `keyword` | string | No | Search keyword, optional, returns all ads if empty |
| `like` | integer | No | Like count filter, 1=All |
| `limit` | integer | No | Items per page, default 20, max 50 |
| `objective` | integer | No | Ad objective, 1=All |
| `order_by` | string | No | Sort method, "for_you"=Recommended, "likes"=Sort by likes |
| `page` | integer | No | Page number, default 1 |
| `pattern_label` | string | No | 创意趋势标签（可选）/Creative pattern label (optional) |
| `period` | integer | No | Time period in days, e.g., 7, 30, 120, 180 days |
| `search_id` | string | No | Search ID (optional) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "materials": [
      {
        "ad_title": "Prism Pavilion — every item earns its place",
        "brand_name": "wondermart",
        "cost": 2,
        "ctr": 0.16,
        "favorite": false,
        "id": "7164467399885864962",
        "industry_key": "label_15100000000",
        "is_search": true,
        "like": 36951,
        "objective_key": "campaign_objective_traffic",
        "tag": 1,
        "video_info": {
          "cover": "https://p16-common-sign.tiktokcdn.com/tos-useast2a-p-0051c799-euttp/ocZdEUNYLDA0…",
          "duration": 17.904,
          "height": 1024,
          "vid": "v14033g50000d7nteivog65o65kvtj6g",
          "video_url": {
            "360p": "https://v16m-default.tiktokcdn.com/3880605c9b6dfc909a49f6d67c0fc8ad/6ae9e52b/vid…",
            "480p": "https://v16m-default.tiktokcdn.com/08003f78c06f5df8e4e3a125013dd0d7/6ae9e52b/vid…",
            "540p": "https://v16m-default.tiktokcdn.com/b4f69654b8cbb8170275f69bfc79d20f/6ae9e52b/vid…",
            "720p": "https://v16m-default.tiktokcdn.com/a2fa185eb2001a03e614595a0bc26843/6ae9e52b/vid…"
          },
          "width": 576
        }
      }
    ],
    "pagination": {
      "has_more": true,
      "page": 1,
      "size": 20,
      "total_count": 400
    }
  },
  "msg": "OK"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.materials[].id` | ID of the ad material. Pass it to other ad APIs that ask for a material ID. |
| `data.materials[].ad_title / data.materials[].brand_name` | Title text of the ad and the name of the brand that runs it. |
| `data.materials[].like` | Like count of the ad. |
| `data.materials[].ctr` | Click-through rate value of the ad, as a number such as `0.16`. |
| `data.materials[].cost` | Cost level value of the ad, returned as a small integer such as `2`. |
| `data.materials[].industry_key / data.materials[].objective_key` | Industry label code and campaign objective of the ad, for example `campaign_objective_traffic`. |
| `data.materials[].video_info.cover` | URL of the cover image of the ad video. |
| `data.materials[].video_info.duration / data.materials[].video_info.width / data.materials[].video_info.height` | Length of the video, and its frame width and height. |
| `data.materials[].video_info.video_url` | Video file URLs keyed by resolution, such as `720p`. Some ads list only one resolution. |
| `data.pagination.has_more / data.pagination.total_count` | Whether more pages exist, and the total number of matching ads. |

### Notes

- Page through results with `page` and `limit`. The response `data.pagination` shows the current `page` and `size`.
- Set `order_by` to `likes` to sort by like count, or `for_you` for recommended order.
- Pass several industry IDs in `industry` separated by commas.
- Use `id` from `data.materials[]` with [TikTok Ad Percentile Rankings](/apis/tiktok/ads/ad-percentile) or [TikTok Ad Keyframe Analysis](/apis/tiktok/ads/ad-keyframe-analysis) for deeper analysis of one ad.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Ad Interactive Analysis](/apis/tiktok/ads/ad-interactive-analysis): Returns audience retention and interaction analytics across video timestamps for a specified ad creative.
- [TikTok Ad Keyframe Analysis](/apis/tiktok/ads/ad-keyframe-analysis): Returns keyframe performance metrics across video ad timestamps for a specified material ID, including retention and conversion figures.
- [TikTok Ad Material Percentile Rankings](/apis/tiktok/ads/ad-percentile): Returns ad performance percentile rankings within the industry for a specific ad material.

---
Machine-readable: [`catalog/models/tiktok/ads/search-ads.json`](../../../../catalog/models/tiktok/ads/search-ads.json) · Store page: https://www.sandbase.ai/model/tiktok/ads/search-ads
