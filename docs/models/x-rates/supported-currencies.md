# X-Rates Supported Currencies API: pricing, parameters and code examples

`x-rates/supported-currencies` · data API · X-Rates · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Retrieves the full list of supported currencies and their codes from x-rates.com. Returns approximately 54 currencies with their display names and ISO 4217 codes.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "x-rates/supported-currencies"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('x-rates/supported-currencies', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("x-rates/supported-currencies", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "x-rates/supported-currencies", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/x-rates/supported-currencies` with the body above minus `model`.

## Details

Retrieves the full list of supported currencies and their codes from x-rates.com. Returns approximately 54 currencies with their display names and ISO 4217 codes.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "x-rates/supported-currencies"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/x-rates/supported-currencies.json`](../../../catalog/models/x-rates/supported-currencies.json) · Store page: https://www.sandbase.ai/model/x-rates/supported-currencies
