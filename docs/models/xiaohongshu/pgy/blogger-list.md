# Xiaohongshu (RED) PGY Blogger Search

`xiaohongshu/pgy/blogger-list` · api · Xiaohongshu

Returns a paginated list of cooperable Xiaohongshu Pugongying bloggers matched under a specific brand. Filter candidate creators using keyword searches, audience profiles, performance metrics, and similar creator IDs.

## Pricing

- **$0.03 per call** (USD)

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

Query cooperable Pugongying bloggers for a brand by passing `brand_user_id`. Refine candidate lists with optional filters such as `keyword`, `column`, `search_type`, and `similar_user_id`.

### Use cases

- Search for potential brand collaboration partners using target note keywords or creator nicknames.
- Discover creators with audiences and performance metrics similar to a reference similar_user_id.
- Rank potential influencers by engagement metrics, follower count, or historical read performance.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/pgy/blogger-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"brand_user_id": "<brand_user_id>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `brand_user_id` | string | Yes | Brand/advertiser user ID, PGY matches under this brand (required) |
| `coop` | string | No | 合作笔记数据筛选/Sponsored note metric filters |
| `fans` | string | No | 粉丝画像筛选/Fans profile filters |
| `goal` | string | No | 合作目标筛选/Cooperation goal filters |
| `live` | string | No | 直播数据筛选/Live metric filters |
| `note` | string | No | 日常笔记数据筛选/Organic note metric filters |
| `sort` | string | No | 排序方向 desc/asc |
| `flags` | string | No | 开关类筛选/Boolean flag filters |
| `column` | string | No | 排序字段，共 34 个，见接口说明的排序字段表/Sort column, 34 options, see endpoint docs |
| `blogger` | string | No | 博主属性筛选/Blogger attribute filters |
| `keyword` | string | No | 搜索词；空=只筛选不搜索/Keyword |
| `page_num` | integer | No | Page number, start from 1 |
| `page_size` | integer | No | Page size (1-100) |
| `search_type` | integer | No | 1=按笔记关键词找博主(默认) 0=按昵称搜/Search mode |
| `similar_word` | string | No | 配合 similar_user_id 的博主昵称，仅用于回显、不影响结果/Nickname echo for similar_user_id; does not affect results |
| `similar_user_id` | string | No | 找相似博主：填一个博主的 userId，返回与他相似的博主，并且可以叠加下面所有筛选（这是它与 /get_blogger_similar 的关键区别）/Find similar bloggers; unlike /get_blogger_similar it can be combined with all filt… |

### Notes

- Set `search_type` to `1` to search by note keywords or `0` to search by creator nickname.
- Pass `brand_user_id` to scope blogger matching under the specified brand or advertiser account.
- Supports pagination through `page_num` starting from 1 and `page_size` between 1 and 100.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Xiaohongshu (RED) Blogger Core Data](/model/xiaohongshu/pgy/blogger-core-data): Returns Pugongying core performance metrics and daily trend data for a specified Xiaohongshu blogger, filterable by date range, note type, and traffic source.
- [Xiaohongshu (RED) PGY Blogger Data Summary](/model/xiaohongshu/pgy/blogger-data-summary): Returns an account-level data summary for a Xiaohongshu blogger on the Pugongying (PGY) platform based on the specified blogger user ID.
- [Xiaohongshu (RED) PGY Blogger Details](/model/xiaohongshu/pgy/blogger-detail): Retrieves detailed profile information for a specific Xiaohongshu blogger on the PGY platform using their user ID.

---
Machine-readable: [`catalog/models/xiaohongshu/pgy/blogger-list.json`](../../../../catalog/models/xiaohongshu/pgy/blogger-list.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/pgy/blogger-list
