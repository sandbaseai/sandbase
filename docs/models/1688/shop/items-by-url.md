# 1688 Shop Products by URL API: pricing, parameters and code examples

`1688/shop/items-by-url` · data API · 1688 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

List a 1688 shop's products from its homepage URL, with sort, page size and category filters.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "1688/shop/items-by-url", "shopUrl": "https://winport.m.1688.com/page/index.html?memberId=b2b-35345497994841a"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('1688/shop/items-by-url', {'shopUrl': 'https://winport.m.1688.com/page/index.html?memberId=b2b-35345497994841a'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("1688/shop/items-by-url", {
  "shopUrl": "https://winport.m.1688.com/page/index.html?memberId=b2b-35345497994841a"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "1688/shop/items-by-url", sandbase.Params{
	"shopUrl": "https://winport.m.1688.com/page/index.html?memberId=b2b-35345497994841a",
})
```

Same call via the path form: `POST /v1/api/1688/shop/items-by-url` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cat` | string |  | Optional category ID filter.  |
| `page` | integer |  | Page number, starting at 1. default `1` |
| `sort` | string |  | Shop product sort order. one of: `default`, `sales`, `price_up`, `price_down`, `time_up`, `time_down`; default `"default"` |
| `catType` | string |  | Optional category mode: 0 or 1. one of: `0`, `1` |
| `shopUrl` | string | yes | 1688 shop homepage URL.  |
| `pageSize` | integer |  | Number of items requested per page. The returned count may differ. default `20` |

## Details

Returns a page of products from a 1688 shop, including title, image, category, unit and sales counts for each item. It needs the shop homepage URL as `shopUrl`.

### Use cases

- Build a catalog snapshot of a supplier's shop to compare its range against other suppliers.
- Rank a shop's products with `sort` set to `sales` to find its best sellers.
- Track new listings by sorting with `time_down` and reading `created_time`.
- Spot items with no recent orders by checking where `orders_count_30days` is `0`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/1688/shop/items-by-url" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"shopUrl": "https://winport.m.1688.com/page/index.html?memberId=b2b-35345497994841a"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `shopUrl` | string | Yes | 1688 shop homepage URL. |
| `cat` | string | No | Optional category ID filter. |
| `catType` | string | No | Optional category mode: 0 or 1. |
| `page` | integer | No | Page number, starting at 1. |
| `pageSize` | integer | No | Number of items requested per page. The returned count may differ. |
| `sort` | string | No | Shop product sort order. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "has_next_page": true,
  "items": [
    {
      "category_name": "手机保护套",
      "created_time": "2025-10-20T14:58:00+0800",
      "img": "https://cbu01.alicdn.com/img/ibank/O1CN01cj5gcs2MG09GeflrL_!!3534549799-0-cib.31…",
      "item_id": 986450227729,
      "price": "3.5",
      "price_info": {
        "drop_ship_price": "3.5",
        "wholesale_price": "3.5"
      },
      "sale_info": {
        "orders_count_30days": 965,
        "sale_quantity": 5412
      },
      "title": "精孔肤感磁吸简约适用iphone16手机壳苹果18PROMAX透黑防摔保护套",
      "unit": "个"
    }
  ],
  "max_count": 3000,
  "page": 1,
  "page_size": 20,
  "price_end": null,
  "price_start": null,
  "shop_cat_id": "",
  "sort": "default",
  "total_count": 1063
}
```

### Response fields

| Field | Meaning |
|---|---|
| `items[].item_id` | Numeric ID of the product. Use it to look up the product in other 1688 APIs. |
| `items[].title` | Product title as listed in the shop, in Chinese. |
| `items[].sale_info.orders_count_30days / items[].sale_info.sale_quantity` | Order count for the last 30 days and the total sold quantity. The 30-day count can be `0` while the total is high. |
| `items[].category_name` | Name of the shop category the product belongs to. |
| `items[].created_time` | Listing time as an ISO 8601 style timestamp with a `+0800` offset. |
| `items[].img / items[].unit` | Product image URL and the selling unit, such as `个`. |
| `has_next_page` | `true` when more pages are available after the current one. |
| `total_count / max_count / page / page_size` | `total_count` is the number of products reported for the shop. `max_count` is returned alongside it. `page` and `page_size` echo the current page number and page size. |

### Notes

- Pass the shop homepage URL as `shopUrl`. The example uses a `memberId` query value in a `winport.m.1688.com` URL.
- Increase `page` while `has_next_page` is `true` to read the full list. The returned count per page may differ from `pageSize`.
- The response echoes the chosen sort order in `sort`. Use `sales` for best sellers or `time_down` for newest listings.
- To get category IDs for the `cat` filter, call [1688 Shop Categories](/apis/1688/shop/categories). To read one product in full, call [1688 Product Details](/apis/1688/item/detail) with `item_id`.

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/1688/shop/items-by-url.json`](../../../../catalog/models/1688/shop/items-by-url.json) · Store page: https://www.sandbase.ai/model/1688/shop/items-by-url
