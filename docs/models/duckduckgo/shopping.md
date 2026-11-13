# DuckDuckGo Shopping API: pricing, parameters and code examples

`duckduckgo/shopping` · data API · DuckDuckGo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Search DuckDuckGo Shopping by keyword and get product listings with title, price, merchant, rating and link, by region.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "duckduckgo/shopping", "q": "airpods"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('duckduckgo/shopping', {'q': 'airpods'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("duckduckgo/shopping", {
  "q": "airpods"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "duckduckgo/shopping", sandbase.Params{
	"q": "airpods",
})
```

Same call via the path form: `POST /v1/api/duckduckgo/shopping` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string | yes | Parameter defines the query you want to search. You can use anything that you would use in a regular DuckDuckGo Shopping search. Parameter length can not exceed 500 characters.  |
| `kl` | string |  | Parameter defines the region to use for the DuckDuckGo Shopping search. It sets the stores, the language, and the currency of the products. Region code examples: `us-en` (default) for the United States, `uk-en` for…  |
| `filters` | string |  | Parameter defines the filters to apply, like a brand, a price range, or a store. You can find its value in `filters` of the results: each option has a `value`. To combine filters, apply them one at a time, like on…  |
| `sort_by` | string |  | Parameter defines the sorting order of the results. It defaults to DuckDuckGo's featured order. Available options: `1` - Price: low to high `2` - Price: high to low  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |
| `next_page_token` | string |  | Parameter defines the next page token. It is used for retrieving the next page of results, like scrolling down on DuckDuckGo Shopping. Up to 30 results are returned per page. The next page token can be found in the the…  |

## Details

Search DuckDuckGo Shopping by keyword and get product listings with title, price, merchant, rating and link, by region.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/duckduckgo/shopping" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "airpods"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | Yes | Parameter defines the query you want to search. You can use anything that you would use in a regular DuckDuckGo Shopping search. Parameter length can not exceed 500 characters. |
| `kl` | string | No | Parameter defines the region to use for the DuckDuckGo Shopping search. It sets the stores, the language, and the currency of the products. Region code examples: `us-en` (default) for the United States, `uk-en` for United Kingdom, or `fr-fr |
| `sort_by` | string | No | Parameter defines the sorting order of the results. It defaults to DuckDuckGo's featured order. Available options: `1` - Price: low to high `2` - Price: high to low |
| `filters` | string | No | Parameter defines the filters to apply, like a brand, a price range, or a store. You can find its value in `filters` of the results: each option has a `value`. To combine filters, apply them one at a time, like on DuckDuckGo: in the results |
| `next_page_token` | string | No | Parameter defines the next page token. It is used for retrieving the next page of results, like scrolling down on DuckDuckGo Shopping. Up to 30 results are returned per page. The next page token can be found in the the API JSON response: `t |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/duckduckgo/shopping.json`](../../../catalog/models/duckduckgo/shopping.json) · Store page: https://www.sandbase.ai/model/duckduckgo/shopping
