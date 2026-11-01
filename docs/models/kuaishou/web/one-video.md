# Kuaishou Single Video Details

`kuaishou/web/one-video` · api · Kuaishou

Returns detailed metadata for a single Kuaishou video post using shared link content. Note that photo-only posts are not supported.

## Pricing

- **$0.003 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/web/one-video", "share_text": "<share_text>"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/web/one-video', {'share_text': '<share_text>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/web/one-video", {
  "share_text": "<share_text>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/web/one-video", sandbase.Params{
	"share_text": "<share_text>",
})
```

Same call via the path form: `POST /v1/api/kuaishou/web/one-video` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `share_text` | string | yes | 作品分享链接/Photo share link  |

## Details

Retrieve detailed metadata for a specific video on Kuaishou using the `share_text` parameter. This endpoint does not return data for photo-only posts.

### Use cases

- Extract video metadata from a shared Kuaishou post link.
- Inspect individual Kuaishou video statistics and attributes.
- Process video content links shared across social platforms.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/web/one-video" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"share_text": "<share_text>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `share_text` | string | Yes | — |

### Notes

- Photo-only posts are not supported by this endpoint.
- Input must be provided via the `share_text` parameter.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Kuaishou Web Share Short URL](/model/kuaishou/web/generate-share-short-url): Returns a shareable short URL for a specified Kuaishou video or photo post.
- [Kuaishou User ID Lookup](/model/kuaishou/web/get-user-id): Resolves a Kuaishou user ID from a provided user share link.
- [Kuaishou Web Hot List](/model/kuaishou/web/hot-list-v1): Returns the current trending hot list from Kuaishou Web.

---
Machine-readable: [`catalog/models/kuaishou/web/one-video.json`](../../../../catalog/models/kuaishou/web/one-video.json) · Store page: https://www.sandbase.ai/model/kuaishou/web/one-video
