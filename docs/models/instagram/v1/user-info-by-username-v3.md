# Instagram User Profile by Username (V3) API: pricing, parameters and code examples

`instagram/v1/user-info-by-username-v3` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed Instagram user account information, including bio links, by querying an account handle.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v1/user-info-by-username-v3", "username": "instagram"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v1/user-info-by-username-v3', {'username': 'instagram'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v1/user-info-by-username-v3", {
  "username": "instagram"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v1/user-info-by-username-v3", sandbase.Params{
	"username": "instagram",
})
```

Same call via the path form: `POST /v1/api/instagram/v1/user-info-by-username-v3` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `username` | string | yes | Instagram username  |

## Details

Retrieve detailed Instagram user profile data by supplying an account handle via the `username` parameter.

### Use cases

- Inspect bio links and external URLs attached to an Instagram profile.
- Retrieve public profile details for a specific Instagram username.
- Verify public Instagram account handles and link metadata.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v1/user-info-by-username-v3" \
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
  "bio_links": [
    {
      "link_type": "external",
      "lynx_url": "https://l.instagram.com/?u=https%3A%2F%2Fhelp.instagram.com%2F&e=AUDPRoUBv2LXTt2…",
      "media_type": "none",
      "url": "http://help.instagram.com"
    }
  ]
}
```

### Notes

- Pass the target Instagram account handle into `username` without the leading @ symbol.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Cities by Country](/model/instagram/v1/cities): Returns a list of Instagram cities and regions for a specified country code.
- [Instagram Hashtag Posts (V1)](/model/instagram/v1/hashtag-posts): Returns public Instagram posts associated with a specific hashtag.
- [Instagram Location Details (V1)](/model/instagram/v1/location-info): Returns detailed metadata and profile information for a specified Instagram location using its unique identifier.

---
Machine-readable: [`catalog/models/instagram/v1/user-info-by-username-v3.json`](../../../../catalog/models/instagram/v1/user-info-by-username-v3.json) · Store page: https://www.sandbase.ai/model/instagram/v1/user-info-by-username-v3
