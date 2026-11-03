# AAA State Price Details API: pricing, parameters and code examples

`aaa/state-price-details` · data API · AAA · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Returns detailed gas price data for a specific state including current prices for all fuel grades, historical averages (yesterday, week ago, month ago, year ago), and all-time highest recorded prices with their dates.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "aaa/state-price-details", "state_code": "WA"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('aaa/state-price-details', {'state_code': 'WA'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("aaa/state-price-details", {
  "state_code": "WA"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "aaa/state-price-details", sandbase.Params{
	"state_code": "WA",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/aaa/state-price-details` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `state_code` | string | yes | Two-letter US state code (e.g. TX, CA, NY, FL). All 50 states and DC are supported.  |

## Details

Returns AAA gas prices for one US state. Each fuel grade has a current price and past prices from yesterday, a week ago, a month ago and a year ago, plus the highest recorded price with its date. Send a two-letter `state_code`.

### Use cases

- Show the current Regular and Diesel price for a state in a fuel cost calculator.
- Compare today's Washington price with the price a month ago and a year ago to chart a trend.
- Check how far current diesel prices sit below the highest recorded diesel price for a state.
- Compare Regular, Mid-Grade and Premium prices in a state to estimate the cost of a higher grade.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/aaa/state-price-details" \
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
    "highest_recorded": {
      "Diesel": {
        "date": "9/23/26",
        "price": "7.4697"
      },
      "Regular Unleaded": {
        "date": "5/20/26",
        "price": "5.7887"
      }
    },
    "prices": {
      "Diesel": {
        "current": 7.2512,
        "month_ago": 7.3739,
        "week_ago": 7.2642,
        "year_ago": 4.9787,
        "yesterday": 7.2685
      },
      "Mid-Grade": {
        "current": 5.4442,
        "month_ago": 5.7645,
        "week_ago": 5.5587,
        "year_ago": 4.5651,
        "yesterday": 5.4577
      },
      "Premium": {
        "current": 5.7146,
        "month_ago": 6.0237,
        "week_ago": 5.8074,
        "year_ago": 4.8184,
        "yesterday": 5.7243
      },
      "Regular": {
        "current": 5.1925,
        "month_ago": 5.4891,
        "week_ago": 5.3047,
        "year_ago": 4.2855,
        "yesterday": 5.203
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
| `data.state_code / data.state_name` | The two-letter code and full name of the state the prices describe. |
| `data.prices.Regular.current` | Current price for Regular fuel in the state. Mid-Grade, Premium and Diesel use the same structure under `data.prices`. |
| `data.prices.Diesel.current` | Current price for Diesel in the state. |
| `data.prices.Regular.yesterday / data.prices.Regular.week_ago / data.prices.Regular.month_ago / data.prices.Regular.year_ago` | Regular price at each earlier point in time. The other grades have the same keys, so you can compare change over time. |
| `data.highest_recorded` | Highest recorded price for each fuel grade, with the date it was recorded. Each entry holds a `price` string and a `date` string in `M/D/YY` format. |
| `data.highest_recorded.Diesel.price / date` | Highest recorded Diesel price and the date it was recorded. |
| `status` | Shows `success` when the call worked. |

### Notes

- Use the two-letter postal code for `state_code`, such as `WA`. The description says all 50 states and DC are supported.
- Current and past prices under `data.prices` are numbers. Prices under `data.highest_recorded` are strings.
- The grade names differ between sections: `data.prices` uses `Regular`, while `data.highest_recorded` labels the regular grade `Regular Unleaded`. Mid-Grade and Premium appear only under `data.prices`.
- For city-level prices in a state, call [AAA Metro Prices By State](/apis/aaa/metro-prices-by-state). For a national figure, call [AAA National Average](/apis/aaa/national-average).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/aaa/state-price-details.json`](../../../catalog/models/aaa/state-price-details.json) · Store page: https://www.sandbase.ai/model/aaa/state-price-details
