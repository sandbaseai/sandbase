# Fundable Location Search API: pricing, parameters and code examples

`fundable/location-search` · data API · Fundable · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0 per run, depending on parameters · **Modes:** async

Search locations by name and optionally filter by type

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
  -d '{"model": "fundable/location-search", "name": "San Francisco"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('fundable/location-search', {'name': 'San Francisco'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("fundable/location-search", {
  "name": "San Francisco"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "fundable/location-search", sandbase.Params{
	"name": "San Francisco",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/fundable/location-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `name` | string | yes | Location name; fuzzy matched.  |
| `type` | string |  | Restrict to one location level. one of: `CITY`, `STATE`, `REGION`, `COUNTRY` |

## Details

Search locations by name and optionally filter by type

---
Machine-readable: [`catalog/models/fundable/location-search.json`](../../../catalog/models/fundable/location-search.json) · Store page: https://www.sandbase.ai/model/fundable/location-search
