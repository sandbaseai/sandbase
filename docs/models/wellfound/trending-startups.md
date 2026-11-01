# Wellfound Trending Startups

`wellfound/trending-startups` · api · Wellfound

Fetch trending startups currently hiring from the Wellfound homepage. Returns a curated list of startups that Wellfound is currently featuring, with basic company info and active job counts.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wellfound/trending-startups"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wellfound/trending-startups', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wellfound/trending-startups", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wellfound/trending-startups", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/wellfound/trending-startups` with the body above minus `model`.

## Details

Fetch trending startups currently hiring from the Wellfound homepage. Returns a curated list of startups that Wellfound is currently featuring, with basic company info and active job counts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wellfound/trending-startups" \
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
Machine-readable: [`catalog/models/wellfound/trending-startups.json`](../../../catalog/models/wellfound/trending-startups.json) · Store page: https://www.sandbase.ai/model/wellfound/trending-startups
