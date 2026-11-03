# Douyin Xingtu IP Activity Industry List API: pricing, parameters and code examples

`douyin/xingtu-v2/ip-activity-industry-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the list of supported industries for the Xingtu IP calendar on Douyin. Use this reference data to filter and categorize upcoming IP activities.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/ip-activity-industry-list"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/ip-activity-industry-list', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/ip-activity-industry-list", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/ip-activity-industry-list", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/ip-activity-industry-list` with the body above minus `model`.

## Details

Returns the list of industries supported by the Xingtu IP calendar on Douyin. Each entry has an industry ID and an industry name. The call takes no input parameters.

### Use cases

- Fill an industry dropdown in a tool that browses Xingtu IP calendar activities.
- Map industry IDs found in IP activity data to readable industry names.
- Map your own industry categories to the Xingtu industry IDs.
- Cache the industry list as reference data for filtering upcoming IP activities.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/ip-activity-industry-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "industry_list": [
    {
      "industry_id": "1930",
      "industry_name": "美妆"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `industry_list` | List of all supported industries. Each item is one industry. |
| `industry_list[].industry_id` | ID of the industry, returned as a string such as `1930`. Use it to refer to this industry in other calls. |
| `industry_list[].industry_name` | Name of the industry in Chinese, for example `美妆` (beauty), `3C及电器` (3C and electrical appliances) or `日化` (daily chemicals). |

### Notes

- Send an empty JSON object `{}` as the request body. The API has no parameters and no pagination.
- `industry_id` values are strings, not numbers. Keep them as strings when you pass them on.
- To see the activities themselves, call [Douyin Xingtu IP Activity List](/apis/douyin/xingtu-v2/ip-activity-list). For one activity's full record, use [Douyin Xingtu IP Activity Detail](/apis/douyin/xingtu-v2/ip-activity-detail).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/apis/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/apis/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/ip-activity-industry-list.json`](../../../../catalog/models/douyin/xingtu-v2/ip-activity-industry-list.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/ip-activity-industry-list
