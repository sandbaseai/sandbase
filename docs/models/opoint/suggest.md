# Opoint Suggest API: pricing, parameters and code examples

`opoint/suggest` · data API · Opoint · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0 per run, depending on parameters · **Modes:** async

Translate a country, site, language, or media name into a search filter id.

## Pricing

- Depends on parameters ().

| parameters | USD |
|---|---|
| defaults | 0 |

Formula: `0`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "opoint/suggest", "query": "bbc"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('opoint/suggest', {'query': 'bbc'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("opoint/suggest", {
  "query": "bbc"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "opoint/suggest", sandbase.Params{
	"query": "bbc",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/opoint/suggest` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Rows to return (default 5). range 1–20 |
| `query` | string | yes | Name or URL to resolve, e.g. 'Norway', 'New York Post', 'bbc.co.uk'.  |
| `types` | array |  | Restrict to these filter types; omitted = all types.  |

## Details

Translate a country, site, language, or media name into a search filter id.

---
Machine-readable: [`catalog/models/opoint/suggest.json`](../../../catalog/models/opoint/suggest.json) · Store page: https://www.sandbase.ai/model/opoint/suggest
