# Douyin Content Categories API: pricing, parameters and code examples

`douyin/creator/creator-content-category` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the list of content categories available on Douyin. Authors and applications can review official topic classifications without requiring input parameters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/creator/creator-content-category"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/creator/creator-content-category', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/creator/creator-content-category", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/creator/creator-content-category", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/creator/creator-content-category` with the body above minus `model`.

## Details

Returns the course categories, selected course topics and hot course videos shown on the Douyin creator platform. The API takes no input parameters. Send an empty JSON object.

### Use cases

- Build a category picker from the course category tree for a creator education tool.
- Track which course topics have the highest `total_views` on the Douyin creator platform.
- List the top hot course videos with their captions and hashtags to see what Douyin promotes to creators.
- Collect category `id` values to use as input for a course lookup.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/creator/creator-content-category" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "activity_list": [],
  "banner_list": [],
  "course_category_list": [
    {
      "children": [
        {
          "children": null,
          "course_list": null,
          "cover_url": "",
          "create_time": 1657791417,
          "id": "184",
          "name": "视频创作",
          "tags": []
        }
      ],
      "course_list": null,
      "cover_url": "",
      "create_time": 1657791107,
      "id": "180",
      "name": "内容创作",
      "tags": []
    }
  ],
  "hot_items": [
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
  "selected_topics": [
    {
      "children": null,
      "course_list": null,
      "cover_url": "",
      "cover_urls": {
        "uri": "douyin-admin-obj/f31374b0793598e7af0bda8ceb2bd82c",
        "url_list": [
          "https://p26-sign.douyinpic.com/douyin-admin-obj/f31374b0793598e7af0bda8ceb2bd82c…"
        ]
      },
      "create_time": 1780544858,
      "id": "238",
      "name": "开启创作之旅",
      "tags": [
        "通用"
      ],
      "title": "开启创作之旅",
      "total_views": 5354833
    }
  ],
  "status_code": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `course_category_list[].id / course_category_list[].name` | ID and Chinese name of a top-level course category, such as `180` for 内容创作. |
| `course_category_list[].children[]` | Sub-categories under a top-level category. Each child has its own `id`, `name` and `create_time`. The `children` of a child is `null`. |
| `course_category_list[].create_time` | Unix timestamp in seconds for when the category was created. |
| `selected_topics[].id / selected_topics[].title` | ID and title of a selected course topic, such as 开启创作之旅. |
| `selected_topics[].tags` | Short labels for the topic, such as 通用 and a lesson count like `4讲`. |
| `selected_topics[].total_views` | View count for the selected topic. |
| `hot_items[].name / hot_items[].rank` | Title of a hot course video and its rank value. |
| `hot_items[].collected_count` | Number of times the hot item has been collected. |
| `hot_items[].item.aweme_id / hot_items[].item.caption` | ID and caption text of the video behind the hot item. |
| `hot_items[].item.cha_list[].cha_name` | Hashtag names attached to the hot video, with the hashtag ID in `cid`. |

### Notes

- Send `{}` as the request body. The API has no parameters.
- `activity_list` and `banner_list` were empty in the sample response.
- Timestamps such as `create_time` are Unix seconds. IDs are returned as strings.
- Pass a category `id` to [Douyin Creator Content Courses](/apis/douyin/creator/creator-content-course) to get the courses in that category.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Creator Activity Details](/apis/douyin/creator/creator-activity-detail): Returns detailed information for a specific Douyin creator activity.
- [Douyin Activity List](/apis/douyin/creator/creator-activity-list): Returns activity and campaign records for Douyin accounts within a specified timestamp window between start_time and end_time.
- [Douyin Creator Content Courses](/apis/douyin/creator/creator-content-course): Returns content development courses from the Douyin creator platform for a specified category.

---
Machine-readable: [`catalog/models/douyin/creator/creator-content-category.json`](../../../../catalog/models/douyin/creator/creator-content-category.json) · Store page: https://www.sandbase.ai/model/douyin/creator/creator-content-category
