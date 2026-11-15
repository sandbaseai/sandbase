# Eastmoney Screen Stocks API: pricing, parameters and code examples

`eastmoney/screen-stocks` · data API · Eastmoney · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Search for stocks using natural language or filter conditions on EastMoney's AI stock screener. Accepts Chinese or symbolic queries like 'PE<20' or '市值>1000亿'. Returns matching stocks with market data columns, parsed filter conditions, and total count. Paginated by page_no/page_size.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "eastmoney/screen-stocks", "query": "PE<20"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('eastmoney/screen-stocks', {'query': 'PE<20'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("eastmoney/screen-stocks", {
  "query": "PE<20"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "eastmoney/screen-stocks", sandbase.Params{
	"query": "PE<20",
})
```

Same call via the path form: `POST /v1/api/eastmoney/screen-stocks` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Search keyword or natural language query (e.g. 'PE<20', '市值>1000亿', '白酒')  |
| `page_no` | integer |  | Page number for results pagination. default `1` |
| `page_size` | integer |  | Number of results per page. default `50` |

## Details

Search for stocks using natural language or filter conditions on EastMoney's AI stock screener. Accepts Chinese or symbolic queries like 'PE<20' or '市值>1000亿'. Returns matching stocks with market data columns, parsed filter conditions, and total count. Paginated by page_no/page_size.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "eastmoney/screen-stocks", "query": "PE<20", "page_no": 1, "page_size": 10}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search keyword or natural language query (e.g. 'PE<20', '市值>1000亿', '白酒') |
| `page_no` | integer | No | Page number for results pagination. |
| `page_size` | integer | No | Number of results per page. |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/eastmoney/screen-stocks.json`](../../../catalog/models/eastmoney/screen-stocks.json) · Store page: https://www.sandbase.ai/model/eastmoney/screen-stocks
