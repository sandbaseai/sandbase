# Xiaohongshu Pugongying Follower Summary API: pricing, parameters and code examples

`xiaohongshu/pgy-v2/data-v3-fans-summary` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get the Xiaohongshu Pugongying follower summary for a known creator. Use it to review the account's aggregate audience status before deeper demographic or trend analysis.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/pgy-v2/data-v3-fans-summary", "userId": "5a73c5fa4eacab4c4ccc9778"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/pgy-v2/data-v3-fans-summary', {'userId': '5a73c5fa4eacab4c4ccc9778'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/pgy-v2/data-v3-fans-summary", {
  "userId": "5a73c5fa4eacab4c4ccc9778"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/pgy-v2/data-v3-fans-summary", sandbase.Params{
	"userId": "5a73c5fa4eacab4c4ccc9778",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/pgy-v2/data-v3-fans-summary` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `userId` | string | yes | KOL's user ID.  |

## Details

Returns an aggregate follower summary for one Xiaohongshu creator listed on Pugongying. It includes total followers, recent follower change, and counts and rates for active, engaged, reading and paying followers. It needs the creator's `userId`.

### Use cases

- Check a creator's total follower count and recent follower change before you shortlist them for a campaign.
- Compare the share of active and engaged followers across several creators.
- Review how many followers read or paid in the last 30 days to judge audience quality.
- Screen creators with a quick audience check before you pull demographic or growth history data.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/pgy-v2/data-v3-fans-summary" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"userId": "5a73c5fa4eacab4c4ccc9778"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `userId` | string | Yes | KOL's user ID. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "activeFansBeyondRate": "36.7",
  "activeFansL28": 12513923,
  "activeFansRate": "50.0",
  "engageFansBeyondRate": "68.1",
  "engageFansL30": 686077,
  "engageFansRate": "2.7",
  "fansGrowthBeyondRate": "39.9",
  "fansGrowthRate": "-0.1",
  "fansIncreaseNum": -18872,
  "fansNum": 25024146,
  "payFansUserNum30d": 3466345,
  "payFansUserRate30d": "13.9"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `fansNum` | Total follower count of the creator. |
| `fansIncreaseNum / fansGrowthRate` | Follower change as a number and as a rate. Negative values mean the account lost followers. `fansGrowthRate` is returned as a string such as `-0.1`. |
| `fansGrowthBeyondRate` | Growth ranking value shown as a string. The name suggests the share of other creators this account beats on growth. |
| `activeFansL28 / activeFansRate` | Number of active followers over the last 28 days (`L28`) and their rate relative to total followers. The rate is a string such as `50.0`. |
| `activeFansBeyondRate` | Ranking value for active followers, returned as a string. The name suggests the share of other creators this account beats. |
| `engageFansL30 / engageFansRate` | Number of engaged followers over the last 30 days (`L30`) and their rate relative to total followers. |
| `engageFansBeyondRate` | Ranking value for engaged followers, returned as a string. |
| `readFansIn30 / readFansRate` | Number of followers who read the creator's content in the last 30 days and their rate. The rate is a string such as `13.6`. |
| `readFansBeyondRate` | Ranking value for reading followers, returned as a string. |
| `payFansUserNum30d / payFansUserRate30d` | Number of paying followers over the last 30 days and their rate. The rate is a string such as `13.9`. |

### Notes

- Pass the creator's ID as `userId`, a 24-character hex string such as `5a73c5fa4eacab4c4ccc9778`. You can find it with [Xiaohongshu Pugongying Creator Search](/apis/xiaohongshu/pgy-v2/blogger-v2).
- Rate and `BeyondRate` fields are strings, while counts are numbers. Convert the strings before you do math.
- For age, gender and location breakdowns, call [Xiaohongshu Pugongying Follower Distribution](/apis/xiaohongshu/pgy-v2/user-id-fans-profile). For follower change over time, call [Xiaohongshu Pugongying Follower Growth History](/apis/xiaohongshu/pgy-v2/user-id-fans-overall-new-history).

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/pgy-v2/data-v3-fans-summary.json`](../../../../catalog/models/xiaohongshu/pgy-v2/data-v3-fans-summary.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/pgy-v2/data-v3-fans-summary
