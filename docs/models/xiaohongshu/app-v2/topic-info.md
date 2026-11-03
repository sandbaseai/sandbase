# Xiaohongshu (RED) Topic Details API: pricing, parameters and code examples

`xiaohongshu/app-v2/topic-info` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns topic page details such as topic name, view count, discussion count, and share info by topic page ID. Supports passing optional context like source note ID.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/app-v2/topic-info", "note_id": "", "page_id": "5c1cc866febed9000184b7c1", "source": "normal"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/app-v2/topic-info', {'note_id': '', 'page_id': '5c1cc866febed9000184b7c1', 'source': 'normal'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/app-v2/topic-info", {
  "note_id": "",
  "page_id": "5c1cc866febed9000184b7c1",
  "source": "normal"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/app-v2/topic-info", sandbase.Params{
	"note_id": "",
	"page_id": "5c1cc866febed9000184b7c1",
	"source": "normal",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/app-v2/topic-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `source` | string |  | Source, default "normal" default `"normal"` |
| `note_id` | string |  | Source note ID, pass when jumping from note to topic (optional) default `""` |
| `page_id` | string | yes | Topic page ID (required), e.g. "5c1cc866febed9000184b7c1"  |

## Details

Retrieve topic overview metadata by specifying a required `page_id`. You can also supply an optional `note_id` and `source` context.

### Use cases

- Inspect engagement metrics such as view and discussion counts for a topic.
- Extract topic names and share configurations for content tracking.
- Track topic metadata when navigating from a specific source note.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/app-v2/topic-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"page_id": "5c1cc866febed9000184b7c1"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `page_id` | string | Yes | Topic page ID (required), e.g. "5c1cc866febed9000184b7c1" |
| `source` | string | No | Source, default "normal" |
| `note_id` | string | No | Source note ID, pass when jumping from note to topic (optional) |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "post_option": {
      "func_items": [
        {
          "link": "xhsdiscover://post_new_note?source=%7B%22type%22%3A%22pages%22%2C%22ids%22%3A%225c1cc866f…",
          "title": "Choose from Album"
        }
      ]
    }
  }
}
```

### Notes

- `page_id` is required to identify the topic page.
- `note_id` can be supplied when navigating from a note to the topic.
- `source` defaults to "normal" if not specified.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Xiaohongshu (RED) Creator Hot Inspiration Feed](/apis/xiaohongshu/app-v2/creator-hot-inspiration-feed): Retrieves creator center hot inspiration feed items with topic titles, popularity scores, and deeplinks.
- [Xiaohongshu (RED) Inspiration Feed](/apis/xiaohongshu/app-v2/creator-inspiration-feed): Returns recommended inspiration feed items and trending topics from Xiaohongshu (RED).
- [Xiaohongshu (RED) Image Note Details](/apis/xiaohongshu/app-v2/image-note-detail): Returns detailed information for a Xiaohongshu image note.

---
Machine-readable: [`catalog/models/xiaohongshu/app-v2/topic-info.json`](../../../../catalog/models/xiaohongshu/app-v2/topic-info.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/app-v2/topic-info
