# Instagram Hashtag Posts (V2) API: pricing, parameters and code examples

`instagram/v2/hashtag-posts` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Returns posts associated with a specific hashtag. Supports filtering by top posts, recent posts, or reels along with cursor-based pagination.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v2/hashtag-posts", "keyword": "cat"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v2/hashtag-posts', {'keyword': 'cat'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v2/hashtag-posts", {
  "keyword": "cat"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v2/hashtag-posts", sandbase.Params{
	"keyword": "cat",
})
```

Same call via the path form: `POST /v1/api/instagram/v2/hashtag-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | Hashtag keyword (without #)  |
| `feed_type` | string |  | Feed type "top", "recent", or "reels", default top default `"top"` |
| `pagination_token` | string |  | Pagination token from previous response  |

## Details

Returns a list of Instagram posts and reels that use a given hashtag. It needs a `keyword` (the hashtag without the `#`) and can switch between top posts, recent posts, and reels with `feed_type`.

### Use cases

- Track likes, comments, and plays on posts under a campaign hashtag.
- Find reels with high `play_count` in a niche topic.
- Collect recent posts for a brand tag to review user-generated content.
- Build a list of accounts that post often under a hashtag.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v2/hashtag-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "cat"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Hashtag keyword (without #) |
| `feed_type` | string | No | Feed type "top", "recent", or "reels", default top |
| `pagination_token` | string | No | Pagination token from previous response |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "count": 30,
    "items": [
      {
        "accessibility_caption": null,
        "caption_hashtags": [
          "#cat"
        ],
        "caption_mentions": [],
        "caption_text": "His favorite brother.\n\n#cat #catstagram #catsofinstagram #cats #cats_of_instagra…",
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
          "audio_canonical_id": "18642912691057530",
          "audio_ranking_info": {
            "best_audio_cluster_id": "27998652563101654"
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
        "coauthor_producers": [],
        "code": "DfPiM_Hh78G",
        "comment_count": 3,
        "comments_disabled": false,
        "has_liked": false,
        "id": "4021583418252312326",
        "image_versions": [
          {
            "height": 1333,
            "is_spatial_image": false,
            "url": "https://scontent-lax7-1.cdninstagram.com/v/t51.82787-15/875347989_18642158602021…",
            "width": 750
          }
        ]
      }
    ]
  },
  "pagination_token": "D01SBBAp…"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.count` | Number of items returned in this response. |
| `data.items[].id / data.items[].code` | Post ID and short post code. The code is the part of the post URL after `/p/` or `/reel/`. |
| `data.items[].caption_text` | Full caption text of the post. |
| `data.items[].caption_hashtags` | List of hashtags found in the caption, each with the leading `#`. |
| `data.items[].like_count / comment_count / play_count` | Engagement counts for the post. `play_count` is set on reels. |
| `data.items[].taken_at / data.items[].taken_at_ts` | When the post was published, as an ISO 8601 time and as a Unix timestamp in seconds. |
| `data.items[].media_name / data.items[].product_type` | Type of post, such as `reel` with product type `clips`. |
| `data.items[].video_url / data.items[].video_duration` | Link to the video file and its length for video posts. The duration value looks like seconds. |
| `data.items[].thumbnail_url` | Link to a preview image of the post. |
| `data.items[].user.username / user.full_name / user.id` | Account that published the post: handle, display name, and numeric ID. |

### Notes

- Pass `keyword` without the `#`. For example, use `cat` for `#cat`.
- `feed_type` accepts `top`, `recent`, or `reels`. The default is `top`.
- To get more items, send the `pagination_token` from the previous response in the next request.
- To get details on one post from the results, call [Instagram Post Details (V2)](/apis/instagram/v2/post-info). To find related hashtags first, use [Instagram Hashtag Search (V2)](/apis/instagram/v2/search-hashtags).

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Comment Replies (V2)](/apis/instagram/v2/comment-replies): Retrieves a paginated list of replies to an Instagram comment using the post URL or shortcode and the target comment ID.
- [Instagram General Search (V2)](/apis/instagram/v2/general-search): Returns Instagram search results matching a specified keyword, including media items, user profiles, and engagement statistics.
- [Instagram Highlight Stories](/apis/instagram/v2/highlight-stories): Returns all stories contained within a specific Instagram highlight using its unique identifier.

---
Machine-readable: [`catalog/models/instagram/v2/hashtag-posts.json`](../../../../catalog/models/instagram/v2/hashtag-posts.json) · Store page: https://www.sandbase.ai/model/instagram/v2/hashtag-posts
