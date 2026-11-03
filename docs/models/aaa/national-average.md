# AAA National Average API: pricing, parameters and code examples

`aaa/national-average` · data API · AAA · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** async

Returns today's AAA national average gas price for all fuel grades (Regular, Mid-Grade, Premium, Diesel) with historical comparisons to yesterday, one week ago, one month ago, and one year ago. Includes the date the.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "aaa/national-average"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('aaa/national-average', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("aaa/national-average", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "aaa/national-average", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/aaa/national-average` with the body above minus `model`.

## Details

Returns the AAA national average gas price for Regular, Mid-Grade, Premium and Diesel. Each grade includes the current price and the prices from yesterday, one week ago, one month ago and one year ago. The API takes no input.

### Use cases

- Show a daily national gas price widget on a travel or fuel-cost site.
- Compare today's Diesel price with the price a year ago to track fleet fuel cost changes.
- Chart short-term moves in Regular gas by comparing `current`, `yesterday`, `week_ago` and `month_ago`.
- Estimate the price gap between Regular and Premium for a fuel budget tool.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/aaa/national-average" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "date": "11/2/26",
    "location": "National",
    "prices": {
      "Diesel": {
        "current": 6.2921,
        "month_ago": 6.3726,
        "week_ago": 6.3492,
        "year_ago": 3.684,
        "yesterday": 6.3039
      },
      "Mid-Grade": {
        "current": 4.66,
        "month_ago": 4.9161,
        "week_ago": 4.78,
        "year_ago": 3.5371,
        "yesterday": 4.6823
      },
      "Premium": {
        "current": 5.0644,
        "month_ago": 5.3073,
        "week_ago": 5.1819,
        "year_ago": 3.8957,
        "yesterday": 5.0807
      },
      "Regular": {
        "current": 4.1694,
        "month_ago": 4.3961,
        "week_ago": 4.2858,
        "year_ago": 3.0361,
        "yesterday": 4.1732
      }
    }
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.date` | Date of the prices, as a string such as `11/2/26`. |
| `data.location` | Area the prices cover. The value here is `National`. |
| `data.prices.Regular / data.prices.Mid-Grade / data.prices.Premium / data.prices.Diesel` | One object per fuel grade. Each holds the same set of price fields. |
| `data.prices.Regular.current` | Current national average price for that grade. Swap `Regular` for another grade key to read it. |
| `data.prices.Regular.yesterday` | National average price for that grade one day earlier. |
| `data.prices.Regular.week_ago` | National average price for that grade one week earlier. |
| `data.prices.Regular.month_ago` | National average price for that grade one month earlier. |
| `data.prices.Regular.year_ago` | National average price for that grade one year earlier. |
| `status` | Result status of the call. The value here is `success`. |

### Notes

- Send an empty JSON object `{}` as the request body. There are no parameters.
- Grade keys are `Regular`, `Mid-Grade`, `Premium` and `Diesel`. `Mid-Grade` contains a hyphen, so use bracket access in code.
- For prices by state, call [AAA State Gas Prices](/apis/aaa/state-gas-prices). For metro-level prices, call [AAA Metro Prices By State](/apis/aaa/metro-prices-by-state).

### Pricing

$0.02 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/aaa/national-average.json`](../../../catalog/models/aaa/national-average.json) · Store page: https://www.sandbase.ai/model/aaa/national-average
