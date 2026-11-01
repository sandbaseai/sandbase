# SECForm4 Search

`secform4/search` · api · SECForm4

Searches for insider trading activity by company ticker symbol, CIK number, or company name. Returns all matching transaction records for the company including buys, sells, and option exercises.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "secform4/search", "query": "Tesla"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('secform4/search', {'query': 'Tesla'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("secform4/search", {
  "query": "Tesla"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "secform4/search", sandbase.Params{
	"query": "Tesla",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/secform4/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Search query - company ticker symbol (e.g. 'AAPL'), CIK number (e.g. '320193'), or company name (e.g. 'Apple')  |

## Details

Searches for insider trading activity by company ticker symbol, CIK number, or company name. Returns all matching transaction records for the company including buys, sells, and option exercises.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/secform4/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "Tesla"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search query - company ticker symbol (e.g. 'AAPL'), CIK number (e.g. '320193'), or company name (e.g. 'Apple') |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/secform4/search.json`](../../../catalog/models/secform4/search.json) · Store page: https://www.sandbase.ai/model/secform4/search
