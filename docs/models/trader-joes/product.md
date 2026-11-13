# Trader Joe's Product API: pricing, parameters and code examples

`trader-joes/product` · data API · Trader Joe's · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Get a Trader Joe's product by product ID with name, price, size, description, ingredients, nutrition and dietary tags.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "trader-joes/product", "product_id": "097234"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('trader-joes/product', {'product_id': '097234'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("trader-joes/product", {
  "product_id": "097234"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "trader-joes/product", sandbase.Params{
	"product_id": "097234",
})
```

Same call via the path form: `POST /v1/api/trader-joes/product` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `store_id` | string |  | Parameter defines the Trader Joe's store to check the product availability in. It's the number at the end of the store page URL on the Trader Joe's store locator (e.g., `454` in…  |
| `product_id` | string | yes | Parameter defines the Trader Joe's product to get results for. It's the number at the end of the product page URL (e.g., `080794` in `https://www.traderjoes.com/home/products/pdp/cold-brew-coffee-black-080794`).  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |

## Details

Get a Trader Joe's product by product ID with name, price, size, description, ingredients, nutrition and dietary tags.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/trader-joes/product" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"product_id": "097234"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `product_id` | string | Yes | Parameter defines the Trader Joe's product to get results for. It's the number at the end of the product page URL (e.g., `080794` in `https://www.traderjoes.com/home/products/pdp/cold-brew-coffee-black-080794`). |
| `store_id` | string | No | Parameter defines the Trader Joe's store to check the product availability in. It's the number at the end of the store page URL on the Trader Joe's store locator (e.g., `454` in `https://locations.traderjoes.com/tx/austin/454/`). When the p |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/trader-joes/product.json`](../../../catalog/models/trader-joes/product.json) · Store page: https://www.sandbase.ai/model/trader-joes/product
