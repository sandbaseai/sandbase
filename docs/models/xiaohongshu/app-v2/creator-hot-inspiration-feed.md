# Xiaohongshu (RED) Creator Hot Inspiration Feed API: pricing, parameters and code examples

`xiaohongshu/app-v2/creator-hot-inspiration-feed` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Retrieves creator center hot inspiration feed items with topic titles, popularity scores, and deeplinks. Supports pagination using a cursor parameter.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/app-v2/creator-hot-inspiration-feed", "cursor": "股票"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/app-v2/creator-hot-inspiration-feed', {'cursor': '股票'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/app-v2/creator-hot-inspiration-feed", {
  "cursor": "股票"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/app-v2/creator-hot-inspiration-feed", sandbase.Params{
	"cursor": "股票",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/app-v2/creator-hot-inspiration-feed` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Pagination cursor, leave empty for first request, pass cursor value from previous response (e.g. "1", "2"...) default `""` |

## Details

Query the trending inspiration feed from the Xiaohongshu creator center using `cursor` for pagination.

### Use cases

- Track trending topic inspirations for content planning.
- Analyze popularity scores of featured platform topics.
- Extract inspiration topic IDs and direct deeplinks.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/app-v2/creator-hot-inspiration-feed" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | string | No | Pagination cursor, leave empty for first request, pass cursor value from previous response (e.g. "1", "2"...) |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "items": [
      {
        "deeplink": "xhsdiscover://post_new_note?attach=%7B%22note_text_v2%22%3A%7B%22content%22%3A%22%20%23%E…",
        "hot_id": "3634568",
        "id": 57942239,
        "score": 23993042,
        "score_text": "2399.3万人在看",
        "title": "揭秘海狗繁殖期生存法则",
        "type": "Hot"
      }
    ]
  }
}
```

### Notes

- Leave `cursor` empty for the initial request, then pass the cursor value from subsequent responses for pagination.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Xiaohongshu (RED) Inspiration Feed](/apis/xiaohongshu/app-v2/creator-inspiration-feed): Returns recommended inspiration feed items and trending topics from Xiaohongshu (RED).
- [Xiaohongshu (RED) Image Note Details](/apis/xiaohongshu/app-v2/image-note-detail): Returns detailed information for a Xiaohongshu image note.
- [Xiaohongshu (RED) Note Comments](/apis/xiaohongshu/app-v2/note-comments): Get the comments on a Xiaohongshu note: comment text, time, likes, reply counts and location, with sorting and cursor pagination.

---
Machine-readable: [`catalog/models/xiaohongshu/app-v2/creator-hot-inspiration-feed.json`](../../../../catalog/models/xiaohongshu/app-v2/creator-hot-inspiration-feed.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/app-v2/creator-hot-inspiration-feed
