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

Returns a list of Instagram accounts that Instagram suggests as related to a target account. You send the target's numeric `user_id`. Each result includes the profile's `id`, `full_name`, profile picture URL, and status flags.

### Use cases

- Find peer or competitor accounts for a brand by listing the profiles Instagram groups with it.
- Build a seed list of similar creators from one known account for influencer research.
- Show an "accounts like this" panel in a social analytics tool.
- Filter suggested accounts to verified or public profiles before outreach.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v1/related-profiles" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "25025320"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | Instagram user ID |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "attempts": "43",
  "data": {
    "user": {
      "edge_related_profiles": {
        "edges": [
          {
            "friendship_status": {
              "blocking": false,
              "followed_by": false,
              "following": false,
              "incoming_request": false,
              "is_bestie": false,
              "is_feed_favorite": false,
              "is_restricted": false,
              "outgoing_request": false
            },
            "full_name": "Kevin Systrom",
            "hd_profile_pic_url_info": {
              "url": "https://instagram.fbcn2-1.fna.fbcdn.net/v/t51.2885-19/13732144_1764457777134045_…"
            },
            "id": "3",
            "is_private": false,
            "is_unpublished": false,
            "is_verified": true,
            "live_broadcast_id": null
          }
        ]
      }
    }
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.user.edge_related_profiles.edges[]` | One related profile suggestion. Each item holds the profile details and the friendship flags. |
| `data.user.edge_related_profiles.edges[].id` | Instagram user ID of the related account. Use it as `user_id` in other Instagram calls. |
| `data.user.edge_related_profiles.edges[].full_name` | Display name of the related account, such as `Ray-Ban`. |
| `data.user.edge_related_profiles.edges[].hd_profile_pic_url_info.url` | URL of the account's profile picture. |
| `data.user.edge_related_profiles.edges[].is_verified` | `true` if the related account has the verified badge. |
| `data.user.edge_related_profiles.edges[].is_private` | `true` if the related account is private. |
| `data.user.edge_related_profiles.edges[].is_unpublished` | Boolean flag on the related account. It is `false` for all items in the sample. |
| `data.user.edge_related_profiles.edges[].live_broadcast_id` | ID of a live broadcast, or `null` when the account is not live. |
| `data.user.edge_related_profiles.edges[].friendship_status.following / followed_by / blocking / is_restricted` | Relationship flags between the related account and the account making the request. All are `false` in the sample. |
| `attempts` | Count returned with the response, shown as a string such as `43`. |

### Notes

- The response does not include a `username` field. Use the returned `id` with [Instagram User Profile by ID](/apis/instagram/v1/user-info-by-id) to get more details about a related account.
- To start from a handle instead of an ID, call [Instagram User Info by Username](/apis/instagram/v1/user-info-by-username) first and read the user ID from it.
- The request takes only `user_id`. There are no pagination parameters.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Cities by Country](/apis/instagram/v1/cities): Returns a list of Instagram cities and regions for a specified country code.
- [Instagram Hashtag Posts (V1)](/apis/instagram/v1/hashtag-posts): Returns public Instagram posts associated with a specific hashtag.
- [Instagram Location Details (V1)](/apis/instagram/v1/location-info): Returns detailed metadata and profile information for a specified Instagram location using its unique identifier.

---
Machine-readable: [`catalog/models/instagram/v1/related-profiles.json`](../../../../catalog/models/instagram/v1/related-profiles.json) · Store page: https://www.sandbase.ai/model/instagram/v1/related-profiles
