# Opoint Search API: pricing, parameters and code examples

`opoint/search` · data API · Opoint · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.06 per call · **Modes:** async

Search global news by keyword, phrase, or boolean query with filters.

## Pricing

- **$0.06 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "opoint/search", "searchterm": "electric vehicles"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('opoint/search', {'searchterm': 'electric vehicles'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("opoint/search", {
  "searchterm": "electric vehicles"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "opoint/search", sandbase.Params{
	"searchterm": "electric vehicles",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/opoint/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `params` | object |  |   |
| `searchterm` | string | yes | Opoint search expression: keywords and 'quoted phrases', section prefixes (header:, summary:, body:, author:, url:), wildcards (spot*), proximity ('Trump Biden'~5), boolean AND / OR / ANDNOT, and filter ids from…  |

## Details

Search global news by keyword, phrase, or boolean query with filters.

---
Machine-readable: [`catalog/models/opoint/search.json`](../../../catalog/models/opoint/search.json) · Store page: https://www.sandbase.ai/model/opoint/search
