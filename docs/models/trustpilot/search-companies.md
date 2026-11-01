# Trustpilot Search Companies

`trustpilot/search-companies` · api · Trustpilot

Search for companies by name or keyword. Returns basic company info including domain, trust score, star rating, and review count.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "trustpilot/search-companies", "query": "airline"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('trustpilot/search-companies', {'query': 'airline'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("trustpilot/search-companies", {
  "query": "airline"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "trustpilot/search-companies", sandbase.Params{
	"query": "airline",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/trustpilot/search-companies` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number range -9007199254740991–9007199254740991 |
| `limit` | integer |  | Results per page (max 20) range -9007199254740991–9007199254740991 |
| `query` | string | yes | Search keyword or company name  |

## Details

Search for companies by name or keyword. Returns basic company info including domain, trust score, star rating, and review count.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/trustpilot/search-companies" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "airline"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search keyword or company name |
| `limit` | integer | No | Results per page (max 20) |
| `page` | integer | No | Page number |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/trustpilot/search-companies.json`](../../../catalog/models/trustpilot/search-companies.json) · Store page: https://www.sandbase.ai/model/trustpilot/search-companies
