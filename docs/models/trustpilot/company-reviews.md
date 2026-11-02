# Trustpilot Company Reviews API: pricing, parameters and code examples

`trustpilot/company-reviews` · data API · Trustpilot · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** async

Fetch paginated reviews for a company with optional star filtering, sort order, and keyword search.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "trustpilot/company-reviews", "domain": "stripe.com"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('trustpilot/company-reviews', {'domain': 'stripe.com'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("trustpilot/company-reviews", {
  "domain": "stripe.com"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "trustpilot/company-reviews", sandbase.Params{
	"domain": "stripe.com",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/trustpilot/company-reviews` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number range -9007199254740991–9007199254740991 |
| `sort` | string |  | Sort order for reviews  |
| `stars` | string |  | Filter by star rating (1-5)  |
| `domain` | string | yes | Company domain/identifying name as used on Trustpilot  |
| `keyword` | string |  | Search keyword within reviews  |

## Details

Fetch paginated reviews for a company with optional star filtering, sort order, and keyword search.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/trustpilot/company-reviews" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"domain": "stripe.com"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `domain` | string | Yes | Company domain/identifying name as used on Trustpilot |
| `keyword` | string | No | Search keyword within reviews |
| `page` | integer | No | Page number |
| `sort` | string | No | Sort order for reviews |
| `stars` | string | No | Filter by star rating (1-5) |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/trustpilot/company-reviews.json`](../../../catalog/models/trustpilot/company-reviews.json) · Store page: https://www.sandbase.ai/model/trustpilot/company-reviews
