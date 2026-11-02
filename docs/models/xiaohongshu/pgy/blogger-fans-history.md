# Xiaohongshu (RED) PGY Blogger Fan History API: pricing, parameters and code examples

`xiaohongshu/pgy/blogger-fans-history` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Returns historical follower growth counts for a Xiaohongshu Pugongying blogger over time based on user ID and a selected date range.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/pgy/blogger-fans-history", "user_id": "60b137080000000001000301"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/pgy/blogger-fans-history', {'user_id': '60b137080000000001000301'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/pgy/blogger-fans-history", {
  "user_id": "60b137080000000001000301"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/pgy/blogger-fans-history", sandbase.Params{
	"user_id": "60b137080000000001000301",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/pgy/blogger-fans-history` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string | yes | Blogger user ID  |
| `date_type` | integer |  | Date range (~1=7d, 2=30d, 3=90d) range 1–12 |

## Details

Retrieve historical follower counts for a specified blogger using `user_id`. You can also filter the date window by passing `date_type`.

### Use cases

- Track follower growth curves for specific Xiaohongshu creators.
- Evaluate long-term audience momentum before partnering with influencers.
- Analyze sudden spikes or drops in blogger follower numbers over time.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/pgy/blogger-fans-history" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "60b137080000000001000301"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | Blogger user ID |
| `date_type` | integer | No | Date range (~1=7d, 2=30d, 3=90d) |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "list": [
      {
        "dateKey": "2026-09-06",
        "num": 37199
      }
    ]
  }
}
```

### Notes

- `date_type` accepts integer values corresponding to time windows: 1 for 7 days, 2 for 30 days, and 3 for 90 days.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Xiaohongshu (RED) Blogger Core Data](/model/xiaohongshu/pgy/blogger-core-data): Returns Pugongying core performance metrics and daily trend data for a specified Xiaohongshu blogger, filterable by date range, note type, and traffic source.
- [Xiaohongshu (RED) PGY Blogger Data Summary](/model/xiaohongshu/pgy/blogger-data-summary): Returns an account-level data summary for a Xiaohongshu blogger on the Pugongying (PGY) platform based on the specified blogger user ID.
- [Xiaohongshu (RED) PGY Blogger Details](/model/xiaohongshu/pgy/blogger-detail): Retrieves detailed profile information for a specific Xiaohongshu blogger on the PGY platform using their user ID.

---
Machine-readable: [`catalog/models/xiaohongshu/pgy/blogger-fans-history.json`](../../../../catalog/models/xiaohongshu/pgy/blogger-fans-history.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/pgy/blogger-fans-history
