# Crunchbase Investor Profile API: pricing, parameters and code examples

`crunchbase/investor-profile` · data API · Crunchbase · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Fetch a comprehensive investor profile by permalink/slug. Makes two API calls: one to retrieve investor-specific data (investment count, exits, investor rank, diversity investments, investor type/stage) and one for.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "crunchbase/investor-profile", "slug": "slack"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('crunchbase/investor-profile', {'slug': 'slack'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("crunchbase/investor-profile", {
  "slug": "slack"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "crunchbase/investor-profile", sandbase.Params{
	"slug": "slack",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/crunchbase/investor-profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `slug` | string | yes | Investor permalink/slug (e.g. 'sequoia-capital', 'andreessen-horowitz'). This is the identifier.permalink from search_investors results.  |

## Details

Fetch a comprehensive investor profile by permalink/slug. Makes two API calls: one to retrieve investor-specific data (investment count, exits, investor rank, diversity investments, investor type/stage) and one for.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/crunchbase/investor-profile" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"slug": "slack"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `slug` | string | Yes | Investor permalink/slug (e.g. 'sequoia-capital', 'andreessen-horowitz'). This is the identifier.permalink from search_investors results. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/crunchbase/investor-profile.json`](../../../catalog/models/crunchbase/investor-profile.json) · Store page: https://www.sandbase.ai/model/crunchbase/investor-profile
