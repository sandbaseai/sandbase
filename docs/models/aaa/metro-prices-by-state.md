# AAA Metro Prices By State API: pricing, parameters and code examples

`aaa/metro-prices-by-state` · data API · AAA · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Returns gas price data for all metro/city areas within a given state, including current and historical prices (yesterday, week ago, month ago, year ago) for all fuel grades. Each metro includes top-level.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "aaa/metro-prices-by-state", "state_code": "WA"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('aaa/metro-prices-by-state', {'state_code': 'WA'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("aaa/metro-prices-by-state", {
  "state_code": "WA"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "aaa/metro-prices-by-state", sandbase.Params{
	"state_code": "WA",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/aaa/metro-prices-by-state` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `state_code` | string | yes | Two-letter US state code (e.g. TX, CA, NY, FL). All 50 states and DC are supported.  |

## Details

Returns gas and diesel prices for every metro area in one US state. Each metro includes current prices and prices from yesterday, a week ago, a month ago and a year ago. The only input is a two-letter `state_code`.

### Use cases

- Compare regular gas prices across Washington metros to find the cheapest area.
- Track how diesel prices in each metro changed over the past week or month.
- Build a regional fuel cost estimate for a delivery or trucking route within one state.
- Chart year-over-year price changes for a state's metro areas.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/aaa/metro-prices-by-state" \
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
    "metros": [
      {
        "diesel": 6.929,
        "metro": "Bellingham",
        "mid_grade": 5.3111,
        "premium": 5.5942,
        "prices": {
          "current": {
            "Diesel": 6.929,
            "Mid-Grade": 5.3111,
            "Premium": 5.5942,
            "Regular": 4.9908
          },
          "month_ago": {
            "Diesel": 7.108,
            "Mid-Grade": 5.6597,
            "Premium": 5.9258,
            "Regular": 5.3468
          },
          "week_ago": {
            "Diesel": 6.9694,
            "Mid-Grade": 5.2417,
            "Premium": 5.5555,
            "Regular": 5.1146
          },
          "year_ago": {
            "Diesel": 4.8277,
            "Mid-Grade": 4.1671,
            "Premium": 4.5994,
            "Regular": 3.9785
          },
          "yesterday": {
            "Diesel": 6.9934,
            "Mid-Grade": 5.3498,
            "Premium": 5.5521,
            "Regular": 5.003
          }
        },
        "regular": 4.9908
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
| `data.state` | Full name of the state, such as `Washington`. |
| `data.metros[].metro` | Name of the metro or city area. |
| `data.metros[].regular / data.metros[].mid_grade / data.metros[].premium / data.metros[].diesel` | Current price for each fuel grade. These match the values in `prices.current`. |
| `data.metros[].prices.current.Regular / data.metros[].prices.current.Mid-Grade / data.metros[].prices.current.Premium / data.metros[].prices.current.Diesel` | Current price for each fuel grade in the metro. |
| `data.metros[].prices.yesterday` | Prices for the same four grades one day earlier. |
| `data.metros[].prices.week_ago` | Prices for the same four grades one week earlier. |
| `data.metros[].prices.month_ago` | Prices for the same four grades one month earlier. |
| `data.metros[].prices.year_ago` | Prices for the same four grades one year earlier. |
| `status` | Shows `success` when the call worked. |

### Notes

- Pass the postal abbreviation, such as `WA`, in `state_code`. The response returns the full state name in `data.state`.
- The `prices` object uses capitalized grade keys (`Regular`, `Mid-Grade`, `Premium`, `Diesel`). The top-level grade fields use lowercase keys with underscores.
- For one state-wide summary instead of a metro list, try [AAA State Gas Prices](/apis/aaa/state-gas-prices) or [AAA State Price Details](/apis/aaa/state-price-details).
- To rank metros by how much prices moved, see [AAA Price Change By Metro](/apis/aaa/price-change-by-metro).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/aaa/metro-prices-by-state.json`](../../../catalog/models/aaa/metro-prices-by-state.json) · Store page: https://www.sandbase.ai/model/aaa/metro-prices-by-state
