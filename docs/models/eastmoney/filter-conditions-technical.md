# Eastmoney Filter Conditions Technical API: pricing, parameters and code examples

`eastmoney/filter-conditions-technical` · data API · Eastmoney · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Get filter conditions related to technical analysis and K-line patterns: MACD (golden/death cross, divergence), KDJ, moving averages, classic candlestick patterns (放量突破, 低位资金净流入), and intraday K-line patterns.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "eastmoney/filter-conditions-technical"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('eastmoney/filter-conditions-technical', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("eastmoney/filter-conditions-technical", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "eastmoney/filter-conditions-technical", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/eastmoney/filter-conditions-technical` with the body above minus `model`.

## Details

Get filter conditions related to technical analysis and K-line patterns: MACD (golden/death cross, divergence), KDJ, moving averages, classic candlestick patterns (放量突破, 低位资金净流入), and intraday K-line patterns.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "eastmoney/filter-conditions-technical"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/eastmoney/filter-conditions-technical.json`](../../../catalog/models/eastmoney/filter-conditions-technical.json) · Store page: https://www.sandbase.ai/model/eastmoney/filter-conditions-technical
