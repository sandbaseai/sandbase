# Instagram User Posts (V1) API: pricing, parameters and code examples

`instagram/v1/user-posts` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a paginated list of posts for a specified Instagram account. Results include captions, like counts, comment counts, and media details.

## Pricing

- **$0.001 per call** (USD)
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

Returns a paginated list of posts for one Instagram account. You send the numeric `user_id` of the account. Each item includes the post `code`, caption data, `comment_count`, and media details such as carousel items and clip metadata.

### Use cases

- Build a media feed for an Instagram account inside another app.
- Track `comment_count` across an account's recent posts to compare engagement.
- Collect accessibility captions and carousel media IDs to catalog an account's images.
- Page back through an account's history with `next_max_id` to archive its posts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v1/user-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "25025320"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | Instagram user ID |
| `count` | integer | No | Count per page, default 12 |
| `max_id` | string | No | Pagination cursor, omit for first request |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "attempts": "79",
  "items": [
    {
      "are_remixes_crosspostable": true,
      "boost_unavailable_identifier": null,
      "boost_unavailable_reason": null,
      "boost_unavailable_reason_v2": null,
      "can_see_insights_as_brand": false,
      "can_viewer_reshare": true,
      "can_viewer_save": true,
      "caption": {
        "bit_flags": 0,
        "content_type": "comment",
        "created_at": 1793647551,
        "created_at_utc": 1793647551,
        "did_report_as_spam": false,
        "is_covered": false,
        "is_ranked_comment": false,
        "media_id": 4021726163100932870
      },
      "caption_is_edited": false,
      "client_cache_key": "NDAyMTcyNjE2MzEwMDkzMjg3MA==.3",
      "clips_metadata": {
        "achievements_info": {
          "num_earned_achievements": null,
          "show_achievements": false
        },
        "additional_audio_info": {
          "additional_audio_username": null,
          "audio_reattribution_info": {
            "should_allow_restore": false
          }
        },
        "asset_recommendation_info": null,
        "audio_ranking_info": {
          "best_audio_cluster_id": "1079281138448348"
        },
        "audio_type": "original_sounds",
        "basel_template_info_for_ig_app": {
          "is_basel_template": null,
          "original_template_media_id": null,
          "should_show_reuse_setting_for_owner": false,
          "use_template_deeplink": null
        },
        "branded_content_tag_info": {
          "can_add_tag": false
        },
        "breaking_content_info": null
      },
      "clips_tab_pinned_user_ids": []
    }
  ],
  "more_available": true,
  "next_max_id": "4007127383642387898_25025320"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `items[]` | List of posts for the account. Each entry is one post, which can be a single video, a clip, or a carousel. |
| `items[].code` | Short post code, for example `DfQCqMnhpsG`. It is the shortcode used in Instagram post links. |
| `items[].comment_count` | Number of comments on the post. |
| `items[].caption.created_at / items[].caption.created_at_utc` | Unix timestamp in seconds for when the caption was created. In the sample both values are equal. |
| `items[].caption.media_id` | Numeric ID of the media that the caption belongs to. |
| `items[].accessibility_caption` | Text description of the image. It appears on image posts and carousel items, not on every post. |
| `items[].carousel_media[]` | Child items of a carousel post. Each one has its own `caption`, `carousel_parent_id`, and `commerciality_status`. |
| `items[].carousel_media_count` | Number of items in the carousel post. |
| `items[].coauthor_producers[]` | Accounts that co-author the post. Each entry has `full_name`, `pk`, `is_verified`, and `is_private`. |
| `items[].clips_metadata.audio_type` | Type of audio on a clip, for example `original_sounds`. |
| `more_available` | `true` when more posts can be fetched after this page. |
| `next_max_id` | Cursor for the next page. Pass it as `max_id` in the next request. |

### Notes

- Pass `next_max_id` from the response as `max_id` to get the next page. Stop when `more_available` is `false`.
- `count` sets the page size from 1 to 50. The default is 12.
- `user_id` is the numeric Instagram account ID. Get it from [Instagram User Info by Username](/apis/instagram/v1/user-info-by-username) if you only have a username.
- Post fields vary by type. Clips include `clips_metadata`, and carousels include `carousel_media`. To read one post in full, use [Instagram Post Details by ID](/apis/instagram/v1/post-by-id).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Cities by Country](/apis/instagram/v1/cities): Returns a list of Instagram cities and regions for a specified country code.
- [Instagram Hashtag Posts (V1)](/apis/instagram/v1/hashtag-posts): Returns public Instagram posts associated with a specific hashtag.
- [Instagram Location Details (V1)](/apis/instagram/v1/location-info): Returns detailed metadata and profile information for a specified Instagram location using its unique identifier.

---
Machine-readable: [`catalog/models/instagram/v1/user-posts.json`](../../../../catalog/models/instagram/v1/user-posts.json) · Store page: https://www.sandbase.ai/model/instagram/v1/user-posts
