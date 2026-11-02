# Instagram Post Details (V3) API: pricing, parameters and code examples

`instagram/v3/post-info` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Returns comprehensive details for an Instagram post, reel, or video. Look up content using either a direct media link or a specific media identifier.

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v3/post-info"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v3/post-info', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v3/post-info", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v3/post-info", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/instagram/v3/post-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` |  |  | Post URL, e.g. `https://www.instagram.com/p/DUajw4YkorV/`, supports `/p/`, `/reel/`, `/reels/`, `/tv/` paths  |
| `media_id` |  |  | Post media ID (numeric ID), can be obtained via `/shortcode_to_media_id` endpoint  |

## Details

Fetch detailed information about an Instagram post by supplying either `url` or `media_id`.

### Use cases

- Retrieve post metadata from standard posts, reels, or video URLs.
- Look up specific media content using a numeric media identifier.
- Monitor engagement and post details across Instagram media links.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/post-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | No | Post URL, e.g. |
| `media_id` | string | No | Post media ID (numeric ID), can be obtained via `/shortcode_to_media_id` endpoint |

### Notes

- `url` accepts standard Instagram web links supporting `/p/`, `/reel/`, `/reels/`, and `/tv/` path formats.
- `media_id` requires a numeric identifier, which can be resolved from a post shortcode.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Comment Bulk Translation](/model/instagram/v3/bulk-translate-comments): Returns bulk translations for multiple Instagram comments using a list of comment identifiers.
- [Instagram Comment Replies (V3)](/model/instagram/v3/comment-replies): Returns child comment replies for a specific Instagram comment using the post media ID and parent comment ID.
- [Instagram Explore Feed](/model/instagram/v3/explore): Returns curated sectional items from the Instagram explore feed, including layout formats and feed types.

---
Machine-readable: [`catalog/models/instagram/v3/post-info.json`](../../../../catalog/models/instagram/v3/post-info.json) · Store page: https://www.sandbase.ai/model/instagram/v3/post-info
