# Douyin Series Detail API: pricing, parameters and code examples

`douyin/app-v3/series-detail` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed information and UI configuration data for a Douyin playlet or video series using its unique series identifier.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/series-detail", "series_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/series-detail', {'series_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/series-detail", {
  "series_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/series-detail", sandbase.Params{
	"series_id": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/series-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `series_id` | string | yes | Series id  |

## Details

Returns metadata and display configuration for a Douyin playlet or video series. It needs one input, the `series_id` of the series.

### Use cases

- Read the name, episode count and play count of a Douyin series to build a catalog of playlets.
- Track `stats.play_vv` and `stats.collect_vv` for a series over time to see how its audience grows.
- Check whether a series is still updating by comparing `stats.updated_to_episode` with `stats.total_episode`.
- Build a share card for a series from its share link, cover image and title.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/series-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"series_id": "7585746250092251178"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `series_id` | string | Yes | Series id |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "extra": {
    "fatal_item_ids": [],
    "logid": "2026110315314096312B120161EE4E8CFD",
    "now": 1793691100000
  },
  "log_pb": {
    "impr_id": "2026110315314096312B120161EE4E8CFD"
  },
  "related_item_tag_infos": null,
  "series_info": {
    "actors": [],
    "ad_setting_info": {
      "biz_extra": "{\"calculate_from\":\"default\",\"is_enter_from_widget\":false,\"mid_ad_index\":[1,2,3,4…",
      "mid_ads_index": [
        1
      ],
      "rewarded_ads_index": null
    },
    "author": {
      "accept_private_policy": false,
      "account_region": "",
      "ad_cover_url": null,
      "allow_story_normal_like": false,
      "apple_account": 0,
      "authority_status": 0,
      "avatar_168x168": {
        "height": 720,
        "uri": "168x168/aweme-avatar/tos-cn-i-0813c000-ce_o8AAjKEQIJgQyYff2SF8fyDjgbmvgBAJDE07A1",
        "url_list": [
          "https://p3.douyinpic.com/img/aweme-avatar/tos-cn-i-0813c000-ce_o8AAjKEQIJgQyYff2…"
        ],
        "width": 720
      },
      "avatar_300x300": {
        "height": 720,
        "uri": "300x300/aweme-avatar/tos-cn-i-0813c000-ce_o8AAjKEQIJgQyYff2SF8fyDjgbmvgBAJDE07A1",
        "url_list": [
          "https://p3.douyinpic.com/img/aweme-avatar/tos-cn-i-0813c000-ce_o8AAjKEQIJgQyYff2…"
        ],
        "width": 720
      },
      "avatar_larger": {
        "height": 720,
        "uri": "1080x1080/aweme-avatar/tos-cn-i-0813c000-ce_o8AAjKEQIJgQyYff2SF8fyDjgbmvgBAJDE07…",
        "url_list": [
          "https://p3.douyinpic.com/aweme/1080x1080/aweme-avatar/tos-cn-i-0813c000-ce_o8AAj…"
        ],
        "width": 720
      },
      "avatar_medium": {
        "height": 720,
        "uri": "720x720/aweme-avatar/tos-cn-i-0813c000-ce_o8AAjKEQIJgQyYff2SF8fyDjgbmvgBAJDE07A1",
        "url_list": [
          "https://p3.douyinpic.com/aweme/720x720/aweme-avatar/tos-cn-i-0813c000-ce_o8AAjKE…"
        ],
        "width": 720
      },
      "avatar_schema_list": null,
      "avatar_thumb": {
        "height": 720,
        "uri": "100x100/aweme-avatar/tos-cn-i-0813c000-ce_o8AAjKEQIJgQyYff2SF8fyDjgbmvgBAJDE07A1",
        "url_list": [
          "https://p3.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-i-0813c000-ce_o8AAjKE…"
        ],
        "width": 720
      }
    },
    "content_sub_type": 3,
    "cover_url": {
      "height": 720,
      "uri": "douyin-user-image-file/5f5555569f02a53d1f7e7ec38a1d0c78",
      "url_list": [
        "https://p3-sign.douyinpic.com/douyin-user-image-file/5f5555569f02a53d1f7e7ec38a1…"
      ],
      "width": 720
    },
    "create_time": 1766194181,
    "dark_icon_url": {
      "height": 720,
      "uri": "tos-cn-i-30241dr4mi/ea30399c1df04270a54821d0cb3f3011",
      "url_list": [
        "https://p3-sign.douyinpic.com/obj/tos-cn-i-30241dr4mi/ea30399c1df04270a54821d0cb…"
      ],
      "width": 720
    },
    "desc": "",
    "directors": [],
    "enable_use_new_ent_data": true,
    "entertainment_suggest_info": "{\"recommend_channel_id\":9105,\"effective_scenes\":[\"aweme_more\"],\"recommend_channe…",
    "extra": "{\"ad_strategy\":\"{\\\"32\\\":1}\",\"content_sub_type\":3,\"continuous_category\":3,\"create…"
  },
  "status_code": 0,
  "status_msg": ""
}
```

### Response fields

| Field | Meaning |
|---|---|
| `series_info.series_id` | ID of the series, returned as a string. It matches the `series_id` you sent. |
| `series_info.series_name / series_info.real_name` | The series name. `series_name` includes the prefix shown in the app, and `real_name` is the plain title. |
| `series_info.stats.play_vv / series_info.stats.collect_vv` | Total play count and total collect (save) count for the series. |
| `series_info.stats.total_episode / series_info.stats.updated_to_episode` | Total number of episodes planned and the episode number the series is updated to. |
| `series_info.status.status_desc` | Short status text shown in the app, for example the update progress. |
| `series_info.create_time / series_info.update_time / series_info.stats.last_added_item_time` | Unix timestamps in seconds for when the series was created, last updated, and last had an episode added. |
| `series_info.series_content_types[].name` | Content category label of the series, with its numeric code in `series_content_type`. |
| `series_info.cover_url.url_list[]` | Cover image URLs for the series in different formats. The URLs are signed and carry an `x-expires` value. |
| `series_info.share_info.share_url` | Web share link for the series. |
| `series_info.series_ui_config.general_position_tag_infos[]` | UI tags for the series page. Each entry has a `tag_position` and the text or icon items to show, such as the play count label and the episode count label. |

### Notes

- Take the `series_id` from a series link. The `schema` value in `series_info.series_comment_top_bar` also shows it as `playlet_id`.
- `series_id` is a numeric ID sent as a string.
- To list the episodes of a series, call [Douyin Series Video List](/apis/douyin/app-v3/series-video-list).
- To find the series published by an author, call [Douyin User Series List](/apis/douyin/app-v3/user-series-list).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Brand Hot Search List](/apis/douyin/app-v3/brand-hot-search-list): Returns the current Douyin brand hot search list and category data.
- [Douyin Brand Hot Search List Detail](/apis/douyin/app-v3/brand-hot-search-list-detail): Returns detailed brand hot search list data from Douyin for a specific category.
- [Douyin Short Link Generator](/apis/douyin/app-v3/generate-short-url): Converts a standard Douyin web link into a shortened Douyin URL.

---
Machine-readable: [`catalog/models/douyin/app-v3/series-detail.json`](../../../../catalog/models/douyin/app-v3/series-detail.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/series-detail
