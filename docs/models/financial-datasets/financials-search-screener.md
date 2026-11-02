# Financial Datasets Stock Screener API: pricing, parameters and code examples

`financial-datasets/financials-search-screener` · data API · Financial Datasets · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Screen US public companies by financial metrics such as revenue, net income or P/E, with gt/lt/eq filters and ticker lists.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "financial-datasets/financials-search-screener", "filters": [{"field": "revenue", "value": 100000000000, "operator": "gt"}]}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('financial-datasets/financials-search-screener', {'filters': [{'field': 'revenue', 'value': 100000000000, 'operator': 'gt'}]})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("financial-datasets/financials-search-screener", {
  "filters": [
    {
      "field": "revenue",
      "value": 100000000000,
      "operator": "gt"
    }
  ]
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "financial-datasets/financials-search-screener", sandbase.Params{
	"filters": []any{map[string]any{
		"field": "revenue",
		"value": 100000000000,
		"operator": "gt",
	}},
})
```

Same call via the path form: `POST /v1/api/financial-datasets/financials-search-screener` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | The maximum number of results to return. default `10`; range 1– |
| `filters` | array | yes | An array of filter objects to apply to the search.  |

## Details

Screen US public companies by financial metrics such as revenue, net income or P/E, with gt/lt/eq filters and ticker lists.

The result is returned in `outputs[0].data` as the official Financial Datasets API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/financial-datasets/financials-search-screener" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"filters": [{"field": "revenue", "operator": "gt", "value": 100000000000}], "limit": 5}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `filters` | array | Yes | An array of filter objects to apply to the search. |
| `limit` | integer | No | The maximum number of results to return. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/financial-datasets/financials-search-screener.json`](../../../catalog/models/financial-datasets/financials-search-screener.json) · Store page: https://www.sandbase.ai/model/financial-datasets/financials-search-screener
