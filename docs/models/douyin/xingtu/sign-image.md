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

Returns signed image URLs for an encrypted Douyin Xingtu image URI. You send the `uri`, and you can also set the image `format` and how long the link stays valid.

### Use cases

- Turn an image URI from a Xingtu creator response into a URL you can show in a dashboard.
- Download Xingtu creator images in `jpg` or `png` instead of the default `webp`.
- Create image links with a custom lifetime by setting `durationTS`.
- Keep a backup link ready in case the main image URL fails to load.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu/sign-image" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uri": "tos-cn-i-0813c000-ce/oMKzDA3A9QGAuebfsDIAwlDoAfCFEEzSEw8FQZ"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uri` | string | Yes | Image URI, usually obtained from other XingTu API responses |
| `durationTS` | integer | No | Duration in seconds, default 86400 (24 hours) |
| `format` | string | No | Image format, default webp, supports: webp, jpg, png, etc. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "backupURL": "https://p3-star-fe-sign.byteimg.com/tos-cn-i-0813c000-ce/oMKzDA3A9QGAuebfsDIAwlD…",
  "img": {
    "format": "webp",
    "tpl": "tplv-9hvokabxw2-image",
    "uri": "tos-cn-i-0813c000-ce/oMKzDA3A9QGAuebfsDIAwlDoAfCFEEzSEw8FQZ"
  },
  "mainURL": "https://p26-star-fe-sign.byteimg.com/tos-cn-i-0813c000-ce/oMKzDA3A9QGAuebfsDIAwl…"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `mainURL` | Signed image URL for the requested `uri`. It includes the image template, the format as the file extension, and an `x-expires` query value. |
| `backupURL` | Alternate signed URL for the same image on a different host. Use it if `mainURL` does not load. |
| `img.uri` | The image URI that was resolved. It matches the `uri` you sent. |
| `img.format` | Image format used in the signed URLs, such as `webp`. |
| `img.tpl` | Image template name that appears in both signed URLs after the `~` character. |

### Notes

- Get the `uri` value from the image fields in other Xingtu responses, such as [Douyin XingTu KOL Profile](/apis/douyin/xingtu/kol-base-info-v1).
- The signed URLs carry an `x-expires` query value. Request a new URL once a link has expired.
- `format` defaults to `webp` and `durationTS` defaults to `86400` seconds (24 hours).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Xingtu Author Hot Comment Keywords](/apis/douyin/xingtu/author-content-hot-comment-keywords-v1): Returns hot comment keywords from content produced by a Douyin Xingtu creator.
- [Douyin Xingtu Author Hot Comment Tokens (Xingtu)](/apis/douyin/xingtu/author-hot-comment-tokens-v1): Returns hot comment tokens for a Douyin Xingtu creator based on the specified creator ID.
- [Douyin Xingtu KOL Audience Portrait (V1)](/apis/douyin/xingtu/kol-audience-portrait-v1): Returns audience demographic and portrait insights for a Douyin Xingtu creator.

---
Machine-readable: [`catalog/models/douyin/xingtu/sign-image.json`](../../../../catalog/models/douyin/xingtu/sign-image.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu/sign-image
