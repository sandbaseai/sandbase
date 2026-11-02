# Douyin XingTu kolId by Douyin ID API: pricing, parameters and code examples

`douyin/xingtu-v2/xingtu-kolid-by-unique-id` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Returns Xingtu author profile details and platform identifiers matching a specified Douyin unique identifier.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/xingtu-kolid-by-unique-id", "unique_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/xingtu-kolid-by-unique-id', {'unique_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/xingtu-kolid-by-unique-id", {
  "unique_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/xingtu-kolid-by-unique-id", sandbase.Params{
	"unique_id": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/xingtu-kolid-by-unique-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `unique_id` | string | yes | Douyin unique_id  |

## Details

Look up Douyin Xingtu creator IDs and basic profile data using the `unique_id` parameter.

### Use cases

- Map Douyin public accounts to internal Xingtu creator IDs.
- Retrieve core user identifiers for influencer campaign tracking.
- Verify creator tags and profile nicknames before campaign assignment.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/xingtu-kolid-by-unique-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"unique_id": "dyczxzs"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `unique_id` | string | Yes | Douyin unique_id |

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

- Requires a valid Douyin `unique_id` string.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/model/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/model/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/model/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/xingtu-kolid-by-unique-id.json`](../../../../catalog/models/douyin/xingtu-v2/xingtu-kolid-by-unique-id.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/xingtu-kolid-by-unique-id
