# H&M Product Details Kr API: pricing, parameters and code examples

`hm/product-details-kr` · data API · H&M · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Get full product details for a Korean H&M product including all color variants, size-level online availability, images with type labels, KRW prices (regular, current, member), and stock state.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "hm/product-details-kr"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('hm/product-details-kr', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("hm/product-details-kr", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "hm/product-details-kr", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/hm/product-details-kr` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string |  | Korean H&M product URL (must contain /ko_kr/). Either article_code or url must be provided.  |
| `article_code` | string |  | 10-digit article code (e.g. '1309848011'). Either article_code or url must be provided.  |

## Details

Get full product details for a Korean H&M product including all color variants, size-level online availability, images with type labels, KRW prices (regular, current, member), and stock state.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "hm/product-details-kr", "url": "", "article_code": "1309848011"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `article_code` | string | No | 10-digit article code (e.g. '1309848011'). Either article_code or url must be provided. |
| `url` | string | No | Korean H&M product URL (must contain /ko_kr/). Either article_code or url must be provided. |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/hm/product-details-kr.json`](../../../catalog/models/hm/product-details-kr.json) · Store page: https://www.sandbase.ai/model/hm/product-details-kr
