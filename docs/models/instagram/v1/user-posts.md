# Instagram User Posts (V1)

`instagram/v1/user-posts` · api · Instagram

Returns a paginated list of posts for a specified Instagram account. Results include captions, like counts, comment counts, and media details.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v1/user-posts", "user_id": "25025320"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v1/user-posts', {'user_id': '25025320'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v1/user-posts", {
  "user_id": "25025320"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v1/user-posts", sandbase.Params{
	"user_id": "25025320",
})
```

Same call via the path form: `POST /v1/api/instagram/v1/user-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Count per page, default 12 default `12`; range 1–50 |
| `max_id` | string |  | Pagination cursor, omit for first request  |
| `user_id` | string | yes | Instagram user ID  |

## Details

Retrieve recent posts from an Instagram account by supplying the target `user_id`. Supports pagination via cursor parameters to browse historical media feeds.

### Use cases

- Display an Instagram account media feed in an external application.
- Monitor engagement metrics such as likes and comments over recent posts.
- Archive captions and post metadata for specific public profiles.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v1/user-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "25025320"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | Instagram user ID |
| `count` | integer | No | Count per page, default 12 |
| `max_id` | string | No | Pagination cursor, omit for first request |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "items": [
    {
      "caption_is_edited": false,
      "coauthor_producer_can_see_organic_insights": false,
      "comment_count": 18380,
      "device_timestamp": 1790870048722622,
      "disable_caption_and_comment": false,
      "filter_type": 0,
      "id": "3998430248382584993_25025320",
      "ig_play_count": 150975683,
      "like_and_view_counts_disabled": false,
      "like_count": 642777,
      "caption": {
        "content_type": "comment",
        "media_id": 3998430248382584993,
        "private_reply_status": 0,
        "status": "Active",
        "text": "DIY fish squishy 🐟⁣ ⁣ @yano4kaa.a made this squishy using stuff she already had at home l…",
        "text_translation": "DIY fish squishy 🐟     @yano4kaa.a made this squishy using stuff she already had at home …"
      },
      "clips_metadata": {
        "audio_type": "licensed_music",
        "music_canonical_id": "18242041438023387",
        "professional_clips_upsell_type": 0
      },
      "user": {
        "account_type": 3,
        "eligible_for_text_app_activation_badge": false,
        "full_name": "Instagram",
        "id": "25025320",
        "pk_id": "25025320",
        "profile_pic_id": "3725434617063385984_25025320"
      }
    }
  ]
}
```

### Notes

- Supply `user_id` to identify the Instagram profile.
- Pass `max_id` as the pagination cursor for requests after the first page.
- Use `count` to specify the number of posts returned per page, defaulting to 12.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Cities by Country](/model/instagram/v1/cities): Returns a list of Instagram cities and regions for a specified country code.
- [Instagram Hashtag Posts (V1)](/model/instagram/v1/hashtag-posts): Returns public Instagram posts associated with a specific hashtag.
- [Instagram Location Details (V1)](/model/instagram/v1/location-info): Returns detailed metadata and profile information for a specified Instagram location using its unique identifier.

---
Machine-readable: [`catalog/models/instagram/v1/user-posts.json`](../../../../catalog/models/instagram/v1/user-posts.json) · Store page: https://www.sandbase.ai/model/instagram/v1/user-posts
