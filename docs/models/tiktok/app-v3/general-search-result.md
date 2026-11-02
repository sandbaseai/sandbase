# TikTok Search API: pricing, parameters and code examples

`tiktok/app-v3/general-search-result` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Search TikTok by keyword across videos and users (Top tab). Returns videos with descriptions, authors and play, like, comment and share counts, with sort and publish-time filters.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/general-search-result", "count": 20, "keyword": "faith sweatshirt", "publish_time": 1}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/general-search-result', {'count': 20, 'keyword': 'faith sweatshirt', 'publish_time': 1})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/general-search-result", {
  "count": 20,
  "keyword": "faith sweatshirt",
  "publish_time": 1
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/general-search-result", sandbase.Params{
	"count": 20,
	"keyword": "faith sweatshirt",
	"publish_time": 1,
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/general-search-result` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number default `20` |
| `offset` | integer |  | Offset default `0` |
| `keyword` | string | yes | Keyword  |
| `sort_type` | integer |  | 0-Relatedness, 1-Most likes default `0` |
| `publish_time` | integer |  | 0-Unlimited, 1-Last day, 7-Last week, 30-Last month, 90-Last three months, 180-Last half year default `0` |

## Details

Search TikTok's Top results for a keyword. Results include videos with statistics and matching user cards. Sort by relevance or likes and filter by publish date.

### Use cases

- Discover trending TikTok content for a keyword.
- Find creators for influencer campaigns.
- Monitor brand or product mentions on TikTok.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/general-search-result" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "openai", "count": 5}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Keyword |
| `count` | integer | No | Number |
| `offset` | integer | No | Offset |
| `sort_type` | integer | No | 0-Relatedness, 1-Most likes |
| `publish_time` | integer | No | 0-Unlimited, 1-Last day, 7-Last week, 30-Last month, 90-Last three months, 180-Last half year |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "has_more": 1,
  "cursor": 5,
  "data": [
    {
      "type": 1,
      "aweme_info": {
        "aweme_id": "7692955431185992991",
        "create_time": 1791155775,
        "desc": "OpenAI Codex is getting an upgrade or a full rese…",
        "author": {
          "nickname": "<user>",
          "sec_uid": "<sec_uid>"
        },
        "statistics": {
          "play_count": 54972,
          "digg_count": 1735,
          "comment_count": 148,
          "share_count": 496,
          "collect_count": 312
        }
      }
    }
  ]
}
```

### Notes

- `sort_type`: 0 relevance, 1 most likes. `publish_time`: 0, 1, 7, 30, 90 or 180 days.
- Paginate with `offset`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok LIVE Status](/model/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Creator Search Insights](/model/tiktok/app-v3/creator-search-insights): Get TikTok Creator Search Insights: trending search queries with popularity scores, trend history and video counts, including content-gap topics, by category a…
- [TikTok Creator Search Insights Detail](/model/tiktok/app-v3/creator-search-insights-detail): Get detailed statistics for a TikTok Creator Search Insights query: popularity over time and audience breakdown by age, gender and country.

---
Machine-readable: [`catalog/models/tiktok/app-v3/general-search-result.json`](../../../../catalog/models/tiktok/app-v3/general-search-result.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/general-search-result
