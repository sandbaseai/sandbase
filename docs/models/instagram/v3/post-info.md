# Instagram Post Details (V3) API: pricing, parameters and code examples

`instagram/v3/post-info` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Returns comprehensive details for an Instagram post, reel, or video. Look up content using either a direct media link or a specific media identifier.

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v3/post-info"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v3/post-info', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v3/post-info", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v3/post-info", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/instagram/v3/post-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` |  |  | Post URL, e.g. `https://www.instagram.com/p/DUajw4YkorV/`, supports `/p/`, `/reel/`, `/reels/`, `/tv/` paths  |
| `media_id` |  |  | Post media ID (numeric ID), can be obtained via `/shortcode_to_media_id` endpoint  |

## Details

Returns details for one Instagram post, reel, or video as a list under `items`. Send a post `url` or a numeric `media_id`.

### Use cases

- Read the comment count and Facebook cross-post counts for a single reel.
- Find the co-authors of a collaboration post and check whether they are verified.
- Convert a post link into its `code`, `fbid`, and caption timestamp for record keeping.
- Check whether comments and reshares are enabled on a post before you build a tool around it.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/post-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"media_id": "3850699893338385742", "url": "https://www.instagram.com/p/DUajw4YkorV/"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `media_id` | string | No | Post media ID (numeric ID), can be obtained via `/shortcode_to_media_id` endpoint |
| `url` | string | No | Post URL, e.g. `https://www.instagram.com/p/DUajw4YkorV/`, supports `/p/`, `/reel/`, `/reels/`, `/tv/` paths |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "_rid": "1ccf10e877cb4",
  "auto_load_more_enabled": false,
  "items": [
    {
      "are_remixes_crosspostable": true,
      "boost_unavailable_identifier": null,
      "boost_unavailable_reason": null,
      "boost_unavailable_reason_v2": null,
      "can_see_insights_as_brand": false,
      "can_view_more_preview_comments": false,
      "can_viewer_reshare": true,
      "can_viewer_save": true,
      "caption": {
        "bit_flags": 0,
        "content_type": "comment",
        "created_at": 1773259206,
        "created_at_utc": 1773259206,
        "did_report_as_spam": false,
        "has_translation": true,
        "is_covered": false,
        "is_ranked_comment": false
      },
      "caption_is_edited": false,
      "client_cache_key": "Mzg1MDY5OTg5MzMzODM4NTc0Mg==.3",
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
          "best_audio_cluster_id": "727312237013877"
        },
        "audio_type": "original_sounds",
        "branded_content_tag_info": {
          "can_add_tag": false
        },
        "breaking_content_info": null,
        "breaking_creator_info": null
      }
    }
  ],
  "more_available": false,
  "num_results": 1,
  "status": "ok"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `items[].code` | Short code of the post. It is the part of the post URL after `/p/` or `/reel/`. |
| `items[].comment_count` | Number of comments on the post. |
| `items[].caption.created_at / items[].caption.created_at_utc` | Time the caption was created, as a Unix timestamp in seconds. |
| `items[].caption.has_translation` | Shows whether a translation exists for the caption. |
| `items[].fb_like_count / items[].fb_play_count / items[].fb_comment_count` | Like, play, and comment counts for the Facebook side of the post. |
| `items[].fbid` | Facebook-side ID for the post. |
| `items[].coauthor_producers[].full_name / items[].coauthor_producers[].id / items[].coauthor_producers[].is_verified` | Name, user ID, and verified status of each co-author on a collaboration post. |
| `items[].clips_metadata.audio_type` | Type of audio used in the reel. The value `original_sounds` marks audio made for this reel. |
| `items[].can_viewer_reshare / items[].can_viewer_save / items[].comment_likes_enabled` | Flags that show whether the viewer can reshare or save the post and whether comment likes are on. |
| `items[].device_timestamp` | Unix timestamp in seconds recorded by the posting device. |

### Notes

- Send either `url` or `media_id`. The `url` can use the `/p/`, `/reel/`, `/reels/`, or `/tv/` path.
- To get a `media_id` from a post link, call [Instagram Shortcode to Media ID (V3)](/apis/instagram/v3/shortcode-to-media-id).
- The response holds one post in `items`, and `num_results` is `1`. `more_available` is `false`, so there is no paging.
- To read the comments on the post, call [Instagram Post Comments (V3)](/apis/instagram/v3/post-comments).

### Pricing

$0.008 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Comment Bulk Translation](/apis/instagram/v3/bulk-translate-comments): Returns bulk translations for multiple Instagram comments using a list of comment identifiers.
- [Instagram Comment Replies (V3)](/apis/instagram/v3/comment-replies): Returns child comment replies for a specific Instagram comment using the post media ID and parent comment ID.
- [Instagram Explore Feed](/apis/instagram/v3/explore): Returns curated sectional items from the Instagram explore feed, including layout formats and feed types.

---
Machine-readable: [`catalog/models/instagram/v3/post-info.json`](../../../../catalog/models/instagram/v3/post-info.json) · Store page: https://www.sandbase.ai/model/instagram/v3/post-info
