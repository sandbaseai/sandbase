# Weibo Hot Search Categories API: pricing, parameters and code examples

`weibo/app/hot-search-categories` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns all available hot search categories from Weibo. Enables browsing trending topics segmented by specific Weibo category classifications.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/app/hot-search-categories"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/app/hot-search-categories', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/app/hot-search-categories", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/app/hot-search-categories", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/weibo/app/hot-search-categories` with the body above minus `model`.

## Details

Returns a set of Weibo hot search ranking categories in one response, keyed by category name. Each category holds its own ranked list, such as anime, games, toys, actors and brand rankings by industry. The API takes no input.

### Use cases

- Pull the weekly brand rankings for industries like appliances, beauty, cars and luxury to compare brand buzz on Weibo.
- Track the top anime, games and toys listed on Weibo with their scores and manufacturers.
- Monitor which actors rank highest by `hot_num` and see their recent heat trend from `chart`.
- List the category keys in `data` to build a category picker for a Weibo trends dashboard.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/app/hot-search-categories" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "acgnAnimation": {
      "rank_data": [
        {
          "desc": "《名侦探柯南》是日本知名漫画家青山刚昌创作的侦探推理漫画，其动画片自 1996 年起开播。",
          "detail_url": "sinaweibo://wbox?id=d7m0w4ekto&page=pages/details/details&item_id=201",
          "evaluation_score": "9.2",
          "icon": "https://mu1.sinaimg.cn/original/weiyinyue.music.sina.com.cn/weibo_media_admin/ad…",
          "id": 238318,
          "item_id": 201,
          "name": "名侦探柯南",
          "rank": 1
        }
      ],
      "rank_url": "sinaweibo://wbox?id=d7m0w4ekto&theme_id=1&type=2"
    },
    "acgnGame": {
      "current": "1",
      "list": [
        {
          "best_selling_val": null,
          "detail_url": "https://m.weibo.cn/c/wbox?id=twxpgvrllf&page=pages/detail/detail&gid=1037",
          "game_score": "8.2",
          "gid": 1037,
          "icon": "https://imgstar.weibo.com/export/vmeeting/300ea7d784df685973ce8e31f031220b.jpg",
          "id": 221623,
          "manufacturer": "腾讯",
          "name": "王者荣耀"
        }
      ],
      "rank_url": "https://m.weibo.cn/c/wbox?id=twxpgvrllf&page=pages/rank/rank",
      "total": "235"
    },
    "acgnToy": {
      "rank_data": [
        {
          "detail_url": "sinaweibo://wbox?id=d7m0w4ekto&page=pages/details/details&item_id=506",
          "icon": "https://mu1.sinaimg.cn/original/weiyinyue.music.sina.com.cn/weibo_media_admin/ad…",
          "id": 238818,
          "item_id": 506,
          "manufacturer_name": "TNT SPACE",
          "name": "ANMOO",
          "rank": 1,
          "rank_type": 1
        }
      ],
      "rank_url": "sinaweibo://wbox?id=d7m0w4ekto&theme_id=1&type=5"
    },
    "actor": {
      "list": [
        {
          "active_num": 6,
          "all_discuss_num": 60610,
          "avatar": "https://tvax2.sinaimg.cn/crop.261.201.600.600.1024/6ade4348ly8ge5avdm8jbj20u00u0…",
          "chart": [
            {
              "dt": "202611031430",
              "value": "6027"
            }
          ],
          "discuss_num": 35,
          "gender": 1,
          "hot_num": 70130000,
          "is_new_1y": 0
        }
      ],
      "rank_scheme": ""
    },
    "babymother": null,
    "beauty": null,
    "car": null,
    "cei_appliances": {
      "industry_code": "appliances",
      "industry_name": "家电",
      "list": [
        {
          "brand_avatar": "https://tvax2.sinaimg.cn/crop.0.0.1080.1080.1024/6d314616ly8i73g9thdwqj20u00u0dg…",
          "brand_name": "格力",
          "brand_uid": "1831945750",
          "id": 1220953,
          "index_value": 65060010,
          "last_index_value": 12766703,
          "last_sort": 19,
          "sort": 1
        }
      ],
      "ranking_time": "2026W43",
      "scheme": "",
      "time_type": "week"
    },
    "cei_beauty": {
      "industry_code": "beauty",
      "industry_name": "美妆",
      "list": [
        {
          "brand_avatar": "https://tvax1.sinaimg.cn/crop.0.0.960.960.1024/67436eebly8hzod0nk4mlj20qo0qowf0.…",
          "brand_name": "巴黎欧莱雅",
          "brand_uid": "1732472555",
          "id": 1228331,
          "index_value": 61564615,
          "last_index_value": 61701353,
          "last_sort": 1,
          "sort": 1
        }
      ],
      "ranking_time": "2026W43",
      "scheme": "",
      "time_type": "week"
    },
    "cei_car": {
      "industry_code": "car",
      "industry_name": "汽车",
      "list": [
        {
          "brand_avatar": "https://tvax4.sinaimg.cn/crop.0.0.600.600.1024/006y8J29ly8h3d87kj93mj30go0goaa4.…",
          "brand_name": "理想汽车",
          "brand_uid": "6001272153",
          "id": 1232501,
          "index_value": 86695959,
          "last_index_value": 28312658,
          "last_sort": 8,
          "sort": 1
        }
      ],
      "ranking_time": "2026W43",
      "scheme": "",
      "time_type": "week"
    },
    "cei_clothing": {
      "industry_code": "clothing",
      "industry_name": "运动鞋服",
      "list": [
        {
          "brand_avatar": "https://tvax1.sinaimg.cn/crop.133.133.333.333.1024/6b9e9ce0ly8fwtinl57h3j20go0go…",
          "brand_name": "斐乐",
          "brand_uid": "1805556960",
          "id": 1218871,
          "index_value": 65829440,
          "last_index_value": 33546281,
          "last_sort": 5,
          "sort": 1
        }
      ],
      "ranking_time": "2026W43",
      "scheme": "",
      "time_type": "week"
    },
    "cei_dairy": null
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.acgnAnimation.rank_data[].name / rank` | Anime title and its position in the anime ranking. |
| `data.acgnAnimation.rank_data[].evaluation_score` | Score for the anime, given as a string such as `9.2`. |
| `data.acgnGame.list[].name / manufacturer / game_score` | Game name, its maker, and its score as a string. |
| `data.acgnGame.total` | Total number of games in the game category, as a string. |
| `data.acgnToy.rank_data[].name / manufacturer_name / rank` | Toy name, its maker, and its rank. |
| `data.actor.list[].hot_num` | Heat value for the actor. Higher values appear first in the sample. |
| `data.actor.list[].chart[].dt / value` | Time series points. `dt` looks like `202611031430` (year, month, day, hour, minute) and `value` is the reading at that time. |
| `data.cei_appliances.list[].brand_name / brand_uid` | Brand name and its Weibo user ID in a brand ranking. The same shape appears in the other `cei_` categories. |
| `data.cei_appliances.list[].index_value / sort` | Brand index value for the period and the brand's rank this period. |
| `data.cei_appliances.list[].last_index_value / last_sort` | Index value and rank from the previous period, for comparison. |

### Notes

- Categories with no data come back as `null`, for example `babymother`, `beauty`, `car` and `cei_dairy`. Check for `null` before reading them.
- The `cei_` categories carry `industry_code`, `industry_name`, `time_type` and `ranking_time`. In the sample, `time_type` is `week` and `ranking_time` is `2026W43`.
- Links such as `detail_url` and `rank_url` use either the `sinaweibo://` app scheme or `https://m.weibo.cn` addresses.
- For live hot search topics, call [Weibo Hot Search Rankings](/apis/weibo/app/hot-search).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Weibo App AI Smart Search](/apis/weibo/app/ai-smart-search): Returns AI smart search channel results and feed metadata from Weibo for a specified keyword query, with optional page-based pagination.
- [Weibo Home Recommend Feed](/apis/weibo/app/home-recommend-feed): Returns recommended feed items from the Weibo app homepage, with options to paginate and specify the number of items per request.
- [Weibo Hot Search Rankings](/apis/weibo/app/hot-search): Returns current Weibo hot search rankings across various categories.

---
Machine-readable: [`catalog/models/weibo/app/hot-search-categories.json`](../../../../catalog/models/weibo/app/hot-search-categories.json) · Store page: https://www.sandbase.ai/model/weibo/app/hot-search-categories
