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

Returns daily follower counts for a Xiaohongshu (RED) Pugongying (PGY) blogger. It needs the blogger's `user_id` and optionally a date range set with `date_type`.

### Use cases

- Plot a creator's follower curve over the last 7, 30 or 90 days.
- Spot days where a blogger's follower count jumps or drops.
- Compare net follower gain across several candidate creators before a campaign.
- Check recent growth against the total gain to screen influencers.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/pgy/blogger-fans-history" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "60b137080000000001000301"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | Blogger user ID |
| `date_type` | integer | No | Date range (~1=7d, 2=30d, 3=90d) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "fansNumInc": 151,
    "fansNumIncRate": 0.004035383094150031,
    "list": [
      {
        "dateKey": "2026-10-04",
        "num": 37419
      }
    ]
  },
  "guid": null,
  "msg": "成功",
  "success": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.fansNumInc` | Net change in followers over the returned period, as a whole number. |
| `data.fansNumIncRate` | Follower growth over the period as a decimal ratio. A value of `0.004` means about 0.4%. |
| `data.list[].dateKey` | Date of the data point, in `YYYY-MM-DD` format. |
| `data.list[].num` | Follower count of the blogger on that date. |
| `success / code` | `success` is `true` and `code` is `0` when the call works. |
| `msg` | Status message text. It reads `成功` (success) on a good call. |

### Notes

- Pass `user_id` as a string. The example value is `60b137080000000001000301`. Look up blogger IDs with [Xiaohongshu (RED) PGY Blogger Search](/apis/xiaohongshu/pgy/blogger-list).
- `date_type` is optional. `1` means 7 days, `2` means 30 days and `3` means 90 days. The schema allows values from 1 to 12.
- For the current audience makeup, call [Xiaohongshu (RED) PGY Blogger Fan Profile](/apis/xiaohongshu/pgy/blogger-fans-profile).

### Pricing

$0.02 per successful call. Failed calls are not charged.

### Related APIs

- [Xiaohongshu (RED) Blogger Core Data](/apis/xiaohongshu/pgy/blogger-core-data): Returns Pugongying core performance metrics and daily trend data for a specified Xiaohongshu blogger, filterable by date range, note type, and traffic source.
- [Xiaohongshu (RED) PGY Blogger Data Summary](/apis/xiaohongshu/pgy/blogger-data-summary): Returns an account-level data summary for a Xiaohongshu blogger on the Pugongying (PGY) platform based on the specified blogger user ID.
- [Xiaohongshu (RED) PGY Blogger Details](/apis/xiaohongshu/pgy/blogger-detail): Retrieves detailed profile information for a specific Xiaohongshu blogger on the PGY platform using their user ID.

---
Machine-readable: [`catalog/models/xiaohongshu/pgy/blogger-fans-history.json`](../../../../catalog/models/xiaohongshu/pgy/blogger-fans-history.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/pgy/blogger-fans-history
