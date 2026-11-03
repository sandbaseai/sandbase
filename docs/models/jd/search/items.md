# JD.com Product Search API: pricing, parameters and code examples

`jd/search/items` · data API · JD.com · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Search JD.com products by keyword with item IDs, titles, images, categories and shop names, with page-based pagination.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "jd/search/items", "keyword": "蓝牙耳机"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('jd/search/items', {'keyword': '蓝牙耳机'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("jd/search/items", {
  "keyword": "蓝牙耳机"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "jd/search/items", sandbase.Params{
	"keyword": "蓝牙耳机",
})
```

Same call via the path form: `POST /v1/api/jd/search/items` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | string |  | Page number for pagination.  |
| `keyword` | string | yes | Search keyword.  |

## Details

Returns a page of JD.com products that match a search keyword. Each product has an item ID, an image path, category IDs, a sales count label and review tags. Send a `keyword` and an optional `page` number.

### Use cases

- Build a list of competing phone case listings for a keyword and track which item IDs appear.
- Collect item IDs from search results, then fetch full details for each one.
- Compare the review tags and positive-rate scores of products in one category.
- Check how many results JD.com shows for a keyword by reading the total count and page count.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/jd/search/items" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "手机壳"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword. |
| `page` | string | No | Page number for pagination. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "currentPage": 1,
  "pageSize": 0,
  "products": [
    {
      "adSkuType": 1,
      "adType": 3,
      "asgAttribute": "",
      "asgHighlight": "",
      "asgRecReason": "",
      "asgStructuredAttribute": "",
      "bId": "13056",
      "bybtTraffic": 0,
      "cc": "10万+",
      "cid1": "9987",
      "cid2": "830",
      "cid3": "866"
    }
  ],
  "totalCount": 7607,
  "totalPages": 159
}
```

### Response fields

| Field | Meaning |
|---|---|
| `products[].id` | Item ID of the product. Use it to look up the product in other JD.com APIs. |
| `products[].imageUrl` | Image path of the product, such as `jfs/t1/.../xxx.jpg`. The response gives a relative path, not a full URL. |
| `products[].bId` | ID of the brand or seller entry tied to the product, as a string. |
| `products[].cid1 / cid2 / cid3` | Category IDs at three levels, from broad to narrow. |
| `products[].cc` | Count label shown on the listing, such as `10万+` or `5000+`. |
| `products[].gcp` | Score from 0 to 100 shown with the product. The key name and values suggest a positive-review percentage. |
| `products[].gcw` | List of short review tags for the product, such as `手感一流`. |
| `products[].gct` | Review tags joined into one text line, starting with `推荐理由：`. |
| `products[].foi` | Installment label, such as `6期免息`. It is an empty string when there is none. |
| `totalCount / totalPages` | Total number of matching products and the number of result pages. |

### Notes

- `keyword` is required. `page` is a string holding the page number, and `currentPage` in the response shows which page you got.
- Many fields in each product, such as `coupons`, `discounts` and `gifts`, can be empty lists or empty strings.
- In the sample response `pageSize` is `0`, so count the items in `products` to get the real page size.
- To get titles, shop details and prices for an item ID, call [JD.com Product Details](/apis/jd/item/detail). For reviews, call [JD.com Product Comments](/apis/jd/item/comments).

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/jd/search/items.json`](../../../../catalog/models/jd/search/items.json) · Store page: https://www.sandbase.ai/model/jd/search/items
