# TikTok Trending Hashtags

`tiktok/ads/trends-hashtag-list` · api · TikTok

Get trending TikTok hashtags from TikTok Creative Center by country and industry: rank, posts, views and popularity curve over 7, 30 or 90 days.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/ads/trends-hashtag-list", "country_code": "DE", "industry_id": 13000000000, "limit": 30, "page": 1, "time_range": 30}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/ads/trends-hashtag-list', {'country_code': 'DE', 'industry_id': 13000000000, 'limit': 30, 'page': 1, 'time_range': 30})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/ads/trends-hashtag-list", {
  "country_code": "DE",
  "industry_id": 13000000000,
  "limit": 30,
  "page": 1,
  "time_range": 30
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/ads/trends-hashtag-list", sandbase.Params{
	"country_code": "DE",
	"industry_id": 13000000000,
	"limit": 30,
	"page": 1,
	"time_range": 30,
})
```

Same call via the path form: `POST /v1/api/tiktok/ads/trends-hashtag-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number, default 1  |
| `limit` | integer |  | Items per page, default 20  |
| `time_range` | integer |  | Time range in days, one of 7 / 30 / 90, default 7  |
| `industry_id` | integer |  | First-level industry ID (optional), filters hashtags by industry; omit for all industries. Options: 10000000000: Education; 11000000000: Vehicle & Transportation; 12000000000: Baby, Kids & Maternity; 13000000000:…  |
| `country_code` | string |  | Country code, default US (see /get_location_list for options)  |

## Details

Fetch the trending hashtag ranking from TikTok Creative Center for a country, optionally filtered by industry.

### Use cases

- Find trending hashtags for content and ads.
- Compare trends across markets.
- Track hashtag momentum over time.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/ads/trends-hashtag-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"country_code": "US", "limit": 5}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `page` | integer | No | Page number, default 1 |
| `limit` | integer | No | Items per page, default 20 |
| `time_range` | integer | No | Time range in days, one of 7 / 30 / 90, default 7 |
| `industry_id` | integer | No | First-level industry ID (optional), filters hashtags by industry; omit for all industries. |
| `country_code` | string | No | Country code, default US (see /get_location_list for options) |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "items": [
    {
      "hashtagID": "7173295778981478443",
      "hashtagName": "cornell7",
      "rankIndex": 2,
      "publishCnt": 44984,
      "vv": 352158608,
      "popularityCurve": [
        {
          "timestamp": "1790553600",
          "value": 0
        },
        {
          "timestamp": "1790640000",
          "value": 62.32516872920672
        }
      ]
    }
  ],
  "pagination": {
    "hasMore": false,
    "limit": 3,
    "page": 1,
    "totalCount": 3
  }
}
```

### Notes

- `time_range`: 7, 30 or 90 days.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Get ad interactive analysis](/model/tiktok/ads/ad-interactive-analysis): Get ad interactive time analysis to understand audience retention and engagement at different video time points Analyze ad video attractiveness curve to find o…
- [Get ad keyframe analysis](/model/tiktok/ads/ad-keyframe-analysis): Get keyframe analysis of ad videos to understand audience retention at different time points Analyze which time points attract viewers most and where viewers d…
- [Get ad percentile data](/model/tiktok/ads/ad-percentile): Get ad percentile ranking data within the industry Understand ad performance levels relative to peers across various metrics Help evaluate ad effectiveness and…

---
Machine-readable: [`catalog/models/tiktok/ads/trends-hashtag-list.json`](../../../../catalog/models/tiktok/ads/trends-hashtag-list.json) · Store page: https://www.sandbase.ai/model/tiktok/ads/trends-hashtag-list
