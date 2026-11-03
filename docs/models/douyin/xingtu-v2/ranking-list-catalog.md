# Douyin Xingtu Ranking List Catalog API: pricing, parameters and code examples

`douyin/xingtu-v2/ranking-list-catalog` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the ranking list catalog from Douyin Xingtu, including available leaderboard dates and qualifiers. Accepts optional business scene and classification code filters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/ranking-list-catalog", "biz_scene": "douyin_flow_split_video_author_ranks", "codes": ""}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/ranking-list-catalog', {'biz_scene': 'douyin_flow_split_video_author_ranks', 'codes': ''})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/ranking-list-catalog", {
  "biz_scene": "douyin_flow_split_video_author_ranks",
  "codes": ""
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/ranking-list-catalog", sandbase.Params{
	"biz_scene": "douyin_flow_split_video_author_ranks",
	"codes": "",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/ranking-list-catalog` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `codes` | string |  | Classification codes, default is empty string default `""` |
| `biz_scene` | string |  | Business scene default `"douyin_flow_split_video_author_ranks"` |

## Details

Returns the ranking list catalog from Douyin Xingtu. The `catalog` object is keyed by ranking code, and each code holds a list of available leaderboard dates with their qualifier and period. Both `biz_scene` and `codes` are optional, and an empty request returns the default `douyin_flow_split_video_author_ranks` scene.

### Use cases

- List every ranking code with its display name to see which Xingtu leaderboards exist.
- Find the latest available `date` for a given ranking and qualifier before you request its data.
- Map a `qualifier_id` such as `1930` to its category name, for example the beauty category.
- Compare 7-day and 30-day versions of the same leaderboard across categories.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/ranking-list-catalog" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `biz_scene` | string | No | Business scene |
| `codes` | string | No | Classification codes, default is empty string |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "base_resp": {
    "status_code": 0,
    "status_message": ""
  },
  "catalog": {
    "1": [
      {
        "attribute_datas": {},
        "code": 1,
        "date": "20261101",
        "display_name": "品牌种草·品牌优选榜",
        "period": "7",
        "qualifier": "3C及电器",
        "qualifier_id": "1901",
        "version": "flow_split"
      }
    ],
    "10": [
      {
        "attribute_datas": {},
        "code": 10,
        "date": "20251228",
        "display_name": "应用下载·高潜榜",
        "period": "7",
        "qualifier": "平台电商",
        "qualifier_id": "平台电商",
        "version": "flow_split"
      }
    ],
    "101319": [
      {
        "attribute_datas": {},
        "code": 101319,
        "date": "20260921",
        "display_name": "种草达人·生活场景种草",
        "period": "7",
        "qualifier": "服装配饰",
        "qualifier_id": "1904",
        "version": "base"
      }
    ],
    "101320": [
      {
        "attribute_datas": {},
        "code": 101320,
        "date": "20260921",
        "display_name": "种草达人·知识科普/溯源",
        "period": "30",
        "qualifier": "服装配饰",
        "qualifier_id": "1904",
        "version": "base"
      }
    ],
    "101321": [
      {
        "attribute_datas": {},
        "code": 101321,
        "date": "20260921",
        "display_name": "种草达人·线下打卡",
        "period": "30",
        "qualifier": "母婴宠物",
        "qualifier_id": "1931",
        "version": "base"
      }
    ],
    "101322": [
      {
        "attribute_datas": {},
        "code": 101322,
        "date": "20260921",
        "display_name": "种草达人·好物分享推荐",
        "period": "30",
        "qualifier": "母婴宠物",
        "qualifier_id": "1931",
        "version": "base"
      }
    ],
    "101323": [
      {
        "attribute_datas": {},
        "code": 101323,
        "date": "20260921",
        "display_name": "种草达人·内容宣发",
        "period": "7",
        "qualifier": "美妆",
        "qualifier_id": "1930",
        "version": "base"
      }
    ],
    "101324": [
      {
        "attribute_datas": {},
        "code": 101324,
        "date": "20260921",
        "display_name": "测评达人·真实体验测评",
        "period": "7",
        "qualifier": "汽车",
        "qualifier_id": "1916",
        "version": "base"
      }
    ],
    "101325": [
      {
        "attribute_datas": {},
        "code": 101325,
        "date": "20260921",
        "display_name": "测评达人·深度专业测评",
        "period": "30",
        "qualifier": "母婴宠物",
        "qualifier_id": "1931",
        "version": "base"
      }
    ],
    "101326": [
      {
        "attribute_datas": {},
        "code": 101326,
        "date": "20260921",
        "display_name": "创意达人",
        "period": "7",
        "qualifier": "食品饮料",
        "qualifier_id": "1903",
        "version": "base"
      }
    ],
    "11": [
      {
        "attribute_datas": {},
        "code": 11,
        "date": "20251228",
        "display_name": "应用下载·投流榜",
        "period": "7",
        "qualifier": "平台电商",
        "qualifier_id": "平台电商",
        "version": "base"
      }
    ],
    "12": [
      {
        "attribute_datas": {},
        "code": 12,
        "date": "20241231",
        "display_name": "线索收集·品牌优选榜",
        "period": "30",
        "qualifier": "家居建材",
        "qualifier_id": "1909",
        "version": "flow_split"
      }
    ]
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `catalog` | Object keyed by ranking code (for example `18` or `101319`). Each value is a list of available leaderboard entries for that code. |
| `catalog.*[].code` | Numeric ranking code. It matches the key of the list that holds the entry. |
| `catalog.*[].display_name` | Name of the leaderboard in Chinese, for example the brand seeding or lead collection lists. |
| `catalog.*[].date` | Leaderboard date as a `YYYYMMDD` string, for example `20261101`. |
| `catalog.*[].period` | Time window of the leaderboard as a string. The response shows `7` and `30`. |
| `catalog.*[].qualifier / qualifier_id` | Category name and its ID that the leaderboard is limited to. Most IDs are numeric strings, but some match the name, such as `平台电商`. |
| `catalog.*[].version` | Leaderboard version label. The response shows `flow_split` and `base`. |
| `base_resp.status_code / base_resp.status_message` | Status of the call. `0` with an empty message means success. |

### Notes

- The paths use `*` for the dynamic ranking code keys under `catalog`. Real keys are values like `1`, `10` and `101319`.
- The same `code` and `date` can appear several times with different `qualifier_id` and `period` values, so use all three to pick one entry.
- Call [Douyin XingTu Ranking List Data](/apis/douyin/xingtu-v2/ranking-list-data) next to fetch the ranking itself.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/apis/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/apis/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/ranking-list-catalog.json`](../../../../catalog/models/douyin/xingtu-v2/ranking-list-catalog.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/ranking-list-catalog
