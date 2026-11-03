# AAA Lowest Metro Prices API: pricing, parameters and code examples

`aaa/lowest-metro-prices` · data API · AAA · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Returns metro areas within a state sorted by lowest regular gas price ascending. Useful for finding the cheapest metros within a state.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "aaa/lowest-metro-prices", "state_code": "WA"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('aaa/lowest-metro-prices', {'state_code': 'WA'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("aaa/lowest-metro-prices", {
  "state_code": "WA"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "aaa/lowest-metro-prices", sandbase.Params{
	"state_code": "WA",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/aaa/lowest-metro-prices` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `state_code` | string | yes | Two-letter US state code (e.g. TX, CA, NY, FL). All 50 states and DC are supported.  |

## Details

Returns the metro areas in one US state, sorted by lowest regular gas price first. Each metro includes current prices for four fuel grades and past prices from yesterday, a week ago, a month ago and a year ago. The only input is a two-letter `state_code`.

### Use cases

- Find the cheapest metro area in a state for regular gas.
- Compare regular, premium and diesel prices across metros in one state for a fuel cost report.
- Track how much a metro's gas price has risen compared with last week, last month or last year.
- Rank a state's metros in a travel or commuting cost tool.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/aaa/lowest-metro-prices" \
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
        "diesel": 6.849,
        "metro": "Clarkson",
        "mid_grade": 0,
        "premium": 4.859,
        "prices": {
          "current": {
            "Diesel": 6.849,
            "Mid-Grade": 0,
            "Premium": 4.859,
            "Regular": 4.779
          },
          "month_ago": {
            "Diesel": 6.999,
            "Mid-Grade": 0,
            "Premium": 5.7657,
            "Regular": 5.049
          },
          "week_ago": {
            "Diesel": 6.899,
            "Mid-Grade": 5.549,
            "Premium": 5.299,
            "Regular": 4.979
          },
          "year_ago": {
            "Diesel": 4.519,
            "Mid-Grade": 0,
            "Premium": 4.404,
            "Regular": 3.844
          },
          "yesterday": {
            "Diesel": 6.849,
            "Mid-Grade": 5.349,
            "Premium": 4.849,
            "Regular": 4.7723
          }
        },
        "regular": 4.779
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
| `data.state` | Full name of the state for the code you sent, such as `Washington`. |
| `data.metros[].metro` | Name of the metro area, such as `Spokane` or `Mount Vernon-Anacortes`. |
| `data.metros[].regular` | Current regular gas price for the metro. The list is sorted by this value, lowest first. |
| `data.metros[].mid_grade / data.metros[].premium / data.metros[].diesel` | Current price for each other fuel grade. A value of `0` appears where no mid-grade price is given. |
| `data.metros[].prices.current` | Current prices for `Regular`, `Mid-Grade`, `Premium` and `Diesel`. These match the top-level price fields. |
| `data.metros[].prices.yesterday` | Prices for the same four grades one day earlier. |
| `data.metros[].prices.week_ago / data.metros[].prices.month_ago` | Prices for the same four grades one week and one month earlier. Compare them with `current` to see short-term change. |
| `data.metros[].prices.year_ago` | Prices for the same four grades one year earlier. Use it for year-over-year comparison. |

### Notes

- Send a two-letter code such as `WA` in `state_code`. The API accepts all 50 states and DC.
- A price of `0` means no value was given for that grade in that period, not a free price.
- For the full list of metros in a state without the lowest-first ranking, use [AAA Metro Prices By State](/apis/aaa/metro-prices-by-state).
- For statewide prices, call [AAA State Gas Prices](/apis/aaa/state-gas-prices).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/aaa/lowest-metro-prices.json`](../../../catalog/models/aaa/lowest-metro-prices.json) · Store page: https://www.sandbase.ai/model/aaa/lowest-metro-prices
