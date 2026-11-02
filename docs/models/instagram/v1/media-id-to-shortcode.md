# Instagram Media ID to Shortcode (V1) API: pricing, parameters and code examples

`instagram/v1/media-id-to-shortcode` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Converts an Instagram post media ID into a shortcode used to construct standard post URLs. Accepts a numerical `media_id` parameter to look up the corresponding code.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v1/media-id-to-shortcode", "media_id": "232788642662632"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v1/media-id-to-shortcode', {'media_id': '232788642662632'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v1/media-id-to-shortcode", {
  "media_id": "232788642662632"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v1/media-id-to-shortcode", sandbase.Params{
	"media_id": "232788642662632",
})
```

Same call via the path form: `POST /v1/api/instagram/v1/media-id-to-shortcode` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `media_id` | string | yes | Post media ID  |

## Details

Provide a post's `media_id` to convert an internal Instagram identifier into its public shortcode. The resulting shortcode allows developers to assemble standard Instagram post web links.

### Use cases

- Generate public Instagram web URLs using numerical post identifiers.
- Convert internal media tracking IDs into human-readable shortcodes.
- Link directly to specific Instagram posts within external dashboards.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v1/media-id-to-shortcode" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"media_id": "3774507992167247878"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `media_id` | string | Yes | Post media ID |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "media_id": "3774507992167247878",
  "status": true
}
```

### Notes

- Construct Instagram post links using the pattern `instagram.com/p/{shortcode}/`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Cities by Country](/model/instagram/v1/cities): Returns a list of Instagram cities and regions for a specified country code.
- [Instagram Hashtag Posts (V1)](/model/instagram/v1/hashtag-posts): Returns public Instagram posts associated with a specific hashtag.
- [Instagram Location Details (V1)](/model/instagram/v1/location-info): Returns detailed metadata and profile information for a specified Instagram location using its unique identifier.

---
Machine-readable: [`catalog/models/instagram/v1/media-id-to-shortcode.json`](../../../../catalog/models/instagram/v1/media-id-to-shortcode.json) · Store page: https://www.sandbase.ai/model/instagram/v1/media-id-to-shortcode
