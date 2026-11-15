# H&M Related Products Kr API: pricing, parameters and code examples

`hm/related-products-kr` · data API · H&M · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Get styling and pairing recommendations for a Korean H&M product.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "hm/related-products-kr", "article_code": "1309848011"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('hm/related-products-kr', {'article_code': '1309848011'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("hm/related-products-kr", {
  "article_code": "1309848011"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "hm/related-products-kr", sandbase.Params{
	"article_code": "1309848011",
})
```

Same call via the path form: `POST /v1/api/hm/related-products-kr` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `article_code` | string | yes | 10-digit article code to get recommendations for (e.g. '1309848011').  |

## Details

Get styling and pairing recommendations for a Korean H&M product.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "hm/related-products-kr", "article_code": "1309848011"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `article_code` | string | Yes | 10-digit article code to get recommendations for (e.g. '1309848011'). |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/hm/related-products-kr.json`](../../../catalog/models/hm/related-products-kr.json) · Store page: https://www.sandbase.ai/model/hm/related-products-kr
