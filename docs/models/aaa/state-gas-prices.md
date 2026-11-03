# AAA State Gas Prices API: pricing, parameters and code examples

`aaa/state-gas-prices` · data API · AAA · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Returns current average gas prices for all 50 US states plus DC across all four fuel grades (Regular, Mid-Grade, Premium, Diesel). States are listed in alphabetical order by full state name.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "aaa/state-gas-prices"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('aaa/state-gas-prices', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("aaa/state-gas-prices", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "aaa/state-gas-prices", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/aaa/state-gas-prices` with the body above minus `model`.

## Details

Returns the current average cost of gas for each US state and DC, based on AAA data. Each row covers Regular, Mid-Grade, Premium and Diesel. The request takes no input.

### Use cases

- Compare Regular gas costs between states to find the cheapest and most expensive places to fill up.
- Estimate fuel costs for a road trip that crosses several states.
- Build a state-by-state fuel cost table or map for a dashboard.
- Track the gap between `diesel` and `regular` in each state for fleet planning.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/aaa/state-gas-prices" \
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
    "states": [
      {
        "diesel": 5.8537,
        "mid_grade": 4.1781,
        "premium": 4.5882,
        "regular": 3.73,
        "state": "Alabama"
      }
    ]
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.states[]` | One entry per state. The list is in alphabetical order by full state name. |
| `data.states[].state` | Full name of the state, for example `Alabama`. |
| `data.states[].regular` | Average cost of Regular gas in that state. |
| `data.states[].mid_grade` | Average cost of Mid-Grade gas in that state. |
| `data.states[].premium` | Average cost of Premium gas in that state. |
| `data.states[].diesel` | Average cost of diesel in that state. |
| `status` | Shows `success` when the call worked. |

### Notes

- Send an empty JSON object `{}` as the request body. There are no parameters.
- Fuel values are plain numbers, such as `3.73` or `5.8537`.
- For the US-wide average, call [AAA National Average](/apis/aaa/national-average).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/aaa/state-gas-prices.json`](../../../catalog/models/aaa/state-gas-prices.json) · Store page: https://www.sandbase.ai/model/aaa/state-gas-prices
