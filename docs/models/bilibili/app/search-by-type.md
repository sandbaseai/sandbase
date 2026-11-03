# Bilibili Search by Type API: pricing, parameters and code examples

`bilibili/app/search-by-type` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns categorized search results from Bilibili based on a target query string. Supports filtering by search type, adjusting sort order, and cursor-based pagination.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/app/search-by-type", "cursor": "", "keyword": "OpenAI", "order": 0, "page_size": 20, "search_type": "video"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/app/search-by-type', {'cursor': '', 'keyword': 'OpenAI', 'order': 0, 'page_size': 20, 'search_type': 'video'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/app/search-by-type", {
  "cursor": "",
  "keyword": "OpenAI",
  "order": 0,
  "page_size": 20,
  "search_type": "video"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/app/search-by-type", sandbase.Params{
	"cursor": "",
	"keyword": "OpenAI",
	"order": 0,
	"page_size": 20,
	"search_type": "video",
})
```

Same call via the path form: `POST /v1/api/bilibili/app/search-by-type` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `order` | integer |  | Sort order default `0` |
| `cursor` | string |  | Pagination cursor. Leave empty for the first page; for the next page pass default `""` |
| `keyword` | string | yes | Search keyword (required)  |
| `page_size` | integer |  | Results per page default `20` |
| `search_type` | string |  | Search type default `"video"` |

## Details

Search Bilibili by keyword within one result type (videos, users, live rooms, articles and more), with sorting and cursor paging. Video results include title, author, play count, danmaku count, duration and publish time.

### Use cases

- Find videos about a topic sorted by plays or recency.
- Search Bilibili users (UP主) by name.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/app/search-by-type" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "OpenAI"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword (required) |
| `cursor` | string | No | Pagination cursor. Leave empty for the first page; for the next page pass |
| `order` | integer | No | Sort order |
| `page_size` | integer | No | Results per page |
| `search_type` | string | No | Search type |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "annotation": {
      "qv_id": "bdbca9b09c444039b387fa922af350e0"
    },
    "exp_str": "100010#5502#6609#81701100#9902#9921#9931#9947#9961",
    "items": [
      {
        "av": {
          "author": "布衣愚者",
          "cover": "https://i0.hdslb.com/bfs/archive/41108b0b9bac8eace885911b7f25dcacc9ecf1b7.jpg",
          "danmaku": 979,
          "duration": "18:38",
          "face": "https://i1.hdslb.com/bfs/face/ab22aa8fcbb6e7c442273cc9c492d8d4826c9c19.jpg",
          "mid": "362809",
          "play": 229119,
          "ptime": "1793494190"
        },
        "goto": "av",
        "param": "117538423901588",
        "uri": "bilibili://video/117538423901588?cid=43222761497&history_progress=0&player_heigh…",
        "user_act": "{\"id\":117538423901588,\"type\":\"video\"}"
      }
    ],
    "keyword": "OpenAI",
    "page": "1",
    "pages": 50,
    "pagination": {
      "next": "CAISIGJkYmNhOWIwOWM0NDQwMzliMzg3ZmE5MjJhZjM1MGUw"
    },
    "real_exposure_ratio": 0.8,
    "result_is_recommend": 1000,
    "trackid": "9348513686332904803"
  },
  "message": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.items[]` | Results. For videos: `av.author`, `av.play`, `av.danmaku` (bullet comments), `av.duration`, `av.ptime` (Unix seconds) and `param` (the aid). |
| `data.pages` | Total pages available. |
| `data.pagination.next` | Cursor for the next page; pass it as `cursor`. |

### Notes

- Use `search_type` to pick the result type and `order` to sort. For a mixed result list use [Bilibili Search All](/apis/bilibili/app/search-all).

### Pricing

$0.001 per successful call. Failed calls, including lookups whose target does not exist, are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Bilibili App Bangumi Tab](/apis/bilibili/app/bangumi-tab): Returns Bilibili app bangumi tab data, providing curated anime recommendations, feed items, and category listings for mobile clients.
- [Bilibili App Cinema Tab](/apis/bilibili/app/cinema-tab): Returns cinema tab content from the Bilibili app, featuring curated movies, TV shows, and entertainment recommendations without requiring additional query para…
- [Bilibili App Home Feed](/apis/bilibili/app/home-feed): Returns recommended video items from the Bilibili app home feed.

---
Machine-readable: [`catalog/models/bilibili/app/search-by-type.json`](../../../../catalog/models/bilibili/app/search-by-type.json) · Store page: https://www.sandbase.ai/model/bilibili/app/search-by-type
