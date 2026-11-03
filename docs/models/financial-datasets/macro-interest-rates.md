# Financial Datasets Get Historical Interest Rates API: pricing, parameters and code examples

`financial-datasets/macro-interest-rates` · data API · Financial Datasets · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

The daily policy rate of one central bank: one row per calendar day, newest first, 10 rows per page. A rate change appears on the first day the new rate is in effect.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "financial-datasets/macro-interest-rates", "bank": "FED"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('financial-datasets/macro-interest-rates', {'bank': 'FED'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("financial-datasets/macro-interest-rates", {
  "bank": "FED"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "financial-datasets/macro-interest-rates", sandbase.Params{
	"bank": "FED",
})
```

Same call via the path form: `POST /v1/api/financial-datasets/macro-interest-rates` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `bank` | string | yes | The central bank code, e.g. FED, ECB, BOJ. Use the /macro/interest-rates/banks endpoint to get the list of available banks.  |
| `cursor` | string |  | Opaque pagination cursor from a previous response's next_page_url. When provided, all other query parameters are ignored: the cursor carries the original request's filters. Treat it as opaque; do not construct or…  |
| `end_date` | string |  | The last date to return, inclusive, in YYYY-MM-DD format. Defaults to today.  |
| `start_date` | string |  | The first date to return, inclusive, in YYYY-MM-DD format. Defaults to five years before end_date when both dates are omitted; omit it with an end_date to get all available history through that date.  |

## Details

Returns the daily policy interest rate of one central bank, one row per calendar day, newest first. It needs a central bank code in `bank`, such as `FED`, `ECB` or `BOJ`.

### Use cases

- Chart the Federal Reserve policy rate over the past five years.
- Find the exact date a central bank changed its rate by scanning for a change in `rate`.
- Join daily policy rates to a price or earnings series to study how rate levels line up with market moves.
- Compare the policy rate on a given day across several banks by calling once per `bank`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/financial-datasets/macro-interest-rates" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"bank": "FED"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `bank` | string | Yes | The central bank code, e.g. FED, ECB, BOJ. Use the /macro/interest-rates/banks endpoint to get the list of available banks. |
| `cursor` | string | No | Opaque pagination cursor from a previous response's next_page_url. When provided, all other query parameters are ignored: the cursor carries the original request's filters. Treat it as opaque; do not construct or modify  |
| `end_date` | string | No | The last date to return, inclusive, in YYYY-MM-DD format. Defaults to today. |
| `start_date` | string | No | The first date to return, inclusive, in YYYY-MM-DD format. Defaults to five years before end_date when both dates are omitted; omit it with an end_date to get all available history through that date. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "interest_rates": [
    {
      "bank": "FED",
      "date": "2026-10-27",
      "name": "Federal Reserve",
      "rate": 3.875
    }
  ],
  "next_page_url": "https://api.financialdatasets.ai/macro/interest-rates?cursor=5hVg4qj4Wsz6weUrOtt…"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `interest_rates[]` | One row per calendar day for the requested bank, newest first. |
| `interest_rates[].bank` | The central bank code for the row, for example `FED`. |
| `interest_rates[].name` | The full name of the central bank, for example `Federal Reserve`. |
| `interest_rates[].date` | The calendar day of the rate in `YYYY-MM-DD` format. |
| `interest_rates[].rate` | The policy rate in effect on that day, for example `3.875`. |
| `next_page_url` | A URL that carries a `cursor` for the next page of older rows. |

### Notes

- Each page holds 10 rows. To get the next page, pass the `cursor` value from `next_page_url` as the `cursor` parameter. The cursor is opaque, so do not edit it.
- When you send `cursor`, the API ignores all other parameters because the cursor already carries the original filters.
- Use `start_date` and `end_date` in `YYYY-MM-DD` format to limit the range. If you omit both, the range covers the five years before today.
- For only the latest rates, call [Financial Datasets Get Latest Interest Rates](/apis/financial-datasets/macro-interest-rates-snapshot).

### Pricing

$0.02 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/financial-datasets/macro-interest-rates.json`](../../../catalog/models/financial-datasets/macro-interest-rates.json) · Store page: https://www.sandbase.ai/model/financial-datasets/macro-interest-rates
