# Opoint Search Advanced API: pricing, parameters and code examples

`opoint/search-advanced` · data API · Opoint · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.06 per call · **Modes:** async

Search news with structured expression lines and typed filter ids.

## Pricing

- **$0.06 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "opoint/search-advanced", "expressions": [{"linemode": "R", "searchline": {"searchterm": "header:spotify AND lang:en"}}]}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('opoint/search-advanced', {'expressions': [{'linemode': 'R', 'searchline': {'searchterm': 'header:spotify AND lang:en'}}]})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("opoint/search-advanced", {
  "expressions": [
    {
      "linemode": "R",
      "searchline": {
        "searchterm": "header:spotify AND lang:en"
      }
    }
  ]
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "opoint/search-advanced", sandbase.Params{
	"expressions": []any{map[string]any{
		"linemode": "R",
		"searchline": map[string]any{
			"searchterm": "header:spotify AND lang:en",
		},
	}},
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/opoint/search-advanced` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `params` | object |  |   |
| `expressions` | array | yes | One or more search lines; R lines must all match.  |

## Details

Search news with structured expression lines and typed filter ids.

---
Machine-readable: [`catalog/models/opoint/search-advanced.json`](../../../catalog/models/opoint/search-advanced.json) · Store page: https://www.sandbase.ai/model/opoint/search-advanced
