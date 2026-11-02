# Crunchbase Search Investors API: pricing, parameters and code examples

`crunchbase/search-investors` · data API · Crunchbase · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** async

Full-text search over Crunchbase investors. Returns results with investor details including number of investments, exits, location, and investor type.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "crunchbase/search-investors"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('crunchbase/search-investors', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("crunchbase/search-investors", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "crunchbase/search-investors", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/crunchbase/search-investors` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Max results to return. range -9007199254740991–9007199254740991 |
| `query` | string |  | Search keyword for investor name (e.g. 'sequoia', 'andreessen'). Omitting returns all investors.  |

## Details

Full-text search over Crunchbase investors. Returns results with investor details including number of investments, exits, location, and investor type.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/crunchbase/search-investors" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `limit` | integer | No | Max results to return. |
| `query` | string | No | Search keyword for investor name (e.g. 'sequoia', 'andreessen'). Omitting returns all investors. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/crunchbase/search-investors.json`](../../../catalog/models/crunchbase/search-investors.json) · Store page: https://www.sandbase.ai/model/crunchbase/search-investors
