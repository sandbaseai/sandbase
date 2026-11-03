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

Search Xiaohongshu (RedNote) notes by keyword, with sorting, note type and time filters. Each note comes with title, text, author, likes, saves, comments and shares, and the `xsec_token` needed to open it.

### Use cases

- Research what users say about a product or brand on Xiaohongshu.
- Find popular notes for a keyword sorted by likes or recency.
- Collect note IDs for detail and comment APIs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/app-v2/search-notes" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "OpenAI"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword |
| `ai_mode` | integer | No | AI mode, 0=off, 1=on |
| `note_type` | string | No | Note type filter |
| `page` | integer | No | Page number, start from 1 |
| `search_id` | string | No | Search ID, pass value from first search response for pagination |
| `search_session_id` | string | No | Search session ID, pass value from first search response for pagination |
| `sort_type` | string | No | Sort type |
| `source` | string | No | Source, default "explore_feed" |
| `time_filter` | string | No | Time filter |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "items": [
      {
        "model_type": "note",
        "note": {
          "id": "68417e340000000012005009",
          "title": "在OpenAI工作一年是什么体验？",
          "desc": "今天是Kay在@openai一周年纪念日。就像所有美好的事物一样，感觉就像一辈子那么长，又像只有一周那么长。 在过去的一",
          "type": "normal",
          "liked_count": 1710,
          "collected_count": 436,
          "comments_count": 45,
          "shared_count": 63,
          "timestamp": 1749122612,
          "xsec_token": "YBInGnHNhG3Mpg74EPpAit_uooczsdD7_5qKSMlc2sqWE=",
          "user": {
            "nickname": "科技漫步者",
            "userid": "60c73fb9000000000101fef2"
          }
        }
      }
    ]
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.items[].note.id` | Note ID. |
| `data.items[].note.title / desc` | Title and text. |
| `data.items[].note.type` | `normal` (image) or `video`. |
| `data.items[].note.liked_count / collected_count / comments_count / shared_count` | Engagement counts. |
| `data.items[].note.user` | Author nickname and `userid`. |
| `data.items[].note.xsec_token` | Token required by the note detail and comment APIs. |

### Notes

- Pages start at 1. Pass the `search_id` from the first response when you request page 2 and later.
- `sort_type` and `time_filter` follow the app's options.

### Pricing

$0.01 per successful call. Failed calls, including lookups whose target does not exist, are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Get creator hot inspiration feed](/apis/xiaohongshu/app-v2/creator-hot-inspiration-feed): Get creator center hot inspiration feed, using cursor pagination.
- [Get creator inspiration feed](/apis/xiaohongshu/app-v2/creator-inspiration-feed): Get creator center recommended inspiration feed, using cursor pagination.
- [Get image note detail](/apis/xiaohongshu/app-v2/image-note-detail): App V2 Image Note Detail provides a focused capability for applications, automation, and data workflows.

---
Machine-readable: [`catalog/models/xiaohongshu/app-v2/search-notes.json`](../../../../catalog/models/xiaohongshu/app-v2/search-notes.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/app-v2/search-notes
