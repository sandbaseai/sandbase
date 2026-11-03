# Xiaohongshu (RED) PGY Blogger Fans Summary API: pricing, parameters and code examples

`xiaohongshu/pgy/blogger-fans-summary` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Returns an overview of a Xiaohongshu blogger audience on PGY, including fan scale and activity metrics. Looks up fan statistics for a specified blogger user ID.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/pgy/blogger-fans-summary", "user_id": "60b137080000000001000301"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/pgy/blogger-fans-summary', {'user_id': '60b137080000000001000301'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/pgy/blogger-fans-summary", {
  "user_id": "60b137080000000001000301"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/pgy/blogger-fans-summary", sandbase.Params{
	"user_id": "60b137080000000001000301",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/pgy/blogger-fans-summary` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string | yes | Blogger user ID  |

## Details

Returns a fan summary for a Xiaohongshu blogger on PGY. It includes total fan count, recent fan growth, and counts and rates for active, engaged, reading and paying fans. It needs the blogger's `user_id`.

### Use cases

- Compare the fan base size and 30-day growth of several bloggers before choosing who to contact for a campaign.
- Check what share of a blogger's fans are active or paying before agreeing on a price.
- Rank candidate bloggers by the `...BeyondRate` fields to see how each one compares with other bloggers.
- Store `fansNum` and `fansIncreaseNum` on a schedule to build your own record of blogger growth.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/pgy/blogger-fans-summary" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "60b137080000000001000301"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | Blogger user ID |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "activeFansBeyondRate": "58.4",
    "activeFansL28": 28342,
    "activeFansRate": "75.4",
    "engageFansBeyondRate": "77.5",
    "engageFansL30": 296,
    "engageFansRate": "0.8",
    "fansGrowthBeyondRate": "77.9",
    "fansGrowthRate": "0.4",
    "fansIncreaseNum": 151,
    "fansNum": 37570,
    "payFansUserNum30d": 6169,
    "payFansUserRate30d": "16.4"
  },
  "guid": null,
  "msg": "成功",
  "success": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.fansNum` | Total number of fans the blogger has. |
| `data.fansIncreaseNum` | Number of fans gained. The response does not state the time window. |
| `data.fansGrowthRate / data.fansGrowthBeyondRate` | Fan growth rate and its `BeyondRate` value. Values are strings such as `0.4` and `77.9`. |
| `data.activeFansL28 / data.activeFansRate / data.activeFansBeyondRate` | Count of active fans (`L28` suggests the last 28 days), the active fan rate, and the matching `BeyondRate` value. |
| `data.engageFansL30 / data.engageFansRate / data.engageFansBeyondRate` | Count of engaged fans (`L30` suggests the last 30 days), the engaged fan rate, and the matching `BeyondRate` value. |
| `data.readFansIn30 / data.readFansRate / data.readFansBeyondRate` | Count of fans who read the blogger's content (the key suggests the last 30 days), the read fan rate, and the matching `BeyondRate` value. |
| `data.payFansUserNum30d / data.payFansUserRate30d` | Count of paying fans over 30 days and the paying fan rate, as a string such as `16.4`. |
| `success / msg` | `success` is `true` when the call works. `msg` holds a status text such as `成功`. |

### Notes

- Rate fields are returned as strings, so convert them to numbers before sorting or comparing.
- The response does not explain the `BeyondRate` fields. Treat them as comparison values and check them against known bloggers before relying on them.
- For fan history over time, call [Xiaohongshu (RED) PGY Blogger Fan History](/apis/xiaohongshu/pgy/blogger-fans-history). For fan demographics, call [Xiaohongshu (RED) PGY Blogger Fan Profile](/apis/xiaohongshu/pgy/blogger-fans-profile).

### Pricing

$0.02 per successful call. Failed calls are not charged.

### Related APIs

- [Xiaohongshu (RED) Blogger Core Data](/apis/xiaohongshu/pgy/blogger-core-data): Returns Pugongying core performance metrics and daily trend data for a specified Xiaohongshu blogger, filterable by date range, note type, and traffic source.
- [Xiaohongshu (RED) PGY Blogger Data Summary](/apis/xiaohongshu/pgy/blogger-data-summary): Returns an account-level data summary for a Xiaohongshu blogger on the Pugongying (PGY) platform based on the specified blogger user ID.
- [Xiaohongshu (RED) PGY Blogger Details](/apis/xiaohongshu/pgy/blogger-detail): Retrieves detailed profile information for a specific Xiaohongshu blogger on the PGY platform using their user ID.

---
Machine-readable: [`catalog/models/xiaohongshu/pgy/blogger-fans-summary.json`](../../../../catalog/models/xiaohongshu/pgy/blogger-fans-summary.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/pgy/blogger-fans-summary
