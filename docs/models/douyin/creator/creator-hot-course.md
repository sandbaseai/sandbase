# Douyin Creator Hot Courses

`douyin/creator/creator-hot-course` · api · Douyin

Returns trending creator courses or curated topic lessons from Douyin. Results can be filtered by topic category and sorted by recommendation, popularity, or upload date.

## Pricing

- **$0.0015 per call** (USD)
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

Access popular Douyin creator academy courses and selected topic materials using `category_id` and custom sorting with `order`.

### Use cases

- Discover trending educational courses for Douyin creators.
- Sort instructional videos by popularity, upload date, or platform recommendations.
- Browse specialized creator curriculum tracks by topic category.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/creator/creator-hot-course" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `limit` | integer | No | Items per page (recommended 24, range 1-100) |
| `order` | integer | No | Order type (1=recommended order, 2=most popular, 3=latest upload) |
| `offset` | integer | No | Offset (starting position) |
| `category_id` | string | No | Selected topic category ID (empty for hot courses, specific ID for selected topics) |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "course_list": [
    {
      "collected_count": 12003,
      "id": "7529857225054063913",
      "name": "抖音精选优质内容指南",
      "rank": 1,
      "item": {
        "author_user_id": 92769419069,
        "aweme_id": "7529857225054063913",
        "aweme_type": 4,
        "caption": "抖音精选优质内容指南来啦～干货满满！从标准解读到作品解析，带你拆解抖音精选作品特征，期待更多好内容被看见～#抖音精选创作课",
        "category": 0,
        "create_time": 1753181521
      }
    }
  ]
}
```

### Notes

- Set `order` to 1 for recommended order, 2 for most popular, or 3 for latest upload.
- Leave `category_id` empty to retrieve general hot courses, or specify an ID for dedicated topics.
- Supports pagination via `limit` (1-100, recommended 24) and `offset`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Creator Activity Details](/model/douyin/creator/creator-activity-detail): Returns detailed information for a specific Douyin creator activity.
- [Douyin Activity List](/model/douyin/creator/creator-activity-list): Returns activity and campaign records for Douyin accounts within a specified timestamp window between start_time and end_time.
- [Douyin Content Categories](/model/douyin/creator/creator-content-category): Returns the list of content categories available on Douyin.

---
Machine-readable: [`catalog/models/douyin/creator/creator-hot-course.json`](../../../../catalog/models/douyin/creator/creator-hot-course.json) · Store page: https://www.sandbase.ai/model/douyin/creator/creator-hot-course
