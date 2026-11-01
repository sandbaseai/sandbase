# Shopee Search Category Facets

`shopee/search/facets` · api · Shopee

Get the category facets Shopee shows for a search keyword, to see which categories a query maps to on each site.

## Pricing

- **$0.027778 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "shopee/search/facets", "site": "TW", "keyword": "iphone case"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('shopee/search/facets', {'site': 'TW', 'keyword': 'iphone case'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("shopee/search/facets", {
  "site": "TW",
  "keyword": "iphone case"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "shopee/search/facets", sandbase.Params{
	"site": "TW",
	"keyword": "iphone case",
})
```

Same call via the path form: `POST /v1/api/shopee/search/facets` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `site` | string | yes | Shopee marketplace site. one of: `TW`, `ID`, `TH` |
| `keyword` | string | yes | Product search keyword.  |

## Details

Get the category facets Shopee shows for a search keyword, to see which categories a query maps to on each site.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/shopee/search/facets" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"site": "TW", "keyword": "iphone case"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `site` | string | Yes | Shopee marketplace site. |
| `keyword` | string | Yes | Product search keyword. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/shopee/search/facets.json`](../../../../catalog/models/shopee/search/facets.json) · Store page: https://www.sandbase.ai/model/shopee/search/facets
