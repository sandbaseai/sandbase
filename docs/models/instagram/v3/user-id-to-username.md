# Instagram User Info by ID API: pricing, parameters and code examples

`instagram/v3/user-id-to-username` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Returns an Instagram profile's details, including username, full name, follower count, and media metrics using an account ID.

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v3/user-id-to-username", "user_id": "1935268808"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v3/user-id-to-username', {'user_id': '1935268808'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v3/user-id-to-username", {
  "user_id": "1935268808"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v3/user-id-to-username", sandbase.Params{
	"user_id": "1935268808",
})
```

Same call via the path form: `POST /v1/api/instagram/v3/user-id-to-username` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string | yes | Instagram user ID (numeric string)  |

## Details

Look up an Instagram user profile by providing a numeric `user_id`. The response returns core account metrics including username, follower count, and profile picture URL.

### Use cases

- Resolve an Instagram numeric account ID to its current username.
- Inspect follower and following counts alongside total media counts.
- Retrieve profile details such as full name, profile picture URL, and external website.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/user-id-to-username" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "25025320"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | Instagram user ID (numeric string) |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "external_url": "http://help.instagram.com",
  "follower_count": 686584231,
  "following_count": 305,
  "full_name": "Instagram",
  "id": "25025320",
  "media_count": 8612,
  "profile_pic_url": "https://instagram.fpit1-1.fna.fbcdn.net/v/t51.82787-19/550891366_186677716840013…",
  "username": "<user>"
}
```

### Notes

- The `user_id` parameter requires a numeric string representing the target account identifier.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Comment Bulk Translation](/model/instagram/v3/bulk-translate-comments): Returns bulk translations for multiple Instagram comments using a list of comment identifiers.
- [Instagram Comment Replies (V3)](/model/instagram/v3/comment-replies): Returns child comment replies for a specific Instagram comment using the post media ID and parent comment ID.
- [Instagram Explore Feed](/model/instagram/v3/explore): Returns curated sectional items from the Instagram explore feed, including layout formats and feed types.

---
Machine-readable: [`catalog/models/instagram/v3/user-id-to-username.json`](../../../../catalog/models/instagram/v3/user-id-to-username.json) · Store page: https://www.sandbase.ai/model/instagram/v3/user-id-to-username
