# H&M Search Products Kr API: pricing, parameters and code examples

`hm/search-products-kr` · data API · H&M · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Search Korean H&M products by keyword.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "hm/search-products-kr", "query": "jeans"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('hm/search-products-kr', {'query': 'jeans'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("hm/search-products-kr", {
  "query": "jeans"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "hm/search-products-kr", sandbase.Params{
	"query": "jeans",
})
```

Same call via the path form: `POST /v1/api/hm/search-products-kr` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number for pagination (1-based). default `1` |
| `sort` | string |  | Sort order. Supported values: 'ascPrice' (lowest first), 'descPrice' (highest first). Omit for relevance.  |
| `query` | string | yes | Search keyword in Korean or English (e.g. 'jeans', '재킷', 'dress').  |
| `page_size` | integer |  | Number of products per page (max observed: 36). default `36` |

## Details

Search Korean H&M products by keyword.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "hm/search-products-kr", "page": 1, "sort": "", "query": "jeans", "page_size": 36}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search keyword in Korean or English (e.g. 'jeans', '재킷', 'dress'). |
| `page` | integer | No | Page number for pagination (1-based). |
| `page_size` | integer | No | Number of products per page (max observed: 36). |
| `sort` | string | No | Sort order. Supported values: 'ascPrice' (lowest first), 'descPrice' (highest first). Omit for relevance. |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/hm/search-products-kr.json`](../../../catalog/models/hm/search-products-kr.json) · Store page: https://www.sandbase.ai/model/hm/search-products-kr
