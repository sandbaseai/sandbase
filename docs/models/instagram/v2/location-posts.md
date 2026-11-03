# Instagram Location Posts (V2) API: pricing, parameters and code examples

`instagram/v2/location-posts` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Returns public Instagram posts tagged at a designated location. Requires a location ID and supports pagination tokens for browsing subsequent results.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v2/location-posts", "location_id": "331004901"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v2/location-posts', {'location_id': '331004901'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v2/location-posts", {
  "location_id": "331004901"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v2/location-posts", sandbase.Params{
	"location_id": "331004901",
})
```

Same call via the path form: `POST /v1/api/instagram/v2/location-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `location_id` | string | yes | Location ID  |
| `pagination_token` | string |  | Pagination token from previous response  |

## Details

Returns public Instagram posts tagged at one location. You send a `location_id` and get a page of posts, a total `count`, and a `pagination_token` for the next page.

### Use cases

- Collect recent public posts from a landmark, venue or neighborhood to see what visitors share.
- Count how many posts are tagged at a place using `data.count`.
- Page through a location's posts to build a media feed for a travel or local-guide site.
- Pull post codes from a location to open each post in a related post-detail call.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v2/location-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"location_id": "331004901"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `location_id` | string | Yes | Location ID |
| `pagination_token` | string | No | Pagination token from previous response |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "count": 63,
    "items": [
      {
        "are_remixes_crosspostable": true,
        "boost_unavailable_identifier": null,
        "boost_unavailable_reason": null,
        "boost_unavailable_reason_v2": null,
        "can_reshare": true,
        "can_save": true,
        "caption": null,
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
          "audio_canonical_id": "18452354581120915",
          "audio_ranking_info": {
            "best_audio_cluster_id": "1162699206086923"
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
    ]
  },
  "pagination_token": "HE1lBBsp…"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.count` | Number of posts reported for this location. |
| `data.items[]` | One post tagged at the location. Posts can be single media, reels (with `clips_metadata`) or carousels (with `carousel_media`). |
| `data.items[].code` | Short post code, such as `DfRKBtKMS51`. Use it to build the post URL or to look the post up in another API. |
| `data.items[].fbid` | Numeric ID string for the post. |
| `data.items[].caption.created_at / data.items[].caption.created_at_utc` | Unix timestamp in seconds for when the caption was created. In this response both fields hold the same value. `caption` is `null` when the post has no caption. |
| `data.items[].comment_count` | Number of comments on the post. |
| `data.items[].carousel_media_count` | Number of items in a carousel post. Only carousel posts include it. `carousel_media` may list fewer items than this count. |
| `data.items[].carousel_media[].id` | ID of one item inside a carousel post. |
| `data.items[].clips_metadata.audio_type` | Type of audio on a reel, such as `original_sounds` or `licensed_music`. |
| `pagination_token` | Token for the next page of results. Send it back as `pagination_token`. |

### Notes

- Find a `location_id` with [Instagram Location Search](/apis/instagram/v2/search-locations), or with [Instagram Location Search by Coordinates](/apis/instagram/v2/search-by-coordinates) if you only have coordinates.
- To get the next page, repeat the call with the same `location_id` and the `pagination_token` from the previous response.
- Not every item has every field. Reels include `clips_metadata`, carousels include `carousel_media`, and `caption` can be `null`.
- For full details on one post, pass its `code` to [Instagram Post Details (V2)](/apis/instagram/v2/post-info).

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Comment Replies (V2)](/apis/instagram/v2/comment-replies): Retrieves a paginated list of replies to an Instagram comment using the post URL or shortcode and the target comment ID.
- [Instagram General Search (V2)](/apis/instagram/v2/general-search): Returns Instagram search results matching a specified keyword, including media items, user profiles, and engagement statistics.
- [Instagram Hashtag Posts (V2)](/apis/instagram/v2/hashtag-posts): Returns posts associated with a specific hashtag.

---
Machine-readable: [`catalog/models/instagram/v2/location-posts.json`](../../../../catalog/models/instagram/v2/location-posts.json) · Store page: https://www.sandbase.ai/model/instagram/v2/location-posts
