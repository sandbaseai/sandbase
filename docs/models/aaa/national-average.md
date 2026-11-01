# AAA National Average

`aaa/national-average` · api · AAA

Returns today's AAA national average gas price for all fuel grades (Regular, Mid-Grade, Premium, Diesel) with historical comparisons to yesterday, one week ago, one month ago, and one year ago. Includes the date the.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "aaa/national-average"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('aaa/national-average', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("aaa/national-average", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "aaa/national-average", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/aaa/national-average` with the body above minus `model`.

## Details

Returns today's AAA national average gas price for all fuel grades (Regular, Mid-Grade, Premium, Diesel) with historical comparisons to yesterday, one week ago, one month ago, and one year ago. Includes the date the.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/aaa/national-average" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

This API takes no parameters.

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/aaa/national-average.json`](../../../catalog/models/aaa/national-average.json) · Store page: https://www.sandbase.ai/model/aaa/national-average
