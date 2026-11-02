# Web3.career Job Detail API: pricing, parameters and code examples

`web3-career/job-detail` · data API · Web3.career · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Fetch full details for a single job listing by URL. Returns the job title, company name, full description text, salary range, and application link.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "web3-career/job-detail", "url": "https://web3.career/junior-crypto-analyst-trader-empire-assets/155554"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('web3-career/job-detail', {'url': 'https://web3.career/junior-crypto-analyst-trader-empire-assets/155554'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("web3-career/job-detail", {
  "url": "https://web3.career/junior-crypto-analyst-trader-empire-assets/155554"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "web3-career/job-detail", sandbase.Params{
	"url": "https://web3.career/junior-crypto-analyst-trader-empire-assets/155554",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/web3-career/job-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | The full URL of the job listing on web3.career (e.g., https://web3.career/senior-fullstack-engineer-backend-focus-rugsdotfun/150325).  |

## Details

Fetch full details for a single job listing by URL. Returns the job title, company name, full description text, salary range, and application link.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/web3-career/job-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://web3.career/junior-crypto-analyst-trader-empire-assets/155554"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | The full URL of the job listing on web3.career (e.g., https://web3.career/senior-fullstack-engineer-backend-focus-rugsdotfun/150325). |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/web3-career/job-detail.json`](../../../catalog/models/web3-career/job-detail.json) · Store page: https://www.sandbase.ai/model/web3-career/job-detail
