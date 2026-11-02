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

The daily policy rate of one central bank: one row per calendar day, newest first, 10 rows per page. A rate change appears on the first day the new rate is in effect.

The response is the official Financial Datasets API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/financial-datasets/macro-interest-rates" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"bank": "FED"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `bank` | string | Yes | The central bank code, e.g. FED, ECB, BOJ. Use the /macro/interest-rates/banks endpoint to get the list of available banks. |
| `cursor` | string | No | Opaque pagination cursor from a previous response's next_page_url. When provided, all other query parameters are ignored: the cursor carries the original reques |
| `end_date` | string | No | The last date to return, inclusive, in YYYY-MM-DD format. Defaults to today. |
| `start_date` | string | No | The first date to return, inclusive, in YYYY-MM-DD format. Defaults to five years before end_date when both dates are omitted; omit it with an end_date to get a |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/financial-datasets/macro-interest-rates.json`](../../../catalog/models/financial-datasets/macro-interest-rates.json) · Store page: https://www.sandbase.ai/model/financial-datasets/macro-interest-rates
