# Instagram User Reels (V2) API: pricing, parameters and code examples

`instagram/v2/user-reels` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Returns a list of Reels from an Instagram account by username or user ID. Supports cursor-based pagination to browse past video content.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v2/user-reels"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v2/user-reels', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v2/user-reels", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v2/user-reels", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/instagram/v2/user-reels` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string |  | User ID (either username or user_id required)  |
| `username` | string |  | Username (either username or user_id required)  |
| `pagination_token` | string |  | Pagination token from previous response  |

## Details

Returns a list of Reels posted by an Instagram account. Each item holds the caption, comment count, audio details and sharing settings. You pass a `username` or a `user_id`.

### Use cases

- Pull the latest Reels from a brand account to track what it posts.
- Compare `comment_count` across Reels to find which videos get the most discussion.
- Collect the hashtags and mentions used in Reel captions to see which creators and tags an account features.
- Check the `audio_type` of each Reel to see how often an account uses original sounds versus licensed music.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v2/user-reels" \
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
        "clips_demotion_control": {
          "confirmation_body": "We'll suggest fewer posts like this.",
          "confirmation_icon": "none",
          "confirmation_style": "bottomsheet",
          "confirmation_title": "Post hidden",
          "confirmation_title_style": "large_left",
          "enable_word_wrapping": true,
          "followup_options": [
            {
              "data": "author_id:25025320",
              "demotion_control": {
                "confirmation_body": "We won't suggest posts from instagram.",
                "confirmation_icon": "eye-off-pano",
                "confirmation_style": "bottomsheet",
                "confirmation_title": "",
                "undo_style": "inline"
              },
              "id": "dislike",
              "show_icon": true,
              "style": null,
              "subtitle": null,
              "text": "Don't suggest posts from instagram"
            }
          ],
          "title": "Not interested"
        },
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
        "coauthor_producer_can_see_organic_insights": false
      }
    ]
  },
  "pagination_token": "GU1VBBop…"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.count` | Number of Reels in this response. |
| `data.items[].code` | Short code of the Reel. It is the part of the Instagram post URL that identifies the Reel. |
| `data.items[].fbid` | Numeric ID of the Reel as a string. |
| `data.items[].comment_count` | Number of comments on the Reel. |
| `data.items[].caption.id` | ID of the caption. |
| `data.items[].caption.created_at / data.items[].caption.created_at_utc` | Time the caption was created, as a Unix timestamp in seconds. |
| `data.items[].caption.hashtags` | List of hashtags in the caption, each with the leading `#`. The list is empty when the caption has none. |
| `data.items[].caption.mentions` | List of accounts mentioned in the caption, each with the leading `@`. |
| `data.items[].clips_metadata.audio_type` | Type of audio on the Reel. Values seen include `original_sounds` and `licensed_music`. |
| `data.items[].clips_metadata.audio_canonical_id` | ID of the audio track used in the Reel. |
| `data.items[].has_audio` | Whether the Reel has an audio track. |

### Notes

- Send either `username` or `user_id`. The example uses `instagram` and `18527`.
- Pass the `pagination_token` from a previous response to get the next page of Reels.
- To get the full details of one Reel, call [Instagram Post Details (V2)](/apis/instagram/v2/post-info) with its `code`.
- To read the comments on a Reel, call [Instagram Post Comments (V2)](/apis/instagram/v2/post-comments).

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Comment Replies (V2)](/apis/instagram/v2/comment-replies): Retrieves a paginated list of replies to an Instagram comment using the post URL or shortcode and the target comment ID.
- [Instagram General Search (V2)](/apis/instagram/v2/general-search): Returns Instagram search results matching a specified keyword, including media items, user profiles, and engagement statistics.
- [Instagram Hashtag Posts (V2)](/apis/instagram/v2/hashtag-posts): Returns posts associated with a specific hashtag.

---
Machine-readable: [`catalog/models/instagram/v2/user-reels.json`](../../../../catalog/models/instagram/v2/user-reels.json) · Store page: https://www.sandbase.ai/model/instagram/v2/user-reels
