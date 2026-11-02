# Douyin Billboard Hot Calendar Detail API: pricing, parameters and code examples

`douyin/billboard/hot-calendar-detail` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed information for a Douyin billboard hot calendar event based on the specified activity identifier. Use this endpoint to inspect schedule metadata and billboard campaign details.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/billboard/hot-calendar-detail", "calendar_id": "1"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/billboard/hot-calendar-detail', {'calendar_id': '1'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/billboard/hot-calendar-detail", {
  "calendar_id": "1"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/billboard/hot-calendar-detail", sandbase.Params{
	"calendar_id": "1",
})
```

Same call via the path form: `POST /v1/api/douyin/billboard/hot-calendar-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `calendar_id` | string | yes | Activity id  |

## Details

Returns detailed information for a Douyin billboard hot calendar activity using a specific `calendar_id`. It helps teams review scheduled campaign metadata and calendar event details.

### Use cases

- Review details for a scheduled Douyin billboard calendar activity.
- Track campaign timelines and billboard event specifics.
- Integrate hot calendar metadata into marketing dashboards.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/billboard/hot-calendar-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"calendar_id": "1720"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `calendar_id` | string | Yes | Activity id |

### Notes

- Specify the target activity identifier via `calendar_id`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Billboard City List](/model/douyin/billboard/city-list): Returns the list of Chinese cities supported by Douyin billboard rankings.
- [Douyin Billboard Vertical Content Tags](/model/douyin/billboard/content-tag): Returns a list of vertical content tags available on the Douyin billboard platform.
- [Douyin Fan Interest Account List](/model/douyin/billboard/hot-account-fans-interest-account-list): Returns a list of 20 accounts that followers of a target creator are interested in on Douyin.

---
Machine-readable: [`catalog/models/douyin/billboard/hot-calendar-detail.json`](../../../../catalog/models/douyin/billboard/hot-calendar-detail.json) · Store page: https://www.sandbase.ai/model/douyin/billboard/hot-calendar-detail
