# AAA Highest Recorded Prices API: pricing, parameters and code examples

`aaa/highest-recorded-prices` · data API · AAA · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Returns all-time highest recorded average gas prices for a specific state or nationally. If no state_code is provided, returns national records.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "aaa/highest-recorded-prices"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('aaa/highest-recorded-prices', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("aaa/highest-recorded-prices", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "aaa/highest-recorded-prices", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/aaa/highest-recorded-prices` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `state_code` | string |  | Two-letter US state code (e.g. TX, CA). Omitting returns national highest recorded prices.  |

## Details

Returns the all-time highest recorded average gas prices from AAA, with the date each record was set. It takes an optional two-letter `state_code`. Without it, the API returns national records.

### Use cases

- Compare today's gas price with the national record for regular unleaded gas.
- Show the record diesel price and its date in a fuel cost dashboard.
- Check how close a state's current average is to its all-time high.
- Add historical context to a news story about rising fuel prices.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/aaa/highest-recorded-prices" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `state_code` | string | No | Two-letter US state code (e.g. TX, CA). Omitting returns national highest recorded prices. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "highest_recorded": {
      "Diesel": {
        "date": "9/22/26",
        "price": "6.5276"
      },
      "Regular Unleaded": {
        "date": "6/14/22",
        "price": "5.0165"
      }
    },
    "location": "National"
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.location` | The area the records cover. The value is `National` when no `state_code` is sent. |
| `data.highest_recorded` | Map of fuel type names to record entries. The sample has two fuel types: Diesel and Regular Unleaded. Each entry holds a `price` and a `date`. |
| `data.highest_recorded.Diesel.price` | Record average price for Diesel, as a string. |
| `data.highest_recorded.Diesel.date` | Date the Diesel record was set, in `M/D/YY` format. |
| `status` | Shows `success` when the call worked. |

### Notes

- Prices are returned as strings with four decimal places. Convert them to numbers before you do math.
- Pass a two-letter code such as `TX` or `CA` in `state_code` to get records for one state.
- To compare a record with current prices, call [AAA National Average](/apis/aaa/national-average) or [AAA State Gas Prices](/apis/aaa/state-gas-prices).
- The call runs asynchronously. Read the result from `outputs[0].data` after the task completes.

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/aaa/highest-recorded-prices.json`](../../../catalog/models/aaa/highest-recorded-prices.json) · Store page: https://www.sandbase.ai/model/aaa/highest-recorded-prices
