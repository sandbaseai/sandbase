# Xiaohongshu (RED) PGY Blogger Search API: pricing, parameters and code examples

`xiaohongshu/pgy/blogger-list` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Returns a paginated list of cooperable Xiaohongshu Pugongying bloggers matched under a specific brand. Filter candidate creators using keyword searches, audience profiles, performance metrics, and similar creator IDs.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/pgy/blogger-list", "blogger": {"content_tag": ["美妆"]}, "brand_user_id": "59ae4dfc5e87e72475fb3bf3", "fans": {"count": {"max": 500000, "min": 10000}}, "page_num": 1, "page_size": 5}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/pgy/blogger-list', {'blogger': {'content_tag': ['美妆']}, 'brand_user_id': '59ae4dfc5e87e72475fb3bf3', 'fans': {'count': {'max': 500000, 'min': 10000}}, 'page_num': 1, 'page_size': 5})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/pgy/blogger-list", {
  "blogger": {
    "content_tag": [
      "美妆"
    ]
  },
  "brand_user_id": "59ae4dfc5e87e72475fb3bf3",
  "fans": {
    "count": {
      "max": 500000,
      "min": 10000
    }
  },
  "page_num": 1,
  "page_size": 5
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/pgy/blogger-list", sandbase.Params{
	"blogger": map[string]any{
		"content_tag": []any{"美妆"},
	},
	"brand_user_id": "59ae4dfc5e87e72475fb3bf3",
	"fans": map[string]any{
		"count": map[string]any{
			"max": 500000,
			"min": 10000,
		},
	},
	"page_num": 1,
	"page_size": 5,
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/pgy/blogger-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `coop` |  |  | 合作笔记数据筛选/Sponsored note metric filters  |
| `fans` |  |  | 粉丝画像筛选/Fans profile filters  |
| `goal` |  |  | 合作目标筛选/Cooperation goal filters  |
| `live` |  |  | 直播数据筛选/Live metric filters  |
| `note` |  |  | 日常笔记数据筛选/Organic note metric filters  |
| `sort` | string |  | 排序方向 desc/asc one of: `desc`, `asc`; default `"desc"` |
| `flags` |  |  | 开关类筛选/Boolean flag filters  |
| `column` | string |  | 排序字段，共 34 个，见接口说明的排序字段表/Sort column, 34 options, see endpoint docs one of: `comprehensiverank`, `fansCount`, `price`, `clickNum`, `mEngagementNum`, `accumCommonImpMedinNum30d`, `accumPicCommonImpMedinNum30d`, `accumVideoCommonImpMedinNum30d`, `pictureClickMidNum`, `videoClickMidNum`, `pictureInterMidNum`, `videoInterMidNum` …; default `"comprehensiverank"` |
| `blogger` |  |  | 博主属性筛选/Blogger attribute filters  |
| `keyword` | string |  | 搜索词；空=只筛选不搜索/Keyword default `""` |
| `page_num` | integer |  | Page number, start from 1 range 1–1000 |
| `page_size` | integer |  | Page size (1-100) range 1–100 |
| `search_type` | integer |  | 1=按笔记关键词找博主(默认) 0=按昵称搜/Search mode one of: `0`, `1`; default `1` |
| `similar_word` |  |  | 配合 similar_user_id 的博主昵称，仅用于回显、不影响结果/Nickname echo for similar_user_id; does not affect results  |
| `brand_user_id` | string | yes | Brand/advertiser user ID, PGY matches under this brand (required)  |
| `similar_user_id` |  |  | 找相似博主：填一个博主的 userId，返回与他相似的博主，**并且可以叠加下面所有筛选**（这是它与 /get_blogger_similar 的关键区别）/Find similar bloggers; unlike /get_blogger_similar it can be combined with all filters below  |

## Details

Returns a paginated list of Xiaohongshu Pugongying (PGY) bloggers that can be matched under one brand. Each blogger row carries follower counts, estimated ad costs, note impression medians and content tags. The only required input is `brand_user_id`.

### Use cases

- Build a shortlist of creators for a brand campaign, then sort them by estimated CPM or engagement cost.
- Filter bloggers by content tags such as `contentTags[].taxonomy1Tag` to find creators in one niche.
- Compare picture note and video note cost estimates to decide which format to buy for a creator.
- Check how much each blogger's fan base has grown in the last 30 days before you contact them.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/pgy/blogger-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"brand_user_id": "5dcfa5370000000001006030"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `brand_user_id` | string | Yes | Brand/advertiser user ID, PGY matches under this brand (required) |
| `blogger` | string | No | 博主属性筛选/Blogger attribute filters |
| `column` | string | No | 排序字段，共 34 个，见接口说明的排序字段表/Sort column, 34 options, see endpoint docs |
| `coop` | string | No | 合作笔记数据筛选/Sponsored note metric filters |
| `fans` | string | No | 粉丝画像筛选/Fans profile filters |
| `flags` | string | No | 开关类筛选/Boolean flag filters |
| `goal` | string | No | 合作目标筛选/Cooperation goal filters |
| `keyword` | string | No | 搜索词；空=只筛选不搜索/Keyword |
| `live` | string | No | 直播数据筛选/Live metric filters |
| `note` | string | No | 日常笔记数据筛选/Organic note metric filters |
| `page_num` | integer | No | Page number, start from 1 |
| `page_size` | integer | No | Page size (1-100) |
| `search_type` | integer | No | 1=按笔记关键词找博主(默认) 0=按昵称搜/Search mode |
| `similar_user_id` | string | No | 找相似博主：填一个博主的 userId，返回与他相似的博主，**并且可以叠加下面所有筛选**（这是它与 /get_blogger_similar 的关键区别）/Find similar bloggers; unlike /get_blogger_similar it can be combined with all filters below |
| `similar_word` | string | No | 配合 similar_user_id 的博主昵称，仅用于回显、不影响结果/Nickname echo for similar_user_id; does not affect results |
| `sort` | string | No | 排序方向 desc/asc |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "highlightWords": [],
    "kols": [
      {
        "accumCommonImpMedinNum30d": 739837,
        "accumCoopImpMedinNum30d": 0,
        "accumPicCommonImpMedinNum30d": 739837,
        "accumVideoCommonImpMedinNum30d": 0,
        "activityList": [],
        "algoRecommendReasons": null,
        "authorityList": null,
        "avgAgmv90d": 0.0,
        "avgLiveViewerNum": 0.0,
        "businessNoteCount": 23,
        "buyerType": 2,
        "classifyCode": 1
      }
    ],
    "redirect2NickSearch": false,
    "resultType": 1,
    "total": 5000,
    "trackId": "kolMatch_0fa798d6f6b6439b9e03e6adcca8f27c"
  },
  "guid": null,
  "msg": "成功",
  "success": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.total` | Number of bloggers that match the query. Use it with the paging parameters to work out how many pages exist. |
| `data.kols[]` | One blogger per row. All fields below sit inside this object. |
| `data.kols[].fansNum` | Follower count of the blogger. |
| `data.kols[].fans30GrowthNum / data.kols[].fans30GrowthRate` | Follower growth over 30 days, as a count and as a rate. |
| `data.kols[].contentTags[].taxonomy1Tag / data.kols[].contentTags[].taxonomy2Tags` | Content categories of the blogger. `taxonomy1Tag` is the top level and `taxonomy2Tags` lists the sub categories. |
| `data.kols[].estimatePictureCpm / data.kols[].estimateVideoCpm` | Estimated CPM for picture notes and for video notes. A value of `0` means no estimate is shown for that format. |
| `data.kols[].estimatePictureEngageCost / data.kols[].estimateVideoEngageCost` | Estimated cost per engagement for picture notes and for video notes. |
| `data.kols[].accumPicCommonImpMedinNum30d / data.kols[].accumVideoCommonImpMedinNum30d` | Median impressions of the blogger's regular picture notes and video notes over 30 days. |
| `data.kols[].businessNoteCount` | Count of sponsored notes for the blogger. |
| `data.kols[].fansActiveIn28dLv` | Level of fan activity over the last 28 days, as a number. |

### Notes

- Pass the `brand_user_id` of the brand you are matching for. The sample request uses `5dcfa5370000000001006030`.
- Page through results with `page_num` (starts at 1) and `page_size` (1 to 100).
- Set `search_type` to `1` to search by note keywords or `0` to search by creator nickname. Use `similar_user_id` to start from one creator and find similar ones.
- Call [Xiaohongshu (RED) PGY Blogger Details](/apis/xiaohongshu/pgy/blogger-detail) to read the full profile of a blogger from the list.

### Pricing

$0.02 per successful call. Failed calls are not charged.

### Related APIs

- [Xiaohongshu (RED) Blogger Core Data](/apis/xiaohongshu/pgy/blogger-core-data): Returns Pugongying core performance metrics and daily trend data for a specified Xiaohongshu blogger, filterable by date range, note type, and traffic source.
- [Xiaohongshu (RED) PGY Blogger Data Summary](/apis/xiaohongshu/pgy/blogger-data-summary): Returns an account-level data summary for a Xiaohongshu blogger on the Pugongying (PGY) platform based on the specified blogger user ID.
- [Xiaohongshu (RED) PGY Blogger Details](/apis/xiaohongshu/pgy/blogger-detail): Retrieves detailed profile information for a specific Xiaohongshu blogger on the PGY platform using their user ID.

---
Machine-readable: [`catalog/models/xiaohongshu/pgy/blogger-list.json`](../../../../catalog/models/xiaohongshu/pgy/blogger-list.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/pgy/blogger-list
