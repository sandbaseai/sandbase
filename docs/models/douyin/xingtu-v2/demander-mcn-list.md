# Douyin Xingtu Demander MCN List API: pricing, parameters and code examples

`douyin/xingtu-v2/demander-mcn-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0075 per call (free daily quota) · **Modes:** sync

Returns a directory of MCN organizations on Douyin Xingtu with creator counts and performance scores, filterable by name and sorted by platform scores.

## Pricing

- **$0.0075 per call** (USD)
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

Retrieve a list of Douyin Xingtu MCN organizations using `mcn_name` for fuzzy matching and `order_by` to rank by platform scores.

### Use cases

- Search for partner MCN agencies by name.
- Rank MCN organizations based on platform performance scores.
- Inspect author counts and growth metrics across agencies.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/demander-mcn-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `page` | integer | No | Page number, default 1 |
| `mcn_name` | string | No | MCN name, supports fuzzy search |
| `order_by` | string | No | Sort by, `platform_scores`=platform scores |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "mcns": [
    {
      "author_num": 868,
      "complex_score": 89.78,
      "growth_score": 55.63,
      "name": "杭州无忧传媒有限公司",
      "user_id": "<user>"
    }
  ]
}
```

### Notes

- `mcn_name` supports fuzzy search.
- Set `order_by` to `platform_scores` to sort by platform ratings.
- `page` defaults to 1.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/model/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/model/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/model/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/demander-mcn-list.json`](../../../../catalog/models/douyin/xingtu-v2/demander-mcn-list.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/demander-mcn-list
