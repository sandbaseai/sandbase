# Douyin High Like Rate Billboard API: pricing, parameters and code examples

`douyin/billboard/hot-total-high-like-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns trending Douyin videos ranked by high like rates. Filter results by category tags, search keywords, time windows, and pagination parameters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/billboard/hot-total-high-like-list"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/billboard/hot-total-high-like-list', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/billboard/hot-total-high-like-list", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/billboard/hot-total-high-like-list", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/billboard/hot-total-high-like-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number default `1` |
| `tags` | array |  | Sub-level vertical category tag, empty for all, multiple tags need to be passed in  |
| `keyword` | string |  | Search keyword to filter the billboard, empty for all default `""` |
| `page_size` | integer |  | Number of items per page default `10` |
| `date_window` | integer |  | Time window, 1 by hour 2 by day default `24` |

## Details

Returns a ranked list of Douyin videos on the high like rate billboard. Each item includes the video, its author, and engagement counts. All inputs are optional, so an empty request returns the first page of the billboard.

### Use cases

- Find Douyin videos that earn many likes relative to their plays.
- Track which creators with small follower counts get strong engagement.
- Filter the billboard by `keyword` or `tags` to study one content niche.
- Compare the same ranking over an hourly and a daily window with `date_window`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/billboard/hot-total-high-like-list" \
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
        "item_url": "https://v11-cold.douyinvod.com/e1c70a0a849acb06512bb2ab740e61ba/6ae99c3d/video/t…"
      }
    ],
    "page": {
      "page": 1,
      "page_size": 10,
      "total": 1000
    }
  },
  "extra": {
    "now": 1793691109000
  },
  "message": ""
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.objs[].item_id` | ID of the video, as a string. |
| `data.objs[].item_title` | Video caption, including its hashtags. |
| `data.objs[].like_cnt / play_cnt` | Number of likes and number of plays for the video. |
| `data.objs[].like_rate` | Likes divided by plays, as a decimal. For example, `0.059227` is about 5.9%. |
| `data.objs[].score` | Ranking score for the video on this billboard. |
| `data.objs[].nick_name` | Display name of the author. |
| `data.objs[].fans_cnt / follow_cnt` | Follower count of the author and the `follow_cnt` count for the video's author. |
| `data.objs[].follow_rate` | Follow rate for the video, as a decimal. |
| `data.objs[].publish_time` | Publish time of the video as a Unix timestamp in seconds. |
| `data.objs[].item_duration` | Length of the video. The values look like milliseconds. |
| `data.page.total` | Total number of items in the billboard for the current filters. |

### Notes

- Use `page` and `page_size` to paginate. The response echoes them in `data.page.page` and `data.page.page_size`.
- `date_window` takes `1` for hourly or `2` for daily, per the parameter description.
- To get values for `tags`, call [Douyin Billboard Vertical Content Tags](/apis/douyin/billboard/content-tag).
- `item_cover_url` and `item_url` are signed links that carry an expiry in the URL, so save the media soon after you fetch it.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Billboard City List](/apis/douyin/billboard/city-list): Returns the list of Chinese cities supported by Douyin billboard rankings.
- [Douyin Billboard Vertical Content Tags](/apis/douyin/billboard/content-tag): Returns a list of vertical content tags available on the Douyin billboard platform.
- [Douyin Fan Interest Account List](/apis/douyin/billboard/hot-account-fans-interest-account-list): Returns a list of 20 accounts that followers of a target creator are interested in on Douyin.

---
Machine-readable: [`catalog/models/douyin/billboard/hot-total-high-like-list.json`](../../../../catalog/models/douyin/billboard/hot-total-high-like-list.json) · Store page: https://www.sandbase.ai/model/douyin/billboard/hot-total-high-like-list
