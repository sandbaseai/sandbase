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

Returns profile details and recent timeline media for one public Instagram account. It needs the account handle in `username`.

### Use cases

- Read follower and following counts for a creator before outreach.
- Collect the links in a brand's bio and check where they point.
- Pull recent timeline posts for an account and read their media type, size, and like counts.
- Check whether an account is a business account and whether it has Reels or highlights.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v1/user-info-by-username-v2" \
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
  "ai_agent_owner_username": null,
  "attempts": "0",
  "bio_links": [
    {
      "link_type": "external",
      "lynx_url": "https://l.instagram.com/?u=http%3A%2F%2Fhelp.instagram.com%2F&e=AUCzbng6B4XEbKuk…",
      "title": "",
      "url": "http://help.instagram.com"
    }
  ],
  "biography": "Discover what's new on Instagram 🔎✨",
  "biography_with_entities": {
    "entities": [],
    "raw_text": "Discover what's new on Instagram 🔎✨"
  },
  "blocked_by_viewer": false,
  "business_address_json": null,
  "business_category_name": null,
  "business_contact_method": "UNKNOWN",
  "business_email": null,
  "business_phone_number": null,
  "category_enum": null
}
```

### Response fields

| Field | Meaning |
|---|---|
| `id / fbid` | Numeric IDs for the account. Use `id` with APIs that take a user ID. |
| `full_name / biography` | The display name and the bio text of the account. |
| `bio_links[].url / bio_links[].title` | Each link listed in the bio, with its label. `lynx_url` holds the Instagram redirect version of the same link. |
| `external_url` | The main website link shown on the profile. |
| `edge_followed_by.count / edge_follow.count` | Number of followers and number of accounts the user follows. |
| `edge_owner_to_timeline_media.count` | Total number of posts on the timeline. |
| `edge_owner_to_timeline_media.edges[].node.__typename` | Post type, such as `GraphVideo` or `GraphSidecar` (a multi-item post). |
| `edge_owner_to_timeline_media.edges[].node.display_url` | Link to the main image or video cover for the post. |
| `edge_owner_to_timeline_media.edges[].node.edge_liked_by.count` | Like count for the post. Some nodes do not include it. |
| `edge_owner_to_timeline_media.edges[].node.coauthor_producers[].username` | Accounts credited as co-authors of the post. |

### Notes

- Pass the handle without the `@` sign, for example `instagram`.
- `edge_owner_to_timeline_media.edges` holds only a few recent posts. This API has no pagination parameter.
- Call [Instagram User Posts (V1)](/apis/instagram/v1/user-posts) to list more posts for the account.
- Call [Instagram User Profile by ID](/apis/instagram/v1/user-info-by-id) if you already have the numeric `id`.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Cities by Country](/apis/instagram/v1/cities): Returns a list of Instagram cities and regions for a specified country code.
- [Instagram Hashtag Posts (V1)](/apis/instagram/v1/hashtag-posts): Returns public Instagram posts associated with a specific hashtag.
- [Instagram Location Details (V1)](/apis/instagram/v1/location-info): Returns detailed metadata and profile information for a specified Instagram location using its unique identifier.

---
Machine-readable: [`catalog/models/instagram/v1/user-info-by-username-v2.json`](../../../../catalog/models/instagram/v1/user-info-by-username-v2.json) · Store page: https://www.sandbase.ai/model/instagram/v1/user-info-by-username-v2
