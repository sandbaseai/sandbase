# Google Finance API: pricing, parameters and code examples

`google/finance` · data API · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Get a Google Finance quote page for a ticker such as GOOGL:NASDAQ: price, movement, key stats, financials, news and price graph over a chosen window.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/finance", "q": "GOOGL:NASDAQ"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/finance', {'q': 'GOOGL:NASDAQ'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/finance", {
  "q": "GOOGL:NASDAQ"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/finance", sandbase.Params{
	"q": "GOOGL:NASDAQ",
})
```

Same call via the path form: `POST /v1/api/google/finance` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string | yes | Parameter defines the query you want to search. It can be a stock, index, mutual fund, currency or futures. Head to the Google Finance Autocomplete API to find the query for a company name or a keyword.  |
| `hl` | string |  | Parameter defines the language to use for the Google Finance search. It's a two or three-letter language code. (e.g., `en` for English, `es` for Spanish, or `fr` for French), optionally followed by a two-letter or…  |
| `window` | string |  | Parameter is used for setting time range for the graph. It can be set to: `1D` - 1 Day(default) `5D` - 5 Days `1M` - 1 Month `6M` - 6 Months `YTD` - Year to Date `1Y` - 1 Year `5Y` - 5 Years `MAX` - Maximum  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |

## Details

Get a Google Finance quote page for a ticker such as GOOGL:NASDAQ: price, movement, key stats, financials, news and price graph over a chosen window.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google/finance" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "GOOGL:NASDAQ"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | Yes | Parameter defines the query you want to search. It can be a stock, index, mutual fund, currency or futures. Head to the Google Finance Autocomplete API to find the query for a company name or a keyword. |
| `hl` | string | No | Parameter defines the language to use for the Google Finance search. It's a two or three-letter language code. (e.g., `en` for English, `es` for Spanish, or `fr` for French), optionally followed by a two-letter or three-digit region code (e |
| `window` | string | No | Parameter is used for setting time range for the graph. It can be set to: `1D` - 1 Day(default) `5D` - 5 Days `1M` - 1 Month `6M` - 6 Months `YTD` - Year to Date `1Y` - 1 Year `5Y` - 5 Years `MAX` - Maximum |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/google/finance.json`](../../../catalog/models/google/finance.json) · Store page: https://www.sandbase.ai/model/google/finance
