# Instagram User Info by Username

`instagram/v1/user-info-by-username` · api · Instagram

Returns Instagram user profile details and related account information for a specified Instagram handle. Input a username to view public profile data.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v1/user-info-by-username", "username": "__whoisashii"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v1/user-info-by-username', {'username': '__whoisashii'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v1/user-info-by-username", {
  "username": "__whoisashii"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v1/user-info-by-username", sandbase.Params{
	"username": "__whoisashii",
})
```

Same call via the path form: `POST /v1/api/instagram/v1/user-info-by-username` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `username` | string | yes | Instagram username  |

## Details

Access Instagram profile details and related accounts by providing a target `username`.

### Use cases

- Retrieve public profile data for a specific Instagram account.
- Explore related profiles associated with a target username.
- Verify account details and profile information before displaying in an application.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v1/user-info-by-username" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "instagram"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | Instagram username |

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
              "full_name": "абу",
              "id": "80458337039",
              "profile_pic_url": "https://instagram.fbcn2-1.fna.fbcdn.net/v/t51.82787-19/809201576_178909588026810…",
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

- Requires a valid `username` string without special formatting.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Cities by Country](/model/instagram/v1/cities): Returns a list of Instagram cities and regions for a specified country code.
- [Instagram Hashtag Posts (V1)](/model/instagram/v1/hashtag-posts): Returns public Instagram posts associated with a specific hashtag.
- [Instagram Location Details (V1)](/model/instagram/v1/location-info): Returns detailed metadata and profile information for a specified Instagram location using its unique identifier.

---
Machine-readable: [`catalog/models/instagram/v1/user-info-by-username.json`](../../../../catalog/models/instagram/v1/user-info-by-username.json) · Store page: https://www.sandbase.ai/model/instagram/v1/user-info-by-username
