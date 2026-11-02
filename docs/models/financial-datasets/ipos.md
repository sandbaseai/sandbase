# Financial Datasets IPO Filings API: pricing, parameters and code examples

`financial-datasets/ipos` · data API · Financial Datasets · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.16 per call · **Modes:** sync

Recent US IPO and registration filings (S-1, F-1 and amendments) with company, form type and filing links.

## Pricing

- **$0.16 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "financial-datasets/ipos"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('financial-datasets/ipos', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("financial-datasets/ipos", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "financial-datasets/ipos", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/financial-datasets/ipos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of filings to return.  |
| `cursor` | string |  | Opaque pagination cursor from a previous response's next_page_url.  |

## Details

Recent US IPO and registration filings (S-1, F-1 and amendments) with company, form type and filing links.

The result is returned in `outputs[0].data` as the official Financial Datasets API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/financial-datasets/ipos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": 5}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `limit` | integer | No | Maximum number of filings to return. |
| `cursor` | string | No | Opaque pagination cursor from a previous response's next_page_url. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/financial-datasets/ipos.json`](../../../catalog/models/financial-datasets/ipos.json) · Store page: https://www.sandbase.ai/model/financial-datasets/ipos
