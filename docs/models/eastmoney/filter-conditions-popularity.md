# Eastmoney Filter Conditions Popularity API: pricing, parameters and code examples

`eastmoney/filter-conditions-popularity` · data API · Eastmoney · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Get filter conditions related to popularity ranking (股吧人气排名, 粉丝占比) and limit-up (涨停) status including 首板, 连板, and consecutive limit-up days.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "eastmoney/filter-conditions-popularity"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('eastmoney/filter-conditions-popularity', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("eastmoney/filter-conditions-popularity", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "eastmoney/filter-conditions-popularity", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/eastmoney/filter-conditions-popularity` with the body above minus `model`.

## Details

Get filter conditions related to popularity ranking (股吧人气排名, 粉丝占比) and limit-up (涨停) status including 首板, 连板, and consecutive limit-up days.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "eastmoney/filter-conditions-popularity"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/eastmoney/filter-conditions-popularity.json`](../../../catalog/models/eastmoney/filter-conditions-popularity.json) · Store page: https://www.sandbase.ai/model/eastmoney/filter-conditions-popularity
