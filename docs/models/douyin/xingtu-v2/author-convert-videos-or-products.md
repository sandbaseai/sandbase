# Douyin Xingtu Creator Conversion Details API: pricing, parameters and code examples

`douyin/xingtu-v2/author-convert-videos-or-products` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Returns conversion details for a creator's videos or associated products on Douyin Xingtu. Filter by creator ID, item type, time range tier, and industry category.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/author-convert-videos-or-products", "o_author_id": "7589271892177518598"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/author-convert-videos-or-products', {'o_author_id': '7589271892177518598'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/author-convert-videos-or-products", {
  "o_author_id": "7589271892177518598"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/author-convert-videos-or-products", sandbase.Params{
	"o_author_id": "7589271892177518598",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/author-convert-videos-or-products` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number, default 1  |
| `time_range` | integer |  | Time range tier, default 2  |
| `detail_type` | integer |  | Detail type, 1=videos, 2=products, default 1  |
| `industry_id` | integer |  | Industry ID, 0=unlimited, default 0  |
| `o_author_id` | string | yes | Creator ID  |
| `platform_source` | integer |  | Platform source, default 1  |
| `platform_channel` | integer |  | Platform channel, default 1  |

## Details

Returns conversion details for one creator on Douyin Xingtu. With `detail_type` set to `1` (the default) it lists the creator's videos with click, sales and engagement stats. With `2` it lists associated products. The only required input is the creator ID in `o_author_id`.

### Use cases

- Check which of a creator's videos drove component clicks and sales before booking a campaign.
- Compare click rate and watch counts across a creator's videos to find the strongest sales content.
- Filter a creator's results by `industry_id` to see conversion in one product category.
- Page through the full list of converted videos for a creator and save it for reporting.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/author-convert-videos-or-products" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"o_author_id": "7589271892177518598"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `o_author_id` | string | Yes | Creator ID |
| `detail_type` | integer | No | Detail type, 1=videos, 2=products, default 1 |
| `industry_id` | integer | No | Industry ID, 0=unlimited, default 0 |
| `page` | integer | No | Page number, default 1 |
| `platform_channel` | integer | No | Platform channel, default 1 |
| `platform_source` | integer | No | Platform source, default 1 |
| `time_range` | integer | No | Time range tier, default 2 |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "base_resp": {
    "status_code": 0,
    "status_message": ""
  },
  "pagination": {
    "has_more": false,
    "limit": 10,
    "page": 1,
    "total_count": 1
  },
  "video_list": [
    {
      "click_rate": 0.0095,
      "component_click_cnt": "2",
      "gpm": "0",
      "gpm_range": "0",
      "industry_id": 1901,
      "item_pay_amt": "0",
      "item_pay_amt_range": "0",
      "item_stats": {
        "author_id": "1113181577281568",
        "cover_uri": "tos-cn-i-dy/ebbf065864914a1e8aa0768fb2a44a0b",
        "create_time": "1792826328",
        "duration": 100.101,
        "id": "7700087804163853610",
        "stats": {
          "avg_watch_dura": "0",
          "comment_cnt": "59",
          "favorite_cnt": "32",
          "finish_rate": 0.0055,
          "interact_rate": 0.00240234896343091,
          "like_cnt": "282",
          "share_cnt": "10",
          "watch_cnt": "146107"
        },
        "title": "预估到手2219起 蚂蚁电竞 ANT272ZQE镜面屏来了 #京东1111电脑抢先购#电脑以旧换新#蚂蚁电竞ANT272ZQE#显示器推荐",
        "url": "https://www.iesdouyin.com/share/video/7700087804163853610/?region=CN&mid=7700087…"
      },
      "prod_list": []
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `video_list[].item_stats.id` | ID of the video, as a string. |
| `video_list[].item_stats.title` | Video caption, including its hashtags. |
| `video_list[].item_stats.url` | Share link to the video on Douyin. |
| `video_list[].item_stats.create_time` | Video creation time as a Unix timestamp in seconds, returned as a string. |
| `video_list[].click_rate / video_list[].component_click_cnt` | Click rate of the video and the number of clicks on its attached component. Both come from the video's conversion record. |
| `video_list[].gpm / video_list[].item_pay_amt` | Sales figures for the video, returned as strings. Both are `0` in this example. |
| `video_list[].industry_id` | ID of the industry category the video is tied to. |
| `video_list[].item_stats.stats.watch_cnt` | Number of views of the video. |
| `video_list[].item_stats.stats.like_cnt / video_list[].item_stats.stats.comment_cnt / video_list[].item_stats.stats.share_cnt / video_list[].item_stats.stats.favorite_cnt` | Counts of likes, comments, shares and favorites on the video. |
| `video_list[].item_stats.stats.finish_rate / video_list[].item_stats.stats.interact_rate` | Completion rate and interaction rate of the video, as decimal fractions. |
| `pagination.has_more / pagination.total_count` | Whether another page exists and the total number of records. |

### Notes

- Pass the creator's Xingtu ID as `o_author_id`. If you only have a Douyin ID, call [Douyin XingTu kolId by Douyin ID](/apis/douyin/xingtu-v2/xingtu-kolid-by-unique-id) first.
- Use `page` to move through results. `pagination.limit` was `10` in the example, and `has_more` tells you when to stop.
- `prod_list` is an empty list inside each video entry in this example. Set `detail_type` to `2` to get product details.
- For a summary score instead of per-item rows, see [Douyin Xingtu Author Conversion Ability](/apis/douyin/xingtu-v2/author-convert-ability).

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/apis/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/apis/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/author-convert-videos-or-products.json`](../../../../catalog/models/douyin/xingtu-v2/author-convert-videos-or-products.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/author-convert-videos-or-products
