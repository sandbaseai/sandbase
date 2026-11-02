# Instagram User Reposts API: pricing, parameters and code examples

`instagram/v1/user-reposts` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns a paginated list of reposts and shared media for a specified Instagram account. Includes engagement metrics, captions, and original owner details.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v1/user-reposts", "user_id": "25025320"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v1/user-reposts', {'user_id': '25025320'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v1/user-reposts", {
  "user_id": "25025320"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v1/user-reposts", sandbase.Params{
	"user_id": "25025320",
})
```

Same call via the path form: `POST /v1/api/instagram/v1/user-reposts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `max_id` | string |  | Pagination cursor, omit for first request  |
| `user_id` | string | yes | Instagram user ID  |

## Details

Retrieve shared posts and reposted media for a specific account using `user_id`. Supports cursor-based pagination through `max_id`.

### Use cases

- Track media reposted by target Instagram profiles.
- Inspect engagement metrics on shared user content.
- Gather repost histories for creator and audience analytics.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v1/user-reposts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "25025320"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | Instagram user ID |
| `max_id` | string | No | Pagination cursor, omit for first request |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "items": [
    {
      "caption_is_edited": false,
      "carousel_media_count": 5,
      "carousel_media_pending_post_count": 0,
      "coauthor_producer_can_see_organic_insights": false,
      "comment_count": 4477,
      "filter_type": 0,
      "id": "3997941272011173993_36623372661",
      "like_and_view_counts_disabled": false,
      "like_count": 26048,
      "media_repost_count": 1502,
      "caption": {
        "__typename": "XDTCommentDict",
        "content_type": "comment",
        "media_id": "3997941272011173993",
        "private_reply_status": 0,
        "status": "Active",
        "text": "Make it Instagram official. You can now add your Muse to your profile."
      },
      "mashup_info": {
        "non_privacy_filtered_mashups_media_count": 0
      },
      "owner": {
        "__typename": "XDTUserDict",
        "full_name": "Muse",
        "id": "36623372661",
        "profile_pic_id": "3981848964622792966_36623372661",
        "profile_pic_url": "https://scontent-phl2-1.cdninstagram.com/v/t51.82787-19/800604240_18094883642220…",
        "username": "<user>"
      },
      "user": {
        "__typename": "XDTUserDict",
        "account_type": 2,
        "full_name": "Muse",
        "id": "36623372661",
        "profile_pic_id": "3981848964622792966_36623372661",
        "profile_pic_url": "https://scontent-phl2-1.cdninstagram.com/v/t51.82787-19/800604240_18094883642220…"
      }
    }
  ]
}
```

### Notes

- Pass `user_id` to identify the target Instagram profile.
- Omit `max_id` on the initial call and pass the pagination cursor to page through results.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Cities by Country](/model/instagram/v1/cities): Returns a list of Instagram cities and regions for a specified country code.
- [Instagram Hashtag Posts (V1)](/model/instagram/v1/hashtag-posts): Returns public Instagram posts associated with a specific hashtag.
- [Instagram Location Details (V1)](/model/instagram/v1/location-info): Returns detailed metadata and profile information for a specified Instagram location using its unique identifier.

---
Machine-readable: [`catalog/models/instagram/v1/user-reposts.json`](../../../../catalog/models/instagram/v1/user-reposts.json) · Store page: https://www.sandbase.ai/model/instagram/v1/user-reposts
