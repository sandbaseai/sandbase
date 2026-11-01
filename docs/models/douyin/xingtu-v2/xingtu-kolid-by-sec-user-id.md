# Douyin XingTu kolId by sec_user_id (V2)

`douyin/xingtu-v2/xingtu-kolid-by-sec-user-id` · api · Douyin

Returns Xingtu creator identifiers and basic profile metrics for a Douyin account using its secure user ID. It provides the Xingtu author ID, core user ID, and performance indicators.

## Pricing

- **$0.003 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/xingtu-kolid-by-sec-user-id", "sec_user_id": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/xingtu-kolid-by-sec-user-id', {'sec_user_id': 'MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/xingtu-kolid-by-sec-user-id", {
  "sec_user_id": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/xingtu-kolid-by-sec-user-id", sandbase.Params{
	"sec_user_id": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/xingtu-kolid-by-sec-user-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sec_user_id` | string | yes | Douyin user sec_user_id, obtainable from Douyin user-profile endpoints  |

## Details

Look up Xingtu creator profile IDs and baseline metrics by supplying a Douyin `sec_user_id`.

### Use cases

- Map standard Douyin accounts to their corresponding Xingtu creator IDs.
- Retrieve core author identifiers for influencer campaign workflows.
- Inspect completion rate performance metrics and profile tags for creators.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/xingtu-kolid-by-sec-user-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sec_user_id": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sec_user_id` | string | Yes | Douyin user sec_user_id, obtainable from Douyin user-profile endpoints |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "core_user_id": "3635433641882579",
  "finish_rate_ovr": 0.8384,
  "id": "7452669161240526898",
  "nick_name": "<user>",
  "tag": "时尚"
}
```

### Notes

- Supply `sec_user_id`, which is obtainable from Douyin user profile endpoints.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/model/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/model/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/model/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/xingtu-kolid-by-sec-user-id.json`](../../../../catalog/models/douyin/xingtu-v2/xingtu-kolid-by-sec-user-id.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/xingtu-kolid-by-sec-user-id
