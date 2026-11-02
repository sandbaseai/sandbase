# SECForm4 Company Insider Trading API: pricing, parameters and code examples

`secform4/company-insider-trading` · data API · SECForm4 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Returns the full insider trading history for a specific company identified by its SEC CIK number. Includes all buy, sell, and option transactions filed in Form 4s for the company.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "secform4/company-insider-trading", "cik": "320193"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('secform4/company-insider-trading', {'cik': '320193'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("secform4/company-insider-trading", {
  "cik": "320193"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "secform4/company-insider-trading", sandbase.Params{
	"cik": "320193",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/secform4/company-insider-trading` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cik` | string | yes | SEC CIK number of the company (e.g. '320193' for Apple Inc, '789019' for Microsoft)  |

## Details

Returns the full insider trading history for a specific company identified by its SEC CIK number. Includes all buy, sell, and option transactions filed in Form 4s for the company.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/secform4/company-insider-trading" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"cik": "320193"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cik` | string | Yes | SEC CIK number of the company (e.g. '320193' for Apple Inc, '789019' for Microsoft) |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/secform4/company-insider-trading.json`](../../../catalog/models/secform4/company-insider-trading.json) · Store page: https://www.sandbase.ai/model/secform4/company-insider-trading
