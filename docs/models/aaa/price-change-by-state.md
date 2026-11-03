# AAA Price Change By State API: pricing, parameters and code examples

`aaa/price-change-by-state` · data API · AAA · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** async

Returns the price change (delta) for a state between the current price and historical averages (day, week, month, year) for all fuel grades. Positive values indicate prices have risen; negative values indicate prices.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "aaa/price-change-by-state", "state_code": "WA"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('aaa/price-change-by-state', {'state_code': 'WA'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("aaa/price-change-by-state", {
  "state_code": "WA"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "aaa/price-change-by-state", sandbase.Params{
	"state_code": "WA",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/aaa/price-change-by-state` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `state_code` | string | yes | Two-letter US state code (e.g. TX, CA, NY, FL). All 50 states and DC are supported.  |

## Details

Returns how AAA fuel prices in one US state have changed over the last day, week, month and year. The response covers Regular, Mid-Grade, Premium and Diesel. It needs a two-letter `state_code`.

### Use cases

- Show a dashboard card that tells drivers in a state whether gas got cheaper or more expensive this week.
- Compare year-over-year diesel change in a state to track fleet fuel costs.
- Flag states where `Regular` prices moved the most over the past month.
- Add a short price trend line to a travel or road-trip planning app.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/aaa/price-change-by-state" \
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
    "price_changes": {
      "Diesel": {
        "day_change": -0.017,
        "month_change": -0.123,
        "week_change": -0.013,
        "year_change": 2.272
      },
      "Mid-Grade": {
        "day_change": -0.013,
        "month_change": -0.32,
        "week_change": -0.114,
        "year_change": 0.879
      },
      "Premium": {
        "day_change": -0.01,
        "month_change": -0.309,
        "week_change": -0.093,
        "year_change": 0.896
      },
      "Regular": {
        "day_change": -0.011,
        "month_change": -0.297,
        "week_change": -0.112,
        "year_change": 0.907
      }
    },
    "state_code": "WA",
    "state_name": "Washington"
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.state_code / data.state_name` | The two-letter code and full name of the state the changes apply to. |
| `data.price_changes.Regular` | Price changes for Regular gas. Other grades use the same structure: `Mid-Grade`, `Premium` and `Diesel`. |
| `data.price_changes.Regular.day_change` | Change between the current price and the price one day ago. A negative value means the price fell. |
| `data.price_changes.Regular.week_change` | Change between the current price and the price one week ago. |
| `data.price_changes.Regular.month_change` | Change between the current price and the price one month ago. |
| `data.price_changes.Regular.year_change` | Change between the current price and the price one year ago. A positive value means the price rose. |
| `data.price_changes.Diesel.day_change / week_change / month_change / year_change` | The same four changes for Diesel. |
| `status` | Shows `success` when the call worked. |

### Notes

- Pass `state_code` as a two-letter US state code such as `WA`. DC is also supported.
- The changes are numeric differences, not percentages. Positive values mean prices rose and negative values mean they fell.
- For the current price levels, call [AAA State Gas Prices](/apis/aaa/state-gas-prices).
- For metro-level changes, call [AAA Price Change By Metro](/apis/aaa/price-change-by-metro).

### Pricing

$0.02 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/aaa/price-change-by-state.json`](../../../catalog/models/aaa/price-change-by-state.json) · Store page: https://www.sandbase.ai/model/aaa/price-change-by-state
