# Google Shopping Product Offers API: pricing, parameters and code examples

`google-shopping/immersive-product` · data API · Google Shopping · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Get the full Google Shopping product view by page token: specifications, ratings, reviews and offers from each store with price and delivery.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google-shopping/immersive-product", "page_token": "<page_token>"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google-shopping/immersive-product', {'page_token': '<page_token>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google-shopping/immersive-product", {
  "page_token": "<page_token>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google-shopping/immersive-product", sandbase.Params{
	"page_token": "<page_token>",
})
```

Same call via the path form: `POST /v1/api/google-shopping/immersive-product` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page_token` | string | yes | Parameter defines the token needed to show more product info in Google immersive popup.  |
| `more_stores` | string |  | Parameter for fetching more stores results in single search. It can be set to `1` or `true`. By default, a search returns `3 to 5` stores. When the `more_stores` parameter is **enabled**, up to `13` stores will be…  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |
| `next_page_token` | string |  | Parameter defines the next page token. It is used for retrieving the next page of results for stores. The token is returned as `stores_next_page_token` from the search results.  |

## Details

Get the full Google Shopping product view by page token: specifications, ratings, reviews and offers from each store with price and delivery.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google-shopping/immersive-product" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"page_token": "<page_token from search results>"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `page_token` | string | Yes | Parameter defines the token needed to show more product info in Google immersive popup. |
| `more_stores` | string | No | Parameter for fetching more stores results in single search. It can be set to `1` or `true`. By default, a search returns `3 to 5` stores. When the `more_stores` parameter is **enabled**, up to `13` stores will be returned, or the maximum a |
| `next_page_token` | string | No | Parameter defines the next page token. It is used for retrieving the next page of results for stores. The token is returned as `stores_next_page_token` from the search results. |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/google-shopping/immersive-product.json`](../../../catalog/models/google-shopping/immersive-product.json) · Store page: https://www.sandbase.ai/model/google-shopping/immersive-product
