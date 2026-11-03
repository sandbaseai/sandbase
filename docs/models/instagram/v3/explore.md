# Instagram Explore Feed API: pricing, parameters and code examples

`instagram/v3/explore` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Returns curated sectional items from the Instagram explore feed, including layout formats and feed types. Supports cursor-based pagination.

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v3/explore"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v3/explore', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v3/explore", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v3/explore", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/instagram/v3/explore` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `max_id` | string |  | Pagination cursor, omit for first request, get from previous response `data.next_max_id`  |

## Details

Returns a page of the Instagram explore feed as a list of `sectional_items`. Each item holds a layout description and a group of media or clips. The only input is the optional `max_id` cursor, so a first request needs no parameters.

### Use cases

- Sample the "For you" explore feed to see which content types (`clips` or media posts) Instagram surfaces.
- Track how the explore grid is laid out by comparing `layout_type` and column settings across pages.
- Collect `clips` IDs from the feed to feed into other Instagram post lookups.
- Check which explore items carry an AI content label by reading `ai_label_info` on each media object.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/explore" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `max_id` | string | No | Pagination cursor, omit for first request, get from previous response `data.next_max_id` |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "auto_load_more_enabled": true,
  "clusters": [
    {
      "can_mute": false,
      "context": "",
      "debug_info": "",
      "description": "",
      "id": "explore_all:0",
      "is_muted": false,
      "labels": [],
      "name": "For you",
      "title": "For you",
      "type": "explore_all"
    }
  ],
  "debug_info": null,
  "grid_overlay_debug_info": null,
  "interests": null,
  "max_id": "GvYSvrGQsfus0rtvwKyiqM2W07RvwqyUwMuVz8hvxJOy2fCI8rhvhu3JrLGqv8Vvio6wkJ6b2alvjOW0…",
  "more_available": true,
  "next_max_id": "0",
  "overlay_info": null,
  "quantum_signals_parsed": false,
  "rank_token": "2dc5a529…",
  "sectional_items": [
    {
      "explore_item_info": {
        "aspect_ratio": 2.25,
        "autoplay": true,
        "num_columns": 3,
        "total_num_columns": 3
      },
      "feed_type": "clips",
      "layout_content": {
        "medias": [
          {
            "media": {
              "algorithm": "edge_dedupe_unicorn",
              "are_remixes_crosspostable": true,
              "boost_unavailable_identifier": null,
              "boost_unavailable_reason": null,
              "boost_unavailable_reason_v2": null,
              "can_see_insights_as_brand": false,
              "can_viewer_reshare": true,
              "can_viewer_save": true
            }
          }
        ]
      },
      "layout_type": "dynamic_grid"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `sectional_items[].feed_type` | The kind of content in this section. The sample value is `clips`. |
| `sectional_items[].layout_type` | How the section is drawn in the grid. The sample value is `dynamic_grid`. |
| `sectional_items[].explore_item_info.aspect_ratio / num_columns / total_num_columns` | Grid sizing for the section. `num_columns` is how many columns this block uses, out of `total_num_columns`. |
| `sectional_items[].explore_item_info.autoplay` | Whether the section is set to autoplay in the grid. |
| `sectional_items[].layout_content.medias[].media` | One media post in the section. It carries many per-post flags such as `algorithm`, `can_viewer_save` and `can_viewer_reshare`, and may include `ai_label_info` and `accessibility_caption`. |
| `sectional_items[].layout_content.medias[].clips.id` | ID of a clips (reel) entry, in the form `clips-<number>_<number>`. |
| `sectional_items[].layout_content.medias[].clips.items[].media` | The media objects inside a clips entry. |
| `clusters[].name / title / type` | The feed cluster the page belongs to. The sample returns `For you` with type `explore_all`. |
| `more_available` | Whether the feed has more pages to load. |
| `next_max_id / max_id` | Cursor values for paging. The sample returns `next_max_id` as `"0"` and a long string in `max_id`. |

### Notes

- Omit `max_id` on the first request. For later pages, pass a cursor from the previous response as `max_id`, and check `more_available` first.
- Each clips entry also has its own `max_id` string, separate from the page-level cursor.
- For a feed of reels only, see [Instagram Recommended Reels Feed](/apis/instagram/v3/recommended-reels).

### Pricing

$0.008 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Comment Bulk Translation](/apis/instagram/v3/bulk-translate-comments): Returns bulk translations for multiple Instagram comments using a list of comment identifiers.
- [Instagram Comment Replies (V3)](/apis/instagram/v3/comment-replies): Returns child comment replies for a specific Instagram comment using the post media ID and parent comment ID.
- [Instagram Shortcode Extractor](/apis/instagram/v3/extract-shortcode): Extracts and returns the unique shortcode identifier from an Instagram post, reel, or TV URL.

---
Machine-readable: [`catalog/models/instagram/v3/explore.json`](../../../../catalog/models/instagram/v3/explore.json) · Store page: https://www.sandbase.ai/model/instagram/v3/explore
