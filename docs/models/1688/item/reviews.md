# 1688 Product Reviews API: pricing, parameters and code examples

`1688/item/reviews` · data API · 1688 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get buyer reviews for a 1688 product by item ID with pagination and default or latest sorting, for supplier and product quality research.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "1688/item/reviews", "itemId": "1046925823679"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('1688/item/reviews', {'itemId': '1046925823679'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("1688/item/reviews", {
  "itemId": "1046925823679"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "1688/item/reviews", sandbase.Params{
	"itemId": "1046925823679",
})
```

Same call via the path form: `POST /v1/api/1688/item/reviews` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number, starting at 1. default `1` |
| `itemId` | string | yes | 1688 product ID.  |
| `sortType` | string |  | Review sort order. one of: `default`, `latest`; default `"default"` |

## Details

Returns buyer reviews for a 1688 product. You pass the product ID as `itemId`, and you can set `page` and `sortType` to move through the reviews.

### Use cases

- Read the star ratings and comments on a product before you place a sourcing order.
- Compare which SKU variants buyers praise or complain about using the `sku_map` text.
- Sort by `latest` to check whether recent buyers report new quality problems.
- Collect review text for a product to run your own sentiment analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/1688/item/reviews" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"itemId": "1046925823679"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `itemId` | string | Yes | 1688 product ID. |
| `page` | integer | No | Page number, starting at 1. |
| `sortType` | string | No | Review sort order. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "item_id": 1046925823679,
  "list": [
    {
      "feedback": "该用户觉得商品非常赞，给出了五星好评",
      "feedback_date": "2026-10-31 15:42:43",
      "id": "41202658087",
      "rate_star": "5",
      "sku_map": "颜色:【升级版丨空洞黑】环绕9D音效★物理降噪★双核双芯片低延迟;类型:爆款【M47】升级版-蓝牙6.0",
      "user_nick": "t**1"
    }
  ],
  "page": 1,
  "page_size": 10,
  "sort_type": "default"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `item_id` | The 1688 product ID the reviews belong to. |
| `list[]` | The reviews on the current page. The sample response shows 3 reviews, and `page_size` is 10. |
| `list[].id` | The ID of a single review, as a string. |
| `list[].rate_star` | The star rating of the review, from the sample values `5` and `4`. It is returned as a string. |
| `list[].feedback` | The review text. In the sample it is a short auto-style sentence that states the star rating. |
| `list[].feedback_date` | The date and time of the review, in the format `YYYY-MM-DD HH:MM:SS`. |
| `list[].sku_map` | The SKU options the buyer purchased, written as `name:value` pairs separated by `;`, such as color and type. |
| `list[].user_nick` | The buyer's nickname, partly masked with `*`. |
| `page / page_size / sort_type` | The page number, the number of reviews per page, and the sort order used for this response. |

### Notes

- Get the `itemId` from a product search or detail call, such as [1688 Product Search](/apis/1688/search/items) or [1688 Product Details](/apis/1688/item/detail).
- Increase `page` by 1 to read more reviews. `page` starts at 1.
- `sortType` accepts `default` or `latest`. The response echoes the choice in `sort_type`.
- The review list is not guaranteed to be in date order when `sortType` is `default`. The sample `feedback_date` values are not sorted.

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/1688/item/reviews.json`](../../../../catalog/models/1688/item/reviews.json) · Store page: https://www.sandbase.ai/model/1688/item/reviews
