# AAA Ev Charging Prices API: pricing, parameters and code examples

`aaa/ev-charging-prices` · data API · AAA · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Returns national and per-state EV charging price data including cost per kWh and total charger counts for each state. Data sourced from a public Google Sheets dataset maintained by AAA.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "aaa/ev-charging-prices"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('aaa/ev-charging-prices', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("aaa/ev-charging-prices", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "aaa/ev-charging-prices", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/aaa/ev-charging-prices` with the body above minus `model`.

## Details

Returns the EV charging cost per kWh and the total number of chargers for each location, with one row per state. The request takes no input.

### Use cases

- Compare the cost per kWh of EV charging across states.
- Rank states by total charger count to see where charging stations are most common.
- Estimate the cost of a full charge in a state by multiplying `ev_costperkwh` by battery size in kWh.
- Feed charging costs into a trip planning or fleet budgeting tool.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/aaa/ev-charging-prices" \
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
    "ev_data": [
      {
        "LOCATION_ID": "Alaska",
        "LOCATION_NAME": "Alaska",
        "LOCATION_STATE": "AK",
        "LOCATION_TYPE": "ST",
        "ev_costperkwh": "0.459",
        "ev_totalchargers": "92"
      }
    ]
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.ev_data[]` | List of locations. Each item holds the charging cost and charger count for one location. |
| `data.ev_data[].LOCATION_NAME / data.ev_data[].LOCATION_ID` | Name of the location, such as `Alaska`. In the sample rows both fields hold the same value. |
| `data.ev_data[].LOCATION_STATE` | Two-letter state code, such as `AK` or `AL`. |
| `data.ev_data[].LOCATION_TYPE` | Location type code. The sample rows show `ST` for each state. |
| `data.ev_data[].ev_costperkwh` | Charging cost per kWh for the location, returned as a string such as `0.459`. |
| `data.ev_data[].ev_totalchargers` | Total number of chargers for the location, returned as a string such as `1008`. |
| `status` | Result of the call. The value is `success` when the data was returned. |

### Notes

- Values such as `ev_costperkwh` and `ev_totalchargers` come back as strings. Convert them to numbers before sorting or doing math.
- Use `LOCATION_TYPE` to filter rows by type, and `LOCATION_STATE` to match a row to a state code.
- For gasoline figures instead of EV charging, call [AAA National Average](/apis/aaa/national-average).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/aaa/ev-charging-prices.json`](../../../catalog/models/aaa/ev-charging-prices.json) · Store page: https://www.sandbase.ai/model/aaa/ev-charging-prices
