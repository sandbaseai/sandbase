# XE Currency Symbols API: pricing, parameters and code examples

`xe/currency-symbols` · data API · XE · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Get metadata and classification for all supported currencies. Each currency includes flags for obsolete status, crypto classification, and whether it is sellable or buyable on the XE platform.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xe/currency-symbols"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xe/currency-symbols', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xe/currency-symbols", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xe/currency-symbols", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/xe/currency-symbols` with the body above minus `model`.

## Details

Get metadata and classification for all supported currencies. Each currency includes flags for obsolete status, crypto classification, and whether it is sellable or buyable on the XE platform.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "xe/currency-symbols"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/xe/currency-symbols.json`](../../../catalog/models/xe/currency-symbols.json) · Store page: https://www.sandbase.ai/model/xe/currency-symbols
