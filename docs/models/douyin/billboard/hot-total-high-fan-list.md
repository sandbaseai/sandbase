# Douyin High Fan Rate Billboard API: pricing, parameters and code examples

`douyin/billboard/hot-total-high-fan-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns Douyin billboard rankings for content with high follower conversion rates, filterable by keyword, category tags, and time window.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/billboard/hot-total-high-fan-list"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/billboard/hot-total-high-fan-list', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/billboard/hot-total-high-fan-list", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/billboard/hot-total-high-fan-list", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/billboard/hot-total-high-fan-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number default `1` |
| `tags` | array |  | Sub-level vertical category tag, empty for all, multiple tags need to be passed in  |
| `keyword` | string |  | Search keyword to filter the billboard, empty for all default `""` |
| `page_size` | integer |  | Number of items per page default `10` |
| `date_window` | integer |  | Time window, 1 by hour 2 by day default `24` |

## Details

Returns a ranked list of Douyin videos and image posts that gained many followers relative to their reach. You can filter by `keyword`, `tags` and `date_window`, and all inputs are optional.

### Use cases

- Find Douyin posts that turn viewers into followers, so you can study what they do differently.
- Compare `follow_rate` across posts from small and large accounts to spot creators who grow fast.
- Narrow the ranking to one vertical with `tags` to see which posts convert best in a niche.
- Switch `date_window` between hourly and daily views to see which posts keep their follower gains.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/billboard/hot-total-high-fan-list" \
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
        "avatar_url": "https://p11.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-avt-0015_533b01a13d6…",
        "fans_cnt": 79,
        "favorite_id": 0,
        "follow_cnt": 5082,
        "follow_rate": 0.016043,
        "image_cnt": 1,
        "is_favorite": false,
        "item_cover_url": "https://p5-ex-gddgtc-sign.douyinpic.com/tos-cn-i-0813c000-ce/o4D5AeGVQEw3iIE6if9…",
        "item_duration": 0,
        "item_id": "7700288074861283185",
        "item_title": "@点贊接单（流量扶持） 抖音推流的核心规则，看懂少踩坑 1️⃣ 只有观众在推荐页刷到你的视频，自愿看完、点赞评论，才算有效互动，能助推继续推流。 2️⃣ 自己刷…",
        "item_url": "https://sf6-cdn-tos.douyinstatic.com/obj/ies-music/7655350214760352566.mp3"
      }
    ],
    "page": {
      "page": 1,
      "page_size": 10,
      "total": 1000
    }
  },
  "extra": {
    "now": 1793691107000
  },
  "message": ""
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.objs[].item_id` | ID of the post, given as a string. |
| `data.objs[].item_title` | Caption text of the post, which may be cut off and may include hashtags and @mentions. |
| `data.objs[].nick_name / data.objs[].avatar_url` | Display name and avatar image link of the account that published the post. |
| `data.objs[].fans_cnt` | Follower count of the publishing account. |
| `data.objs[].follow_cnt` | Number of follows linked to this post. |
| `data.objs[].follow_rate` | Follow conversion ratio for the post, as a decimal. For example, `0.016043` is about 1.6%. This is the value the billboard is built around. |
| `data.objs[].play_cnt / data.objs[].like_cnt` | Play count and like count of the post. |
| `data.objs[].like_rate` | Like ratio for the post, as a decimal. |
| `data.objs[].publish_time` | Publish time of the post as a Unix timestamp in seconds. |
| `data.objs[].media_type / data.objs[].image_cnt / data.objs[].item_duration` | Type of the post, the number of images, and its duration. Image posts show `item_duration` as `0`. |
| `data.page.total` | Total number of items in the billboard for the current filters. |

### Notes

- Page through results with `page` and `page_size`. The response echoes both values in `data.page`.
- `date_window` takes `1` for hourly or `2` for daily. The schema default is `24`.
- To fill `tags`, get the category values from [Douyin Billboard Vertical Content Tags](/apis/douyin/billboard/content-tag).
- `extra.now` is the server time in milliseconds. `publish_time` is in seconds.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Billboard City List](/apis/douyin/billboard/city-list): Returns the list of Chinese cities supported by Douyin billboard rankings.
- [Douyin Billboard Vertical Content Tags](/apis/douyin/billboard/content-tag): Returns a list of vertical content tags available on the Douyin billboard platform.
- [Douyin Fan Interest Account List](/apis/douyin/billboard/hot-account-fans-interest-account-list): Returns a list of 20 accounts that followers of a target creator are interested in on Douyin.

---
Machine-readable: [`catalog/models/douyin/billboard/hot-total-high-fan-list.json`](../../../../catalog/models/douyin/billboard/hot-total-high-fan-list.json) · Store page: https://www.sandbase.ai/model/douyin/billboard/hot-total-high-fan-list
