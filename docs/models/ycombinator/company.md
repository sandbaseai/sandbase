# Y Combinator Company API: pricing, parameters and code examples

`ycombinator/company` · data API · Y Combinator · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Retrieve full details for a YC company by its slug. Returns comprehensive company profile including founders with bios, social links, team size, description, and funding information.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "ycombinator/company", "slug": "airbnb"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('ycombinator/company', {'slug': 'airbnb'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("ycombinator/company", {
  "slug": "airbnb"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "ycombinator/company", sandbase.Params{
	"slug": "airbnb",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/ycombinator/company` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `slug` | string | yes | Company slug identifier (e.g. 'airbnb', 'coinbase', 'stripe'). Obtainable from search_companies results.  |

## Details

Retrieve full details for a YC company by its slug. Returns comprehensive company profile including founders with bios, social links, team size, description, and funding information.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/ycombinator/company" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"slug": "airbnb"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `slug` | string | Yes | Company slug identifier (e.g. 'airbnb', 'coinbase', 'stripe'). Obtainable from search_companies results. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/ycombinator/company.json`](../../../catalog/models/ycombinator/company.json) · Store page: https://www.sandbase.ai/model/ycombinator/company
