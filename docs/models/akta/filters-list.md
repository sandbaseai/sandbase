# Akta Filters List API: pricing, parameters and code examples

`akta/filters-list` · data API · Akta · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0 per run, depending on parameters · **Modes:** async

List every filter key accepted by company list generation. Free.

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
  -d '{"model": "akta/filters-list"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('akta/filters-list', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("akta/filters-list", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "akta/filters-list", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/akta/filters-list` with the body above minus `model`.

## Details

List every filter key accepted by company list generation. Free.

---
Machine-readable: [`catalog/models/akta/filters-list.json`](../../../catalog/models/akta/filters-list.json) · Store page: https://www.sandbase.ai/model/akta/filters-list
