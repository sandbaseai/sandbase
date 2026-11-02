# Trustpilot Company Review Summary API: pricing, parameters and code examples

`trustpilot/company-review-summary` · data API · Trustpilot · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.05 per call · **Modes:** async

Get AI summary, review topics, rating breakdown, and recent review texts for a company. Accepts either a direct company domain or a search query.

## Pricing

- **$0.05 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "trustpilot/company-review-summary"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('trustpilot/company-review-summary', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("trustpilot/company-review-summary", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "trustpilot/company-review-summary", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/trustpilot/company-review-summary` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of company summaries to return when using query mode (max 10). Ignored when domain is provided. range -9007199254740991–9007199254740991 |
| `query` | string |  | Search keyword to find companies (e.g. 'AI Services'). When provided, searches for matching companies and returns their review summaries. Either 'domain' or 'query' must be provided.  |
| `domain` | string |  | Company domain/identifying name as used on Trustpilot (e.g. 'www.nike.com'). Either 'domain' or 'query' must be provided.  |

## Details

Get AI summary, review topics, rating breakdown, and recent review texts for a company. Accepts either a direct company domain or a search query.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/trustpilot/company-review-summary" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"domain": "www.nike.com"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `domain` | string | No | Company domain/identifying name as used on Trustpilot (e.g. 'www.nike.com'). Either 'domain' or 'query' must be provided. |
| `limit` | integer | No | Maximum number of company summaries to return when using query mode (max 10). Ignored when domain is provided. |
| `query` | string | No | Search keyword to find companies (e.g. 'AI Services'). When provided, searches for matching companies and returns their review summaries. Either 'domain' or 'query' must be provided. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/trustpilot/company-review-summary.json`](../../../catalog/models/trustpilot/company-review-summary.json) · Store page: https://www.sandbase.ai/model/trustpilot/company-review-summary
