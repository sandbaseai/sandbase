# Weibo Post Sub-Comments API: pricing, parameters and code examples

`weibo/web-v2/post-sub-comments` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns the list of sub-comments or replies for a specific Weibo comment. Supports pagination cursors and adjustable result counts per request.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/web-v2/post-sub-comments", "id": "5283574244704555"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/web-v2/post-sub-comments', {'id': '5283574244704555'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/web-v2/post-sub-comments", {
  "id": "5283574244704555"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/web-v2/post-sub-comments", sandbase.Params{
	"id": "5283574244704555",
})
```

Same call via the path form: `POST /v1/api/weibo/web-v2/post-sub-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string | yes | Main comment ID (required)  |
| `count` | integer |  | Number of sub-comments (default 10)  |
| `max_id` | string |  | Pagination cursor, pass empty for first request, use returned max_id for subsequent requests  |

## Details

Retrieve sub-comments and replies for a designated Weibo comment by passing its `id`.

### Use cases

- Display threaded reply discussions underneath main comments on Weibo.
- Extract nested user conversations for social sentiment analysis.
- Track ongoing audience responses to key discussion points.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/web-v2/post-sub-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"id": "7648703289"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string | Yes | Main comment ID (required) |
| `count` | integer | No | Number of sub-comments (default 10) |
| `max_id` | string | No | Pagination cursor, pass empty for first request, use returned max_id for subsequent requests |

### Notes

- Set `count` to control the number of sub-comments returned, which defaults to 10.
- Pass `max_id` empty on the initial call, then provide the returned `max_id` for cursor-based pagination.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Weibo Advanced Search](/model/weibo/web-v2/advanced-search): Search Weibo posts by keyword with filters for time range, post type (hot, original, verified, media) and content type (images, video, links).
- [Weibo AI Related Search Content](/model/weibo/web-v2/ai-related-search): Returns AI-generated content extensions for a keyword, including related questions, recommended bloggers, and reference posts.
- [Weibo AI Search](/model/weibo/web-v2/ai-search): Returns multimodal search results and relevance scores from Weibo intelligent search for a specified keyword or topic query.

---
Machine-readable: [`catalog/models/weibo/web-v2/post-sub-comments.json`](../../../../catalog/models/weibo/web-v2/post-sub-comments.json) · Store page: https://www.sandbase.ai/model/weibo/web-v2/post-sub-comments
