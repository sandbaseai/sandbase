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

Returns a list of top spotlight TikTok ad cases with a creative highlight, like count, click-through rate, cost, and video file details. Needs no input. You can add an `industry` ID to narrow the list, and use `page` and `limit` to paginate.

### Use cases

- Pull the top-liked video ads in one industry to study which creative formats work.
- Read the `highlight` text on each ad to see why TikTok flags it as a good example.
- Download cover images and video links to build a swipe file of reference ads.
- Compare `ctr` and `like` across ads to benchmark your own creative.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/ads/top-ads-spotlight" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `industry` | string | No | Industry ID, optional, returns cross-industry list if omitted, e.g., Education: 25000000000 |
| `limit` | integer | No | Items per page, default 20 |
| `page` | integer | No | Page number, default 1 |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "materials": [
      {
        "cost": 2,
        "ctr": 0.22,
        "id": "7182310470102122497",
        "like": 33506,
        "video_info": {
          "cover": "https://p16-common-sign.tiktokcdn.com/v0201/d7f3c49928d44c02a8788be62fe9487b_167…",
          "duration": 43.542,
          "height": 1024,
          "vid": "v10033g50000cemat43c77u2ehil0a1g",
          "video_url": {
            "720p": "https://v16m-default.tiktokcdn.com/c4b2e149232f4d2105b7e0af7121727a/6ae9e541/vid…"
          },
          "width": 576
        }
      }
    ],
    "pagination": {
      "has_more": false,
      "page": 1,
      "size": 20,
      "total": 5
    }
  },
  "msg": "OK"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.materials[].id` | ID of the ad material. Use it to look up more detail on the same ad in other ad APIs. |
| `data.materials[].highlight` | Short text that explains what the ad does well. Some items do not include it. |
| `data.materials[].like` | Number of likes on the ad. |
| `data.materials[].ctr` | Click-through rate of the ad, shown as a number such as `0.22`. |
| `data.materials[].cost` | Cost value for the ad, shown as a small integer such as `2`. The response does not state a unit. |
| `data.materials[].video_info.cover` | URL of the cover image for the ad video. |
| `data.materials[].video_info.video_url` | Object that holds video file URLs. In this response it has one entry, keyed by resolution (`720p`). |
| `data.materials[].video_info.duration / data.materials[].video_info.width / data.materials[].video_info.height` | Length of the video, and its frame width and height. |
| `data.materials[].video_info.vid` | Video ID string for the ad video. |
| `data.pagination.has_more / data.pagination.page / data.pagination.size / data.pagination.total` | Pagination state. `has_more` tells you if another page exists, and `total` is the total item count. |

### Notes

- Pass an `industry` ID as a string, for example `25000000000` for Education. Leave it out to get a cross-industry list.
- `page` starts at 1 and `limit` defaults to 20. Check `data.pagination.has_more` before you request the next page.
- Cover and video URLs carry an `x-expires` parameter in the query string, so download the files soon after you call.
- Pass a material `id` to [TikTok Ad Material Percentile Rankings](/apis/tiktok/ads/ad-percentile) or [TikTok Ad Keyframe Analysis](/apis/tiktok/ads/ad-keyframe-analysis) for deeper metrics on one ad.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Ad Interactive Analysis](/apis/tiktok/ads/ad-interactive-analysis): Returns audience retention and interaction analytics across video timestamps for a specified ad creative.
- [TikTok Ad Keyframe Analysis](/apis/tiktok/ads/ad-keyframe-analysis): Returns keyframe performance metrics across video ad timestamps for a specified material ID, including retention and conversion figures.
- [TikTok Ad Material Percentile Rankings](/apis/tiktok/ads/ad-percentile): Returns ad performance percentile rankings within the industry for a specific ad material.

---
Machine-readable: [`catalog/models/tiktok/ads/top-ads-spotlight.json`](../../../../catalog/models/tiktok/ads/top-ads-spotlight.json) · Store page: https://www.sandbase.ai/model/tiktok/ads/top-ads-spotlight
