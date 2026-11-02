# Financial Datasets Institutional Holdings API: pricing, parameters and code examples

`financial-datasets/institutional-holdings` · data API · Financial Datasets · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

13F institutional holdings of a US stock by ticker: holder, shares, value and report period.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "financial-datasets/institutional-holdings", "ticker": "AAPL"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('financial-datasets/institutional-holdings', {'ticker': 'AAPL'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("financial-datasets/institutional-holdings", {
  "ticker": "AAPL"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "financial-datasets/institutional-holdings", sandbase.Params{
	"ticker": "AAPL",
})
```

Same call via the path form: `POST /v1/api/financial-datasets/institutional-holdings` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of holdings to return.  |
| `cursor` | string |  | Opaque pagination cursor from a previous response's next_page_url.  |
| `ticker` | string | yes | Stock ticker, e.g. `AAPL`.  |

## Details

13F institutional holdings of a US stock by ticker: holder, shares, value and report period.

The result is returned in `outputs[0].data` as the official Financial Datasets API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/financial-datasets/institutional-holdings" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"ticker": "AAPL", "limit": 5}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `ticker` | string | Yes | Stock ticker, e.g. `AAPL`. |
| `limit` | integer | No | Maximum number of holdings to return. |
| `cursor` | string | No | Opaque pagination cursor from a previous response's next_page_url. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/financial-datasets/institutional-holdings.json`](../../../catalog/models/financial-datasets/institutional-holdings.json) · Store page: https://www.sandbase.ai/model/financial-datasets/institutional-holdings
