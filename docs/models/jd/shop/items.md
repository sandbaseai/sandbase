# JD.com Shop Products API: pricing, parameters and code examples

`jd/shop/items` · data API · JD.com · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.028571 per call · **Modes:** sync

List products from a JD.com shop by shop ID, page by page, to collect item IDs for follow-up lookups.

## Pricing

- **$0.028571 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "jd/shop/items", "shopId": "1000278560"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('jd/shop/items', {'shopId': '1000278560'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("jd/shop/items", {
  "shopId": "1000278560"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "jd/shop/items", sandbase.Params{
	"shopId": "1000278560",
})
```

Same call via the path form: `POST /v1/api/jd/shop/items` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | string |  | Page number for the paginated shop product list.  |
| `shopId` | string | yes | A unique shop identifier on JD.com (Shop ID).  |

## Details

This API returns a page of products from a JD.com shop. Each item has an ID, a product link, and a title. You send the shop ID in `shopId` and can add `page` to move through the list.

### Use cases

- Collect every item ID in a competitor's JD.com shop for catalog tracking.
- Build a product list for one brand's flagship store to feed later detail lookups.
- Count how many products a shop lists by reading `totalResults`.
- Match shop product titles against your own catalog to find overlapping items.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/jd/shop/items" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"shopId": "1000278560"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `shopId` | string | Yes | A unique shop identifier on JD.com (Shop ID). |
| `page` | string | No | Page number for the paginated shop product list. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "ItemList": [
    {
      "itemId": "100431386728",
      "link": "https://item.jd.com/100431386728.html",
      "title": "决色iPhone DUO蒙德里安·平衡"
    }
  ],
  "TotalPage": 24,
  "shopId": "1000278560",
  "shopName": "决色（DEFENSE）京东自营旗舰店",
  "totalResults": 563,
  "venderId": "1000278560"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `ItemList[].itemId` | JD.com item ID of the product. Use it as input for follow-up item lookups. |
| `ItemList[].link` | Direct URL of the product page on item.jd.com. |
| `ItemList[].title` | Product title as listed in the shop. The text is in Chinese. |
| `TotalPage` | Total number of pages available for this shop's product list. |
| `totalResults` | Total number of products in the shop's list. |
| `shopId / venderId` | Identifiers of the shop. Both have the same value in this response. |
| `shopName` | Display name of the shop. |

### Notes

- Pass `page` as a string to read later pages. Use `TotalPage` to know where to stop.
- Item IDs are numeric strings such as `100431386728`. Pass them to [JD.com Product Details](/apis/jd/item/detail) for full product data.
- Call [JD.com Product Comments](/apis/jd/item/comments) with an item ID to read reviews for a product.

### Pricing

$0.028571 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/jd/shop/items.json`](../../../../catalog/models/jd/shop/items.json) · Store page: https://www.sandbase.ai/model/jd/shop/items
