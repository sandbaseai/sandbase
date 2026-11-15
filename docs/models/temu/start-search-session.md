# Temu Start Search Session API: pricing, parameters and code examples

`temu/start-search-session` · data API · Temu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Start a paginated search session over Temu's product catalog.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "temu/start-search-session", "query": "wireless earbuds"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('temu/start-search-session', {'query': 'wireless earbuds'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("temu/start-search-session", {
  "query": "wireless earbuds"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "temu/start-search-session", sandbase.Params{
	"query": "wireless earbuds",
})
```

Same call via the path form: `POST /v1/api/temu/start-search-session` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Number of results to return per page (max 40). default `40` |
| `query` | string | yes | Search keyword (e.g. 'wireless earbuds', 'kitchen gadgets').  |
| `locale` | string |  | Locale/language code for localized results (e.g. 'en', 'it', 'de', 'fr', 'es'). Controls language of titles and currency of prices. default `"en"` |

## Details

Start a paginated search session over Temu's product catalog.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "temu/start-search-session", "limit": 40, "query": "wireless earbuds", "locale": "en"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search keyword (e.g. 'wireless earbuds', 'kitchen gadgets'). |
| `limit` | integer | No | Number of results to return per page (max 40). |
| `locale` | string | No | Locale/language code for localized results (e.g. 'en', 'it', 'de', 'fr', 'es'). Controls language of titles and currency of prices. |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/temu/start-search-session.json`](../../../catalog/models/temu/start-search-session.json) · Store page: https://www.sandbase.ai/model/temu/start-search-session
