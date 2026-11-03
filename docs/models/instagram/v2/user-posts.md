# Instagram User Posts (V2) API: pricing, parameters and code examples

`instagram/v2/user-posts` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Returns a list of posts from a specific Instagram account using their username or user ID. Supports paginated results via a pagination token.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v2/user-posts"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v2/user-posts', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v2/user-posts", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v2/user-posts", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/instagram/v2/user-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string |  | User ID (either username or user_id required)  |
| `username` | string |  | Username (either username or user_id required)  |
| `pagination_token` | string |  | Pagination token from previous response  |

## Details

Returns a page of recent posts from one Instagram account, plus basic details about the account. You pass a `username` or a `user_id`. Each post includes its caption, comment count, and media details.

### Use cases

- Pull the latest posts from a brand account to track what it publishes.
- Collect comment counts per post to compare engagement across an account's content.
- Extract caption mentions to see which accounts a profile tags or collaborates with.
- Page through an account's feed to build an archive of its post codes and captions.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v2/user-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "instagram", "user_id": "18527"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `pagination_token` | string | No | Pagination token from previous response |
| `user_id` | string | No | User ID (either username or user_id required) |
| `username` | string | No | Username (either username or user_id required) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "count": 12,
    "items": [
      {
        "are_remixes_crosspostable": true,
        "boost_unavailable_identifier": null,
        "boost_unavailable_reason": null,
        "boost_unavailable_reason_v2": null,
        "can_reshare": true,
        "can_save": true,
        "caption": {
          "created_at": 1793647551,
          "created_at_utc": 1793647551,
          "did_report_as_spam": false,
          "hashtags": [],
          "id": "4021726163100932870",
          "is_covered": false,
          "is_ranked_comment": false,
          "mentions": [
            "@troyesivan"
          ]
        },
        "caption_is_edited": false,
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
          "audio_canonical_id": "18418030405089197",
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
          }
        },
        "clips_tab_pinned_user_ids": [],
        "coauthor_producer_can_see_organic_insights": false,
        "coauthor_producers": []
      }
    ],
    "user": {
      "full_name": "Instagram",
      "id": "25025320",
      "is_active_on_text_post_app": false,
      "is_private": false,
      "is_verified": true,
      "profile_pic_id": "3725434617063385984",
      "profile_pic_url": "https://scontent-arn2-1.cdninstagram.com/v/t51.82787-19/550891366_18667771684001…",
      "username": "instagram"
    }
  },
  "pagination_token": "D01MBAwp…"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.user.username / data.user.full_name` | Handle and display name of the account that owns the posts. |
| `data.user.id` | Numeric ID of the account. You can reuse it as `user_id` in other calls. |
| `data.user.is_verified / data.user.is_private` | Whether the account has a verification badge and whether it is private. |
| `data.count` | Number of posts in this page of results. |
| `data.items[].code` | Short post code. It appears in the post URL on Instagram. |
| `data.items[].comment_count` | Number of comments on the post. |
| `data.items[].caption.mentions` | Accounts mentioned in the caption, each with a leading `@`. |
| `data.items[].caption.created_at` | Unix timestamp (seconds) for when the caption was created. |
| `data.items[].carousel_media[]` | Slides of a carousel post. Each slide has its own caption data and, where present, an `accessibility_caption` that describes the image. |
| `data.items[].coauthor_producers[]` | Collaborator accounts on the post, with `username`, `full_name` and `is_verified`. |
| `pagination_token` | Token that selects the next page of posts. |

### Notes

- Send either `username` or `user_id`. The sample call sent both.
- To get the next page, send the returned `pagination_token` in the next request along with the same account.
- Reels items include a `clips_metadata` object with audio details. For reels only, see [Instagram User Reels (V2)](/apis/instagram/v2/user-reels).
- To read comments on a post, call [Instagram Post Comments (V2)](/apis/instagram/v2/post-comments).

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Comment Replies (V2)](/apis/instagram/v2/comment-replies): Retrieves a paginated list of replies to an Instagram comment using the post URL or shortcode and the target comment ID.
- [Instagram General Search (V2)](/apis/instagram/v2/general-search): Returns Instagram search results matching a specified keyword, including media items, user profiles, and engagement statistics.
- [Instagram Hashtag Posts (V2)](/apis/instagram/v2/hashtag-posts): Returns posts associated with a specific hashtag.

---
Machine-readable: [`catalog/models/instagram/v2/user-posts.json`](../../../../catalog/models/instagram/v2/user-posts.json) · Store page: https://www.sandbase.ai/model/instagram/v2/user-posts
