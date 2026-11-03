# Kuaishou Web Share Short URL API: pricing, parameters and code examples

`kuaishou/web/generate-share-short-url` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a shareable short URL for a specified Kuaishou video or photo post. Supply the target post identifier using the photo_id query parameter.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/web/generate-share-short-url", "photo_id": "5193494945927590140"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/web/generate-share-short-url', {'photo_id': '5193494945927590140'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/web/generate-share-short-url", {
  "photo_id": "5193494945927590140"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/web/generate-share-short-url", sandbase.Params{
	"photo_id": "5193494945927590140",
})
```

Same call via the path form: `POST /v1/api/kuaishou/web/generate-share-short-url` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `photo_id` | string | yes | 作品ID/Photo ID  |

## Details

Retrieve a shareable short link for a Kuaishou post by supplying its `photo_id`.

### Use cases

- Generating compact share links for external distribution.
- Embedding shortened links to Kuaishou posts in mobile messaging.
- Simplifying URL presentation across marketing channels.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/web/generate-share-short-url" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"photo_id": "5193494945927590140"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `photo_id` | string | Yes | — |

### Notes

- Requires a valid `photo_id` corresponding to the Kuaishou post.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Kuaishou User ID Lookup](/apis/kuaishou/web/get-user-id): Resolves a Kuaishou user ID from a provided user share link.
- [Kuaishou Web Hot List](/apis/kuaishou/web/hot-list-v1): Returns the current trending hot list from Kuaishou Web.
- [Kuaishou Web Hot List (V2)](/apis/kuaishou/web/hot-list-v2): Returns current trending search rankings and hot topics on Kuaishou web.

---
Machine-readable: [`catalog/models/kuaishou/web/generate-share-short-url.json`](../../../../catalog/models/kuaishou/web/generate-share-short-url.json) · Store page: https://www.sandbase.ai/model/kuaishou/web/generate-share-short-url
