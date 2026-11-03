# Douyin XingTu Ranking List Data API: pricing, parameters and code examples

`douyin/xingtu-v2/ranking-list-data` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Returns Douyin XingTu author business ranking records by type, date, and category qualifier. It provides author rankings, performance scores, and order metrics.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/ranking-list-data", "code": 1, "date": "20260131", "period": 30, "qualifier": "1901", "version": "flow_split"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/ranking-list-data', {'code': 1, 'date': '20260131', 'period': 30, 'qualifier': '1901', 'version': 'flow_split'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/ranking-list-data", {
  "code": 1,
  "date": "20260131",
  "period": 30,
  "qualifier": "1901",
  "version": "flow_split"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/ranking-list-data", sandbase.Params{
	"code": 1,
	"date": "20260131",
	"period": 30,
	"qualifier": "1901",
	"version": "flow_split",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/ranking-list-data` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `code` | integer |  | Ranking type code default `1` |
| `date` | string |  | Date, format YYYYMMDD default `"20260131"` |
| `period` | integer |  | 7=weekly, 30=monthly default `30` |
| `version` | string |  | `flow_split`=default for video rankings, `base`=commonly used for live rankings default `"flow_split"` |
| `qualifier` | string |  | Category qualifier_id from `get_ranking_list_catalog` default `"1901"` |

## Details

Returns a Douyin XingTu author ranking list for a ranking type, date, period and category. Each record has the author's rank, score, profile attributes and top videos. All inputs have defaults, so an empty request returns a ranking.

### Use cases

- Pull the monthly brand-preferred author ranking for one category and store it as a snapshot.
- Find authors that newly entered the list by checking `is_new` and comparing `old_rank` with `rank`.
- Screen authors by `cpm`, `follower` and `finish_order_cnt` before choosing creators for a campaign.
- Read the ranking rule text in `info.description` to explain how a list is scored.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/ranking-list-data" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `code` | integer | No | Ranking type code |
| `date` | string | No | Date, format YYYYMMDD |
| `period` | integer | No | 7=weekly, 30=monthly |
| `qualifier` | string | No | Category qualifier_id from `get_ranking_list_catalog` |
| `version` | string | No | `flow_split`=default for video rankings, `base`=commonly used for live rankings |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "authors": [
    {
      "attribute_datas": {
        "author_id": "7146074596666507300",
        "author_status": "1",
        "avatar_uri": "https://p3.douyinpic.com/aweme/1080x1080/aweme-avatar/tos-cn-avt-0015_2cd7dc35ac…",
        "city": "",
        "core_user_id": "3777519688105684",
        "cpm": "36",
        "finish_order_cnt": "> 20",
        "follower": "706656"
      },
      "is_new": false,
      "items": [
        {
          "item_id": "7661088907202776354",
          "video_tag": 3,
          "vv": 8507
        }
      ],
      "old_rank": "1",
      "rank": "1",
      "score": 0.58994708994709,
      "star_id": "7146074596666507300"
    }
  ],
  "base_resp": {
    "status_code": 0,
    "status_message": ""
  },
  "info": {
    "code": 1,
    "description": "【榜单规则】：根据创作者在所选周期内的星图商单数、复购率计算榜单排名 【上榜达人特点】：星图商单数量多、客户复购率高",
    "display_name": "品牌种草·品牌优选榜",
    "entry_type": 1,
    "modify_time": 1769932545,
    "platform_channel": 1,
    "ranking_list_factor": 0,
    "version": "flow_split"
  },
  "pagination": {
    "has_more": false,
    "limit": 100,
    "page": 1,
    "total_count": 100
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `authors[].rank / authors[].old_rank` | Current rank and previous rank of the author, both as strings. An `old_rank` of `0` appears together with `is_new` set to `true`. |
| `authors[].score` | Ranking score of the author. Higher scores rank higher. |
| `authors[].star_id / authors[].attribute_datas.author_id` | XingTu ID of the author. Both fields hold the same value in this response. |
| `authors[].attribute_datas.core_user_id` | Numeric user ID stored with the author's attributes. |
| `authors[].attribute_datas.follower` | Follower count of the author, as a string. |
| `authors[].attribute_datas.cpm` | CPM value for the author, as a string. |
| `authors[].attribute_datas.finish_order_cnt` | Completed order count, shown as a range such as `> 20`. |
| `authors[].items[].item_id / authors[].items[].vv` | ID of a listed video and its `vv` value. |
| `info.display_name / info.description` | Name of the ranking list and the text of its ranking rule. |
| `pagination.has_more / pagination.total_count` | Shows whether more records exist and how many records the list holds in total. |

### Notes

- Get the `qualifier` value from [Douyin Xingtu Ranking List Catalog](/apis/douyin/xingtu-v2/ranking-list-catalog) and use the same catalog to find the `code` for a ranking type.
- Set `period` to `7` for weekly or `30` for monthly. Send `date` as `YYYYMMDD`.
- Use `flow_split` in `version` for video rankings and `base` for live rankings.
- Pass an author's `star_id` to [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info) for the full creator profile.

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/apis/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/apis/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/ranking-list-data.json`](../../../../catalog/models/douyin/xingtu-v2/ranking-list-data.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/ranking-list-data
