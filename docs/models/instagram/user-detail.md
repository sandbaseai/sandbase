# Instagram User Profile API: pricing, parameters and code examples

`instagram/user-detail` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get an Instagram user profile by username. Use it to review a known account before creator research, brand monitoring, or related post analysis.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/user-detail", "username": "instagram"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/user-detail', {'username': 'instagram'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/user-detail", {
  "username": "instagram"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/user-detail", sandbase.Params{
	"username": "instagram",
})
```

Same call via the path form: `POST /v1/api/instagram/user-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `username` | string | yes | The Instagram username whose profile details are to be retrieved.  |

## Details

Returns the public profile of one Instagram account, including bio, bio links, follower and following counts, and the first page of recent posts and videos. It needs one input: the account `username`.

### Use cases

- Check the follower count and verified status of a creator before you contact them.
- Read the bio, external link and business contact fields to find how a brand wants to be reached.
- Track follower and post totals for a brand account over repeated calls.
- Pull the related profiles list to find similar accounts for competitor or creator research.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/user-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "instagram"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | The Instagram username whose profile details are to be retrieved. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "attempts": "0",
  "data": {
    "user": {
      "ai_agent_owner_username": null,
      "ai_agent_type": null,
      "bio_links": [
        {
          "link_type": "external",
          "lynx_url": "https://l.instagram.com/?u=http%3A%2F%2Fhelp.instagram.com%2F&e=AUB7qfn3OfnzWlG5…",
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
  },
  "status": "ok"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.user.full_name` | Display name of the account. |
| `data.user.biography` | Bio text shown on the profile. `biography_with_entities.raw_text` holds the same text. |
| `data.user.edge_followed_by.count / data.user.edge_follow.count` | Number of followers and number of accounts the user follows. |
| `data.user.edge_owner_to_timeline_media.count` | Total number of posts on the account. |
| `data.user.edge_owner_to_timeline_media.edges[].node` | One recent post. It includes `__typename` (such as `GraphVideo` or `GraphSidecar`), `display_url`, `dimensions`, `comments_disabled`, `accessibility_caption` and `edge_liked_by.count`. |
| `data.user.edge_owner_to_timeline_media.page_info.end_cursor / data.user.edge_owner_to_timeline_media.page_info.has_next_page` | Cursor for the next page of posts and a flag that shows whether more posts exist. |
| `data.user.edge_felix_video_timeline.count` | Total number of videos in the video timeline. The `edges` list holds the first page of those videos. |
| `data.user.bio_links[].url / data.user.bio_links[].title` | Links listed in the bio with their titles. `lynx_url` is the Instagram redirect version of the same link. |
| `data.user.external_url` | Main external link on the profile. |
| `data.user.edge_related_profiles.edges[].node.username / data.user.edge_related_profiles.edges[].node.is_verified` | Username and verified flag of each related account. Each node also has `full_name` and `id`. |
| `data.user.business_email / data.user.business_phone_number / data.user.business_category_name` | Business contact and category details. They are `null` when the account does not set them. |

### Notes

- Pass the handle without the `@` sign as `username`, for example `instagram`.
- Post lists are the first page only. The `end_cursor` values appear in each `page_info`, but this API takes only `username` as input.
- To look up an account by numeric ID, use [Instagram User Profile by ID](/apis/instagram/v1/user-info-by-id).
- For a lighter profile call, try [Instagram Basic Profile](/apis/instagram/basic-profile).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/instagram/user-detail.json`](../../../catalog/models/instagram/user-detail.json) · Store page: https://www.sandbase.ai/model/instagram/user-detail
