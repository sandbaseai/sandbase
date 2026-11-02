# Xiaohongshu (RED) Image Note Details API: pricing, parameters and code examples

`xiaohongshu/app-v2/image-note-detail` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.015 per call (free daily quota) · **Modes:** sync

Returns detailed information for a Xiaohongshu image note. Queries accept a specific note identifier or a post sharing link from the app or web interface.

## Pricing

- **$0.015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/app-v2/image-note-detail", "note_id": "6ab0d3640000000035013990"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/app-v2/image-note-detail', {'note_id': '6ab0d3640000000035013990'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/app-v2/image-note-detail", {
  "note_id": "6ab0d3640000000035013990"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/app-v2/image-note-detail", sandbase.Params{
	"note_id": "6ab0d3640000000035013990",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/app-v2/image-note-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `note_id` | string |  | Note ID, e.g. "697c0eee000000000a03c308" default `""` |
| `share_text` | string |  | Xiaohongshu sharing link (support APP and Web sharing link) default `""` |

## Details

Retrieve detailed metadata and content for a Xiaohongshu image post using `note_id` or `share_text`.

### Use cases

- Retrieve image note metadata using a post identifier.
- Parse Xiaohongshu post details directly from a shared link.
- Monitor image note content and engagement indicators.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/app-v2/image-note-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `note_id` | string | No | Note ID, e.g. "697c0eee000000000a03c308" |
| `share_text` | string | No | Xiaohongshu sharing link (support APP and Web sharing link) |

### Notes

- Supports input via `note_id` or via `share_text` containing an app or web sharing link.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Xiaohongshu (RED) Creator Hot Inspiration Feed](/model/xiaohongshu/app-v2/creator-hot-inspiration-feed): Retrieves creator center hot inspiration feed items with topic titles, popularity scores, and deeplinks.
- [Xiaohongshu (RED) Inspiration Feed](/model/xiaohongshu/app-v2/creator-inspiration-feed): Returns recommended inspiration feed items and trending topics from Xiaohongshu (RED).
- [Xiaohongshu (RED) Note Comments](/model/xiaohongshu/app-v2/note-comments): Get the comments on a Xiaohongshu note: comment text, time, likes, reply counts and location, with sorting and cursor pagination.

---
Machine-readable: [`catalog/models/xiaohongshu/app-v2/image-note-detail.json`](../../../../catalog/models/xiaohongshu/app-v2/image-note-detail.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/app-v2/image-note-detail
