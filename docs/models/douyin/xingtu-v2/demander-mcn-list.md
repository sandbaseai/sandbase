# Douyin Xingtu Demander MCN List API: pricing, parameters and code examples

`douyin/xingtu-v2/demander-mcn-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.005 per call (free daily quota) · **Modes:** sync

Returns a directory of MCN organizations on Douyin Xingtu with creator counts and performance scores, filterable by name and sorted by platform scores.

## Pricing

- **$0.005 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/demander-mcn-list", "mcn_name": "", "order_by": "platform_scores", "page": 1}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/demander-mcn-list', {'mcn_name': '', 'order_by': 'platform_scores', 'page': 1})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/demander-mcn-list", {
  "mcn_name": "",
  "order_by": "platform_scores",
  "page": 1
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/demander-mcn-list", sandbase.Params{
	"mcn_name": "",
	"order_by": "platform_scores",
	"page": 1,
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/demander-mcn-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number, default 1 default `1` |
| `mcn_name` | string |  | MCN name, supports fuzzy search default `""` |
| `order_by` | string |  | Sort by, `platform_scores`=platform scores default `"platform_scores"` |

## Details

Returns a paged directory of MCN organizations listed on Douyin Xingtu. Each entry has creator counts, scores, tags and top creators. All inputs are optional: `mcn_name` filters by name, `order_by` sets the sort, and `page` picks the page.

### Use cases

- Find MCN agencies on Xingtu by a partial company name.
- Rank agencies by `complex_score` and `growth_score` to build a shortlist.
- Compare roster size and total followers across agencies in the same content category.
- Pull the top creators of an agency and look each one up by `author_id`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/demander-mcn-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `mcn_name` | string | No | MCN name, supports fuzzy search |
| `order_by` | string | No | Sort by, `platform_scores`=platform scores |
| `page` | integer | No | Page number, default 1 |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "base_resp": {
    "status_code": 0,
    "status_message": "Success"
  },
  "mcns": [
    {
      "author_num": 868,
      "author_tags": [],
      "avatar_uri": "https://p6-starfe-sign.xingtu.cn/tos-cn-i-9hvokabxw2/9b1086075c43498498857fb4497…",
      "complex_score": 90.15,
      "growth_score": 55.86,
      "introduction": "无忧传媒2016年在北京成立，2017-2019年在杭州、成都、广州、上海、重庆、长沙、武汉、合肥、海南、常德等地陆续设立分公司或办事处。五年来公司稳健向上发展…",
      "is_partner_plan": false,
      "mcn_tags": [
        "科技数码"
      ],
      "name": "杭州无忧传媒有限公司",
      "opened_platforms": [
        1
      ],
      "star_tags": [
        {
          "tag_desc": "三星",
          "tag_type": 6,
          "tag_value": "3"
        }
      ],
      "sum_follower": "1720322144"
    }
  ],
  "pagination": {
    "has_more": true,
    "limit": 20,
    "page": 1,
    "total_count": 2983
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `mcns[].name` | Name of the MCN organization. |
| `mcns[].user_id` | ID of the MCN as a string. |
| `mcns[].author_num` | Number of creators the MCN has. |
| `mcns[].complex_score / mcns[].growth_score` | Performance scores for the MCN. `complex_score` is the overall score and `growth_score` is the growth score. |
| `mcns[].sum_follower` | Total follower count across the MCN's creators, returned as a string. |
| `mcns[].mcn_tags / mcns[].author_tags` | Content category labels for the MCN and for its creators, in Chinese. `author_tags` can be an empty list. |
| `mcns[].star_tags[].tag_desc` | Star level label of the MCN, for example `三星` (three stars). |
| `mcns[].top_authors[].author_id / mcns[].top_authors[].nick_name` | ID and display name of a leading creator in the MCN. |
| `mcns[].introduction` | Free-text company description. Long text may be cut. |
| `pagination.has_more / pagination.total_count` | Whether more pages exist and how many MCNs match in total. |

### Notes

- Page through results with `page`. Each page holds `pagination.limit` items (20 in the sample), and `pagination.has_more` tells you when to stop.
- `mcn_name` is a fuzzy match. Leave it empty to list all MCNs, sorted by `platform_scores` by default.
- Pass a value from `mcns[].top_authors[].author_id` to [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info) to get the creator's profile.
- The `avatar_uri` links for some MCNs include an `x-expires` parameter, so they may stop working after that time.

### Pricing

$0.005 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/apis/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/apis/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/demander-mcn-list.json`](../../../../catalog/models/douyin/xingtu-v2/demander-mcn-list.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/demander-mcn-list
