# Douyin Xingtu Author ID by UID API: pricing, parameters and code examples

`douyin/xingtu-v2/xingtu-kolid-by-uid` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Returns the Xingtu creator identifier and basic profile details for a given Douyin user account. Provide a Douyin user ID to retrieve associated Xingtu platform metadata.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/xingtu-kolid-by-uid", "uid": "92769419069"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/xingtu-kolid-by-uid', {'uid': '92769419069'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/xingtu-kolid-by-uid", {
  "uid": "92769419069"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/xingtu-kolid-by-uid", sandbase.Params{
	"uid": "92769419069",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/xingtu-kolid-by-uid` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | Douyin user ID, obtainable from Douyin user-profile endpoints  |

## Details

Look up a Douyin creator's Xingtu author profile details by providing their Douyin user ID in `uid`.

### Use cases

- Map standard Douyin user IDs to Xingtu creator IDs for campaign workflows.
- Verify creator tags and completion rates for marketing evaluation.
- Bridge creator profile data across Douyin and Xingtu platforms.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/xingtu-kolid-by-uid" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "92769419069"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | Douyin user ID, obtainable from Douyin user-profile endpoints |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "core_user_id": "92769419069",
  "finish_rate_ovr": 0,
  "id": "6870164585236660237",
  "nick_name": "<user>",
  "tag": "教育培训"
}
```

### Notes

- The `uid` parameter can be obtained from Douyin user-profile endpoints.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/model/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/model/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/model/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/xingtu-kolid-by-uid.json`](../../../../catalog/models/douyin/xingtu-v2/xingtu-kolid-by-uid.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/xingtu-kolid-by-uid
