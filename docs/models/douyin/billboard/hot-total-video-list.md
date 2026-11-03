# Douyin Hot Video Ranking API: pricing, parameters and code examples

`douyin/billboard/hot-total-video-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get Douyin hot video rankings: overall hot videos, low-follower breakouts, high completion, follower growth and like-rate lists, with play, like and follower stats, filters by category and time window.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/billboard/hot-total-video-list", "keyword": "", "page": 20, "page_size": 50, "sub_type": 1001, "tags": []}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/billboard/hot-total-video-list', {'keyword': '', 'page': 20, 'page_size': 50, 'sub_type': 1001, 'tags': []})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/billboard/hot-total-video-list", {
  "keyword": "",
  "page": 20,
  "page_size": 50,
  "sub_type": 1001,
  "tags": []
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/billboard/hot-total-video-list", sandbase.Params{
	"keyword": "",
	"page": 20,
	"page_size": 50,
	"sub_type": 1001,
	"tags": []any{},
})
```

Same call via the path form: `POST /v1/api/douyin/billboard/hot-total-video-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number default `1` |
| `tags` | array |  | Sub-level vertical category tag, empty for all, multiple tags need to be passed in  |
| `keyword` | string |  | Search keyword to filter the billboard, empty for all default `""` |
| `sub_type` | integer |  | List category, 1001 Video total list 1002 Low fan explosion 1003 High completion rate 1004 High fan growth rate 1005 High like rate default `1001` |
| `page_size` | integer |  | Number of items per page default `10` |
| `date_window` | integer |  | Time window, 1 by hour 2 by day default `24` |

## Details

Returns a ranked list of hot Douyin videos from the billboard. Each item has play, like and follower stats for the video and its creator. All inputs are optional. Use `sub_type` to pick the list and `date_window` to pick the time window.

### Use cases

- Track which videos lead the overall Douyin hot list right now.
- Find videos from small creators that reach high play counts by switching `sub_type` to `1002`.
- Compare `like_rate` and `follow_rate` across videos to see which content turns views into likes and new followers.
- Pull a keyword or category filtered list to see which videos lead in a niche.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/billboard/hot-total-video-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `date_window` | integer | No | Time window, 1 by hour 2 by day |
| `keyword` | string | No | Search keyword to filter the billboard, empty for all |
| `page` | integer | No | Page number |
| `page_size` | integer | No | Number of items per page |
| `sub_type` | integer | No | List category, 1001 Video total list 1002 Low fan explosion 1003 High completion rate 1004 High fan growth rate 1005 High like rate |
| `tags` | array | No | Sub-level vertical category tag, empty for all, multiple tags need to be passed in |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "objs": [
      {
        "avatar_url": "https://p3.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-i-0813_okXaKjzBEfAYIO…",
        "fans_cnt": 16669,
        "favorite_id": 0,
        "follow_cnt": 6810,
        "follow_rate": 0.000148,
        "image_cnt": 0,
        "is_favorite": false,
        "item_cover_url": "https://p9-sign.douyinpic.com/tos-cn-i-0813c000-ce/o0sEAmqIkvtD3C5awhnaGfEdFAA9D…",
        "item_duration": 19434,
        "item_id": "7702397404621350821",
        "item_title": "哈哈哈病人有活的风险吗#运动会封神现场 #医学生 #医学生接力赛 #药学院",
        "item_url": "https://v5-coldp.douyinvod.com/506f005831394f7cc7b8fe459c6c7cdd/6ae99c09/video/t…"
      }
    ],
    "page": {
      "page": 1,
      "page_size": 10,
      "total": 1000
    }
  },
  "extra": {
    "now": 1793691110000
  },
  "message": ""
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.objs[].item_id` | ID of the video, returned as a string. |
| `data.objs[].item_title` | Video caption, including its hashtags. |
| `data.objs[].nick_name` | Display name of the creator who posted the video. |
| `data.objs[].play_cnt / like_cnt` | Play count and like count of the video. |
| `data.objs[].like_rate / follow_rate` | Ratios for the video. `like_rate` matches `like_cnt` divided by `play_cnt` in the sample. `follow_rate` is a small decimal that relates to follower gain. |
| `data.objs[].fans_cnt` | Follower count of the creator. |
| `data.objs[].score` | Ranking score of the video on the list. |
| `data.objs[].publish_time` | Publish time of the video as a Unix timestamp in seconds. |
| `data.objs[].item_duration` | Video length. The value is likely in milliseconds, for example `19434`. |
| `data.objs[].item_cover_url / avatar_url / item_url` | Links to the cover image, the creator avatar and the video file. |
| `data.page.page / page_size / total` | Current page number, items per page and total number of items in the list. |

### Notes

- Pass `page` and `page_size` to move through the list. The sample shows `total` as `1000`.
- `sub_type` values: `1001` overall, `1002` low-follower breakouts, `1003` high completion, `1004` high follower growth, `1005` high like rate.
- `date_window` takes `1` for by hour and `2` for by day.
- To fill `tags`, call [Douyin Billboard Vertical Content Tags](/apis/douyin/billboard/content-tag) to look up the vertical category tags.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Fetch Chinese city list](/apis/douyin/billboard/city-list): Get city list.
- [Fetch vertical content tags](/apis/douyin/billboard/content-tag): Get vertical content tags.
- [Fetch fan interest author 20 users](/apis/douyin/billboard/hot-account-fans-interest-account-list): Get the fan interest author 20 users.

---
Machine-readable: [`catalog/models/douyin/billboard/hot-total-video-list.json`](../../../../catalog/models/douyin/billboard/hot-total-video-list.json) · Store page: https://www.sandbase.ai/model/douyin/billboard/hot-total-video-list
