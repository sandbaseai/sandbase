# Financial Datasets Get Latest Interest Rates API: pricing, parameters and code examples

`financial-datasets/macro-interest-rates-snapshot` · data API · Financial Datasets · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

The newest published policy rate of every central bank we cover, one row per bank with the date it is in effect. Pass bank to get one bank only.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "financial-datasets/macro-interest-rates-snapshot"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('financial-datasets/macro-interest-rates-snapshot', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("financial-datasets/macro-interest-rates-snapshot", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "financial-datasets/macro-interest-rates-snapshot", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/financial-datasets/macro-interest-rates-snapshot` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `bank` | string |  | Optional central bank code (e.g., FED, ECB, BOJ) to return one bank only. Use the /macro/interest-rates/banks endpoint to get a list of available banks.  |

## Details

Returns the newest published policy interest rate for each central bank covered, one row per bank. It needs no input, and you can pass the optional `bank` code to get a single bank.

### Use cases

- Show a dashboard of current policy rates for major central banks side by side.
- Compare the Bank of Canada, Bank of England and Bank of Japan rates in a single call.
- Feed the latest rate for one bank into a loan or bond pricing model.
- Check which central banks changed their rate most recently by sorting on `date`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/financial-datasets/macro-interest-rates-snapshot" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `bank` | string | No | Optional central bank code (e.g., FED, ECB, BOJ) to return one bank only. Use the /macro/interest-rates/banks endpoint to get a list of available banks. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "interest_rates": [
    {
      "bank": "BOC",
      "date": "2026-10-26",
      "name": "Bank of Canada",
      "rate": 2.25
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `interest_rates[]` | One row per central bank with its latest policy rate. |
| `interest_rates[].bank` | Short central bank code, such as `BOC`, `BOE` or `BOJ`. Use this value as the `bank` parameter. |
| `interest_rates[].name` | Full name of the central bank, such as `Bank of Canada`. |
| `interest_rates[].rate` | The policy rate for that bank. Values like `2.25` and `3.75` look like percentages. |
| `interest_rates[].date` | Date the rate is in effect, in `YYYY-MM-DD` format. |

### Notes

- Send an empty body `{}` to get every bank, or set `bank` to a code such as `BOJ` to get one row.
- Get valid `bank` codes from the `/macro/interest-rates/banks` endpoint named in the parameter description.
- For past rate changes, call [Financial Datasets Get Historical Interest Rates](/apis/financial-datasets/macro-interest-rates).

### Pricing

$0.02 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/financial-datasets/macro-interest-rates-snapshot.json`](../../../catalog/models/financial-datasets/macro-interest-rates-snapshot.json) · Store page: https://www.sandbase.ai/model/financial-datasets/macro-interest-rates-snapshot
