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

Convert a numeric Instagram media ID into the post shortcode, so you can rebuild the public link `https://www.instagram.com/p/<shortcode>/`.

### Use cases

- Build clickable post links for media IDs returned by comment, tag or analytics APIs.
- Store posts by ID and render links only when needed.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v1/media-id-to-shortcode" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"media_id": "3774507992167247878"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `media_id` | string | Yes | Post media ID |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "media_id": "3774507992167247878",
  "shortcode": "DRhvwVLAHAG",
  "status": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `shortcode` | Shortcode for `instagram.com/p/<shortcode>/`. |
| `media_id` | The media ID you sent. |
| `status` | `true` when the conversion succeeded. |

### Notes

- An Instagram media ID and its shortcode are the same number in two encodings. The shortcode is the media ID written in base 64 with the alphabet `A-Z a-z 0-9 - _` (A = 0, _ = 63), so `DRhvwVLAHAG` and `3774507992167247878` name the same post. The media ID itself is a 64-bit snowflake: the top 41 bits are milliseconds since Instagram's epoch (2011-08-24 21:07:01.721 UTC), followed by 13 bits of shard ID and 10 bits of sequence, so `media_id >> 23` plus 1314220021721 gives the post's creation time in Unix milliseconds. Media IDs longer than 19 digits, with a `_<user_id>` suffix, are the same ID with the owner appended: drop the suffix before converting.
- Same result as the v2 and v3 versions at the lowest price.

### Pricing

$0.001 per successful call. Failed calls, including lookups whose target does not exist, are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Cities by Country](/apis/instagram/v1/cities): Returns a list of Instagram cities and regions for a specified country code.
- [Instagram Hashtag Posts (V1)](/apis/instagram/v1/hashtag-posts): Returns public Instagram posts associated with a specific hashtag.
- [Instagram Location Details (V1)](/apis/instagram/v1/location-info): Returns detailed metadata and profile information for a specified Instagram location using its unique identifier.

---
Machine-readable: [`catalog/models/instagram/v1/media-id-to-shortcode.json`](../../../../catalog/models/instagram/v1/media-id-to-shortcode.json) · Store page: https://www.sandbase.ai/model/instagram/v1/media-id-to-shortcode
