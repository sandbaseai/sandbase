# Instagram Reels Search API: pricing, parameters and code examples

`instagram/v2/search-reels` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Search Instagram Reels by keyword: reel IDs, captions, creators, play, like and comment counts, with pagination.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v2/search-reels", "keyword": "openai"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v2/search-reels', {'keyword': 'openai'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v2/search-reels", {
  "keyword": "openai"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v2/search-reels", sandbase.Params{
	"keyword": "openai",
})
```

Same call via the path form: `POST /v1/api/instagram/v2/search-reels` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | Search keyword  |
| `pagination_token` | string |  | Pagination token from previous response  |

## Details

Returns Instagram Reels that match a keyword. Each item includes the reel code, caption data, and engagement counts. The only required input is `keyword`.

### Use cases

- Find reels about a topic such as `openai` and rank them by `comment_count`.
- Collect the hashtags used in captions of matching reels to see which tags travel with a topic.
- Find creators who post about a subject by reading the author shown in each result.
- Track mentions of a brand in short video by searching its name on a schedule.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v2/search-reels" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "openai"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword |
| `pagination_token` | string | No | Pagination token from previous response |

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
          "created_at": 1788649979,
          "created_at_utc": 1788649979,
          "did_report_as_spam": false,
          "hashtags": [
            "#ChatGPT"
          ],
          "id": "3979805292819643726",
          "is_covered": false,
          "is_ranked_comment": false,
          "mentions": []
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
              "data": "author_id:38717249519",
              "demotion_control": {
                "confirmation_body": "We won't suggest posts from aiwithsachi.",
                "confirmation_icon": "eye-off-pano",
                "confirmation_style": "bottomsheet",
                "confirmation_title": "",
                "undo_style": "inline"
              },
              "id": "dislike",
              "show_icon": true,
              "style": null,
              "subtitle": null,
              "text": "Don't suggest posts from aiwithsachi"
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
          "audio_canonical_id": "18490968535098900",
          "audio_ranking_info": {
            "best_audio_cluster_id": "949900630772750"
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
  "pagination_token": "GU1bBDYp…"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.count` | Number of items in this page of results. |
| `data.items[].code` | Short code of the reel. It is the part of the reel URL after `/reel/`. |
| `data.items[].fbid` | Numeric ID attached to the reel. |
| `data.items[].caption.id` | ID of the caption object for the reel. |
| `data.items[].caption.hashtags` | List of hashtags used in the caption, each with the leading `#`. |
| `data.items[].caption.mentions` | List of accounts tagged in the caption, each with the leading `@`. The list is empty when none are tagged. |
| `data.items[].caption.created_at / data.items[].caption.created_at_utc` | Unix timestamps in seconds for when the caption was created. |
| `data.items[].comment_count` | Number of comments on the reel. |
| `data.items[].clips_metadata.audio_type` | Type of audio on the reel, for example `original_sounds`. |
| `data.items[].clips_metadata.audio_canonical_id` | ID of the audio track used in the reel. |
| `data.items[].has_audio` | Whether the reel has an audio track. |

### Notes

- Pass the `pagination_token` from a previous response to get the next page. Keep the same `keyword`.
- The creator's user ID appears in `data.items[].clips_demotion_control.followup_options[].data` as `author_id:<id>`. Use it with [Instagram User Profile](/apis/instagram/v2/user-info) to look up the creator.
- Use `code` with [Instagram Post Details (V2)](/apis/instagram/v2/post-info) for full details on one reel, or [Instagram Post Comments (V2)](/apis/instagram/v2/post-comments) to read its comments.

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram User Profile](/apis/instagram/v2/user-info): Get an Instagram user profile by username or user ID: full name, bio, website, follower, following and post counts, verification and category.
- [Get comment replies](/apis/instagram/v2/comment-replies): Get list of replies to a comment Need to get comment ID from fetch_post_comments first Support pagination.
- [General search](/apis/instagram/v2/general-search): Perform general search on Instagram by keyword Support pagination.

---
Machine-readable: [`catalog/models/instagram/v2/search-reels.json`](../../../../catalog/models/instagram/v2/search-reels.json) · Store page: https://www.sandbase.ai/model/instagram/v2/search-reels
