# XE All Rates API: pricing, parameters and code examples

`xe/all-rates` · data API · XE · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.06 per call · **Modes:** sync

Get all mid-market exchange rates relative to USD. Returns a timestamp and a rates object mapping every supported currency code to its USD-relative rate. The rate sheet refreshes every few minutes.

## Pricing

- **$0.06 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xe/all-rates"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xe/all-rates', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xe/all-rates", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xe/all-rates", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/xe/all-rates` with the body above minus `model`.

## Details

Get all mid-market exchange rates relative to USD. Returns a timestamp and a rates object mapping every supported currency code to its USD-relative rate. The rate sheet refreshes every few minutes.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "xe/all-rates"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|

### Pricing

Flat $0.06 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/xe/all-rates.json`](../../../catalog/models/xe/all-rates.json) · Store page: https://www.sandbase.ai/model/xe/all-rates
