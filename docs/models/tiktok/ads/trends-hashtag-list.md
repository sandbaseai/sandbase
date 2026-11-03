# TikTok Trending Hashtags API: pricing, parameters and code examples

`tiktok/ads/trends-hashtag-list` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get trending TikTok hashtags from TikTok Creative Center by country and industry: rank, posts, views and popularity curve over 7, 30 or 90 days.

## Pricing

- **$0.001 per call** (USD)
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

Returns a ranked list of trending TikTok hashtags from TikTok Creative Center for one country. Each item has post count, view count, a popularity curve and top creators. All inputs are optional, and `country_code` defaults to `US`.

### Use cases

- Pick hashtags for a new ad campaign in a given country and industry.
- Compare the top hashtags in different countries by passing different `country_code` values.
- Plot a hashtag's popularity curve to see whether it is rising or fading.
- Find creators who rank highest on a trending hashtag for outreach.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/ads/trends-hashtag-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"country_code": "US", "limit": 5}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `country_code` | string | No | Country code, default US (see /get_location_list for options) |
| `industry_id` | integer | No | First-level industry ID (optional), filters hashtags by industry; omit for all industries. Options: 10000000000: Education; 11000000000: Vehicle & Transportation; 12000000000: Baby, Kids & Maternity; 13000000000: Financi |
| `limit` | integer | No | Items per page, default 20 |
| `page` | integer | No | Page number, default 1 |
| `time_range` | integer | No | Time range in days, one of 7 / 30 / 90, default 7 |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "BaseResp": {
    "StatusCode": 0,
    "StatusMessage": ""
  },
  "items": [
    {
      "hashtagID": "7691443554018656263",
      "hashtagName": "tiktokscaryhorrorcontest",
      "industryIDs": [],
      "popularityCurve": [
        {
          "timestamp": "1791504000",
          "value": 0
        }
      ],
      "publishCnt": 73462,
      "rankIndex": 1,
      "topCreators": [
        {
          "aioCreatorID": "",
          "avatarURL": "https://p16-common-sign.tiktokcdn.com/tos-maliva-avt-0068/8ef1054a783a3d7a1123e5…",
          "countryCode": "US",
          "creatorRank": 1,
          "followedCnt": 118559,
          "handleName": "sadwds213s",
          "nickname": "sadwd",
          "ttUID": "7395829863795999787"
        }
      ],
      "vv": 312182870
    }
  ],
  "pagination": {
    "hasMore": true,
    "limit": 5,
    "page": 1,
    "totalCount": 100
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `items[].hashtagID / items[].hashtagName` | The hashtag's ID and its text, without the # sign. |
| `items[].rankIndex` | Position of the hashtag in the ranking. `1` is the top hashtag. |
| `items[].publishCnt` | Number of posts published with this hashtag. |
| `items[].vv` | View count for the hashtag. |
| `items[].industryIDs` | List of first-level industry IDs linked to the hashtag. It can be empty. |
| `items[].popularityCurve[].timestamp / items[].popularityCurve[].value` | One point on the popularity curve. `timestamp` is a Unix time in seconds as a string, and `value` is a score from 0 to 100. |
| `items[].topCreators[].handleName / items[].topCreators[].nickname` | Handle and display name of a top creator for the hashtag. |
| `items[].topCreators[].followedCnt` | Follower count of the creator. |
| `items[].topCreators[].creatorRank` | Rank of the creator within the hashtag's top creators. |
| `pagination.hasMore / pagination.totalCount` | Whether more pages exist, and the total number of hashtags in the result. |

### Notes

- Use `page` and `limit` to move through the list. The example request with `limit` set to `5` returned `totalCount` of `100` and `hasMore` as `true`.
- Set `time_range` to `7`, `30` or `90` days. The default is `7`.
- Set `industry_id` to a first-level industry ID such as `25000000000` (Games) to filter the list. Leave it out for all industries.
- Get valid `country_code` values from [TikTok Ads Location List](/apis/tiktok/ads/location-list).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Get ad interactive analysis](/apis/tiktok/ads/ad-interactive-analysis): Get ad interactive time analysis to understand audience retention and engagement at different video time points Analyze ad video attractiveness curve to find o…
- [Get ad keyframe analysis](/apis/tiktok/ads/ad-keyframe-analysis): Get keyframe analysis of ad videos to understand audience retention at different time points Analyze which time points attract viewers most and where viewers d…
- [Get ad percentile data](/apis/tiktok/ads/ad-percentile): Get ad percentile ranking data within the industry Understand ad performance levels relative to peers across various metrics Help evaluate ad effectiveness and…

---
Machine-readable: [`catalog/models/tiktok/ads/trends-hashtag-list.json`](../../../../catalog/models/tiktok/ads/trends-hashtag-list.json) · Store page: https://www.sandbase.ai/model/tiktok/ads/trends-hashtag-list
