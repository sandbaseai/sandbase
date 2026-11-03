# Xiaohongshu (RED) Image Search API: pricing, parameters and code examples

`xiaohongshu/app-v2/search-images` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns image notes and matching post metadata for a specified search keyword. Results include image URLs, engagement metrics, note identifiers, and author information.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/app-v2/search-images", "keyword": "OpenAI", "page": 1, "search_id": "", "search_session_id": "", "source": "explore_feed", "word_request_id": ""}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/app-v2/search-images', {'keyword': 'OpenAI', 'page': 1, 'search_id': '', 'search_session_id': '', 'source': 'explore_feed', 'word_request_id': ''})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/app-v2/search-images", {
  "keyword": "OpenAI",
  "page": 1,
  "search_id": "",
  "search_session_id": "",
  "source": "explore_feed",
  "word_request_id": ""
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/app-v2/search-images", sandbase.Params{
	"keyword": "OpenAI",
	"page": 1,
	"search_id": "",
	"search_session_id": "",
	"source": "explore_feed",
	"word_request_id": "",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/app-v2/search-images` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number, start from 1 default `1` |
| `source` | string |  | Source, default "explore_feed" default `"explore_feed"` |
| `keyword` | string | yes | Search keyword  |
| `search_id` | string |  | Search ID, pass value from first search response for pagination default `""` |
| `word_request_id` | string |  | Word request ID, pass value from first search response for pagination default `""` |
| `search_session_id` | string |  | Search session ID, pass value from first search response for pagination default `""` |

## Details

Search for image notes on Xiaohongshu (RED) by supplying a query in `keyword`. Supports pagination across result sets using `page`, `search_id`, `word_request_id`, and `search_session_id`.

### Use cases

- Discover image-based notes matching targeted topic keywords.
- Extract visual content URLs alongside post engagement statistics.
- Analyze trending community imagery and creator profiles.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/app-v2/search-images" \
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
| `search_id` | string | No | Search ID, pass value from first search response for pagination |
| `word_request_id` | string | No | Word request ID, pass value from first search response for pagination |
| `search_session_id` | string | No | Search session ID, pass value from first search response for pagination |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "items": [
      {
        "image_info": {
          "trace_id": "spectrum/1040g0k030ua64rtp56005o5h6s4080o1j0fbkl8",
          "url": "https://sns-na-i11.xhscdn.com/spectrum/1040g0k030ua64rtp56005o5h6s4080o1j0fbkl8?…"
        },
        "note_info": {
          "collected_count": 228,
          "comments_count": 49,
          "desc": "关键词[微笑R] lino cut of large crowd of people energetically moves towards a giant squere, ea…",
          "liked_count": 397,
          "model_type": "image_card",
          "note_id": "65b0a37a000000002c014b93"
        },
        "share_info": {
          "content": "关键词[微笑R] lino cut of large crowd of people energetically mov",
          "link": "https://www.xiaohongshu.com/discovery/item/65b0a37a000000002c014b93?app_platform…",
          "title": "Midjourney绘图 | 人潮汹涌"
        },
        "user_info": {
          "nickname": "<user>",
          "red_id": "9549661040",
          "red_official_verified": false,
          "red_official_verify_type": 0,
          "user_id": "<user>"
        }
      }
    ]
  }
}
```

### Notes

- Pagination starts at 1 using `page`.
- Pass `search_id`, `word_request_id`, and `search_session_id` from the initial search response to retrieve subsequent pages.
- The `source` parameter defaults to "explore_feed".

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Xiaohongshu (RED) Creator Hot Inspiration Feed](/apis/xiaohongshu/app-v2/creator-hot-inspiration-feed): Retrieves creator center hot inspiration feed items with topic titles, popularity scores, and deeplinks.
- [Xiaohongshu (RED) Inspiration Feed](/apis/xiaohongshu/app-v2/creator-inspiration-feed): Returns recommended inspiration feed items and trending topics from Xiaohongshu (RED).
- [Xiaohongshu (RED) Image Note Details](/apis/xiaohongshu/app-v2/image-note-detail): Returns detailed information for a Xiaohongshu image note.

---
Machine-readable: [`catalog/models/xiaohongshu/app-v2/search-images.json`](../../../../catalog/models/xiaohongshu/app-v2/search-images.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/app-v2/search-images
