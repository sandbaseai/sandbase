# Weibo User Video List API: pricing, parameters and code examples

`weibo/web-v2/user-video-list` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Retrieves a waterfall list of videos posted by a specified user. Supports pagination via cursor parameters to browse historical video entries.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/web-v2/user-video-list", "uid": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/web-v2/user-video-list', {'uid': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/web-v2/user-video-list", {
  "uid": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/web-v2/user-video-list", sandbase.Params{
	"uid": "example",
})
```

Same call via the path form: `POST /v1/api/weibo/web-v2/user-video-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | User ID (required)  |
| `cursor` | string |  | Pagination cursor, pass "0" for first request, use returned next_cursor for subsequent requests  |

## Details

Retrieve video posts associated with a specific user profile by supplying their `uid`. You can also paginate through results using the `cursor` parameter.

### Use cases

- Browse video content posted by a specific Weibo account.
- Collect historical video post listings for creator profile analysis.
- Track multimedia posts and video feeds for target Weibo users.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/web-v2/user-video-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "8431518763"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | User ID (required) |
| `cursor` | string | No | Pagination cursor, pass "0" for first request, use returned next_cursor for subsequent requests |

### Notes

- Pass "0" to `cursor` for the initial request, then use the returned next_cursor value for following pages.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Weibo Advanced Search](/model/weibo/web-v2/advanced-search): Search Weibo posts by keyword with filters for time range, post type (hot, original, verified, media) and content type (images, video, links).
- [Weibo AI Related Search Content](/model/weibo/web-v2/ai-related-search): Returns AI-generated content extensions for a keyword, including related questions, recommended bloggers, and reference posts.
- [Weibo AI Search](/model/weibo/web-v2/ai-search): Returns multimodal search results and relevance scores from Weibo intelligent search for a specified keyword or topic query.

---
Machine-readable: [`catalog/models/weibo/web-v2/user-video-list.json`](../../../../catalog/models/weibo/web-v2/user-video-list.json) · Store page: https://www.sandbase.ai/model/weibo/web-v2/user-video-list
