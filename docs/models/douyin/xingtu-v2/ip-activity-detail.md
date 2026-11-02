# Douyin Xingtu IP Activity Detail API: pricing, parameters and code examples

`douyin/xingtu-v2/ip-activity-detail` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns detailed information for a specific Xingtu IP calendar activity on Douyin. Queries activity data using the unique activity identifier.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/ip-activity-detail", "id": 1}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/ip-activity-detail', {'id': 1})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/ip-activity-detail", {
  "id": 1
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/ip-activity-detail", sandbase.Params{
	"id": 1,
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/ip-activity-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | integer | yes | Activity ID, from `get_ip_activity_list`  |

## Details

Retrieve details for a specific Xingtu IP calendar activity by supplying its `id`. Activity identifiers can be obtained from the activity list endpoint.

### Use cases

- Inspect specific Xingtu IP calendar activity parameters and guidelines.
- Retrieve full activity profiles to coordinate Douyin marketing campaigns.
- Display detailed calendar event information within marketing dashboards.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/ip-activity-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"id": 1224}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | integer | Yes | Activity ID, from `get_ip_activity_list` |

### Notes

- Obtain the required `id` value from `get_ip_activity_list`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/model/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/model/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/model/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/ip-activity-detail.json`](../../../../catalog/models/douyin/xingtu-v2/ip-activity-detail.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/ip-activity-detail
