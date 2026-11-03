# Pipixia App Home Feed API: pricing, parameters and code examples

`pipixia/app/home-feed` · data API · Pipixia · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns recommended posts from the Pipixia home feed. Supports cursor-based pagination to browse subsequent pages of feed items.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "pipixia/app/home-feed"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('pipixia/app/home-feed', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("pipixia/app/home-feed", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "pipixia/app/home-feed", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/pipixia/app/home-feed` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Page cursor, default is 0, get the corresponding value from the `loadmore_cursor` Key in the previous page. default `"0"` |

## Details

Returns a page of recommended posts from the Pipixia home feed. Each entry holds the post text, author details, hashtag data and image links. The only input is an optional `cursor`, which defaults to `0` for the first page.

### Use cases

- Collect recommended Pipixia posts and their text for content analysis.
- Track which hashtags appear in the home feed and how many people have entered them.
- Build a list of authors that Pipixia recommends, with their follower counts and certification labels.
- Page through the feed over repeated calls to build a larger sample of posts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/pipixia/app/home-feed" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | string | No | Page cursor, default is 0, get the corresponding value from the `loadmore_cursor` Key in the previous page. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "cursor": {
      "feed_len": 0,
      "has_more": true,
      "loadmore_cursor": 1793691694783,
      "refresh_cursor": 1793691705783
    },
    "data": [
      {
        "cell_id": 7674408936241371432,
        "cell_id_str": "7674408936241371432",
        "cell_type": 1,
        "city_name": "广东",
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
                  "url": "https://p6-ppx-sign.byteimg.com/tos-cn-i-0000/8e60799021a94ccfbdf49e44225f94e6~t…"
                }
              ],
              "width": 69
            },
            "option_id": 0
          }
        ],
        "display_time": 1786837572,
        "hashtag": {
          "base_hashtag": {
            "action_end_time": 0,
            "action_start_time": 0,
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
              "name": "福州"
            },
            "atmosphere": "皮友正在讨论",
            "avatars": [
              {
                "download_list": [
                  {
                    "url": "https://p3-ppx-sign.byteimg.com/tos-cn-i-0000/7b05eac20b164c4ea3aa3af5b9921dc6~t…"
                  }
                ],
                "height": 200,
                "is_gif": false,
                "uri": "tos-cn-i-0000/7b05eac20b164c4ea3aa3af5b9921dc6",
                "url_list": [
                  {
                    "url": "https://p9-ppx-sign.byteimg.com/tos-cn-i-0000/7b05eac20b164c4ea3aa3af5b9921dc6~t…"
                  }
                ],
                "width": 200
              }
            ],
            "background_image": {
              "download_list": [
                {
                  "url": "https://p9-ppx-sign.byteimg.com/tos-cn-i-8gu37r9deh/oAdcnt7DAn1cAQfI0CekA3FngKCI…"
                }
              ],
              "height": 340,
              "is_gif": false,
              "uri": "tos-cn-i-8gu37r9deh/oAdcnt7DAn1cAQfI0CekA3FngKCIAAScbmrEIZ",
              "url_list": [
                {
                  "url": "https://p3-ppx-sign.byteimg.com/tos-cn-i-8gu37r9deh/oAdcnt7DAn1cAQfI0CekA3FngKCI…"
                }
              ],
              "width": 750
            },
            "category_list": [
              {
                "display_order": 1,
                "id": 34,
                "name": "同城生活"
              }
            ],
            "create_time": 1689153268
          },
          "enter_num": 2543819,
          "followers_num": 2508,
          "host_user_ids": [
            562585424656391
          ],
          "id_str": "156277",
          "is_follow": false,
          "is_host": false,
          "master_host_uids": [
            562585424656391
          ]
        },
        "item": {
          "aha_image": [
            {
              "download_list": [
                {
                  "url": "https://p9-ppx.byteimg.com/img/tos-cn-i-0000/ed3016f26d4a4abd86c38074eb0a4470~tp…"
                }
              ],
              "height": 200,
              "is_gif": false,
              "uri": "tos-cn-i-0000/ed3016f26d4a4abd86c38074eb0a4470",
              "url_list": [
                {
                  "url": "https://p9-ppx.byteimg.com/img/tos-cn-i-0000/ed3016f26d4a4abd86c38074eb0a4470~c5…"
                }
              ],
              "width": 200
            }
          ],
          "ancestor_id": "7674408936241371432",
          "author": {
            "achievements": [
              {
                "achieve_id": 0,
                "achieve_type": 1,
                "description": "590条神评",
                "icon": "https://p3-ppx-sign.byteimg.com/tos-cn-i-8gu37r9deh/b8ef7242b919a026896beb32e0ea…",
                "schema": "bds://webview?url=https%3A%2F%2Fi.snssdk.com%2Fbds_web%2Ffalcon%2Fbds_channel%2F…"
              }
            ],
            "age": "",
            "author_info": {
              "AuthorStatus": 1,
              "author_item_type": 1,
              "author_type": 9,
              "level": 3,
              "origin_status": 0,
              "owner": "script",
              "recommend_tag": "",
              "tags": [
                {
                  "description": "",
                  "id": 104007571,
                  "name": ""
                }
              ]
            },
            "avatar": {
              "download_list": [
                {
                  "url": "https://p3-ppx-sign.byteimg.com/tos-cn-i-8gu37r9deh/46dc6c16ff4a477cb0226b72b719…"
                }
              ],
              "height": 200,
              "is_gif": false,
              "uri": "tos-cn-i-8gu37r9deh/46dc6c16ff4a477cb0226b72b7191812",
              "url_list": [
                {
                  "url": "https://p9-ppx-sign.byteimg.com/tos-cn-i-8gu37r9deh/46dc6c16ff4a477cb0226b72b719…"
                }
              ],
              "width": 200
            },
            "certify_info": {
              "certify_type": 3,
              "description": "皮皮虾游戏领域创作者"
            },
            "commerce_permission_list": [
              8
            ],
            "description": "不是本人",
            "followers_count": 28098
          },
          "author_tags": "不是本人",
          "can_download": true,
          "cell_ui_ctrl": {
            "show_author_tags": false
          },
          "comment_post_item": false,
          "content": "怀疑男生都喜欢这种"
        },
        "last_view_time": 0,
        "pass_through": "{\"cell_id_str\":\"7674408936241371432\",\"cell_type\":\"1\"}",
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
  "time": 1793691705783
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.cursor.loadmore_cursor` | Value to pass as `cursor` to load the next page. |
| `data.cursor.has_more` | Shows whether more feed items are available after this page. |
| `data.data[].cell_id_str` | Feed cell ID as a string. The numeric `cell_id` holds the same value. |
| `data.data[].item.content` | Text of the post. |
| `data.data[].item.author.description / data.data[].item.author.followers_count` | Author bio and number of followers. |
| `data.data[].item.author.certify_info.description` | Certification label shown for the author, such as a creator title. |
| `data.data[].city_name` | Region name attached to the post, such as `广东` or `北京`. |
| `data.data[].display_time` | Time the cell is displayed, as a Unix timestamp in seconds. |
| `data.data[].hashtag.base_hashtag.activity_icon.name` | Name of the hashtag linked to the post. |
| `data.data[].hashtag.enter_num / data.data[].hashtag.followers_num` | Counts for the hashtag: `enter_num` is the number of entries and `followers_num` is the number of followers. |

### Notes

- Leave `cursor` out or send `0` for the first page. For later pages, send the `data.cursor.loadmore_cursor` value from the previous response.
- The hashtag `id_str` can be used with [Pipixia Hashtag Details](/apis/pipixia/app/hashtag-detail) or [Pipixia Hashtag Post List](/apis/pipixia/app/hashtag-post-list).
- Image URLs in the response include `x-expires` and `x-signature` query values, so save the images soon if you need them.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Pipixia Hashtag Details](/apis/pipixia/app/hashtag-detail): Retrieves metadata and profile assets for a specific Pipixia hashtag by its unique identifier.
- [Pipixia Hashtag Post List](/apis/pipixia/app/hashtag-post-list): Returns a list of posts associated with a specific hashtag on Pipixia.
- [Pipixia Home Short Drama Feed](/apis/pipixia/app/home-short-drama-feed): Returns short drama and novel recommendations from the Pipixia home feed.

---
Machine-readable: [`catalog/models/pipixia/app/home-feed.json`](../../../../catalog/models/pipixia/app/home-feed.json) · Store page: https://www.sandbase.ai/model/pipixia/app/home-feed
