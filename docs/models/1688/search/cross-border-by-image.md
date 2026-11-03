# 1688 Cross-border Image Search API: pricing, parameters and code examples

`1688/search/cross-border-by-image` · data API · 1688 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Find 1688 cross-border products that match an image URL, with translated titles, sorting and sourcing filters such as dropshipping, factory and verified supplier.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "1688/search/cross-border-by-image", "imgUrl": "https://cbu01.alicdn.com/img/ibank/O1CN01Zb1jbH1Bs2wE7Uu3W_!!2215541593486-0-cib.jpg"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('1688/search/cross-border-by-image', {'imgUrl': 'https://cbu01.alicdn.com/img/ibank/O1CN01Zb1jbH1Bs2wE7Uu3W_!!2215541593486-0-cib.jpg'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("1688/search/cross-border-by-image", {
  "imgUrl": "https://cbu01.alicdn.com/img/ibank/O1CN01Zb1jbH1Bs2wE7Uu3W_!!2215541593486-0-cib.jpg"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "1688/search/cross-border-by-image", sandbase.Params{
	"imgUrl": "https://cbu01.alicdn.com/img/ibank/O1CN01Zb1jbH1Bs2wE7Uu3W_!!2215541593486-0-cib.jpg",
})
```

Same call via the path form: `POST /v1/api/1688/search/cross-border-by-image` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number, starting at 1. default `1` |
| `sort` | string |  | Product sort order. one of: `default`, `sales`, `price_up`, `price_down`; default `"default"` |
| `imgUrl` | string | yes | Image URL or image reference returned by Image Conversion. Convert external images for the selected search target before searching.  |
| `language` | string |  | Output language. one of: `en`, `zh`, `ru`, `th`, `pt`, `es`, `tr`, `vi`, `ja`, `ko`; default `"en"` |
| `pageSize` | integer |  | Number of items requested per page. The returned count may differ. default `20` |
| `priceEnd` | string |  | Maximum price filter in CNY.  |
| `isFactory` | boolean |  | Filter by factory status.  |
| `newArrival` | boolean |  | Filter for new products.  |
| `priceStart` | string |  | Minimum price filter in CNY.  |
| `freeShipping` | boolean |  | Filter for free shipping.  |
| `verifiedSupplier` | boolean |  | Filter for verified sellers.  |
| `supportDropshipping` | boolean |  | Filter for support for dropshipping.  |

## Details

Returns a list of 1688 cross-border products that match an image, plus the paging and sort values used for the request. It needs an image URL in `imgUrl`. You can also set the output language, sort order and sourcing filters.

### Use cases

- Find cross-border suppliers that sell a product you saw on another site by searching with its photo.
- Compare matching listings sorted by `sales` to pick a sourcing candidate.
- Narrow matches to dropshipping, factory or verified suppliers before contacting sellers.
- Check whether a product image has any cross-border matches on 1688.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/1688/search/cross-border-by-image" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"imgUrl": "https://cbu01.alicdn.com/img/ibank/O1CN01Zb1jbH1Bs2wE7Uu3W_!!2215541593486-0-cib.jpg"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `imgUrl` | string | Yes | Image URL or image reference returned by Image Conversion. Convert external images for the selected search target before searching. |
| `freeShipping` | boolean | No | Filter for free shipping. |
| `isFactory` | boolean | No | Filter by factory status. |
| `language` | string | No | Output language. |
| `newArrival` | boolean | No | Filter for new products. |
| `page` | integer | No | Page number, starting at 1. |
| `pageSize` | integer | No | Number of items requested per page. The returned count may differ. |
| `priceEnd` | string | No | Maximum price filter in CNY. |
| `priceStart` | string | No | Minimum price filter in CNY. |
| `sort` | string | No | Product sort order. |
| `supportDropshipping` | boolean | No | Filter for support for dropshipping. |
| `verifiedSupplier` | boolean | No | Filter for verified sellers. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "filters": {},
  "items": [],
  "page": 1,
  "page_size": 20,
  "sort": "default",
  "total_count": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `items[]` | List of matching products on the current page. In the sample response it is empty, so no matches were found for that image. |
| `total_count` | Total number of matches reported for the search. The sample response returns `0`. |
| `page` | Page number of this result, starting at 1. |
| `page_size` | Number of items requested per page. The number of items actually returned may differ. |
| `sort` | Sort order applied to the results. The sample response shows `default`. |
| `filters` | Object that holds the filters applied to the search. It is empty when no filters are sent. |

### Notes

- Only `imgUrl` is required. Use `page` and `pageSize` to move through results.
- `imgUrl` accepts an image URL or an image reference returned by Image Conversion. Convert external images before searching.
- For a text-based search, use [1688 Cross-border Product Search](/apis/1688/search/cross-border). To search all 1688 products by image, use [1688 Image Search](/apis/1688/search/by-image).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/1688/search/cross-border-by-image.json`](../../../../catalog/models/1688/search/cross-border-by-image.json) · Store page: https://www.sandbase.ai/model/1688/search/cross-border-by-image
