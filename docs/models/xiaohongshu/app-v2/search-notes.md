# Xiaohongshu (RED) Note Search API: pricing, parameters and code examples

`xiaohongshu/app-v2/search-notes` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Search Xiaohongshu (RED / Little Red Book) notes by keyword and get titles, authors, cover images and like, collect, comment and share counts, with sort, note-type and time filters.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/app-v2/search-notes", "ai_mode": 0, "keyword": "OpenAI", "note_type": "不限", "page": 1, "search_id": "", "search_session_id": "", "sort_type": "general", "source": "explore_feed", "time_filter": "不限"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/app-v2/search-notes', {'ai_mode': 0, 'keyword': 'OpenAI', 'note_type': '不限', 'page': 1, 'search_id': '', 'search_session_id': '', 'sort_type': 'general', 'source': 'explore_feed', 'time_filter': '不限'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/app-v2/search-notes", {
  "ai_mode": 0,
  "keyword": "OpenAI",
  "note_type": "不限",
  "page": 1,
  "search_id": "",
  "search_session_id": "",
  "sort_type": "general",
  "source": "explore_feed",
  "time_filter": "不限"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/app-v2/search-notes", sandbase.Params{
	"ai_mode": 0,
	"keyword": "OpenAI",
	"note_type": "不限",
	"page": 1,
	"search_id": "",
	"search_session_id": "",
	"sort_type": "general",
	"source": "explore_feed",
	"time_filter": "不限",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/app-v2/search-notes` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number, start from 1 default `1` |
| `source` | string |  | Source, default "explore_feed" default `"explore_feed"` |
| `ai_mode` | integer |  | AI mode, 0=off, 1=on default `0` |
| `keyword` | string | yes | Search keyword  |
| `note_type` | string |  | Note type filter default `"不限"` |
| `search_id` | string |  | Search ID, pass value from first search response for pagination default `""` |
| `sort_type` | string |  | Sort type default `"general"` |
| `time_filter` | string |  | Time filter default `"不限"` |
| `search_session_id` | string |  | Search session ID, pass value from first search response for pagination default `""` |

## Details

Search Xiaohongshu for a keyword and get matching notes with title, author, images and engagement counts. Sort by relevance, popularity or time and filter by note type.

### Use cases

- Research consumer opinions and trends on Xiaohongshu.
- Find KOLs and popular notes for a product category.
- Monitor brand mentions on RED.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/app-v2/search-notes" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "OpenAI"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword |
| `page` | integer | No | Page number, start from 1 |
| `source` | string | No | Source, default "explore_feed" |
| `ai_mode` | integer | No | AI mode, 0=off, 1=on |
| `note_type` | string | No | Note type filter |
| `search_id` | string | No | Search ID, pass value from first search response for pagination |
| `sort_type` | string | No | Sort type |
| `time_filter` | string | No | Time filter |
| `search_session_id` | string | No | Search session ID, pass value from first search response for pagination |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "code": 0,
  "page": 1,
  "next_page": 2,
  "search_id": "<search_id>",
  "data": {
    "items": [
      {
        "model_type": "note",
        "note": {
          "id": "6a6c688000000000060041d4",
          "type": "normal",
          "liked_count": 98,
          "collected_count": 78,
          "comments_count": 56,
          "shared_count": 25,
          "timestamp": 1785489536,
          "title": "我发现我真的很会面OpenAI的MLE（已上岸",
          "user": {
            "nickname": "<user>"
          }
        }
      }
    ]
  }
}
```

### Notes

- For the next page, pass `page`, plus `search_id` and `search_session_id` from the first response.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Get creator hot inspiration feed](/model/xiaohongshu/app-v2/creator-hot-inspiration-feed): Get creator center hot inspiration feed, using cursor pagination.
- [Get creator inspiration feed](/model/xiaohongshu/app-v2/creator-inspiration-feed): Get creator center recommended inspiration feed, using cursor pagination.
- [Get image note detail](/model/xiaohongshu/app-v2/image-note-detail): App V2 Image Note Detail provides a focused capability for applications, automation, and data workflows.

---
Machine-readable: [`catalog/models/xiaohongshu/app-v2/search-notes.json`](../../../../catalog/models/xiaohongshu/app-v2/search-notes.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/app-v2/search-notes
