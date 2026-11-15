# Yahoo! Auctions Japan Compare Market Price API: pricing, parameters and code examples

`yahoo-auctions-jp/compare-market-price` · data API · Yahoo! Auctions Japan · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Compound endpoint that identifies active listings priced significantly below the 180-day market average (less than 80% of average).

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "yahoo-auctions-jp/compare-market-price", "query": "iPhone"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('yahoo-auctions-jp/compare-market-price', {'query': 'iPhone'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("yahoo-auctions-jp/compare-market-price", {
  "query": "iPhone"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "yahoo-auctions-jp/compare-market-price", sandbase.Params{
	"query": "iPhone",
})
```

Same call via the path form: `POST /v1/api/yahoo-auctions-jp/compare-market-price` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Search keyword (e.g., 'Nintendo Switch')  |

## Details

Compound endpoint that identifies active listings priced significantly below the 180-day market average (less than 80% of average).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "yahoo-auctions-jp/compare-market-price", "query": "iPhone"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search keyword (e.g., 'Nintendo Switch') |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/yahoo-auctions-jp/compare-market-price.json`](../../../catalog/models/yahoo-auctions-jp/compare-market-price.json) · Store page: https://www.sandbase.ai/model/yahoo-auctions-jp/compare-market-price
