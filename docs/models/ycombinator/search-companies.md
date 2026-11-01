# Y Combinator Search Companies

`ycombinator/search-companies` · api · Y Combinator

Search and filter the YC company directory via Algolia. Returns paginated results with company metadata including name, batch, industry, team size, and hiring status.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "ycombinator/search-companies"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('ycombinator/search-companies', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("ycombinator/search-companies", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "ycombinator/search-companies", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/ycombinator/search-companies` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number (0-indexed). range -9007199254740991–9007199254740991 |
| `batch` | string |  | Filter by YC batch name (e.g. 'Winter 2024', 'Summer 2023').  |
| `limit` | integer |  | Number of results per page. range -9007199254740991–9007199254740991 |
| `query` | string |  | Search keyword to match against company name, description, and tags.  |
| `industry` | string |  | Filter by industry (e.g. 'Fintech', 'B2B', 'Healthcare').  |
| `is_hiring` | string |  | Filter by hiring status. Accepts 'true' or 'false'.  |
| `top_company` | string |  | Filter for YC top companies. Accepts 'true' or 'false'.  |

## Details

Search and filter the YC company directory via Algolia. Returns paginated results with company metadata including name, batch, industry, team size, and hiring status.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/ycombinator/search-companies" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `batch` | string | No | Filter by YC batch name (e.g. 'Winter 2024', 'Summer 2023'). |
| `industry` | string | No | Filter by industry (e.g. 'Fintech', 'B2B', 'Healthcare'). |
| `is_hiring` | string | No | Filter by hiring status. Accepts 'true' or 'false'. |
| `limit` | integer | No | Number of results per page. |
| `page` | integer | No | Page number (0-indexed). |
| `query` | string | No | Search keyword to match against company name, description, and tags. |
| `top_company` | string | No | Filter for YC top companies. Accepts 'true' or 'false'. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/ycombinator/search-companies.json`](../../../catalog/models/ycombinator/search-companies.json) · Store page: https://www.sandbase.ai/model/ycombinator/search-companies
