# Pipixia Hot Search API: pricing, parameters and code examples

`pipixia/app/hot-search-board-list` · data API · Pipixia · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get the Pipixia hot search boards: trending posts with daily likes and top comments.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "pipixia/app/hot-search-board-list"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('pipixia/app/hot-search-board-list', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("pipixia/app/hot-search-board-list", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "pipixia/app/hot-search-board-list", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/pipixia/app/hot-search-board-list` with the body above minus `model`.

## Details

Returns the current Pipixia hot boards. Each board lists trending posts with the author, cover image, duration and a daily stat such as likes or plays. The request takes no input parameters.

### Use cases

- Track which posts lead the comment board each day by comparing `today_digg_num` across items.
- Build a daily digest of the most played videos using `today_show_num` and the post `content`.
- Collect cover images and author details of trending posts for a content mood board.
- Find the regions where top comments come from using `god_comment.city_name`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/pipixia/app/hot-search-board-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "boards": [
      {
        "background_image": {
          "download_list": null,
          "height": 192,
          "is_gif": false,
          "uri": "tos-cn-i-0000/ec1b306b701d48a0a6960124a86cb2b0",
          "url_list": [
            {
              "url": "https://p3-ppx-sign.byteimg.com/tos-cn-i-0000/ec1b306b701d48a0a6960124a86cb2b0~t…"
            }
          ],
          "width": 340
        },
        "block_event_name": null,
        "block_id": 0,
        "block_tag": null,
        "block_tail_type": 0,
        "block_type": 12,
        "board_items": [
          {
            "god_comment": {
              "alias_item_id": null,
              "author_display_tags": null,
              "bds_origin_type": 1,
              "bury_count": -1,
              "can_delete": false,
              "can_download": true,
              "city_name": "江苏",
              "click_tag": null
            },
            "item": {
              "author": {
                "achievements": [
                  {
                    "achieve_id": 0,
                    "achieve_type": 1,
                    "description": "29条神评",
                    "icon": "https://p6-ppx-sign.byteimg.com/tos-cn-i-8gu37r9deh/b8ef7242b919a026896beb32e0ea…",
                    "schema": "bds://webview?url=https%3A%2F%2Fi.snssdk.com%2Fbds_web%2Ffalcon%2Fbds_channel%2F…"
                  }
                ],
                "age": "24岁",
                "author_info": null,
                "avatar": {
                  "download_list": [
                    {
                      "url": "https://p3-ppx-sign.byteimg.com/tos-cn-i-8gu37r9deh/12fea765adb6482cb4b861a994fd…"
                    }
                  ],
                  "height": 200,
                  "is_gif": false,
                  "uri": "tos-cn-i-8gu37r9deh/12fea765adb6482cb4b861a994fd2ebc",
                  "url_list": [
                    {
                      "url": "https://p6-ppx-sign.byteimg.com/tos-cn-i-8gu37r9deh/12fea765adb6482cb4b861a994fd…"
                    }
                  ],
                  "width": 200
                },
                "broadcast_info": null,
                "certify_info": null,
                "commerce_permission_list": null,
                "creative_level_info": null
              },
              "can_download": true,
              "content": "“都说知足常乐 可我想要的不止这些”",
              "cover": {
                "download_list": [
                  {
                    "url": "https://p3-ppx-sign.byteimg.com/tos-cn-p-0076/e0db9a5ec44348a2ad5b5ccf775c199f_1…"
                  }
                ],
                "height": 1280,
                "is_gif": false,
                "uri": "tos-cn-p-0076/e0db9a5ec44348a2ad5b5ccf775c199f_1793411019",
                "url_list": [
                  {
                    "url": "https://p6-ppx-sign.byteimg.com/tos-cn-p-0076/e0db9a5ec44348a2ad5b5ccf775c199f_1…"
                  }
                ],
                "width": 720
              },
              "create_time": 1793411001,
              "default_schema": null,
              "drainage_info": null,
              "duration": 8.9
            },
            "item_info": "今日神评点赞",
            "today_digg_num": 1915,
            "today_show_num": null
          }
        ],
        "board_push": null,
        "cell_list": null,
        "has_more_schema": "bds://webview?hide_bar=1&hide_status_bar=1&hide_status_bar_icon=1&transparent_bg…",
        "has_more_text": "完整榜单",
        "layout": null
      }
    ],
    "popular_boards": null
  },
  "message": "success",
  "prompt": "",
  "status_code": 0,
  "time": 1793691709951
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.boards[].title` | Name of the board, for example `神评热榜`. |
| `data.boards[].update_title` | Short label that says how often the board updates, for example `每日更新`. |
| `data.boards[].board_items[].item_info` | Label that says what the daily number on the item means, for example `今日神评点赞` or `今日播放`. |
| `data.boards[].board_items[].today_digg_num / today_show_num` | Daily like count or daily play count for the item. Only one is filled per item, the other is `null`. |
| `data.boards[].board_items[].item.content` | Text of the post. It can be an empty string. |
| `data.boards[].board_items[].item.create_time` | Creation time of the post as a Unix timestamp in seconds. |
| `data.boards[].board_items[].item.duration` | Length of the post video. The values look like seconds. |
| `data.boards[].board_items[].item.cover.url_list[].url` | Signed URL of the cover image. `width` and `height` sit next to it. |
| `data.boards[].board_items[].item.author.age / data.boards[].board_items[].item.author.achievements[].description` | Author age label and badges such as `29条神评`. Both can be empty. |
| `data.boards[].board_items[].god_comment.city_name` | Region name tied to the top comment. `god_comment` is `null` on boards that do not show comments. |

### Notes

- The API takes no parameters. Send an empty JSON object `{}`.
- Image URLs are signed and carry an `x-expires` value, so download them soon after the call.
- Each board has `has_more_schema` and `has_more_text` for the full list. For board items beyond this preview, try [Pipixia Hot Search Board Detail](/apis/pipixia/app/hot-search-board-detail).
- For trending search terms instead of posts, use [Pipixia Hot Search Words](/apis/pipixia/app/hot-search-words).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Pipixia Search](/apis/pipixia/app/search): Search Pipixia (ByteDance humor community) by keyword across posts, videos, images, users and hashtags.
- [Get hashtag detail](/apis/pipixia/app/hashtag-detail): Get hashtag detail data.
- [Get hashtag post list](/apis/pipixia/app/hashtag-post-list): Get hashtag post list data.

---
Machine-readable: [`catalog/models/pipixia/app/hot-search-board-list.json`](../../../../catalog/models/pipixia/app/hot-search-board-list.json) · Store page: https://www.sandbase.ai/model/pipixia/app/hot-search-board-list
