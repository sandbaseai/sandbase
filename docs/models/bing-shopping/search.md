# Bing Shopping Search

`bing-shopping/search` · api · Bing Shopping

Search Bing Shopping by keyword: product title, price, old price, seller, rating, reviews and shipping, with market and filter options.

## Pricing

- **$0.015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bing-shopping/search", "q": "wireless earbuds"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bing-shopping/search', {'q': 'wireless earbuds'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bing-shopping/search", {
  "q": "wireless earbuds"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bing-shopping/search", sandbase.Params{
	"q": "wireless earbuds",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/bing-shopping/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string \\| number \\| boolean | yes | The search query. You can use anything that you would use in a regular Bing Shopping search.  |
| `cc` | string \\| number \\| boolean |  | The country to search from. It follows the 2-character ISO_3166-1 format. (e.g., `us` for United States, `de` for Germany, `gb` for United Kingdom, etc.).  |
| `mkt` | string \\| number \\| boolean |  | The market where the results come from (e.g. `en-US`). Typically, `mkt` is the country where the user is making the request from. However, it could be a different country if the user is not located in a country where…  |
| `device` | string \\| number \\| boolean |  | The device to use to get the results. It can be set to `desktop` (default) to use a regular browser, `tablet` to use a tablet browser (currently using iPads), or `mobile` to use a mobile browser.  |
| `efirst` | string \\| number \\| boolean |  | Controls the offset of the shopping results. (e.g., `efirst=10` will move the 10th shopping result to the first position).  |
| `filters` | string \\| number \\| boolean |  | Allows usage of a more complex filtering options such as filtering by date range `ex1:"ez5_18169_18230"` or using a specific display filters such as…  |
| `json_restrictor` | string \\| number \\| boolean |  | The fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |

## Details

Search Bing Shopping by keyword: product title, price, old price, seller, rating, reviews and shipping, with market and filter options.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bing-shopping/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "wireless earbuds"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string/number/boolean | Yes | The search query. You can use anything that you would use in a regular Bing Shopping search. |
| `cc` | string/number/boolean | No | The country to search from. It follows the 2-character ISO_3166-1 format. (e.g., `us` for United States, `de` for Germany, `gb` for United Kingdom, etc.). |
| `device` | string/number/boolean | No | The device to use to get the results. It can be set to `desktop` (default) to use a regular browser, `tablet` to use a tablet browser (currently using iPads), or `mobile` to use a mobile browser. |
| `efirst` | string/number/boolean | No | Controls the offset of the shopping results. (e.g., `efirst=10` will move the 10th shopping result to the first position). |
| `filters` | string/number/boolean | No | Allows usage of a more complex filtering options such as filtering by date range `ex1:"ez5_18169_18230"` or using a specific display filters such as `ufn:"Wunderman+Thompson"+sid:"5bede9a2-1bda-9887-e… |
| `json_restrictor` | string/number/boolean | No | The fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |
| `mkt` | string/number/boolean | No | The market where the results come from (e.g. `en-US`). Typically, `mkt` is the country where the user is making the request from. However, it could be a different country if the user is not located in… |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/bing-shopping/search.json`](../../../catalog/models/bing-shopping/search.json) · Store page: https://www.sandbase.ai/model/bing-shopping/search
