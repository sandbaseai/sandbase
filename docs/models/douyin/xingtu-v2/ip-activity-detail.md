# Douyin Xingtu IP Activity Detail API: pricing, parameters and code examples

`douyin/xingtu-v2/ip-activity-detail` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed information for a specific Xingtu IP calendar activity on Douyin. Queries activity data using the unique activity identifier.

## Pricing

- **$0.001 per call** (USD)
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

Returns the detail record for one Xingtu IP calendar activity on Douyin. You send the activity `id` as an integer. The sample response for `id` 1224 contains only the `base_resp` status object.

### Use cases

- Look up a single IP calendar activity after you pick its ID from the activity list.
- Check a calendar activity entry before you plan a Douyin campaign around it.
- Test whether an activity `id` returns a detail record before you show it in a marketing dashboard.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/ip-activity-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"id": 1224}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | integer | Yes | Activity ID, from `get_ip_activity_list` |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "base_resp": {
    "status_code": 0,
    "status_message": ""
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `base_resp` | Status object that wraps the result of the call. |
| `base_resp.status_code` | Numeric result code. It is `0` in the sample response. |
| `base_resp.status_message` | Text message that goes with the status code. It is an empty string in the sample response. |

### Notes

- Get the `id` value from the [Douyin Xingtu IP Activity List](/apis/douyin/xingtu-v2/ip-activity-list) API.
- `id` is an integer, for example `1224`.
- The sample response for `id` 1224 holds no activity fields beyond `base_resp`, so check `base_resp.status_code` before you read any other data.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/apis/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/apis/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/ip-activity-detail.json`](../../../../catalog/models/douyin/xingtu-v2/ip-activity-detail.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/ip-activity-detail
