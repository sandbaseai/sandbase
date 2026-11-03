# Douyin Xingtu Signed Image URL API: pricing, parameters and code examples

`douyin/xingtu/sign-image` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Resolves encrypted Xingtu image URIs into accessible image URLs. Callers can specify preferred image formats such as webp, jpg, or png along with link expiration times.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu/sign-image", "uri": "tos-cn-i-0813c000-ce/oMKzDA3A9QGAuebfsDIAwlDoAfCFEEzSEw8FQZ"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu/sign-image', {'uri': 'tos-cn-i-0813c000-ce/oMKzDA3A9QGAuebfsDIAwlDoAfCFEEzSEw8FQZ'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu/sign-image", {
  "uri": "tos-cn-i-0813c000-ce/oMKzDA3A9QGAuebfsDIAwlDoAfCFEEzSEw8FQZ"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu/sign-image", sandbase.Params{
	"uri": "tos-cn-i-0813c000-ce/oMKzDA3A9QGAuebfsDIAwlDoAfCFEEzSEw8FQZ",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu/sign-image` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uri` | string | yes | Image URI, usually obtained from other XingTu API responses  |
| `format` | string |  | Image format, default webp, supports: webp, jpg, png, etc.  |
| `durationTS` | integer |  | Duration in seconds, default 86400 (24 hours)  |

## Details

Convert encrypted Xingtu image URIs into accessible URLs using the `uri` parameter. You can optionally set custom image formats and link validity periods.

### Use cases

- Convert Xingtu image URIs into directly accessible image links.
- Retrieve Xingtu images in formats such as jpg, png, or webp.
- Generate temporary media URLs with custom expiration lifetimes.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu/sign-image" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uri": "tos-cn-i-0813c000-ce/oMKzDA3A9QGAuebfsDIAwlDoAfCFEEzSEw8FQZ"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uri` | string | Yes | Image URI, usually obtained from other XingTu API responses |
| `format` | string | No | Image format, default webp, supports: webp, jpg, png, etc. |
| `durationTS` | integer | No | Duration in seconds, default 86400 (24 hours) |

### Notes

- The `uri` parameter is typically retrieved from other Xingtu endpoint responses.
- The `format` parameter defaults to webp and accepts formats such as jpg and png.
- The `durationTS` parameter controls link validity in seconds, defaulting to 86400 (24 hours).

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Xingtu Author Hot Comment Keywords](/apis/douyin/xingtu/author-content-hot-comment-keywords-v1): Returns hot comment keywords from content produced by a Douyin Xingtu creator.
- [Douyin Xingtu Author Hot Comment Tokens (Xingtu)](/apis/douyin/xingtu/author-hot-comment-tokens-v1): Returns hot comment tokens for a Douyin Xingtu creator based on the specified creator ID.
- [Douyin Xingtu KOL Audience Portrait (V1)](/apis/douyin/xingtu/kol-audience-portrait-v1): Returns audience demographic and portrait insights for a Douyin Xingtu creator.

---
Machine-readable: [`catalog/models/douyin/xingtu/sign-image.json`](../../../../catalog/models/douyin/xingtu/sign-image.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu/sign-image
