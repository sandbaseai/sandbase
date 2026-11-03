# Instagram General Search (V3) API: pricing, parameters and code examples

`instagram/v3/general-search` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Returns search results across media grids based on a keyword query. Supports pagination tokens and optional metadata flags.

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v3/general-search", "query": "openai"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v3/general-search', {'query': 'openai'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v3/general-search", {
  "query": "openai"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v3/general-search", sandbase.Params{
	"query": "openai",
})
```

Same call via the path form: `POST /v1/api/instagram/v3/general-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Search keyword  |
| `rank_token` | string |  | Rank token, omit for first request, get from previous response `data.rank_token`  |
| `next_max_id` | string |  | Pagination ID, omit for first request, get from previous response `data.next_max_id`  |
| `enable_metadata` | boolean |  | Enable metadata default `true` |

## Details

Returns a grid of Instagram content that matches a keyword. The only required input is `query`. The response holds paged sections of clips and a token set for loading the next page.

### Use cases

- Pull the first pages of Instagram clips that match a brand name such as `openai`.
- Page through a keyword's result grid to build a sample of matching media.
- Collect media IDs and caption timestamps from search results to feed a deeper post lookup.
- Check whether a topic still has more results by reading `has_more` before the next call.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/general-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "openai"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search keyword |
| `enable_metadata` | boolean | No | Enable metadata |
| `next_max_id` | string | No | Pagination ID, omit for first request, get from previous response `data.next_max_id` |
| `rank_token` | string | No | Rank token, omit for first request, get from previous response `data.rank_token` |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "clear_client_cache": false,
  "has_more": true,
  "media_grid": {
    "auto_load_more_enabled": true,
    "autoplay_type": "single",
    "grid_post_click_experience": "contextual",
    "has_more": true,
    "has_more_reels": true,
    "next_max_id": "10692e605b574eab901683f8fa706045",
    "rank_token": "12a27009…",
    "reels_max_id": "r:d92259cd69fa4283b518166f7c93d539",
    "reels_page_index": 3,
    "refinements": {},
    "sections": [
      {
        "explore_item_info": {
          "aspect_ratio": 1.5,
          "autoplay": true,
          "num_columns": 3,
          "total_num_columns": 3
        },
        "feed_type": "clips",
        "layout_content": {
          "fill_items": [
            {
              "media": {
                "boost_unavailable_identifier": null,
                "boost_unavailable_reason": null,
                "boost_unavailable_reason_v2": null,
                "can_see_insights_as_brand": false,
                "can_viewer_reshare": true,
                "can_viewer_save": true,
                "caption": {
                  "bit_flags": 0,
                  "content_type": "comment",
                  "created_at": 1786283390,
                  "created_at_utc": 1786283390,
                  "did_report_as_spam": false,
                  "has_translation": true,
                  "is_covered": false,
                  "is_ranked_comment": false
                },
                "caption_add_on": {
                  "poll": {
                    "color": "black",
                    "expires_at": 1786542599,
                    "finished": true,
                    "id": "polling_sticker_vibrant",
                    "is_multi_option_poll": false,
                    "is_shared_result": false,
                    "poll_id": 18176712871423680,
                    "poll_type": "comment_poll"
                  }
                }
              }
            }
          ],
          "one_by_two_item": {
            "clips": {
              "badge_label": null,
              "chaining_info": null,
              "content_source": null,
              "design": "bottom_with_icon_horizontal",
              "id": "clips-e314f03e-350e-424d-b59b-095c2a34f505",
              "items": [
                {
                  "media": {
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
                      "created_at": 1791726819,
                      "created_at_utc": 1791726819,
                      "did_report_as_spam": false,
                      "is_covered": false,
                      "is_ranked_comment": false,
                      "media_id": 4005616888212600576
                    }
                  }
                }
              ],
              "label": "",
              "max_id": "r:d92259cd69fa4283b518166f7c93d539"
            }
          }
        },
        "layout_type": "one_by_two_right"
      }
    ],
    "topic_status": -1
  },
  "next_max_id": "10692e605b574eab901683f8fa706045",
  "rank_token": "12a27009…",
  "reels_max_id": "r:d92259cd69fa4283b518166f7c93d539",
  "status": "ok"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `has_more / media_grid.has_more` | Whether more results exist after this page. `media_grid.has_more_reels` does the same for the reels part of the grid. |
| `next_max_id` | Pagination ID for the next page. Pass it as `next_max_id` in the next request. The same value also appears at `media_grid.next_max_id`. |
| `rank_token` | Token that keeps the ranking consistent across pages. Pass it as `rank_token` in the next request. |
| `reels_max_id` | Cursor for the reels part of the grid. It starts with `r:`. The `media_grid.reels_page_index` field shows the current reels page number. |
| `media_grid.sections[].feed_type` | Content type of the section. Here the value is `clips`. |
| `media_grid.sections[].layout_type` | How the section is laid out in the grid, for example `one_by_two_right` or `one_by_two_left`. |
| `media_grid.sections[].layout_content.fill_items[].media` | A media item in the section. It holds flags such as `can_viewer_save` and `can_viewer_reshare`, and often a `caption` object. |
| `media_grid.sections[].layout_content.fill_items[].media.caption.created_at / created_at_utc` | Unix timestamp in seconds for when the caption was created. |
| `media_grid.sections[].layout_content.fill_items[].media.caption.media_id` | ID of the media the caption belongs to. Some items omit it. |
| `media_grid.sections[].layout_content.one_by_two_item.clips.items[].media` | The featured clip shown in the large tile of the section. It has the same structure as items in `fill_items`. |

### Notes

- For the first request, send only `query`. Omit `rank_token` and `next_max_id`.
- For the next page, send `next_max_id` and `rank_token` from the previous response, together with the same `query`.
- The pagination values appear at the top level of the response and inside `media_grid`. Both copies match.
- Use [Instagram Post Details (V3)](/apis/instagram/v3/post-info) to look up a post, or [Instagram Hashtag Posts (V3)](/apis/instagram/v3/hashtag-posts) to browse a hashtag.

### Pricing

$0.008 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Comment Bulk Translation](/apis/instagram/v3/bulk-translate-comments): Returns bulk translations for multiple Instagram comments using a list of comment identifiers.
- [Instagram Comment Replies (V3)](/apis/instagram/v3/comment-replies): Returns child comment replies for a specific Instagram comment using the post media ID and parent comment ID.
- [Instagram Explore Feed](/apis/instagram/v3/explore): Returns curated sectional items from the Instagram explore feed, including layout formats and feed types.

---
Machine-readable: [`catalog/models/instagram/v3/general-search.json`](../../../../catalog/models/instagram/v3/general-search.json) · Store page: https://www.sandbase.ai/model/instagram/v3/general-search
