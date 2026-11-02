# Instagram User Profile (V3) API: pricing, parameters and code examples

`instagram/v3/user-profile` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Returns complete profile details for an Instagram account, including follower counts, media metrics, and bio links based on the provided username.

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v3/user-profile", "username": "nasa"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v3/user-profile', {'username': 'nasa'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v3/user-profile", {
  "username": "nasa"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v3/user-profile", sandbase.Params{
	"username": "nasa",
})
```

Same call via the path form: `POST /v1/api/instagram/v3/user-profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `username` | string | yes | Instagram username (required)  |

## Details

Retrieve public Instagram profile details and account statistics using the `username` parameter.

### Use cases

- Display public Instagram profile details and bio links.
- Track follower and media counts for social media analytics.
- Look up account IDs and avatar URLs for user profiles.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/user-profile" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "nasa"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | Instagram username (required) |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "external_url": "https://www.nasa.gov",
  "follower_count": 104283560,
  "following_count": 90,
  "full_name": "NASA",
  "id": "528817151",
  "media_count": 4947,
  "profile_pic_url": "https://instagram.flas1-2.fna.fbcdn.net/v/t51.2885-19/29090066_159271188110124_1…",
  "username": "<user>"
}
```

### Notes

- Requires a valid `username` to look up profile information.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Comment Bulk Translation](/model/instagram/v3/bulk-translate-comments): Returns bulk translations for multiple Instagram comments using a list of comment identifiers.
- [Instagram Comment Replies (V3)](/model/instagram/v3/comment-replies): Returns child comment replies for a specific Instagram comment using the post media ID and parent comment ID.
- [Instagram Explore Feed](/model/instagram/v3/explore): Returns curated sectional items from the Instagram explore feed, including layout formats and feed types.

---
Machine-readable: [`catalog/models/instagram/v3/user-profile.json`](../../../../catalog/models/instagram/v3/user-profile.json) · Store page: https://www.sandbase.ai/model/instagram/v3/user-profile
