# Douyin Creator Content Courses API: pricing, parameters and code examples

`douyin/creator/creator-content-course` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns content development courses from the Douyin creator platform for a specified category. Results can be sorted by recommendation, popularity, or upload date.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/creator/creator-content-course", "category_id": 1}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/creator/creator-content-course', {'category_id': 1})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/creator/creator-content-course", {
  "category_id": 1
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/creator/creator-content-course", sandbase.Params{
	"category_id": 1,
})
```

Same call via the path form: `POST /v1/api/douyin/creator/creator-content-course` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Items per page (recommended 24, range 1-100) range 1–100 |
| `order` | integer |  | Order type (1=recommended order, 2=most popular, 3=latest upload)  |
| `offset` | integer |  | Offset (starting position) range 0– |
| `category_id` | integer | yes | Category ID (for more category IDs, please refer to the content creation category interface)  |

## Details

Returns a page of content creation courses from the Douyin creator platform for one category. The only required input is `category_id`. You can sort the list and page through it with `order`, `limit` and `offset`.

### Use cases

- Build a catalog of Douyin creator tutorials for one topic category.
- Rank courses by `collected_count` to find the tutorials creators save most.
- Pull the newest uploads with `order` set to `3` to track new course releases.
- Export course titles, captions and cover images into a learning directory.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/creator/creator-content-course" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"category_id": 180}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `category_id` | integer | Yes | Category ID (for more category IDs, please refer to the content creation category interface) |
| `limit` | integer | No | Items per page (recommended 24, range 1-100) |
| `offset` | integer | No | Offset (starting position) |
| `order` | integer | No | Order type (1=recommended order, 2=most popular, 3=latest upload) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "category_name": "",
  "course_list": [
    {
      "collected_count": 8669,
      "hot_order": 0,
      "id": "7034444962406075679",
      "is_collected": false,
      "item": {
        "Cover": {
          "height": 960,
          "uri": "tos-cn-i-dy/913a59dbc568443ead25ffa95e2c8cc6",
          "url_list": [
            "https://p26-sign.douyinpic.com/tos-cn-i-dy/913a59dbc568443ead25ffa95e2c8cc6~tplv…"
          ],
          "width": 540
        },
        "author": {
          "avatar_larger": {
            "uri": "1080x1080/aweme-avatar/tos-cn-avt-0015_3beaaeb52d39e341205653ab779a6e5b",
            "url_list": [
              "https://p3.douyinpic.com/aweme/1080x1080/aweme-avatar/tos-cn-avt-0015_3beaaeb52d…"
            ]
          },
          "avatar_medium": {
            "uri": "720x720/aweme-avatar/tos-cn-avt-0015_3beaaeb52d39e341205653ab779a6e5b",
            "url_list": [
              "https://p3.douyinpic.com/aweme/720x720/aweme-avatar/tos-cn-avt-0015_3beaaeb52d39…"
            ]
          },
          "avatar_thumb": {
            "uri": "100x100/aweme-avatar/tos-cn-avt-0015_3beaaeb52d39e341205653ab779a6e5b",
            "url_list": [
              "https://p3.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-avt-0015_3beaaeb52d39…"
            ]
          },
          "birthday": "***",
          "card_entries": null,
          "followers_detail": null,
          "geofencing": null,
          "mix_info": null
        },
        "author_user_id": 92769419069,
        "aweme_id": "7034444962406075679",
        "aweme_type": 4,
        "caption": "",
        "category": 0,
        "cha_list": [
          {
            "cha_name": "抖音创作者学习中心",
            "cid": "1701253626367048",
            "connect_music": null,
            "cover_item": {
              "uri": "douyin-admin-obj/9fcacc744a1287879b360c63a44a7792",
              "url_list": [
                "https://p26-sign.douyinpic.com/douyin-admin-obj/9fcacc744a1287879b360c63a44a7792…"
              ]
            },
            "desc": "",
            "hash_tag_profile": "douyin-admin-obj/9fcacc744a1287879b360c63a44a7792",
            "is_commerce": false,
            "type": 2
          }
        ]
      },
      "name": "抖音玩法之发光文字卡点教程#抖音创作者学习中心  #剪映模板 @吴莱",
      "offset": 0,
      "rank": 1
    }
  ],
  "has_more": 1,
  "offset": 24,
  "selected_topic_categories": null,
  "status_code": 0,
  "total": 319
}
```

### Response fields

| Field | Meaning |
|---|---|
| `course_list[].id / course_list[].item.aweme_id` | ID of the course video. In the sample response both values are the same string. |
| `course_list[].name` | Course title. |
| `course_list[].collected_count` | Number of times users saved the course. `is_collected` shows whether the current account saved it. |
| `course_list[].rank / course_list[].hot_order` | Position values for the course in the list. `hot_order` is `0` or `1` in the sample. |
| `course_list[].item.caption` | Caption text of the course video. It can be empty. |
| `course_list[].item.Cover.url_list` | Cover image URLs for the course video, with `width` and `height` of the image. |
| `course_list[].item.author_user_id` | Numeric ID of the account that published the course. |
| `course_list[].item.cha_list[].cha_name` | Name of a hashtag attached to the course, such as a learning center tag. |
| `has_more` | Shows `1` when more results remain after this page. |
| `total` | Total number of courses in the category. The sample shows `319`. |

### Notes

- Get `category_id` values from [Douyin Content Categories](/apis/douyin/creator/creator-content-category).
- For the next page, send the `offset` value returned in the response. The sample returned `24`. Keep going while `has_more` is `1`.
- `order` accepts `1` (recommended), `2` (most popular) or `3` (latest upload). `limit` accepts `1` to `100`.
- Cover image URLs carry an `x-expires` value in the query string, so fetch them soon after you call the API. For trending courses, see [Douyin Creator Hot Courses](/apis/douyin/creator/creator-hot-course).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Creator Activity Details](/apis/douyin/creator/creator-activity-detail): Returns detailed information for a specific Douyin creator activity.
- [Douyin Activity List](/apis/douyin/creator/creator-activity-list): Returns activity and campaign records for Douyin accounts within a specified timestamp window between start_time and end_time.
- [Douyin Content Categories](/apis/douyin/creator/creator-content-category): Returns the list of content categories available on Douyin.

---
Machine-readable: [`catalog/models/douyin/creator/creator-content-course.json`](../../../../catalog/models/douyin/creator/creator-content-course.json) · Store page: https://www.sandbase.ai/model/douyin/creator/creator-content-course
