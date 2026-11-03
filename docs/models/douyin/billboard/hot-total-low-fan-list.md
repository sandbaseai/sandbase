# Douyin Low Fan Billboard Items API: pricing, parameters and code examples

`douyin/billboard/hot-total-low-fan-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns viral Douyin videos produced by creators with low follower counts. Filter results by search keyword, category tags, time window, and pagination.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/billboard/hot-total-low-fan-list"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/billboard/hot-total-low-fan-list', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/billboard/hot-total-low-fan-list", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/billboard/hot-total-low-fan-list", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/billboard/hot-total-low-fan-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number default `1` |
| `tags` | array |  | Sub-level vertical category tag, empty for all, multiple tags need to be passed in  |
| `keyword` | string |  | Search keyword to filter the billboard, empty for all default `""` |
| `page_size` | integer |  | Number of items per page default `10` |
| `date_window` | integer |  | Time window, 1 by hour 2 by day default `24` |

## Details

Returns a ranked list of viral Douyin videos posted by creators with low follower counts. Each item has video stats, creator stats, and a score. All inputs are optional: `keyword`, `tags`, `date_window`, `page` and `page_size`.

### Use cases

- Find breakout Douyin videos from small accounts before they reach larger audiences.
- Compare `fans_cnt` with `play_cnt` to spot videos that reached far beyond the creator's follower base.
- Filter by `keyword` or `tags` to study what works for small creators in one niche.
- Pull the list on a schedule to track which small creators keep appearing in the ranking.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/billboard/hot-total-low-fan-list" \
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
        "avatar_url": "https://p26.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-i-0813_okXaKjzBEfAYI…",
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
        "item_url": "https://v5-coldp.douyinvod.com/b20f1ef856812fc9ca2548b94908e3b6/6ae99c08/video/t…"
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
| `data.objs[].item_id` | ID of the video, as a string. |
| `data.objs[].item_title` | Video caption, including hashtags. |
| `data.objs[].nick_name` | Display name of the creator. |
| `data.objs[].fans_cnt / follow_cnt` | Follower count of the creator, and the number of accounts the creator follows. |
| `data.objs[].play_cnt / like_cnt` | Total plays and likes of the video. |
| `data.objs[].like_rate / follow_rate` | Ratios for the video. `like_rate` matches `like_cnt` divided by `play_cnt`. `follow_rate` is a small decimal that appears to be follower gain relative to plays. |
| `data.objs[].score` | Ranking score of the item. Higher values rank higher in the sample. |
| `data.objs[].publish_time` | Publish time as a Unix timestamp in seconds. |
| `data.objs[].item_cover_url / item_url` | Link to the cover image, and link to the media file. For audio-only items, `item_url` points to an mp3 file. |
| `data.objs[].media_type / item_duration / image_cnt` | Numeric media type code, the duration value of the item, and the number of images. `item_duration` is `0` for the image item in the sample. |
| `data.page.total` | Total number of items in the result set. |

### Notes

- Send an empty body `{}` to get the first page with defaults: `page` 1, `page_size` 10 and `date_window` 24.
- Use `page` and `page_size` to move through results. The response `data.page` echoes `page`, `page_size` and `total`.
- Set `date_window` to `1` for hourly or `2` for daily, as described in the parameter docs.
- To find values for `tags`, call [Douyin Billboard Vertical Content Tags](/apis/douyin/billboard/content-tag).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Billboard City List](/apis/douyin/billboard/city-list): Returns the list of Chinese cities supported by Douyin billboard rankings.
- [Douyin Billboard Vertical Content Tags](/apis/douyin/billboard/content-tag): Returns a list of vertical content tags available on the Douyin billboard platform.
- [Douyin Fan Interest Account List](/apis/douyin/billboard/hot-account-fans-interest-account-list): Returns a list of 20 accounts that followers of a target creator are interested in on Douyin.

---
Machine-readable: [`catalog/models/douyin/billboard/hot-total-low-fan-list.json`](../../../../catalog/models/douyin/billboard/hot-total-low-fan-list.json) · Store page: https://www.sandbase.ai/model/douyin/billboard/hot-total-low-fan-list
