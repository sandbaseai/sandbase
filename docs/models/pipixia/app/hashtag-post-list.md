# Pipixia Hashtag Post List API: pricing, parameters and code examples

`pipixia/app/hashtag-post-list` · data API · Pipixia · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of posts associated with a specific hashtag on Pipixia. Filter by hashtag identifier, sort options, and paginate through results.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "pipixia/app/hashtag-post-list", "hashtag_id": "129559"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('pipixia/app/hashtag-post-list', {'hashtag_id': '129559'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("pipixia/app/hashtag-post-list", {
  "hashtag_id": "129559"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "pipixia/app/hashtag-post-list", sandbase.Params{
	"hashtag_id": "129559",
})
```

Same call via the path form: `POST /v1/api/pipixia/app/hashtag-post-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Page cursor, default is 0, get the corresponding value from the `loadmore_cursor` Key in the previous page. default `"0"` |
| `feed_count` | string |  | Page count, default is 0, add 1 for each page, such as 0 for the first page, 1 for the second page, 2 for the third page, and so on. default `"0"` |
| `hashtag_id` | string | yes | AKA hashtag id, can be obtained from the share link.  |
| `hashtag_sort_type` | string |  | Hashtag sort type default `"3"` |
| `hashtag_request_type` | string |  | Hashtag request type default `"0"` |

## Details

Returns a page of posts filed under one Pipixia hashtag. Each entry holds the post content, its author, and details about the hashtag. The only required input is `hashtag_id`.

### Use cases

- Collect recent posts under a hashtag such as `129559` to review what users share on that topic.
- Page through a hashtag feed to build a dataset of post text and author profiles.
- Compare `enter_num` and `followers_num` for a hashtag to see how many people visit it and how many follow it.
- Find authors who post often under a topic by reading each post's `author` object.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/pipixia/app/hashtag-post-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"hashtag_id": "129559"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `hashtag_id` | string | Yes | AKA hashtag id, can be obtained from the share link. |
| `cursor` | string | No | Page cursor, default is 0, get the corresponding value from the `loadmore_cursor` Key in the previous page. |
| `feed_count` | string | No | Page count, default is 0, add 1 for each page, such as 0 for the first page, 1 for the second page, 2 for the third page, and so on. |
| `hashtag_request_type` | string | No | Hashtag request type |
| `hashtag_sort_type` | string | No | Hashtag sort type |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "cursor": {
      "feed_len": 0,
      "has_more": true,
      "loadmore_cursor": 1398012000,
      "refresh_cursor": 0
    },
    "data": [
      {
        "cell_id": 7685342951509072138,
        "cell_id_str": "7685342951509072138",
        "cell_type": 1,
        "city_name": "湖北",
        "comment_show_ad": true,
        "dislike_options": [
          {
            "dislike_desc": "不感兴趣",
            "dislike_type": 1,
            "icon_image": {
              "download_list": [
                {
                  "url": "https://p3-ppx-sign.byteimg.com/tos-cn-i-0000/8e60799021a94ccfbdf49e44225f94e6~t…"
                }
              ],
              "height": 69,
              "is_gif": false,
              "uri": "tos-cn-i-0000/8e60799021a94ccfbdf49e44225f94e6",
              "url_list": [
                {
                  "url": "https://p9-ppx-sign.byteimg.com/tos-cn-i-0000/8e60799021a94ccfbdf49e44225f94e6~t…"
                }
              ],
              "width": 69
            },
            "option_id": 0
          }
        ],
        "display_time": 1789383346,
        "hashtag": {
          "base_hashtag": {
            "action_end_time": 1591632000,
            "action_start_time": 1591027200,
            "activity_icon": {
              "color": "FFFF6880",
              "icon_image": {
                "download_list": [
                  {
                    "url": "https://p6-ppx-sign.byteimg.com/tos-cn-i-8gu37r9deh/428d745dce031ce630f5db129c6b…"
                  }
                ],
                "height": 48,
                "is_gif": false,
                "uri": "tos-cn-i-8gu37r9deh/428d745dce031ce630f5db129c6bee23.png",
                "url_list": [
                  {
                    "url": "https://p3-ppx-sign.byteimg.com/tos-cn-i-8gu37r9deh/428d745dce031ce630f5db129c6b…"
                  }
                ],
                "width": 48
              },
              "name": "追剧不能停"
            },
            "atmosphere": "皮友正在讨论",
            "avatars": [
              {
                "download_list": [
                  {
                    "url": "https://p6-ppx-sign.byteimg.com/tos-cn-i-0000/a4de3fd9420c4fe89c7b0877fe108d93~t…"
                  }
                ],
                "height": 200,
                "is_gif": false,
                "uri": "tos-cn-i-0000/a4de3fd9420c4fe89c7b0877fe108d93",
                "url_list": [
                  {
                    "url": "https://p3-ppx-sign.byteimg.com/tos-cn-i-0000/a4de3fd9420c4fe89c7b0877fe108d93~t…"
                  }
                ],
                "width": 200
              }
            ],
            "background_image": {
              "download_list": [
                {
                  "url": "https://p3-ppx-sign.byteimg.com/tos-cn-i-0000/d66884d83ca342b2a1963256f4491dc8~t…"
                }
              ],
              "height": 340,
              "is_gif": false,
              "uri": "tos-cn-i-0000/d66884d83ca342b2a1963256f4491dc8",
              "url_list": [
                {
                  "url": "https://p6-ppx-sign.byteimg.com/tos-cn-i-0000/d66884d83ca342b2a1963256f4491dc8~t…"
                }
              ],
              "width": 750
            },
            "category_list": [
              {
                "display_order": 1,
                "id": 58,
                "name": "影视娱乐"
              }
            ],
            "create_time": 1531921918
          },
          "enter_num": 21014839,
          "followers_num": 227536,
          "host_user_ids": [
            1759652656449688
          ],
          "id_str": "129559",
          "is_follow": false,
          "is_host": false,
          "master_host_uids": [
            1759652656449688
          ]
        },
        "item": {
          "aha_image": [
            {
              "download_list": [
                {
                  "url": "https://p3-ppx.byteimg.com/img/tos-cn-i-0000/847cb942875b4042a3b125f507d17ece~tp…"
                }
              ],
              "height": 200,
              "is_gif": false,
              "uri": "tos-cn-i-0000/847cb942875b4042a3b125f507d17ece",
              "url_list": [
                {
                  "url": "https://p9-ppx.byteimg.com/img/tos-cn-i-0000/847cb942875b4042a3b125f507d17ece~c5…"
                }
              ],
              "width": 200
            }
          ],
          "ancestor_id": "7685342951509072138",
          "author": {
            "age": "36岁",
            "author_info": {
              "AuthorStatus": 1,
              "author_item_type": 1,
              "author_type": 104007473,
              "level": 0,
              "origin_status": 0,
              "owner": "script",
              "recommend_tag": "",
              "tags": []
            },
            "avatar": {
              "download_list": [
                {
                  "url": "https://p6-ppx-sign.byteimg.com/tos-cn-i-8gu37r9deh/ba804bc702db4d568d93d2ef2a8f…"
                }
              ],
              "height": 200,
              "is_gif": false,
              "uri": "tos-cn-i-8gu37r9deh/ba804bc702db4d568d93d2ef2a8f3c51",
              "url_list": [
                {
                  "url": "https://p9-ppx-sign.byteimg.com/tos-cn-i-8gu37r9deh/ba804bc702db4d568d93d2ef2a8f…"
                }
              ],
              "width": 200
            },
            "description": "那就这样皮一下吧！",
            "followers_count": 11363,
            "followings_count": 7,
            "gender": 0,
            "god_comment_count": 0
          },
          "author_tags": "36岁·白羊座",
          "can_download": true,
          "cell_ui_ctrl": {
            "show_author_tags": false
          },
          "comment_post_item": false,
          "content": "最像模仿者"
        },
        "last_view_time": 0,
        "pass_through": "{\"cell_id_str\":\"7685342951509072138\",\"cell_type\":\"1\"}",
        "stickup": false
      }
    ],
    "play_defer_time": 0,
    "play_sound": true,
    "tips": "有12条新内容",
    "video_aspect_ratio_style": 0
  },
  "message": "success",
  "prompt": "",
  "status_code": 0,
  "time": 1793691703827
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.cursor.has_more` | Shows whether another page of posts is available. |
| `data.cursor.loadmore_cursor` | Value to send as `cursor` to request the next page. |
| `data.data[].cell_id_str` | Post cell ID as a string. Use the string form, because the numeric `cell_id` is a very large integer. |
| `data.data[].display_time` | Time value attached to the post entry. It looks like a Unix timestamp in seconds. |
| `data.data[].city_name` | Location name shown with the post, for example `湖北`. |
| `data.data[].item.content` | Text of the post. |
| `data.data[].item.author.description` | Author's profile bio. |
| `data.data[].item.author.followers_count / data.data[].item.author.followings_count` | Number of accounts that follow the author, and number of accounts the author follows. |
| `data.data[].item.author_tags` | Short label shown with the author, such as age and zodiac sign. |
| `data.data[].hashtag.enter_num / data.data[].hashtag.followers_num` | Counts for the hashtag: `enter_num` is the number of entries or visits, and `followers_num` is the number of followers. |

### Notes

- Get `hashtag_id` from a Pipixia share link. If the link is shortened, convert it first with [Pipixia Short URL Conversion](/apis/pipixia/app/short-url).
- For the next page, pass `data.cursor.loadmore_cursor` as `cursor` and raise `feed_count` by 1.
- Image fields hold lists of URLs with `width` and `height`. The URLs in this response carry `x-expires` and `x-signature` query parameters.
- Call [Pipixia Hashtag Details](/apis/pipixia/app/hashtag-detail) for the hashtag profile on its own.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Pipixia Hashtag Details](/apis/pipixia/app/hashtag-detail): Retrieves metadata and profile assets for a specific Pipixia hashtag by its unique identifier.
- [Pipixia App Home Feed](/apis/pipixia/app/home-feed): Returns recommended posts from the Pipixia home feed.
- [Pipixia Home Short Drama Feed](/apis/pipixia/app/home-short-drama-feed): Returns short drama and novel recommendations from the Pipixia home feed.

---
Machine-readable: [`catalog/models/pipixia/app/hashtag-post-list.json`](../../../../catalog/models/pipixia/app/hashtag-post-list.json) · Store page: https://www.sandbase.ai/model/pipixia/app/hashtag-post-list
