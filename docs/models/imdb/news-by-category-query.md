# IMDb News by Category API: pricing, parameters and code examples

`imdb/news-by-category-query` · data API · IMDb · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.006944 per call (free daily quota) · **Modes:** sync

Get IMDb news for a selected top, movie, TV, or celebrity category using language and country preferences. Use it to monitor entertainment news or research a specific category.

## Pricing

- **$0.006944 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "imdb/news-by-category-query", "category": "TOP"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('imdb/news-by-category-query', {'category': 'TOP'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("imdb/news-by-category-query", {
  "category": "TOP"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "imdb/news-by-category-query", sandbase.Params{
	"category": "TOP",
})
```

Same call via the path form: `POST /v1/api/imdb/news-by-category-query` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `category` | string | yes | News category to filter by. one of: `TOP`, `MOVIE`, `TV`, `CELEBRITY` |
| `languageCountry` | string |  | Language and country preferences. one of: `en_US`, `fr_CA`, `fr_FR`, `de_DE`, `hi_IN`, `it_IT`, `pt_BR`, `es_ES`, `es_US`, `es_MX`; default `"en_US"` |

## Details

Get IMDb news for a selected top, movie, TV, or celebrity category using language and country preferences. Use it to monitor entertainment news or research a specific category.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/imdb/news-by-category-query" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"category": "TOP"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `category` | string | Yes | News category to filter by. |
| `languageCountry` | string | No | Language and country preferences. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/imdb/news-by-category-query.json`](../../../catalog/models/imdb/news-by-category-query.json) · Store page: https://www.sandbase.ai/model/imdb/news-by-category-query
