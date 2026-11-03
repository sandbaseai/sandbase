# Douyin High Completion Rate Billboard API: pricing, parameters and code examples

`douyin/billboard/hot-total-high-play-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns Douyin billboard rankings for videos with high completion rates. Filter results by search keyword, category tags, time window, and pagination settings.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/billboard/hot-total-high-play-list"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/billboard/hot-total-high-play-list', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/billboard/hot-total-high-play-list", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/billboard/hot-total-high-play-list", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/billboard/hot-total-high-play-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number default `1` |
| `tags` | array |  | Sub-level vertical category tag, empty for all, multiple tags need to be passed in  |
| `keyword` | string |  | Search keyword to filter the billboard, empty for all default `""` |
| `page_size` | integer |  | Number of items per page default `10` |
| `date_window` | integer |  | Time window, 1 by hour 2 by day default `24` |

## Details

Returns a ranked list of Douyin videos from the high completion rate billboard. Every parameter is optional, so an empty request returns the first page of 10 items. You can narrow the list with `keyword`, `tags` and `date_window`.

### Use cases

- Find Douyin videos that hold viewers' attention within a niche by passing category `tags`.
- Compare creators of different sizes by checking `fans_cnt` against `play_cnt` and `like_rate` on ranked videos.
- Search the billboard with a `keyword` to see which videos on a topic rank highest.
- Collect video titles, cover images and durations to study what formats rank well.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/billboard/hot-total-high-play-list" \
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
| `tags` | array | No | Sub-level vertical category tag, empty for all, multiple tags need to be passed in |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "objs": [
      {
        "avatar_url": "https://p11.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-i-c9aec8xkvj_bcd40e4…",
        "fans_cnt": 3105051,
        "favorite_id": 0,
        "follow_cnt": 2023,
        "follow_rate": 0.000176,
        "image_cnt": 0,
        "is_favorite": false,
        "item_cover_url": "https://p3-sign.douyinpic.com/tos-cn-i-dy/0e589841a8d345298f6595376262a04f~tplv-…",
        "item_duration": 72122,
        "item_id": "7703456989958999305",
        "item_title": "偶遇“sha人魔”并用电动滑板“严肃逃跑”吗？！#离谱 #逃跑 #心脏 #细思极恐",
        "item_url": "https://v11-cold.douyinvod.com/0daacd73e14db63cbae04468889f1466/6ae99c3c/video/t…"
      }
    ],
    "page": {
      "page": 1,
      "page_size": 10,
      "total": 1000
    }
  },
  "extra": {
    "now": 1793691108000
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
| `data.objs[].score` | Ranking score of the video on this billboard. Higher scores appear to rank higher in the list. |
| `data.objs[].play_cnt / like_cnt` | Number of plays and likes on the video. |
| `data.objs[].like_rate / follow_rate` | Ratios of likes and of follows for the video, given as decimals (for example `0.059227`). |
| `data.objs[].fans_cnt / follow_cnt` | Follower count of the creator, and the follow count tied to the video. |
| `data.objs[].item_duration` | Length of the video as a number. The values look like milliseconds, for example `72122`. |
| `data.objs[].publish_time` | Unix timestamp in seconds for when the video was published. |
| `data.objs[].item_cover_url / item_url / avatar_url` | Links to the cover image, the video file and the creator avatar. |

### Notes

- Set `date_window` to `1` for an hourly window or `2` for a daily window. The schema default is `24`.
- Paginate with `page` and `page_size`. The response returns `data.page.page`, `data.page.page_size` and `data.page.total`.
- To get valid values for `tags`, call [Douyin Billboard Vertical Content Tags](/apis/douyin/billboard/content-tag).
- The `item_cover_url` links are signed and contain an `x-expires` value, so save the images soon after you fetch them.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Billboard City List](/apis/douyin/billboard/city-list): Returns the list of Chinese cities supported by Douyin billboard rankings.
- [Douyin Billboard Vertical Content Tags](/apis/douyin/billboard/content-tag): Returns a list of vertical content tags available on the Douyin billboard platform.
- [Douyin Fan Interest Account List](/apis/douyin/billboard/hot-account-fans-interest-account-list): Returns a list of 20 accounts that followers of a target creator are interested in on Douyin.

---
Machine-readable: [`catalog/models/douyin/billboard/hot-total-high-play-list.json`](../../../../catalog/models/douyin/billboard/hot-total-high-play-list.json) · Store page: https://www.sandbase.ai/model/douyin/billboard/hot-total-high-play-list
