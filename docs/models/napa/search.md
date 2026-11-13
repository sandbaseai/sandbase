# NAPA Auto Parts Search API: pricing, parameters and code examples

`napa/search` · data API · NAPA · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Search NAPA auto parts by keyword with part number, brand, price, rating and store availability.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "napa/search", "q": "brake pads"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('napa/search', {'q': 'brake pads'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("napa/search", {
  "q": "brake pads"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "napa/search", sandbase.Params{
	"q": "brake pads",
})
```

Same call via the path form: `POST /v1/api/napa/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string | yes | Parameter defines the search query. You can use anything that you would use in a regular NAPA Auto Parts search: a part name, a brand, or a part number, including the part numbers of other brands that NAPA products…  |
| `page` | string |  | Value is used to get results on a specific page. (e.g., `1` (default) is the first page of results, `2` is the 2nd page of results, `3` is the 3rd page of results, etc.). NAPA returns up to 12 results per page.  |
| `sort` | string |  | Parameter defines the sorting of the results. It defaults to `relevance`. Available options: `relevance` - Relevance `price_low_to_high` - Price - low to high `price_high_to_low` - Price - high to low…  |
| `store_id` | string |  | Parameter defines the NAPA Auto Parts store to get the prices, promotions, and availability from. It's the number at the end of the URL of the store page on napaonline.com (e.g., `22706` for…  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |

## Details

Search NAPA auto parts by keyword with part number, brand, price, rating and store availability.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/napa/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "brake pads"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | Yes | Parameter defines the search query. You can use anything that you would use in a regular NAPA Auto Parts search: a part name, a brand, or a part number, including the part numbers of other brands that NAPA products replace (e.g., `brake cle |
| `store_id` | string | No | Parameter defines the NAPA Auto Parts store to get the prices, promotions, and availability from. It's the number at the end of the URL of the store page on napaonline.com (e.g., `22706` for `https://www.napaonline.com/en/ca/healdsburg/stor |
| `sort` | string | No | Parameter defines the sorting of the results. It defaults to `relevance`. Available options: `relevance` - Relevance `price_low_to_high` - Price - low to high `price_high_to_low` - Price - high to low `product_description` - Product descrip |
| `page` | string | No | Value is used to get results on a specific page. (e.g., `1` (default) is the first page of results, `2` is the 2nd page of results, `3` is the 3rd page of results, etc.). NAPA returns up to 12 results per page. |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/napa/search.json`](../../../catalog/models/napa/search.json) · Store page: https://www.sandbase.ai/model/napa/search
