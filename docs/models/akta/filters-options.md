# Akta Filters Options API: pricing, parameters and code examples

`akta/filters-options` · data API · Akta · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0 per run, depending on parameters · **Modes:** async

Get the allowed values for company list filter keys. Free.

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
  -d '{"model": "akta/filters-options", "dropdowns": [{"dropdown_type": "firmographic.company_type"}]}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('akta/filters-options', {'dropdowns': [{'dropdown_type': 'firmographic.company_type'}]})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("akta/filters-options", {
  "dropdowns": [
    {
      "dropdown_type": "firmographic.company_type"
    }
  ]
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "akta/filters-options", sandbase.Params{
	"dropdowns": []any{map[string]any{
		"dropdown_type": "firmographic.company_type",
	}},
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/akta/filters-options` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `dropdowns` | array | yes | Filter keys to look up values for.  |

## Details

Get the allowed values for company list filter keys. Free.

---
Machine-readable: [`catalog/models/akta/filters-options.json`](../../../catalog/models/akta/filters-options.json) · Store page: https://www.sandbase.ai/model/akta/filters-options
