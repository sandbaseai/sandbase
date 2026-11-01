# Yahoo Finance Company Profile

`yahoo-finance/company-profile` · api · Yahoo Finance

Obtain a detailed company profile including business summary, key executives, sector, industry, and financial metrics such as revenue, profit margins, and analyst recommendations. Returns structured modules:.

## Pricing

- **$0.05 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "yahoo-finance/company-profile", "symbol": "AAPL"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('yahoo-finance/company-profile', {'symbol': 'AAPL'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("yahoo-finance/company-profile", {
  "symbol": "AAPL"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "yahoo-finance/company-profile", sandbase.Params{
	"symbol": "AAPL",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/yahoo-finance/company-profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `symbol` | string | yes | Stock ticker symbol (e.g., AAPL).  |

## Details

Obtain a detailed company profile including business summary, key executives, sector, industry, and financial metrics such as revenue, profit margins, and analyst recommendations. Returns structured modules:.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/yahoo-finance/company-profile" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"symbol": "AAPL"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | string | Yes | Stock ticker symbol (e.g., AAPL). |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/yahoo-finance/company-profile.json`](../../../catalog/models/yahoo-finance/company-profile.json) · Store page: https://www.sandbase.ai/model/yahoo-finance/company-profile
