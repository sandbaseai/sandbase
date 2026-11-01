# IMDb Streaming Picks

`imdb/streaming-picks-query` · api · IMDb

Get IMDb streaming picks for Prime Video using selected language and country preferences. Use it to explore streaming titles for discovery, catalog review, or watchlist research.

## Pricing

- **$0.006944 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "imdb/streaming-picks-query"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('imdb/streaming-picks-query', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("imdb/streaming-picks-query", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "imdb/streaming-picks-query", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/imdb/streaming-picks-query` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `languageCountry` | string |  | Language and country preferences. one of: `en_US`, `fr_CA`, `fr_FR`, `de_DE`, `hi_IN`, `it_IT`, `pt_BR`, `es_ES`, `es_US`, `es_MX`; default `"en_US"` |

## Details

Get IMDb streaming picks for Prime Video using selected language and country preferences. Use it to explore streaming titles for discovery, catalog review, or watchlist research.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/imdb/streaming-picks-query" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `languageCountry` | string | No | Language and country preferences. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/imdb/streaming-picks-query.json`](../../../catalog/models/imdb/streaming-picks-query.json) · Store page: https://www.sandbase.ai/model/imdb/streaming-picks-query
