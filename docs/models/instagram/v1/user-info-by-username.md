# Instagram User Info by Username API: pricing, parameters and code examples

`instagram/v1/user-info-by-username` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns Instagram user profile details and related account information for a specified Instagram handle. Input a username to view public profile data.

## Pricing

- **$0.001 per call** (USD)
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

Get an Instagram profile by username in the format of Instagram's web profile API: bio, bio links, follower and following counts, post count, verification, privacy and business details.

### Use cases

- Enrich a list of usernames with audience size and bio.
- Read a business account's category and contact options.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v1/user-info-by-username" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "instagram"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | Instagram username |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "user": {
      "id": "25025320",
      "username": "instagram",
      "full_name": "Instagram",
      "biography": "Discover what's new on Instagram 🔎✨",
      "is_private": false,
      "is_verified": true,
      "is_business_account": false,
      "category_name": null,
      "external_url": "http://help.instagram.com/",
      "edge_followed_by": {
        "count": 686358280
      },
      "edge_follow": {
        "count": 165
      },
      "edge_owner_to_timeline_media": {
        "count": 8634
      }
    }
  },
  "status": "ok"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.user.id / username / full_name` | Numeric ID, handle and display name. |
| `data.user.edge_followed_by.count / edge_follow.count` | Followers and accounts followed. |
| `data.user.edge_owner_to_timeline_media.count` | Number of posts. |
| `data.user.is_private / is_verified / is_business_account` | Account flags. |
| `data.user.bio_links` | Links in bio. |

### Notes

- Counts sit under `edge_*` keys, as in Instagram's web API. For flat `follower_count` fields use [Instagram User Info (v2)](/apis/instagram/v2/user-info).

### Pricing

$0.001 per successful call. Failed calls, including lookups whose target does not exist, are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Cities by Country](/apis/instagram/v1/cities): Returns a list of Instagram cities and regions for a specified country code.
- [Instagram Hashtag Posts (V1)](/apis/instagram/v1/hashtag-posts): Returns public Instagram posts associated with a specific hashtag.
- [Instagram Location Details (V1)](/apis/instagram/v1/location-info): Returns detailed metadata and profile information for a specified Instagram location using its unique identifier.

---
Machine-readable: [`catalog/models/instagram/v1/user-info-by-username.json`](../../../../catalog/models/instagram/v1/user-info-by-username.json) · Store page: https://www.sandbase.ai/model/instagram/v1/user-info-by-username
