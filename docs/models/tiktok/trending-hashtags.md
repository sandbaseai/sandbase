# TikTok Trending Hashtags API: pricing, parameters and code examples

`tiktok/trending-hashtags` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

Rank TikTok's trending hashtags for one country and industry, with each hashtag's daily popularity curve, post count, video views, and leading creators. Ranks 15 industry categories, or omit industry for the all-industries board. TikTok publishes only the top 3 hashtags per board to anonymous callers, so limit 1-3 is served cheaply; a limit above 3 routes to a dearer authenticated source that returns the full ranking. Covers 27 markets: AE, AR, AU, BR, CA, CO, DE, EG, ES, FR, GB, ID, IL, IT, JP, KR, MX, MY, PH, SA, SG, TH, TR, TW, US, VN, ZA.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/trending-hashtags"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/trending-hashtags', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/trending-hashtags", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/trending-hashtags", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok/trending-hashtags` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of ranked hashtags to return, from 1 through 100 (default 3). TikTok publishes only the top 3 hashtags per board to anonymous callers, so 1 through 3 is served by the cheapest source; a higher limit… default `3`; range 1–100 |
| `period` | integer |  | Lookback window in days that the ranking and the popularity curve cover (default 7). one of: `7`, `30`, `90`; default `7` |
| `region` | string |  | Two-letter country code of the market whose hashtag ranking to read (default US). Each market is ranked independently, so US and DE return different boards. one of: `US`, `FR`, `DE`, `IT`, `ES`, `GB`, `AR`, `AU`, `BR`, `CA`, `CO`, `EG` …; default `"US"` |
| `industry` | string |  | Restrict the ranking to one industry. Omit for the all-industries board. one of: `apparel_accessories`, `baby_kids_maternity`, `beauty_personal_care`, `education`, `food_beverage`, `games`, `health`, `home_improvement`, `household_products`, `news_entertainment`, `pets`, `sports_outdoor` … |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `industryIds`, and it is served only by a source that returns every…  |

## Details

Returns TikTok's ranked trending hashtags for one country, with each hashtag's daily popularity curve, post count, video views, and top creators. It needs no required input. You can set `region`, `industry`, `period`, and `limit`.

### Use cases

- Spot which hashtags are rising in the US or another market before planning a TikTok campaign.
- Compare the hashtag board for one industry, such as `games` or `beauty_personal_care`, against the all-industries board.
- Find creators who lead a trending hashtag and add them to an outreach list.
- Track a hashtag's popularity curve over 7, 30, or 90 days to judge whether it is peaking or fading.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/trending-hashtags" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": 3, "period": 7, "region": "US"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `industry` | string | No | Restrict the ranking to one industry. Omit for the all-industries board. |
| `limit` | integer | No | Maximum number of ranked hashtags to return, from 1 through 100 (default 3). TikTok publishes only the top 3 hashtags per board to anonymous callers, so 1 through 3 is served by the cheapest source; a higher limit routes |
| `period` | integer | No | Lookback window in days that the ranking and the popularity curve cover (default 7). |
| `region` | string | No | Two-letter country code of the market whose hashtag ranking to read (default US). Each market is ranked independently, so US and DE return different boards. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `industryIds`, and it is served only by a source that returns every on |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "items": [
      {
        "hashtag": "tiktokscaryhorrorcontest",
        "hashtagId": "7691443554018656263",
        "industryIds": [],
        "popularity": [
          {
            "atUtc": 1791504000,
            "value": 0
          }
        ],
        "posts": 73462,
        "rank": 1,
        "topCreators": [
          {
            "countryCode": "US",
            "followers": 118558,
            "handle": "sadwds213s",
            "image": "https://p16-common-sign.tiktokcdn.com/tos-maliva-avt-0068/8ef1054a783a3d7a1123e5…",
            "nickname": "sadwd",
            "rank": 1,
            "userId": "7395829863795999787"
          }
        ],
        "views": 312182870
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.items[].rank` | Position of the hashtag on the board, starting at 1. |
| `data.items[].hashtag / data.items[].hashtagId` | The hashtag text without the `#` sign, and its numeric ID as a string. |
| `data.items[].posts / data.items[].views` | Number of posts and total video views for the hashtag. |
| `data.items[].popularity[].atUtc` | Timestamp of the data point, in Unix seconds (UTC). |
| `data.items[].popularity[].value` | Popularity score for that point. The values in the sample run from 0 to 100. |
| `data.items[].industryIds` | List of numeric industry IDs for the hashtag. It can be empty, as on the first item. |
| `data.items[].topCreators[].handle / data.items[].topCreators[].nickname` | The creator's TikTok handle and display name. |
| `data.items[].topCreators[].followers` | Follower count of the creator. |
| `data.items[].topCreators[].userId / data.items[].topCreators[].countryCode` | The creator's numeric user ID as a string, and a two-letter country code. |
| `found` | `true` when the ranking returned results. |

### Notes

- Use `limit` of 1 to 3 for the cheapest source. A `limit` above 3, up to 100, returns the full ranking.
- `period` accepts `7`, `30`, or `90` days. `region` takes a two-letter code such as `US` or `DE`.
- Omit `industry` for the all-industries board. Add `requireFields` with `industryIds` if you need industry IDs on every hashtag that has them.
- For more detail on a single hashtag, call [TikTok Hashtag Detail](/apis/tiktok/app-v3/hashtag-detail) or [TikTok Hashtag Video List](/apis/tiktok/app-v3/hashtag-video-list) with the `hashtagId`.

### Pricing

Billed at the actual cost of each call, about $0.0012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/tiktok/trending-hashtags.json`](../../../catalog/models/tiktok/trending-hashtags.json) · Store page: https://www.sandbase.ai/model/tiktok/trending-hashtags
