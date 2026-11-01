# Web3.career Jobs By Tag

`web3-career/jobs-by-tag` · api · Web3.career

Fetch job listings filtered by a skill or category tag. Returns paginated results for the given tag.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "web3-career/jobs-by-tag", "tag": "solidity"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('web3-career/jobs-by-tag', {'tag': 'solidity'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("web3-career/jobs-by-tag", {
  "tag": "solidity"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "web3-career/jobs-by-tag", sandbase.Params{
	"tag": "solidity",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/web3-career/jobs-by-tag` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `tag` | string | yes | The skill or category tag to filter jobs by.  |
| `page` | integer |  | Page number for pagination. range -9007199254740991–9007199254740991 |

## Details

Fetch job listings filtered by a skill or category tag. Returns paginated results for the given tag.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/web3-career/jobs-by-tag" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"tag": "solidity", "page": 1}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `tag` | string | Yes | The skill or category tag to filter jobs by. |
| `page` | integer | No | Page number for pagination. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/web3-career/jobs-by-tag.json`](../../../catalog/models/web3-career/jobs-by-tag.json) · Store page: https://www.sandbase.ai/model/web3-career/jobs-by-tag
