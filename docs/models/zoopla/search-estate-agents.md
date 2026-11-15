# Zoopla Search Estate Agents API: pricing, parameters and code examples

`zoopla/search-estate-agents` · data API · Zoopla · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Search for estate agents in a specific location. Returns a paginated list of agents with contact details, logo, display address, and listing statistics (average asking price, weeks on market, available listings for both sales and lettings).

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zoopla/search-estate-agents", "location": "london"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zoopla/search-estate-agents', {'location': 'london'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zoopla/search-estate-agents", {
  "location": "london"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zoopla/search-estate-agents", sandbase.Params{
	"location": "london",
})
```

Same call via the path form: `POST /v1/api/zoopla/search-estate-agents` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `location` | string | yes | Location slug matching Zoopla URL structure (e.g., 'london', 'manchester').  |

## Details

Search for estate agents in a specific location. Returns a paginated list of agents with contact details, logo, display address, and listing statistics (average asking price, weeks on market, available listings for both sales and lettings).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "zoopla/search-estate-agents", "location": "london"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `location` | string | Yes | Location slug matching Zoopla URL structure (e.g., 'london', 'manchester'). |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/zoopla/search-estate-agents.json`](../../../catalog/models/zoopla/search-estate-agents.json) · Store page: https://www.sandbase.ai/model/zoopla/search-estate-agents
