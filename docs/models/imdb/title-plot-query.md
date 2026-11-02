# IMDb Plot Summary API: pricing, parameters and code examples

`imdb/title-plot-query` · data API · IMDb · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.007143 per call (free daily quota) · **Modes:** sync

Get IMDb plot information for a title ID using selected language and country preferences. Use it to review a movie or series storyline or enrich title descriptions.

## Pricing

- **$0.007143 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "imdb/title-plot-query", "id": "tt0111161"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('imdb/title-plot-query', {'id': 'tt0111161'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("imdb/title-plot-query", {
  "id": "tt0111161"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "imdb/title-plot-query", sandbase.Params{
	"id": "tt0111161",
})
```

Same call via the path form: `POST /v1/api/imdb/title-plot-query` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string | yes | The IMDb title identifier in tt<digits> format.  |
| `languageCountry` | string |  | Language and country preferences. one of: `en_US`, `fr_CA`, `fr_FR`, `de_DE`, `hi_IN`, `it_IT`, `pt_BR`, `es_ES`, `es_US`, `es_MX`; default `"en_US"` |

## Details

Get IMDb plot information for a title ID using selected language and country preferences. Use it to review a movie or series storyline or enrich title descriptions.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/imdb/title-plot-query" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"id": "tt0111161"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string | Yes | The IMDb title identifier in tt<digits> format. |
| `languageCountry` | string | No | Language and country preferences. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/imdb/title-plot-query.json`](../../../catalog/models/imdb/title-plot-query.json) · Store page: https://www.sandbase.ai/model/imdb/title-plot-query
