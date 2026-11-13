# Google Finance Autocomplete API: pricing, parameters and code examples

`google/finance-autocomplete` · data API · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Get Google Finance ticker suggestions for a partial company name or symbol, with exchange and instrument type.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/finance-autocomplete", "q": "nvid"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/finance-autocomplete', {'q': 'nvid'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/finance-autocomplete", {
  "q": "nvid"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/finance-autocomplete", sandbase.Params{
	"q": "nvid",
})
```

Same call via the path form: `POST /v1/api/google/finance-autocomplete` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string | yes | Parameter defines the search query. A query that would be used to provide completion options. It can be a company name, ticker symbol, index, mutual fund, currency, futures contract, prediction market or private market.  |
| `gl` | string |  | Parameter defines the country to use for the Google Finance Autocomplete search. It's a two-letter country code. (e.g., `us` (default) for the United States, `uk` for United Kingdom, or `fr` for France). Head to the…  |
| `hl` | string |  | Parameter defines the language to use for the Google Finance Autocomplete search. It's a two or three-letter language code. (e.g., `en` (default) for English, `es` for Spanish, or `fr` for French), optionally followed…  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |

## Details

Get Google Finance ticker suggestions for a partial company name or symbol, with exchange and instrument type.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google/finance-autocomplete" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "nvid"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | Yes | Parameter defines the search query. A query that would be used to provide completion options. It can be a company name, ticker symbol, index, mutual fund, currency, futures contract, prediction market or private market. |
| `gl` | string | No | Parameter defines the country to use for the Google Finance Autocomplete search. It's a two-letter country code. (e.g., `us` (default) for the United States, `uk` for United Kingdom, or `fr` for France). Head to the Google countries page fo |
| `hl` | string | No | Parameter defines the language to use for the Google Finance Autocomplete search. It's a two or three-letter language code. (e.g., `en` (default) for English, `es` for Spanish, or `fr` for French), optionally followed by a two-letter or thr |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/google/finance-autocomplete.json`](../../../catalog/models/google/finance-autocomplete.json) · Store page: https://www.sandbase.ai/model/google/finance-autocomplete
