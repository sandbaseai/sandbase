# AAA Price Change By Metro API: pricing, parameters and code examples

`aaa/price-change-by-metro` · data API · AAA · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Returns price changes for all metro areas within a given state, showing the difference between current and historical prices for each fuel grade. Includes yesterday_change, week_ago_change, month_ago_change, and.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "aaa/price-change-by-metro", "state_code": "WA"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('aaa/price-change-by-metro', {'state_code': 'WA'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("aaa/price-change-by-metro", {
  "state_code": "WA"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "aaa/price-change-by-metro", sandbase.Params{
	"state_code": "WA",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/aaa/price-change-by-metro` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `state_code` | string | yes | Two-letter US state code (e.g. TX, CA, NY, FL). All 50 states and DC are supported.  |

## Details

Returns gas and diesel changes since yesterday, last week, last month and last year for every metro area in a US state. It needs a two-letter `state_code` such as `WA`. Each metro lists changes for Regular, Mid-Grade, Premium and Diesel.

### Use cases

- Compare how fast Regular gas is moving in Bellingham, Bremerton and Olympia.
- Flag metros where `yesterday_change` shows a sudden jump or drop.
- Chart month over month and year over year fuel trends for a state.
- Add local fuel trends to a logistics or fleet dashboard.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/aaa/price-change-by-metro" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"state_code": "WA"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `state_code` | string | Yes | Two-letter US state code (e.g. TX, CA, NY, FL). All 50 states and DC are supported. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "metro_price_changes": [
      {
        "changes": {
          "Diesel": {
            "month_ago_change": -0.179,
            "week_ago_change": -0.04,
            "year_ago_change": 2.101,
            "yesterday_change": -0.064
          },
          "Mid-Grade": {
            "month_ago_change": -0.349,
            "week_ago_change": 0.069,
            "year_ago_change": 1.144,
            "yesterday_change": -0.039
          },
          "Premium": {
            "month_ago_change": -0.332,
            "week_ago_change": 0.039,
            "year_ago_change": 0.995,
            "yesterday_change": 0.042
          },
          "Regular": {
            "month_ago_change": -0.356,
            "week_ago_change": -0.124,
            "year_ago_change": 1.012,
            "yesterday_change": -0.012
          }
        },
        "metro": "Bellingham"
      }
    ],
    "state": "Washington"
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.state` | Full name of the state the metros belong to, such as `Washington`. |
| `data.metro_price_changes[].metro` | Name of the metro area. |
| `data.metro_price_changes[].changes` | Changes for this metro, keyed by fuel grade: `Regular`, `Mid-Grade`, `Premium` and `Diesel`. |
| `data.metro_price_changes[].changes.Regular.yesterday_change` | Difference between the current Regular value and yesterday's value for this metro. |
| `data.metro_price_changes[].changes.Regular.week_ago_change / month_ago_change / year_ago_change` | Difference between the current Regular value and the value one week, one month or one year ago. |
| `data.metro_price_changes[].changes.Diesel.yesterday_change / week_ago_change / month_ago_change / year_ago_change` | The same set of changes for Diesel. |
| `data.metro_price_changes[].changes.Mid-Grade` | Same four change fields for Mid-Grade gas. |
| `data.metro_price_changes[].changes.Premium` | Same four change fields for Premium gas. |
| `status` | Shows `success` when the call worked. |

### Notes

- Pass the two-letter state code in `state_code`. The response returns the full state name in `data.state`.
- The fuel grades are object keys under `changes`, and `Mid-Grade` includes a hyphen.
- Change values are decimals with up to three places, such as `-0.012`. Negative values mean the current value is lower than the earlier one.

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/aaa/price-change-by-metro.json`](../../../catalog/models/aaa/price-change-by-metro.json) · Store page: https://www.sandbase.ai/model/aaa/price-change-by-metro
