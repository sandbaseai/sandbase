# Trustpilot Company Overview

`trustpilot/company-overview` · api · Trustpilot

Get full company profile overview including TrustScore, rating distribution, AI summary, and initial reviews.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "trustpilot/company-overview", "domain": "stripe.com"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('trustpilot/company-overview', {'domain': 'stripe.com'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("trustpilot/company-overview", {
  "domain": "stripe.com"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "trustpilot/company-overview", sandbase.Params{
	"domain": "stripe.com",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/trustpilot/company-overview` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `domain` | string | yes | Company domain/identifying name as used on Trustpilot (e.g. 'www.amazon.com')  |

## Details

Get full company profile overview including TrustScore, rating distribution, AI summary, and initial reviews.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/trustpilot/company-overview" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"domain": "stripe.com"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `domain` | string | Yes | Company domain/identifying name as used on Trustpilot (e.g. 'www.amazon.com') |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/trustpilot/company-overview.json`](../../../catalog/models/trustpilot/company-overview.json) · Store page: https://www.sandbase.ai/model/trustpilot/company-overview
