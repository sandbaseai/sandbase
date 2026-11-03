# Instagram Post Details (V2) API: pricing, parameters and code examples

`instagram/v2/post-info` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Returns detailed information for an Instagram post, including available media streams and video versions, using a post shortcode or full URL.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v2/post-info", "code_or_url": "DRhvwVLAHAG"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v2/post-info', {'code_or_url': 'DRhvwVLAHAG'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v2/post-info", {
  "code_or_url": "DRhvwVLAHAG"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v2/post-info", sandbase.Params{
	"code_or_url": "DRhvwVLAHAG",
})
```

Same call via the path form: `POST /v1/api/instagram/v2/post-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `code_or_url` | string | yes | Post shortcode or full URL  |

## Details

Returns detailed data for one Instagram post, including its caption, audio details, and permission flags. It needs a post shortcode or a full post URL in `code_or_url`.

### Use cases

- Read the caption text, mentions, and hashtags of a single post.
- Check which original or licensed audio a Reel uses, including artist and title.
- Convert a post URL into structured data such as its shortcode and creation time.
- Check whether a post allows resharing, saving, and comment likes before you build a feature around it.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v2/post-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"code_or_url": "DRhvwVLAHAG"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `code_or_url` | string | Yes | Post shortcode or full URL |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "accessibility_caption": null,
    "are_remixes_crosspostable": true,
    "boost_unavailable_identifier": null,
    "boost_unavailable_reason": null,
    "boost_unavailable_reason_v2": null,
    "can_reshare": true,
    "can_save": true,
    "caption": {
      "created_at": 1764176515,
      "created_at_utc": 1764176515,
      "did_report_as_spam": false,
      "hashtags": [],
      "id": "3774507992167247878",
      "is_covered": false,
      "is_ranked_comment": false,
      "mentions": [
        "@sadiesink_"
      ],
      "pk": "17844901506605283",
      "private_reply_status": 0,
      "share_enabled": false,
      "text": "@sadiesink_ (Sadie Sink) and @maya_hawke (Maya Hawke) are returning to Hawkins f…"
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
      "audio_canonical_id": "18367181326095461",
      "audio_ranking_info": {
        "best_audio_cluster_id": "1490444716426084"
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
      "breaking_content_info": null,
      "breaking_creator_info": null,
      "challenge_info": null,
      "clips_creation_entry_point": "feed"
    },
    "clips_tab_pinned_user_ids": [],
    "coauthor_producer_can_see_organic_insights": false
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.code` | The post shortcode. It matches the `code_or_url` value in the request. |
| `data.caption.text` | The caption of the post. Mentions appear as @usernames inside the text. |
| `data.caption.created_at / data.caption.created_at_utc` | Unix timestamp in seconds for when the caption was created. |
| `data.caption.mentions[]` | List of accounts mentioned in the caption, each with a leading @. |
| `data.caption.hashtags[]` | List of hashtags found in the caption. It is empty when the caption has none. |
| `data.caption.text_translation` | A translated version of the caption text. |
| `data.clips_metadata.audio_type` | The kind of audio on the Reel, such as `original_sounds`. |
| `data.clips_metadata.original_sound_info.audio_parts[].display_title / data.clips_metadata.original_sound_info.audio_parts[].display_artist` | Title and artist of each audio part used in the sound. |
| `data.has_audio` | Whether the post has an audio track. |
| `data.can_reshare / data.can_save / data.comment_likes_enabled` | Flags that show whether viewers can reshare the post, save it, and like its comments. |

### Notes

- Pass either the shortcode, such as `DRhvwVLAHAG`, or the full post URL in `code_or_url`.
- To turn a shortcode into a numeric media ID, use [Instagram Shortcode to Media ID (V2)](/apis/instagram/v2/shortcode-to-media-id).
- To read the discussion on the post, call [Instagram Post Comments (V2)](/apis/instagram/v2/post-comments).
- To see who liked the post, call [Instagram Post Likes (V2)](/apis/instagram/v2/post-likes).

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Comment Replies (V2)](/apis/instagram/v2/comment-replies): Retrieves a paginated list of replies to an Instagram comment using the post URL or shortcode and the target comment ID.
- [Instagram General Search (V2)](/apis/instagram/v2/general-search): Returns Instagram search results matching a specified keyword, including media items, user profiles, and engagement statistics.
- [Instagram Hashtag Posts (V2)](/apis/instagram/v2/hashtag-posts): Returns posts associated with a specific hashtag.

---
Machine-readable: [`catalog/models/instagram/v2/post-info.json`](../../../../catalog/models/instagram/v2/post-info.json) · Store page: https://www.sandbase.ai/model/instagram/v2/post-info
