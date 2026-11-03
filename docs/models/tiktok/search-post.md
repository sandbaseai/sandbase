# TikTok Post Search API: pricing, parameters and code examples

`tiktok/search-post` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Search TikTok posts by keyword with offset pagination plus sorting, publish-time, and region controls. Use it to support regional content discovery, topic research, or monitoring keyword-related videos.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/search-post", "keyword": "cooking"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/search-post', {'keyword': 'cooking'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/search-post", {
  "keyword": "cooking"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/search-post", sandbase.Params{
	"keyword": "cooking",
})
```

Same call via the path form: `POST /v1/api/tiktok/search-post` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `offset` | integer |  | Pagination offset, starting from 0 and stepping by 20. default `0` |
| `region` | string |  | ISO 3166-1 alpha-2 country code (e.g., 'US', 'GB'). default `"US"` |
| `keyword` | string | yes | Search keywords.  |
| `sortType` | string |  | Sorting criteria for search results. one of: `RELEVANCE`, `MOST_LIKED`; default `"RELEVANCE"` |
| `publishTime` | string |  | Filter posts by publishing time. one of: `ALL`, `ONE_DAY`, `ONE_WEEK`, `ONE_MONTH`, `THREE_MONTHS`, `HALF_YEAR`; default `"ALL"` |

## Details

Returns a page of TikTok posts that match a search keyword. Each result is a full post object with author, sound, and tag data. The only required input is `keyword`.

### Use cases

- Find videos about a topic such as `cooking` in a chosen country with the `region` parameter.
- Rank recent posts for a keyword by setting `sortType` to `MOST_LIKED` and `publishTime` to `ONE_WEEK`.
- Collect the authors and sounds that appear for a keyword to build a creator or music shortlist.
- Re-run the same keyword on a schedule and compare the returned posts to monitor a brand or trend.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/search-post" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "cooking"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keywords. |
| `offset` | integer | No | Pagination offset, starting from 0 and stepping by 20. |
| `publishTime` | string | No | Filter posts by publishing time. |
| `region` | string | No | ISO 3166-1 alpha-2 country code (e.g., 'US', 'GB'). |
| `sortType` | string | No | Sorting criteria for search results. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "aweme_list": [],
  "backtrace": "",
  "components": null,
  "cursor": 20,
  "extra": {
    "api_debug_info": null,
    "fatal_item_ids": [],
    "logid": "2026110307441120B3F9B5AF29F202A109",
    "now": 1793691851000,
    "search_request_id": "",
    "server_stream_time": 373
  },
  "feedback_type": "video",
  "global_doodle_config": {
    "disable_inner_flow": false,
    "display_filter_bar": 1,
    "enable_image_record": true,
    "feedback_survey": [
      {
        "feedback_type": "video",
        "long_stress_info": null,
        "multiple_choices": [
          {
            "key": "Dislike",
            "value": "Dislike"
          }
        ],
        "send_us_multiple_choices": null
      }
    ],
    "hide_results": false,
    "hit_dolphin": false,
    "hit_shark": true,
    "keyword": "cooking",
    "new_source": "switch_tab",
    "search_channel": "musically_video",
    "search_intent": {},
    "tns_search_result": "Pass"
  },
  "has_more": 1,
  "log_pb": {
    "impr_id": "2026110307441120B3F9B5AF29F202A109"
  },
  "search_item_list": [
    {
      "aweme_info": {
        "added_sound_music_info": {
          "album": "",
          "allow_offline_music_to_detail_page": false,
          "artists": [],
          "audition_duration": 100,
          "author": "MariClareMacLamroc",
          "author_deleted": false,
          "author_position": null,
          "avatar_medium": {
            "data_size": 0,
            "height": 720,
            "uri": "tos-useast5-avt-0068-tx/b0ef0515ef314de260854510a17933c1",
            "url_list": [
              "https://p19-common-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/b0ef0515ef314de…"
            ],
            "url_prefix": null,
            "width": 720
          }
        },
        "ai_remix_info": {
          "has_entrance": false
        },
        "aigc_info": {
          "aigc_label_type": 0,
          "created_by_ai": false
        },
        "allow_gift": true,
        "anchors": [
          {
            "actions": [
              {
                "action_type": 1,
                "icon": {
                  "height": 720,
                  "uri": "tiktok-obj/28px_primary_create_onDark3x.png",
                  "url_list": [
                    "https://p16-common.tiktokcdn-us.com/tiktok-obj/28px_primary_create_onDark3x.png~…"
                  ],
                  "url_prefix": null,
                  "width": 720
                },
                "schema": "shoot"
              }
            ],
            "anchor_strong": null,
            "component_key": "anchor_effect",
            "description": "Effects",
            "extra": "{\"effect_source\":102,\"is_commerce\":0,\"resource_id\":29649069847}",
            "icon": {
              "height": 720,
              "uri": "tiktok-obj/20px_anchor_effect3x.png",
              "url_list": [
                "https://p16-common.tiktokcdn-us.com/tiktok-obj/20px_anchor_effect3x.png~tplv-tik…"
              ],
              "url_prefix": null,
              "width": 720
            },
            "id": "3317039869",
            "keyword": "Lite Cutie face"
          }
        ],
        "anchors_extras": "",
        "animated_image_info": {
          "effect": 0,
          "type": 0
        },
        "author": {
          "accept_private_policy": false,
          "account_labels": null,
          "ad_cover_url": null,
          "advance_feature_item_order": null,
          "advanced_feature_info": null,
          "authority_status": 0,
          "avatar_168x168": {
            "data_size": 0,
            "height": 720,
            "uri": "tos-useast5-avt-0068-tx/b0ef0515ef314de260854510a17933c1",
            "url_list": [
              "https://p16-common-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/b0ef0515ef314de…"
            ],
            "url_prefix": null,
            "width": 720
          },
          "avatar_300x300": {
            "data_size": 0,
            "height": 720,
            "uri": "tos-useast5-avt-0068-tx/b0ef0515ef314de260854510a17933c1",
            "url_list": [
              "https://p16-common-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/b0ef0515ef314de…"
            ],
            "url_prefix": null,
            "width": 720
          }
        }
      },
      "search_aweme_info": {
        "has_creation_intention": false
      }
    }
  ],
  "status_code": 0,
  "version": "v2"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `search_item_list[]` | One search result per entry. The post data sits inside `aweme_info`. |
| `search_item_list[].aweme_info.author` | The account that published the post. It includes avatar images in several sizes, such as `avatar_168x168` and `avatar_300x300`, each with a `url_list`. |
| `search_item_list[].aweme_info.author_user_id` | Numeric ID of the account that published the post. |
| `search_item_list[].aweme_info.added_sound_music_info.author` | Name of the artist or account behind the sound used in the post. |
| `search_item_list[].aweme_info.added_sound_music_info.album / search_item_list[].aweme_info.added_sound_music_info.artists[].handle` | Album title and artist handles for the sound. `album` is an empty string when the sound has no album. |
| `search_item_list[].aweme_info.anchors[].keyword / search_item_list[].aweme_info.anchors[].description` | Label of an anchor attached to the post, for example an effect name. `anchors` is `null` on posts without one. |
| `search_item_list[].aweme_info.aigc_info.created_by_ai` | Boolean flag showing whether the post is marked as made with AI. |
| `has_more` | Set to `1` in this response, which signals that more results are available. |
| `cursor` | Pagination position returned with the page. It is `20` for the request at offset 0. |
| `extra.logid / extra.now` | Request log ID and a 13-digit millisecond timestamp for the response. |

### Notes

- Page through results with `offset` set to 0, 20, 40, and so on. Keep `has_more` in mind when deciding whether to continue.
- Read the results from `search_item_list`. In this response the top-level `aweme_list` is an empty array.
- `region` takes a two-letter ISO 3166-1 code such as `US` or `GB`. `sortType` accepts `RELEVANCE` or `MOST_LIKED`.
- To get more detail on one post from the results, call [TikTok Video Details](/apis/tiktok/app-v3/one-video).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/tiktok/search-post.json`](../../../catalog/models/tiktok/search-post.json) · Store page: https://www.sandbase.ai/model/tiktok/search-post
