# Douyin Creator Hot Courses API: pricing, parameters and code examples

`douyin/creator/creator-hot-course` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns trending creator courses or curated topic lessons from Douyin. Results can be filtered by topic category and sorted by recommendation, popularity, or upload date.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/creator/creator-hot-course", "limit": 24, "offset": 0, "order": 1}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/creator/creator-hot-course', {'limit': 24, 'offset': 0, 'order': 1})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/creator/creator-hot-course", {
  "limit": 24,
  "offset": 0,
  "order": 1
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/creator/creator-hot-course", sandbase.Params{
	"limit": 24,
	"offset": 0,
	"order": 1,
})
```

Same call via the path form: `POST /v1/api/douyin/creator/creator-hot-course` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Items per page (recommended 24, range 1-100) default `24`; range 1–100 |
| `order` | integer |  | Order type (1=recommended order, 2=most popular, 3=latest upload) default `1` |
| `offset` | integer |  | Offset (starting position) default `0`; range 0– |
| `category_id` |  |  | Selected topic category ID (empty for hot courses, specific ID for selected topics)  |

## Details

Returns a page of trending creator courses from Douyin, or curated topic lessons when you pass a topic category. Each course is a video with its title, caption, cover image, author and hashtags. The request needs no input, and you can add `category_id`, `order`, `limit` and `offset`.

### Use cases

- Track which creator lessons Douyin ranks highest right now.
- Compare courses by `collected_count` to see which lessons creators save most.
- Pull the hashtags attached to each course to find the topics Douyin promotes to creators.
- Build a reading list of lessons for one topic category, sorted by popularity or upload date.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/creator/creator-hot-course" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `category_id` | string | No | Selected topic category ID (empty for hot courses, specific ID for selected topics) |
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
      "collected_count": 12051,
      "hot_order": 1,
      "id": "7529857225054063913",
      "is_collected": false,
      "item": {
        "Cover": {
          "height": 720,
          "uri": "tos-cn-i-dy/8c62d3d8585c40cab3a6b72b31218a4a",
          "url_list": [
            "https://p26-sign.douyinpic.com/tos-cn-i-dy/8c62d3d8585c40cab3a6b72b31218a4a~tplv…"
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
        "aweme_id": "7529857225054063913",
        "aweme_type": 4,
        "caption": "抖音精选优质内容指南来啦～干货满满！从标准解读到作品解析，带你拆解抖音精选作品特征，期待更多好内容被看见～#抖音精选创作课",
        "category": 0,
        "cha_list": [
          {
            "cha_name": "抖音精选创作课",
            "cid": "7431072586374580243",
            "connect_music": null,
            "cover_item": {
              "uri": "",
              "url_list": []
            },
            "desc": "",
            "hash_tag_profile": "",
            "is_commerce": false,
            "type": 1
          }
        ]
      },
      "name": "抖音精选优质内容指南",
      "offset": 0,
      "rank": 1
    }
  ],
  "has_more": 1,
  "offset": 24,
  "selected_topic_categories": null,
  "status_code": 0,
  "total": 33
}
```

### Response fields

| Field | Meaning |
|---|---|
| `course_list[].id / course_list[].item.aweme_id` | ID of the course. In this response both values are the same string, and `item.aweme_id` is the ID of the video behind the course. |
| `course_list[].name` | Title of the course. |
| `course_list[].rank / course_list[].hot_order` | Position values for the course in the list. `rank` differs between items, while `hot_order` is 1 for all three items shown. |
| `course_list[].collected_count` | Number of times the course has been collected (saved). |
| `course_list[].is_collected` | Boolean flag. It is `false` in this response. |
| `course_list[].item.caption` | Caption text of the course video, including its hashtags. |
| `course_list[].item.Cover.url_list` | Links to the cover image of the course video. `width` and `height` give its size. |
| `course_list[].item.cha_list[].cha_name / course_list[].item.cha_list[].cid` | Name and ID of each hashtag (challenge) attached to the course video. |
| `course_list[].item.author_user_id` | Numeric ID of the account that published the course. |
| `has_more / offset / total` | Paging values. `has_more` is 1 when more results exist, `offset` is the next start position, and `total` is the number of courses available. |

### Notes

- Use the `offset` value from the response as the `offset` of your next request to get the next page. Stop when `has_more` is not 1.
- Leave `category_id` empty for hot courses. Pass a topic category ID to get selected topics. The [Douyin Content Categories](/apis/douyin/creator/creator-content-category) API lists Douyin content categories.
- `order` takes 1 for recommended, 2 for most popular and 3 for latest upload.
- `aweme_id` values are strings. Pass them to [Douyin Single Video Details](/apis/douyin/app-v3/one-video) to get full video data.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Creator Activity Details](/apis/douyin/creator/creator-activity-detail): Returns detailed information for a specific Douyin creator activity.
- [Douyin Activity List](/apis/douyin/creator/creator-activity-list): Returns activity and campaign records for Douyin accounts within a specified timestamp window between start_time and end_time.
- [Douyin Content Categories](/apis/douyin/creator/creator-content-category): Returns the list of content categories available on Douyin.

---
Machine-readable: [`catalog/models/douyin/creator/creator-hot-course.json`](../../../../catalog/models/douyin/creator/creator-hot-course.json) · Store page: https://www.sandbase.ai/model/douyin/creator/creator-hot-course
