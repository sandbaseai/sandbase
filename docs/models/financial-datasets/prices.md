# Financial Datasets Get Historical Stock Prices API: pricing, parameters and code examples

`financial-datasets/prices` · data API · Financial Datasets · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Get Historical Stock Prices from Financial Datasets. Returns the official Financial Datasets API response unchanged.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "financial-datasets/prices"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('financial-datasets/prices', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("financial-datasets/prices", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "financial-datasets/prices", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/financial-datasets/prices` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Opaque pagination cursor from a previous response's next_page_url. When provided, all other query parameters are ignored: the cursor carries the original request's filters. Treat it as opaque; do not construct or…  |
| `ticker` | string |  | The stock ticker symbol (e.g. AAPL, MSFT).  |
| `end_date` | string |  | The end date for the price data (format: YYYY-MM-DD). Provider reference (supplier schema): `{"format":"date","type":"string"}`.  |
| `interval` | string |  | The time interval for the price data. Provider reference (supplier schema): `{"enum":["day","week","month","year"],"type":"string"}`.  |
| `start_date` | string |  | The start date for the price data (format: YYYY-MM-DD). Provider reference (supplier schema): `{"format":"date","type":"string"}`.  |
| `interval_multiplier` | string |  | interval_multiplier  |

## Details

Get Historical Stock Prices from Financial Datasets. Returns the official Financial Datasets API response unchanged.

The response is the official Financial Datasets API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/financial-datasets/prices" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"ticker": "AAPL", "interval": "day", "interval_multiplier": "1", "start_date": "2026-10-01", "end_date": "2026-10-10"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | string | No | Opaque pagination cursor from a previous response's next_page_url. When provided, all other query parameters are ignored: the cursor carries the original reques |
| `end_date` | string | No | The end date for the price data (format: YYYY-MM-DD). Provider reference (supplier schema): `{"format":"date","type":"string"}`. |
| `interval` | string | No | The time interval for the price data. Provider reference (supplier schema): `{"enum":["day","week","month","year"],"type":"string"}`. |
| `interval_multiplier` | string | No | interval_multiplier |
| `start_date` | string | No | The start date for the price data (format: YYYY-MM-DD). Provider reference (supplier schema): `{"format":"date","type":"string"}`. |
| `ticker` | string | No | The stock ticker symbol (e.g. AAPL, MSFT). |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/financial-datasets/prices.json`](../../../catalog/models/financial-datasets/prices.json) · Store page: https://www.sandbase.ai/model/financial-datasets/prices
