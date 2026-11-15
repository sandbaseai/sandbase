# H&M Product Detail API: pricing, parameters and code examples

`hm/product-detail` · data API · H&M · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Fetch product details including pricing, availability, color variants, and images for a given article code or product URL. Returns full variant information with all color options, stock states, and image galleries. Either article_code or url must be provided.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "hm/product-detail"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('hm/product-detail', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("hm/product-detail", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "hm/product-detail", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/hm/product-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string |  | Full product URL (e.g. 'https://www2.hm.com/en_us/productpage.0685816001.html'). Either article_code or url must be provided.  |
| `article_code` | string |  | Article code (e.g. '0685816001', '1347416001'). Either article_code or url must be provided.  |

## Details

Fetch product details including pricing, availability, color variants, and images for a given article code or product URL. Returns full variant information with all color options, stock states, and image galleries. Either article_code or url must be provided.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "hm/product-detail", "url": "", "article_code": "1347416001"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `article_code` | string | No | Article code (e.g. '0685816001', '1347416001'). Either article_code or url must be provided. |
| `url` | string | No | Full product URL (e.g. 'https://www2.hm.com/en_us/productpage.0685816001.html'). Either article_code or url must be provided. |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/hm/product-detail.json`](../../../catalog/models/hm/product-detail.json) · Store page: https://www.sandbase.ai/model/hm/product-detail
