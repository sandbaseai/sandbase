# Instagram User Profile by ID API: pricing, parameters and code examples

`instagram/v1/user-info-by-id` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns Instagram account information and recent timeline media details for a specified account. Queries using the unique numerical user ID.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v1/user-info-by-id", "user_id": "25025320"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v1/user-info-by-id', {'user_id': '25025320'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v1/user-info-by-id", {
  "user_id": "25025320"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v1/user-info-by-id", sandbase.Params{
	"user_id": "25025320",
})
```

Same call via the path form: `POST /v1/api/instagram/v1/user-info-by-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string | yes | Instagram user ID  |

## Details

Returns profile data for one Instagram account, plus a page of its recent timeline media. It needs the numeric Instagram `user_id`.

### Use cases

- Read follower and following counts for an account when you only have its numeric ID.
- Collect the external links and bio text an account lists on its profile.
- Check whether an account is a business account and whether it has contact details such as email or phone.
- Pull display URLs, dimensions and like counts of recent posts for a quick content review.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v1/user-info-by-id" \
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
  "ai_agent_owner_username": null,
  "attempts": "0",
  "bio_links": [
    {
      "link_type": "external",
      "lynx_url": "https://l.instagram.com/?u=http%3A%2F%2Fhelp.instagram.com%2F&e=AUAVag0WPMwXU8S1…",
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
| `id` | The numeric Instagram user ID of the account. It matches the `user_id` you sent. |
| `full_name` | The display name of the account. |
| `biography` | The bio text. `biography_with_entities.raw_text` holds the same text, and `biography_with_entities.entities` lists any tagged entities. |
| `edge_followed_by.count / edge_follow.count` | Number of followers and number of accounts this profile follows. |
| `bio_links[].url / bio_links[].title / bio_links[].link_type` | Links listed in the bio, with their title and type. `bio_links[].lynx_url` is the same link wrapped in an Instagram redirect URL. |
| `external_url` | The main website link on the profile. |
| `is_business_account` | Whether the account is a business account. Related fields include `business_email`, `business_phone_number` and `business_category_name`, which are `null` when not set. |
| `highlight_reel_count` | Number of story highlights on the profile. |
| `edge_owner_to_timeline_media.count` | Total number of posts on the account. |
| `edge_owner_to_timeline_media.edges[].node` | One recent post. It includes `__typename` (such as `GraphVideo` or `GraphSidecar`), `display_url`, `dimensions.height` / `dimensions.width`, `comments_disabled` and `edge_liked_by.count`. |

### Notes

- The `edges` list in `edge_owner_to_timeline_media` holds only a few recent posts. The API has no pagination parameter, so use [Instagram User Posts (V1)](/apis/instagram/v1/user-posts) to read more posts.
- If you only have a username, call [Instagram User Info by Username](/apis/instagram/v1/user-info-by-username) to look up the profile.
- Posts with `coauthor_producers` list the co-author's `id`, `username` and `is_verified` flag.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Cities by Country](/apis/instagram/v1/cities): Returns a list of Instagram cities and regions for a specified country code.
- [Instagram Hashtag Posts (V1)](/apis/instagram/v1/hashtag-posts): Returns public Instagram posts associated with a specific hashtag.
- [Instagram Location Details (V1)](/apis/instagram/v1/location-info): Returns detailed metadata and profile information for a specified Instagram location using its unique identifier.

---
Machine-readable: [`catalog/models/instagram/v1/user-info-by-id.json`](../../../../catalog/models/instagram/v1/user-info-by-id.json) · Store page: https://www.sandbase.ai/model/instagram/v1/user-info-by-id
