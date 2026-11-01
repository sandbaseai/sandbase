# Web3.career Company Jobs

`web3-career/company-jobs` · api · Web3.career

Fetch all job listings for a specific company by its URL slug. Returns paginated job listings posted by the company.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "web3-career/company-jobs", "company_slug": "stripe"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('web3-career/company-jobs', {'company_slug': 'stripe'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("web3-career/company-jobs", {
  "company_slug": "stripe"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "web3-career/company-jobs", sandbase.Params{
	"company_slug": "stripe",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/web3-career/company-jobs` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number for pagination. range -9007199254740991–9007199254740991 |
| `company_slug` | string | yes | The URL slug of the company (e.g., binance, crypto-com, coinbase). Available from get_web3_companies results.  |

## Details

Fetch all job listings for a specific company by its URL slug. Returns paginated job listings posted by the company.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/web3-career/company-jobs" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"company_slug": "stripe"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `company_slug` | string | Yes | The URL slug of the company (e.g., binance, crypto-com, coinbase). Available from get_web3_companies results. |
| `page` | integer | No | Page number for pagination. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/web3-career/company-jobs.json`](../../../catalog/models/web3-career/company-jobs.json) · Store page: https://www.sandbase.ai/model/web3-career/company-jobs
