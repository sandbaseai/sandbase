# TikTok Creator Search Insights API: pricing, parameters and code examples

`tiktok/app-v3/creator-search-insights` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get TikTok Creator Search Insights: trending search queries with popularity scores, trend history and video counts, including content-gap topics, by category and language.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/creator-search-insights", "language_filters": "en", "limit": 10, "offset": 0, "tab": "all"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/creator-search-insights', {'language_filters': 'en', 'limit': 10, 'offset': 0, 'tab': 'all'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/creator-search-insights", {
  "language_filters": "en",
  "limit": 10,
  "offset": 0,
  "tab": "all"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/creator-search-insights", sandbase.Params{
	"language_filters": "en",
	"limit": 10,
	"offset": 0,
	"tab": "all",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/creator-search-insights` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `tab` | string |  | Tab type (all/content_gap/follower_searched/life_style/topics/challenges/sounds/hashtags) default `"all"` |
| `limit` | integer |  | Number per page, default 20 default `20` |
| `offset` | integer |  | Pagination offset, default 0 default `0` |
| `force_refresh` | boolean |  | Force refresh, default False default `false` |
| `creator_source` | string |  | Creator source, default "general_search" default `"general_search"` |
| `category_filters` | string |  | Category filters, separated by comma, options: Gaming, Fashion, Tourism, Science, Food, Sports default `""` |
| `language_filters` | string |  | Language filters, separated by comma, options: id, de, en, es, fr, pt, vi, tr, ar, th, ja, ko default `"en"` |

## Details

Fetch the search topics TikTok shows creators in Creator Search Insights. Each query includes a popularity score, a recent trend series and how many videos already cover it.

### Use cases

- Find trending search topics to create content for.
- Spot content gaps with high demand and few videos (`tab=content_gap`).
- Track topic popularity by category and language.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/creator-search-insights" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `tab` | string | No | Tab type (all/content_gap/follower_searched/life_style/topics/challenges/sounds/hashtags) |
| `limit` | integer | No | Number per page, default 20 |
| `offset` | integer | No | Pagination offset, default 0 |
| `force_refresh` | boolean | No | Force refresh, default False |
| `creator_source` | string | No | Creator source, default "general_search" |
| `category_filters` | string | No | Category filters, separated by comma, options: Gaming, Fashion, Tourism, Science, Food, Sports |
| `language_filters` | string | No | Language filters, separated by comma, options: id, de, en, es, fr, pt, vi, tr, ar, th, ja, ko |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "has_more": true,
  "cursor": 20,
  "inspiration_list": [
    {
      "query_text": "new account on tiktok",
      "query_id_str": "7449584484497752069",
      "popularity": 72,
      "popularity_v2": 202860,
      "video_num": 123206,
      "trending_seq": [
        80,
        80,
        79,
        75,
        74,
        80,
        72
      ],
      "inspiration_types": [
        "search"
      ]
    }
  ]
}
```

### Notes

- `tab`: all, content_gap, follower_searched, life_style, topics, challenges, sounds or hashtags.
- Filter with `category_filters` (e.g. Gaming, Fashion) and `language_filters` (e.g. en, es).

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok LIVE Status](/apis/tiktok/app-v3/check-live-room-online): Check if live room is online The Room ID of the live room can be obtained from the `/api/v1/tiktok/web/get_live_room_id` interface through the live room link.
- [Batch check if live rooms are online](/apis/tiktok/app-v3/check-live-room-online-batch): Batch check TikTok live rooms' online status, supports up to 50 room IDs Room IDs can be retrieved from `/api/v1/tiktok/web/get_live_room_id`.
- [Get content translation data](/apis/tiktok/app-v3/content-translate): Get content translation data.

---
Machine-readable: [`catalog/models/tiktok/app-v3/creator-search-insights.json`](../../../../catalog/models/tiktok/app-v3/creator-search-insights.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/creator-search-insights
