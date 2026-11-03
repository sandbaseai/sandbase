# Douyin Hashtag Video List API: pricing, parameters and code examples

`douyin/app-v3/hashtag-video-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of videos associated with a specific Douyin hashtag. Supports sorting by comprehensive rank, most likes, or latest release along with cursor pagination.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/hashtag-video-list", "ch_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/hashtag-video-list', {'ch_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/hashtag-video-list", {
  "ch_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/hashtag-video-list", sandbase.Params{
	"ch_id": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/hashtag-video-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `ch_id` | string | yes | Hashtag id  |
| `count` | integer |  | Number Please keep the default, otherwise there will be BUG.  |
| `cursor` | integer |  | Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response.  |
| `sort_type` | integer |  | 0: Comprehensive sorting 1: Most likes 2: Latest release  |

## Details

Returns a page of videos posted under one Douyin hashtag. It needs the hashtag id in `ch_id`, and you can sort by default rank, most likes or latest release.

### Use cases

- Collect the videos posted under a campaign hashtag to see who is taking part.
- Pull the most liked videos for a hashtag with `sort_type` set to `1` to study what content works.
- Pull the newest videos for a hashtag with `sort_type` set to `2` to watch new posts as they appear.
- Build a list of creators active in a topic from the author data of each video.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/hashtag-video-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"ch_id": "1575791821492238"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `ch_id` | string | Yes | Hashtag id |
| `count` | integer | No | Number Please keep the default, otherwise there will be BUG. |
| `cursor` | integer | No | Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. |
| `sort_type` | integer | No | 0: Comprehensive sorting 1: Most likes 2: Latest release |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "aweme_list": [],
  "cursor": 10,
  "extra": {
    "fatal_item_ids": [],
    "logid": "20261103153135911EFF7F3C1CEA5D8041",
    "now": 1793691096000
  },
  "has_more": 1,
  "log_pb": {
    "impr_id": "20261103153135911EFF7F3C1CEA5D8041"
  },
  "mix_list": [
    {
      "aweme_info": {
        "activity_video_type": -1,
        "ad_charge_passive_unlock_config": {
          "broadcast_btn_config": {
            "btn_show_frequency": 1,
            "btn_show_second": 5,
            "btn_text": "秒后解锁下一集",
            "show_second_type": 2
          },
          "trial_btn_config": {
            "btn_show_frequency": 1,
            "btn_show_second": 3,
            "btn_text": "秒后解锁本集",
            "show_second_type": 2
          }
        },
        "ai_follow_images": null,
        "anchors": null,
        "authentication_token": "MS4wLjAA…",
        "author": {
          "accept_private_policy": false,
          "account_region": "",
          "ad_cover_url": null,
          "allow_story_normal_like": false,
          "apple_account": 0,
          "authority_status": 0,
          "avatar_168x168": {
            "height": 720,
            "uri": "168x168/aweme-avatar/tos-cn-i-0813c000-ce_oUiarAJqYAblEMeAi89JB9lEe1gfI2DAAgdwEB",
            "url_list": [
              "https://p3.douyinpic.com/img/aweme-avatar/tos-cn-i-0813c000-ce_oUiarAJqYAblEMeAi…"
            ],
            "width": 720
          },
          "avatar_300x300": {
            "height": 720,
            "uri": "300x300/aweme-avatar/tos-cn-i-0813c000-ce_oUiarAJqYAblEMeAi89JB9lEe1gfI2DAAgdwEB",
            "url_list": [
              "https://p3.douyinpic.com/img/aweme-avatar/tos-cn-i-0813c000-ce_oUiarAJqYAblEMeAi…"
            ],
            "width": 720
          }
        },
        "author_mask_tag": 0,
        "author_user_id": 7640751860513522725
      },
      "search_result_id": "7700554531473526057",
      "type": 1
    }
  ],
  "status_code": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `mix_list[]` | The list of results on this page. Each item wraps one video. |
| `mix_list[].aweme_info` | The video object. It holds the author, the video controls and other video data. |
| `mix_list[].search_result_id` | The id of the video result, as a string. It matches the video id format used by other Douyin video APIs. |
| `mix_list[].aweme_info.author` | The creator of the video. It includes avatar images as `avatar_168x168` and `avatar_300x300`, each with a `url_list` of image links. |
| `mix_list[].aweme_info.author_user_id` | The numeric id of the creator who posted the video. |
| `mix_list[].aweme_info.aweme_control.can_comment / can_forward / can_share` | Boolean flags that show whether commenting, forwarding and sharing are allowed on the video. |
| `cursor` | The cursor value to send in the next request to get the following page. |
| `has_more` | Shows whether more results exist. The value `1` means there is another page. |
| `status_code` | The status of the call. The value `0` was returned for this successful request. |

### Notes

- Start with `cursor` set to `0`. For the next page, send the `cursor` value from the previous response.
- Check `has_more` before you request another page. The `aweme_list` array was empty in this response, and the videos were in `mix_list`.
- Keep `count` at its default. The parameter description warns that other values can cause bugs.
- Use [Douyin Hashtag Details](/apis/douyin/app-v3/hashtag-detail) for information about the hashtag itself, and [Douyin Single Video Details](/apis/douyin/app-v3/one-video) to look up one video by its id.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Brand Hot Search List](/apis/douyin/app-v3/brand-hot-search-list): Returns the current Douyin brand hot search list and category data.
- [Douyin Brand Hot Search List Detail](/apis/douyin/app-v3/brand-hot-search-list-detail): Returns detailed brand hot search list data from Douyin for a specific category.
- [Douyin Short Link Generator](/apis/douyin/app-v3/generate-short-url): Converts a standard Douyin web link into a shortened Douyin URL.

---
Machine-readable: [`catalog/models/douyin/app-v3/hashtag-video-list.json`](../../../../catalog/models/douyin/app-v3/hashtag-video-list.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/hashtag-video-list
