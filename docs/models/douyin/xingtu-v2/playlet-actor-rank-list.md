# Douyin Xingtu Playlet Actor Ranking List API: pricing, parameters and code examples

`douyin/xingtu-v2/playlet-actor-rank-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Returns Xingtu ranking lists for Douyin playlet actors based on specified dates and evaluation periods. Filter rankings by actor category and ranking types.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/playlet-actor-rank-list", "category": "playlet_actor_list", "date": "20251130", "name": "playlet_actor_composite_list", "period": 30, "qualifier": ""}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/playlet-actor-rank-list', {'category': 'playlet_actor_list', 'date': '20251130', 'name': 'playlet_actor_composite_list', 'period': 30, 'qualifier': ''})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/playlet-actor-rank-list", {
  "category": "playlet_actor_list",
  "date": "20251130",
  "name": "playlet_actor_composite_list",
  "period": 30,
  "qualifier": ""
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/playlet-actor-rank-list", sandbase.Params{
	"category": "playlet_actor_list",
	"date": "20251130",
	"name": "playlet_actor_composite_list",
	"period": 30,
	"qualifier": "",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/playlet-actor-rank-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `date` | string |  | Date, format YYYYMMDD default `"20251130"` |
| `name` | string |  | Ranking name, `playlet_actor_composite_list`=composite list default `"playlet_actor_composite_list"` |
| `period` | integer |  | 7=weekly, 30=monthly default `30` |
| `category` | string |  | Category, default `playlet_actor_list` default `"playlet_actor_list"` |
| `qualifier` | string |  | Actor type, empty=all default `""` |

## Details

Returns a Xingtu ranking list of Douyin playlet actors for a given date and evaluation period. Each entry has the actor's ID, name, follower count and a set of scores. All inputs have defaults, so an empty request returns the monthly composite list.

### Use cases

- Pull the top-ranked playlet actors for a given month to build a casting shortlist.
- Compare an actor's `composite_score` with their `commercial_conversion_score` to judge sales value against acting quality.
- Track rank movement by reading `old_rank` against the current list position.
- Filter the list by actor type with `qualifier` to review a single group of actors.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/playlet-actor-rank-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `category` | string | No | Category, default `playlet_actor_list` |
| `date` | string | No | Date, format YYYYMMDD |
| `name` | string | No | Ranking name, `playlet_actor_composite_list`=composite list |
| `period` | integer | No | 7=weekly, 30=monthly |
| `qualifier` | string | No | Actor type, empty=all |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "author_rank_list": [
    {
      "avatar_uri": "https://p11.douyinpic.com/aweme/1080x1080/aweme-avatar/tos-cn-avt-0015_88c16cb6a…",
      "core_user_id": "59187082550",
      "extra": {
        "act_performance_score": "95.44",
        "actor_name": "傅汉源",
        "commercial_conversion_score": "100.0",
        "compass_virality_score": "100.0",
        "composite_score": "99.54",
        "cover": "tos-cn-i-dy/720f8f97f48c8c678e06d42d57f1e379",
        "gender": "男",
        "old_rank": "32"
      },
      "follower": 105720,
      "id": "59187082550",
      "name": "傅汉源"
    }
  ],
  "base_resp": {
    "status_code": 0,
    "status_message": ""
  },
  "modify_time": "1765124053"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `author_rank_list[]` | One ranked actor. The list order is the ranking order. |
| `author_rank_list[].core_user_id / author_rank_list[].id` | The actor's numeric user ID, returned as a string. Both fields hold the same value in the sample. |
| `author_rank_list[].name` | The actor's display name on Douyin. |
| `author_rank_list[].follower` | The actor's follower count as a number. |
| `author_rank_list[].avatar_uri` | URL of the actor's avatar image. |
| `author_rank_list[].extra.composite_score` | The overall score used for the composite list. It is returned as a string. |
| `author_rank_list[].extra.act_performance_score / author_rank_list[].extra.commercial_conversion_score / author_rank_list[].extra.compass_virality_score` | Component scores for acting performance, commercial conversion and virality. Each is a string. |
| `author_rank_list[].extra.old_rank` | The actor's earlier rank, returned as a string. Compare it with the current position to see movement. |
| `author_rank_list[].extra.actor_name / author_rank_list[].extra.gender` | The actor's name and gender as shown on the ranking. |
| `modify_time` | Unix timestamp in seconds for the last update of the ranking. |

### Notes

- Set `period` to `7` for a weekly list or `30` for a monthly list.
- Send `date` as `YYYYMMDD`, for example `20251130`.
- Leave `qualifier` empty to include all actor types. To see the available ranking options, call [Douyin Xingtu Playlet Actor Rank Catalog](/apis/douyin/xingtu-v2/playlet-actor-rank-catalog).
- Pass an actor's `id` to [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info) for more profile data.

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/apis/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/apis/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/playlet-actor-rank-list.json`](../../../../catalog/models/douyin/xingtu-v2/playlet-actor-rank-list.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/playlet-actor-rank-list
