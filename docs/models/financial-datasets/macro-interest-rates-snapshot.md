# Financial Datasets Get Latest Interest Rates

`financial-datasets/macro-interest-rates-snapshot` · api · Financial Datasets

The newest published policy rate of every central bank we cover, one row per bank with the date it is in effect. Pass bank to get one bank only.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "financial-datasets/macro-interest-rates-snapshot"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('financial-datasets/macro-interest-rates-snapshot', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("financial-datasets/macro-interest-rates-snapshot", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "financial-datasets/macro-interest-rates-snapshot", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/financial-datasets/macro-interest-rates-snapshot` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `bank` | string |  | Optional central bank code (e.g., FED, ECB, BOJ) to return one bank only. Use the /macro/interest-rates/banks endpoint to get a list of available banks.  |

## Details

The newest published policy rate of every central bank we cover, one row per bank with the date it is in effect. Pass bank to get one bank only.

The response is the official Financial Datasets API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/financial-datasets/macro-interest-rates-snapshot" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `bank` | string | No | Optional central bank code (e.g., FED, ECB, BOJ) to return one bank only. Use the /macro/interest-rates/banks endpoint to get a list of available banks. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/financial-datasets/macro-interest-rates-snapshot.json`](../../../catalog/models/financial-datasets/macro-interest-rates-snapshot.json) · Store page: https://www.sandbase.ai/model/financial-datasets/macro-interest-rates-snapshot
