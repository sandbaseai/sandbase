# Instagram User Data by Username (V2) API: pricing, parameters and code examples

`instagram/v1/user-info-by-username-v2` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns user profile details and recent timeline media for a specified Instagram account. Input the target handle to retrieve media nodes and account data.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v1/user-info-by-username-v2", "username": "instagram"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v1/user-info-by-username-v2', {'username': 'instagram'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v1/user-info-by-username-v2", {
  "username": "instagram"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v1/user-info-by-username-v2", sandbase.Params{
	"username": "instagram",
})
```

Same call via the path form: `POST /v1/api/instagram/v1/user-info-by-username-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `username` | string | yes | Instagram username  |

## Details

Look up Instagram account details and recent timeline media by passing the target account handle in `username`.

### Use cases

- Inspect recent timeline clips and video posts for an Instagram account.
- Retrieve profile information and public media nodes using an account handle.
- Monitor timeline media entries for specific public creators.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v1/user-info-by-username-v2" \
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
  "edge_owner_to_timeline_media": {
    "edges": [
      {
        "node": {
          "__typename": "GraphVideo",
          "display_url": "https://instagram.ftrn5-2.fna.fbcdn.net/v/t51.82787-15/830594125_187989641290013…",
          "id": "3998430248382584993",
          "like_and_view_counts_disabled": false,
          "media_preview": "ABgq58LngDmums2JgXPVRtP4dP0xUY0uJectke//ANarMdusYwMke5zUvUaKmd3U4YnnP8h7D+dFWZIFYZ6H2oqLF…",
          "product_type": "clips"
        }
      }
    ]
  }
}
```

### Notes

- Specify the target account handle using the required `username` parameter.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Cities by Country](/apis/instagram/v1/cities): Returns a list of Instagram cities and regions for a specified country code.
- [Instagram Hashtag Posts (V1)](/apis/instagram/v1/hashtag-posts): Returns public Instagram posts associated with a specific hashtag.
- [Instagram Location Details (V1)](/apis/instagram/v1/location-info): Returns detailed metadata and profile information for a specified Instagram location using its unique identifier.

---
Machine-readable: [`catalog/models/instagram/v1/user-info-by-username-v2.json`](../../../../catalog/models/instagram/v1/user-info-by-username-v2.json) · Store page: https://www.sandbase.ai/model/instagram/v1/user-info-by-username-v2
