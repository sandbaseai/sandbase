# AAA Lowest State Prices API: pricing, parameters and code examples

`aaa/lowest-state-prices` · data API · AAA · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Returns all states sorted by lowest average regular gas price ascending. Useful for identifying the cheapest states for gasoline.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "aaa/lowest-state-prices"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('aaa/lowest-state-prices', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("aaa/lowest-state-prices", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "aaa/lowest-state-prices", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/aaa/lowest-state-prices` with the body above minus `model`.

## Details

Returns every US state with its average fuel figures per grade, sorted by regular gasoline from lowest to highest. It takes no input. Each row has values for `regular`, `mid_grade`, `premium` and `diesel`.

### Use cases

- Find the cheapest states for regular gasoline for a road trip or fuel budget.
- Rank states by `regular` in a dashboard or chart.
- Compare `diesel` and `premium` values across low-cost states for fleet planning.
- Track how the cheapest states change by saving the response on a schedule.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/aaa/lowest-state-prices" \
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
        "diesel": 5.491,
        "mid_grade": 3.8096,
        "premium": 4.2414,
        "regular": 3.3814,
        "state": "North Carolina"
      }
    ]
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.states[]` | List of states. The list is sorted by `regular`, lowest first. |
| `data.states[].state` | Full name of the state, for example `North Carolina`. |
| `data.states[].regular` | Average value for regular gasoline in the state. Rows are ordered by this value. |
| `data.states[].mid_grade` | Average value for mid-grade gasoline in the state. |
| `data.states[].premium` | Average value for premium gasoline in the state. |
| `data.states[].diesel` | Average value for diesel in the state. |
| `status` | Result of the call. The value is `success` when the request worked. |

### Notes

- This API has no parameters. Send an empty JSON object `{}`.
- Fuel values are plain numbers with up to four decimal places. The response does not show a currency or unit.

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/aaa/lowest-state-prices.json`](../../../catalog/models/aaa/lowest-state-prices.json) · Store page: https://www.sandbase.ai/model/aaa/lowest-state-prices
