# X-Rates 24H Percent Changes API: pricing, parameters and code examples

`x-rates/24h-percent-changes` · data API · X-Rates · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Extracts the 'Percent Change in the Last 24 Hours' widget data for major currency pairs from the homepage. Returns ~8 major pairs with their percentage change and direction (up/down).

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "x-rates/24h-percent-changes"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('x-rates/24h-percent-changes', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("x-rates/24h-percent-changes", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "x-rates/24h-percent-changes", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/x-rates/24h-percent-changes` with the body above minus `model`.

## Details

Extracts the 'Percent Change in the Last 24 Hours' widget data for major currency pairs from the homepage. Returns ~8 major pairs with their percentage change and direction (up/down).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "x-rates/24h-percent-changes"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/x-rates/24h-percent-changes.json`](../../../catalog/models/x-rates/24h-percent-changes.json) · Store page: https://www.sandbase.ai/model/x-rates/24h-percent-changes
