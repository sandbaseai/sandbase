# IQAir World Air Quality API: pricing, parameters and code examples

`iqair/world-air-quality` · data API · IQAir · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Global air quality overview returning the top 15 most polluted and top 15 cleanest major cities worldwide. Each city entry includes current AQI, geographic identifiers, and a URL slug path usable with.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "iqair/world-air-quality"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('iqair/world-air-quality', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("iqair/world-air-quality", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "iqair/world-air-quality", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/iqair/world-air-quality` with the body above minus `model`.

## Details

Global air quality overview returning the top 15 most polluted and top 15 cleanest major cities worldwide. Each city entry includes current AQI, geographic identifiers, and a URL slug path usable with.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/iqair/world-air-quality" \
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
Machine-readable: [`catalog/models/iqair/world-air-quality.json`](../../../catalog/models/iqair/world-air-quality.json) · Store page: https://www.sandbase.ai/model/iqair/world-air-quality
