# Pipixia Hot Search Board Detail API: pricing, parameters and code examples

`pipixia/app/hot-search-board-detail` · data API · Pipixia · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed items from a Pipixia hot search board, including item identifiers, like metrics, and highlighted comments for a specified board type.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "pipixia/app/hot-search-board-detail", "block_type": 12}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('pipixia/app/hot-search-board-detail', {'block_type': 12})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("pipixia/app/hot-search-board-detail", {
  "block_type": 12
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "pipixia/app/hot-search-board-detail", sandbase.Params{
	"block_type": 12,
})
```

Same call via the path form: `POST /v1/api/pipixia/app/hot-search-board-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `block_type` | integer | yes | Board type, can be obtained from the `/fetch_hot_search_board_list` interface.  |

## Details

Returns the ranked items of one Pipixia hot search board. Each entry holds the post, its author, a highlighted comment and a daily like count. The only input is the `block_type` of the board.

### Use cases

- Track which posts rank on the Pipixia god comment board (`title` is 神评热榜 for `block_type` 12).
- Compare `today_digg_num` across ranked posts to see which entries gain the most likes in a day.
- Collect cover images, durations and author details of top-ranked videos for a content review.
- Read the highlighted comment's `city_name` to see where top commenters are located.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/pipixia/app/hot-search-board-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"block_type": 12}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `block_type` | integer | Yes | Board type, can be obtained from the `/fetch_hot_search_board_list` interface. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "board": {
      "background_image": null,
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
                  "icon": "https://p9-ppx-sign.byteimg.com/tos-cn-i-8gu37r9deh/b8ef7242b919a026896beb32e0ea…",
                  "schema": "bds://webview?url=https%3A%2F%2Fi.snssdk.com%2Fbds_web%2Ffalcon%2Fbds_channel%2F…"
                }
              ],
              "age": "24岁",
              "author_info": null,
              "avatar": {
                "download_list": [
                  {
                    "url": "https://p9-ppx-sign.byteimg.com/tos-cn-i-8gu37r9deh/12fea765adb6482cb4b861a994fd…"
                  }
                ],
                "height": 200,
                "is_gif": false,
                "uri": "tos-cn-i-8gu37r9deh/12fea765adb6482cb4b861a994fd2ebc",
                "url_list": [
                  {
                    "url": "https://p3-ppx-sign.byteimg.com/tos-cn-i-8gu37r9deh/12fea765adb6482cb4b861a994fd…"
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
                  "url": "https://p9-ppx-sign.byteimg.com/tos-cn-p-0076/e0db9a5ec44348a2ad5b5ccf775c199f_1…"
                }
              ],
              "height": 1280,
              "is_gif": false,
              "uri": "tos-cn-p-0076/e0db9a5ec44348a2ad5b5ccf775c199f_1793411019",
              "url_list": [
                {
                  "url": "https://p3-ppx-sign.byteimg.com/tos-cn-p-0076/e0db9a5ec44348a2ad5b5ccf775c199f_1…"
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
      "board_push": false,
      "cell_list": null,
      "has_more_schema": "bds://webview?url=https%3A%2F%2Fapi.ribaoapi.com%2Ftool%2Fsentry%2Fcomment-board…",
      "has_more_text": "完整榜单",
      "layout": null
    }
  },
  "message": "success",
  "prompt": "",
  "status_code": 0,
  "time": 1793691708079
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.board.title` | Display name of the board. For `block_type` 12 it is 神评热榜. |
| `data.board.board_items[]` | Ranked entries on the board, in list order. |
| `data.board.board_items[].today_digg_num` | Like count shown for the entry today. |
| `data.board.board_items[].item_info` | Short label that explains the count, for example 今日神评点赞. |
| `data.board.board_items[].item.content` | Text of the post. It can be an empty string. |
| `data.board.board_items[].item.create_time / data.board.board_items[].item.duration` | Post creation time as a Unix timestamp in seconds, and the video length (a decimal number, such as 8.9). |
| `data.board.board_items[].item.cover.url_list[].url` | Cover image URL of the post. `width` and `height` sit next to the list. |
| `data.board.board_items[].item.author.avatar.url_list[].url` | Avatar image URL of the post author. |
| `data.board.board_items[].item.author.age / data.board.board_items[].item.author.certify_info.description` | Author age text and, when present, a certification description such as a creator domain. |
| `data.board.board_items[].god_comment.city_name` | Region name attached to the highlighted comment. |

### Notes

- Get valid `block_type` values from [Pipixia Hot Search](/apis/pipixia/app/hot-search-board-list).
- The response has no pagination parameters. `data.board.has_more_text` and `has_more_schema` point to the full board in the app.
- Image URLs are signed and carry an `x-expires` query value, so save the files if you need them later.
- To get more detail on a ranked post, call [Pipixia Post Detail](/apis/pipixia/app/post-detail).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Pipixia Hashtag Details](/apis/pipixia/app/hashtag-detail): Retrieves metadata and profile assets for a specific Pipixia hashtag by its unique identifier.
- [Pipixia Hashtag Post List](/apis/pipixia/app/hashtag-post-list): Returns a list of posts associated with a specific hashtag on Pipixia.
- [Pipixia App Home Feed](/apis/pipixia/app/home-feed): Returns recommended posts from the Pipixia home feed.

---
Machine-readable: [`catalog/models/pipixia/app/hot-search-board-detail.json`](../../../../catalog/models/pipixia/app/hot-search-board-detail.json) · Store page: https://www.sandbase.ai/model/pipixia/app/hot-search-board-detail
