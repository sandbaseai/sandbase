# Douyin Xingtu Resource List API: pricing, parameters and code examples

`douyin/xingtu-v2/resource-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns marketing activity resources from Douyin Xingtu. Queries resource details using a specific resource identifier.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/resource-list", "resource_id": 1}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/resource-list', {'resource_id': 1})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/resource-list", {
  "resource_id": 1
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/resource-list", sandbase.Params{
	"resource_id": 1,
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/resource-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `resource_id` | integer | yes | Resource ID  |

## Details

Access marketing activity resources from Douyin Xingtu by providing a `resource_id`.

### Use cases

- Look up marketing resources associated with a specific resource ID.
- Inspect campaign asset listings for Douyin Xingtu activities.
- Monitor marketing activity resources for campaign tracking.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/resource-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"resource_id": "<resource_id>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `resource_id` | integer | Yes | Resource ID |

### Notes

- Requires `resource_id` to specify which marketing resource to retrieve.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/model/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/model/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/model/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/resource-list.json`](../../../../catalog/models/douyin/xingtu-v2/resource-list.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/resource-list
