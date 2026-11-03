# Douyin Xingtu Conversion Resources API: pricing, parameters and code examples

`douyin/xingtu-v3/data-sp-author-convert-videos-or-products` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

List Douyin Creator Marketplace (Xingtu) conversion-related videos or products for a creator, with industry, period, resource-type, and page filters. Use it to review commerce examples before creator selection.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v3/data-sp-author-convert-videos-or-products", "oAuthorId": "6870161898013196295"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v3/data-sp-author-convert-videos-or-products', {'oAuthorId': '6870161898013196295'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v3/data-sp-author-convert-videos-or-products", {
  "oAuthorId": "6870161898013196295"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v3/data-sp-author-convert-videos-or-products", sandbase.Params{
	"oAuthorId": "6870161898013196295",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v3/data-sp-author-convert-videos-or-products` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number. default `1` |
| `range` | string |  | Time range. one of: `DAY_30`, `DAY_90`; default `"DAY_30"` |
| `platform` | string |  | Platform type. one of: `SHORT_VIDEO`, `LIVE_STREAMING`, `PICTURE_TEXT`, `SHORT_DRAMA`; default `"SHORT_VIDEO"` |
| `oAuthorId` | string | yes | Author's unique ID.  |
| `detailType` | string |  | Resource type. one of: `VIDEO`, `PRODUCT`; default `"VIDEO"` |
| `industryId` | string |  | Industry category. one of: `ALL`, `ELECTRONICS_AND_APPLIANCES`, `SHOPPING`, `FOOD_AND_BEVERAGE`, `CLOTHING_AND_ACCESSORIES`, `HEALTHCARE_AND_MEDICAL`, `MEDICAL_INSTITUTIONS`, `HOME_AND_BUILDING_MATERIALS`, `LOCAL_SERVICES`, `BUSINESS_SERVICES`, `CULTURE_SPORTS_ENTERTAINMENT`, `BEAUTY_SERVICES` …; default `"ALL"` |

## Details

Returns the videos or products linked to a creator's commerce results on Douyin Creator Marketplace (Xingtu). It needs the creator's `oAuthorId`. You can filter by platform type, industry, time range and resource type.

### Use cases

- Check which videos a creator used to sell products before you book them.
- Compare a creator's commerce video views and engagement across industries with `industryId`.
- Switch `detailType` to `PRODUCT` to see the products tied to the creator's sales.
- Compare the `DAY_30` and `DAY_90` windows to see how recent commerce work differs from the longer period.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v3/data-sp-author-convert-videos-or-products" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"oAuthorId": "6870161898013196295"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `oAuthorId` | string | Yes | Author's unique ID. |
| `detailType` | string | No | Resource type. |
| `industryId` | string | No | Industry category. |
| `page` | integer | No | Page number. |
| `platform` | string | No | Platform type. |
| `range` | string | No | Time range. |

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
      "click_rate": 0,
      "component_click_cnt": "0",
      "gpm": "0",
      "gpm_range": "0",
      "industry_id": 1930,
      "item_pay_amt": "0",
      "item_pay_amt_range": "0",
      "item_stats": {
        "author_id": "66598046050",
        "cover_uri": "tos-cn-i-dy/64c6cb23275c44adba8a6f1dfbbe1525",
        "create_time": "1793421043",
        "duration": 235.034,
        "id": "7702648112405384486",
        "stats": {
          "avg_watch_dura": "0",
          "comment_cnt": "84",
          "favorite_cnt": "33086",
          "finish_rate": 0.0056,
          "interact_rate": 0.01983214632537254,
          "like_cnt": "429130",
          "share_cnt": "42867",
          "watch_cnt": "23803828"
        },
        "title": "只用清水洗脸、缺乏护肤知识、选护肤品犯难……困扰不少男士的护肤难题如何解？秋冬时节，跟着总台主持人杨帆学护肤小技巧，一起长知识！#海洋至尊",
        "url": "https://www.iesdouyin.com/share/video/7702648112405384486/?region=CN&mid=7702648…"
      },
      "prod_list": []
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `video_list[]` | One commerce-related video record. Each entry holds sales figures, the video details in `item_stats`, and a product list in `prod_list`. |
| `video_list[].gpm / gpm_range` | GPM value for the video and its range value. Both are strings, and both are `0` in this sample. |
| `video_list[].item_pay_amt / item_pay_amt_range` | Payment amount tied to the video and its range value. Both are strings, and both are `0` in this sample. |
| `video_list[].click_rate / component_click_cnt` | Click rate and click count for the video's commerce component. |
| `video_list[].industry_id` | Numeric ID of the industry the video belongs to. |
| `video_list[].prod_list` | Products linked to the video. It is an empty list in this sample. |
| `video_list[].item_stats.title / url` | Video title with its hashtags, and a share link to the video. |
| `video_list[].item_stats.id / author_id / create_time / duration` | Video ID, creator ID, creation time as a Unix timestamp string, and video length as a number. |
| `video_list[].item_stats.stats.watch_cnt / like_cnt / comment_cnt / share_cnt / favorite_cnt` | Counts of views, likes, comments, shares and favorites for the video. |
| `video_list[].item_stats.stats.finish_rate / interact_rate / avg_watch_dura` | Completion rate, interaction rate and average watch duration. |

### Notes

- `oAuthorId` is the only required parameter. Defaults are `platform=SHORT_VIDEO`, `industryId=ALL`, `range=DAY_30` and `detailType=VIDEO`.
- Page through results with `page`. The `pagination` object returns `page`, `limit`, `total_count` and `has_more`.
- Most counts and amounts come back as strings, so convert them to numbers before you do math.
- To find a creator's ID first, use [Douyin Xingtu Creator Search](/apis/douyin/xingtu-v3/gsearch-search-for-author-square). For a summary of conversion results, call [Douyin Xingtu Conversion Analysis](/apis/douyin/xingtu-v3/data-sp-author-convert-ability).

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/douyin/xingtu-v3/data-sp-author-convert-videos-or-products.json`](../../../../catalog/models/douyin/xingtu-v3/data-sp-author-convert-videos-or-products.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v3/data-sp-author-convert-videos-or-products
