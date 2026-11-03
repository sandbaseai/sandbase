# Bilibili App Search All API: pricing, parameters and code examples

`bilibili/app/search-all` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns comprehensive search results across Bilibili content via the mobile app interface. Filters results by search keyword, sorting order, and pagination parameters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/app/search-all", "cursor": "", "keyword": "OpenAI", "order": 0, "page_size": 20}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/app/search-all', {'cursor': '', 'keyword': 'OpenAI', 'order': 0, 'page_size': 20})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/app/search-all", {
  "cursor": "",
  "keyword": "OpenAI",
  "order": 0,
  "page_size": 20
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/app/search-all", sandbase.Params{
	"cursor": "",
	"keyword": "OpenAI",
	"order": 0,
	"page_size": 20,
})
```

Same call via the path form: `POST /v1/api/bilibili/app/search-all` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `order` | integer |  | Sort order (0=comprehensive) default `0` |
| `cursor` | string |  | Pagination cursor. Leave empty for the first page; for the next page pass default `""` |
| `keyword` | string | yes | Search keyword (required)  |
| `page_size` | integer |  | Results per page default `20` |

## Details

Search Bilibili by keyword across all result types at once, the same mixed list the Bilibili app shows: videos, users, live rooms, bangumi and topics, with cursor paging.

### Use cases

- Get a quick overview of what Bilibili has for a keyword.
- Collect top videos for a topic with their play counts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/app/search-all" \
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
| `order` | integer | No | Sort order (0=comprehensive) |
| `page_size` | integer | No | Results per page |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "annotation": {
      "qv_id": "e9f7f7fb7ae849f1b103a7f2a59ebbdc"
    },
    "item": [
      {
        "av": {
          "author": "深圳卫视科创最前沿",
          "cover": "https://i0.hdslb.com/bfs/archive/0c5051baa569f3e2c742b4f6a6ad5a8b18bfc0f7.jpg",
          "danmaku": 1,
          "duration": "1:30",
          "face": "https://i0.hdslb.com/bfs/face/aaaa766a2817d5946a8f64ba53bc72651d7b6b36.jpg",
          "mid": "1173642672",
          "play": 10891,
          "ptime": "1793191441"
        },
        "goto": "av",
        "linktype": "video",
        "param": "117518576392229",
        "position": 1,
        "trackid": "9528089372420496240",
        "uri": "bilibili://video/117518576392229?cid=43128062303&history_progress=0&player_heigh…",
        "user_act": "{\"id\":117518576392229,\"type\":\"video\"}"
      }
    ],
    "keyword": "OpenAI",
    "nav": [
      {
        "pages": 7
      }
    ],
    "page": "1",
    "pagination": {
      "next": "CAISIGU5ZjdmN2ZiN2FlODQ5ZjFiMTAzYTdmMmE1OWViYmRj"
    },
    "trackid": "9528089372420496240"
  },
  "message": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.item[]` | Mixed results; `linktype` tells the type (`video`, `bili_user`, `live` ...). Video rows carry `av.author`, `av.play`, `av.danmaku`, `av.duration`, `av.ptime`. |
| `data.nav[].pages` | Pages available. |
| `data.pagination.next` | Cursor for the next page; pass it as `cursor`. |

### Notes

- To search one type only, with type-specific sorting, use [Bilibili Search by Type](/apis/bilibili/app/search-by-type).

### Pricing

$0.001 per successful call. Failed calls, including lookups whose target does not exist, are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Bilibili App Bangumi Tab](/apis/bilibili/app/bangumi-tab): Returns Bilibili app bangumi tab data, providing curated anime recommendations, feed items, and category listings for mobile clients.
- [Bilibili App Cinema Tab](/apis/bilibili/app/cinema-tab): Returns cinema tab content from the Bilibili app, featuring curated movies, TV shows, and entertainment recommendations without requiring additional query para…
- [Bilibili App Home Feed](/apis/bilibili/app/home-feed): Returns recommended video items from the Bilibili app home feed.

---
Machine-readable: [`catalog/models/bilibili/app/search-all.json`](../../../../catalog/models/bilibili/app/search-all.json) · Store page: https://www.sandbase.ai/model/bilibili/app/search-all
