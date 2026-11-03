# Instagram Related Profiles API: pricing, parameters and code examples

`instagram/v1/related-profiles` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns related and similar user profile recommendations for a target Instagram account. Takes an Instagram user ID to look up connected profiles, usernames, and profile picture URLs.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v1/related-profiles", "user_id": "25025320"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v1/related-profiles', {'user_id': '25025320'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v1/related-profiles", {
  "user_id": "25025320"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v1/related-profiles", sandbase.Params{
	"user_id": "25025320",
})
```

Same call via the path form: `POST /v1/api/instagram/v1/related-profiles` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string | yes | Instagram user ID  |

## Details

Look up recommended or similar accounts for an Instagram user by providing their `user_id`. The response returns related profile nodes with IDs, usernames, and display names.

### Use cases

- Discover competitor or peer accounts within the same niche.
- Expand creator research by identifying similar profile suggestions.
- Display account recommendations based on a target user.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v1/related-profiles" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "25025320"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | Instagram user ID |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "user": {
      "edge_related_profiles": {
        "edges": [
          {
            "node": {
              "full_name": "Meta Prosper",
              "id": "52276426143",
              "profile_pic_url": "https://scontent-phl2-1.cdninstagram.com/v/t51.82787-19/551333341_18025298243738…",
              "username": "<user>"
            }
          }
        ]
      }
    }
  }
}
```

### Notes

- Requires a valid Instagram `user_id` as input.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Cities by Country](/apis/instagram/v1/cities): Returns a list of Instagram cities and regions for a specified country code.
- [Instagram Hashtag Posts (V1)](/apis/instagram/v1/hashtag-posts): Returns public Instagram posts associated with a specific hashtag.
- [Instagram Location Details (V1)](/apis/instagram/v1/location-info): Returns detailed metadata and profile information for a specified Instagram location using its unique identifier.

---
Machine-readable: [`catalog/models/instagram/v1/related-profiles.json`](../../../../catalog/models/instagram/v1/related-profiles.json) · Store page: https://www.sandbase.ai/model/instagram/v1/related-profiles
