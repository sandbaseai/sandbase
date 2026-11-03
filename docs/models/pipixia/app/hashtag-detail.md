# Pipixia Hashtag Details API: pricing, parameters and code examples

`pipixia/app/hashtag-detail` · data API · Pipixia · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Retrieves metadata and profile assets for a specific Pipixia hashtag by its unique identifier.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "pipixia/app/hashtag-detail", "hashtag_id": "129559"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('pipixia/app/hashtag-detail', {'hashtag_id': '129559'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("pipixia/app/hashtag-detail", {
  "hashtag_id": "129559"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "pipixia/app/hashtag-detail", sandbase.Params{
	"hashtag_id": "129559",
})
```

Same call via the path form: `POST /v1/api/pipixia/app/hashtag-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `hashtag_id` | string | yes | AKA hashtag id, can be obtained from the share link.  |

## Details

Returns details for one Pipixia hashtag, including its post and follower counts, cover images, category, and host users. It needs the `hashtag_id` of the hashtag.

### Use cases

- Track how many posts, followers and views a Pipixia hashtag has.
- Collect the cover image, avatars and category of a hashtag for a content catalog.
- Find the host users who manage a hashtag and read their profile counts.
- Check the dates of a hashtag campaign from its start and end timestamps.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/pipixia/app/hashtag-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"hashtag_id": "129559"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `hashtag_id` | string | Yes | AKA hashtag id, can be obtained from the share link. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "hashtag": {
      "background_image": null,
      "base_hashtag": {
        "action_end_time": 1591632000,
        "action_start_time": 1591027200,
        "activity_icon": {
          "color": "FFFF6880",
          "icon_image": {
            "download_list": [
              {
                "url": "https://p9-ppx-sign.byteimg.com/tos-cn-i-8gu37r9deh/428d745dce031ce630f5db129c6b…"
              }
            ],
            "height": 48,
            "is_gif": false,
            "uri": "tos-cn-i-8gu37r9deh/428d745dce031ce630f5db129c6bee23.png",
            "url_list": [
              {
                "url": "https://p9-ppx-sign.byteimg.com/tos-cn-i-8gu37r9deh/428d745dce031ce630f5db129c6b…"
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
                "url": "https://p6-ppx-sign.byteimg.com/tos-cn-i-0000/d0254823138a477c926601d7b7089da2~t…"
              }
            ],
            "height": 200,
            "is_gif": false,
            "uri": "tos-cn-i-0000/d0254823138a477c926601d7b7089da2",
            "url_list": [
              {
                "url": "https://p9-ppx-sign.byteimg.com/tos-cn-i-0000/d0254823138a477c926601d7b7089da2~t…"
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
        "boost_info": null,
        "category_list": [
          {
            "display_order": 1,
            "id": 58,
            "name": "影视娱乐"
          }
        ]
      },
      "display_tag": null,
      "display_tag_info": null,
      "enter_num": 21014838,
      "extra": null,
      "followers_num": 227536,
      "host_avatar": [],
      "host_user_ids": [
        1759652656449688
      ],
      "icon": null,
      "id_str": "129559",
      "intro": null
    },
    "host_list": [
      {
        "achievements": [],
        "age": "26岁",
        "article_count": 0,
        "authentication": null,
        "author_ecom_info": null,
        "author_info": null,
        "avatar": {
          "download_list": [
            {
              "url": "https://p3-ppx-sign.byteimg.com/tos-cn-i-8gu37r9deh/4a8a2d32d5d740a5b8497b36c7a0…"
            }
          ],
          "height": 200,
          "is_gif": false,
          "uri": "tos-cn-i-8gu37r9deh/4a8a2d32d5d740a5b8497b36c7a02cc2",
          "url_list": [
            {
              "url": "https://p3-ppx-sign.byteimg.com/tos-cn-i-8gu37r9deh/4a8a2d32d5d740a5b8497b36c7a0…"
            }
          ],
          "width": 200
        },
        "background": {
          "download_list": [],
          "height": 0,
          "is_gif": false,
          "uri": "",
          "url_list": [],
          "width": 0
        },
        "birthday": null,
        "broadcast_info": null,
        "certify_info": null,
        "city": "滁州"
      }
    ],
    "introduce": "话题大当家与二当家是官方在众多皮友中层层选拔出来，负责话题的内容建设、发掘优质帖子以及话题内氛围管理，初期在部分话题进行试点。主持人权力包括：1）将不符合条件的…",
    "leaderboard_info": {
      "day_board": null,
      "week_board": null
    },
    "popup": null,
    "related_hashtag": null,
    "signin_status": false,
    "top_items": []
  },
  "message": "success",
  "prompt": "",
  "status_code": 0,
  "time": 1793691701130
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.hashtag.id_str` | The hashtag ID as a string. It matches the `hashtag_id` you sent. |
| `data.hashtag.works_num` | Number of posts under the hashtag. |
| `data.hashtag.followers_num` | Number of users who follow the hashtag. |
| `data.hashtag.show_num / data.hashtag.enter_num` | Counters for the hashtag. `show_num` is much larger than `enter_num`. The response does not define either one, so check them against the Pipixia app. |
| `data.hashtag.base_hashtag.category_list[].name` | Category name of the hashtag, with its `id` and `display_order`. |
| `data.hashtag.base_hashtag.action_start_time / data.hashtag.base_hashtag.action_end_time` | Start and end of the hashtag activity, as Unix timestamps in seconds. |
| `data.hashtag.base_hashtag.background_image.url_list[].url` | Link to the hashtag background image, with `width` and `height` next to it. |
| `data.hashtag.base_hashtag.avatars[].url_list[].url` | Links to avatar images shown for the hashtag. |
| `data.hashtag.host_user_ids / data.hashtag.master_host_uids` | IDs of the users who host the hashtag. |
| `data.host_list[].followers_count / data.host_list[].like_count` | Follower and like totals for each host user. Each host also has `id_str`, `city` and `create_time`. |

### Notes

- Take `hashtag_id` from the hashtag share link. The `schema` field in the response also contains it as `hashtag_id=129559`.
- Image URLs are signed links and carry an `x-expires` value, so save the files if you need them long term.
- To read the posts under a hashtag, call [Pipixia Hashtag Post List](/apis/pipixia/app/hashtag-post-list).
- To get full profiles for the host users, call [Pipixia User Information](/apis/pipixia/app/user-info).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Pipixia Hashtag Post List](/apis/pipixia/app/hashtag-post-list): Returns a list of posts associated with a specific hashtag on Pipixia.
- [Pipixia App Home Feed](/apis/pipixia/app/home-feed): Returns recommended posts from the Pipixia home feed.
- [Pipixia Home Short Drama Feed](/apis/pipixia/app/home-short-drama-feed): Returns short drama and novel recommendations from the Pipixia home feed.

---
Machine-readable: [`catalog/models/pipixia/app/hashtag-detail.json`](../../../../catalog/models/pipixia/app/hashtag-detail.json) · Store page: https://www.sandbase.ai/model/pipixia/app/hashtag-detail
