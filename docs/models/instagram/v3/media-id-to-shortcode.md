# Instagram Media ID to Shortcode (V3) API: pricing, parameters and code examples

`instagram/v3/media-id-to-shortcode` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.003 per call (free daily quota) · **Modes:** sync

Converts a numeric Instagram media ID into a post shortcode for constructing web URLs. Requires the target post numeric identifier via media_id.

## Pricing

- **$0.003 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v3/media-id-to-shortcode", "media_id": "3964706607397327650"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v3/media-id-to-shortcode', {'media_id': '3964706607397327650'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v3/media-id-to-shortcode", {
  "media_id": "3964706607397327650"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v3/media-id-to-shortcode", sandbase.Params{
	"media_id": "3964706607397327650",
})
```

Same call via the path form: `POST /v1/api/instagram/v3/media-id-to-shortcode` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `media_id` | string | yes | Post media ID (numeric ID)  |

## Details

This endpoint converts a numeric Instagram post identifier into a post shortcode. Provide the numeric identifier in `media_id` to build standard post URLs.

### Use cases

- Generate web links for Instagram posts from internal numeric database identifiers.
- Convert media IDs retrieved from platform analytics into user-facing post shortcodes.
- Standardize Instagram post representations across external reporting dashboards.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/media-id-to-shortcode" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"media_id": "3850699893338385742"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `media_id` | string | Yes | Post media ID (numeric ID) |

### Notes

- Pass the numeric Instagram post identifier into `media_id`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Comment Bulk Translation](/model/instagram/v3/bulk-translate-comments): Returns bulk translations for multiple Instagram comments using a list of comment identifiers.
- [Instagram Comment Replies (V3)](/model/instagram/v3/comment-replies): Returns child comment replies for a specific Instagram comment using the post media ID and parent comment ID.
- [Instagram Explore Feed](/model/instagram/v3/explore): Returns curated sectional items from the Instagram explore feed, including layout formats and feed types.

---
Machine-readable: [`catalog/models/instagram/v3/media-id-to-shortcode.json`](../../../../catalog/models/instagram/v3/media-id-to-shortcode.json) · Store page: https://www.sandbase.ai/model/instagram/v3/media-id-to-shortcode
