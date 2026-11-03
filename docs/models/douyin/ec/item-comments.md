# Douyin Shop Item Comments API: pricing, parameters and code examples

`douyin/ec/item-comments` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.025714 per call · **Modes:** sync

Get paginated buyer comments for a Douyin shop product by item ID, with rating, text and media.

## Pricing

- **$0.025714 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/ec/item-comments", "itemId": "3734619545235751048"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/ec/item-comments', {'itemId': '3734619545235751048'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/ec/item-comments", {
  "itemId": "3734619545235751048"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/ec/item-comments", sandbase.Params{
	"itemId": "3734619545235751048",
})
```

Same call via the path form: `POST /v1/api/douyin/ec/item-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | string |  | Page number for paginated comments.  |
| `itemId` | string | yes | The unique ID of the item on Douyin E-commerce.  |

## Details

Returns buyer comments for one Douyin shop product, 'itemId' in, a page of comments out. Each comment has the review text, a star rating, photos, the SKU bought, and a snapshot of the order. The response also gives the total comment count and a flag for more pages.

### Use cases

- Read buyer feedback on a competing product to see what customers praise or complain about.
- Collect comment text and ratings for sentiment analysis on one product.
- Pull review photos to check how the product looks in real use.
- Compare which SKUs buyers choose by reading the `Sku` and order price fields.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/ec/item-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"itemId": "3734619545235751048"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `itemId` | string | Yes | The unique ID of the item on Douyin E-commerce. |
| `page` | string | No | Page number for paginated comments. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "Comments": [
    {
      "AppId": 1128,
      "AppealStatus": 0,
      "BrowseCount": 0,
      "CanAppend": true,
      "CommentTime": "2026-11-03 13:03:17",
      "CommentType": 0,
      "Content": "非常实惠，用着效果也很好。",
      "Id": 5218347791751037220,
      "IsAbnormalOrder": 0,
      "IsAnonymous": true,
      "KolId": 1382519684468436,
      "Liked": false
    }
  ],
  "Count": 4264,
  "HasMore": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `Comments[].Content` | Review text written by the buyer. It can be an empty string when the buyer left only a rating or photos. |
| `Comments[].Rank / RankProduct / RankLogistic / RankShop` | Star-style scores. `Rank` is the overall score and `RankProduct` is the product score. `RankLogistic` and `RankShop` are scores for delivery and shop, and show `0` when not given. |
| `Comments[].CommentTime` | Time the comment was posted, as a `YYYY-MM-DD HH:MM:SS` string. |
| `Comments[].Id` | Unique ID of the comment. |
| `Comments[].UserName / IsAnonymous` | Masked display name of the buyer and whether the comment was posted anonymously. |
| `Comments[].Sku` | Name of the SKU variant the buyer purchased. |
| `Comments[].OrderSnapshot.order_sku_price / order_item_num` | Price of the SKU and number of items in the order. In the sample, `3990` sits with a single item, so the price is likely in minor currency units, but the response does not state the unit. |
| `Comments[].Photos[].url / thumbnail` | Links to the full-size and small versions of each photo attached to the comment. `PhotoPoster` holds the cover image when present. |
| `Comments[].Likes / ShopReply` | Number of likes on the comment and the shop's reply text. `ShopReply` is empty when the shop has not replied. |
| `Count / HasMore` | `Count` is the total number of comments for the item. `HasMore` is `true` when more pages exist. |

### Notes

- Get `itemId` from [Douyin Shop Product Search](/apis/douyin/ec/search-items) or [Douyin Shop Items](/apis/douyin/ec/shop-items).
- Send `page` to move through the results. Keep requesting while `HasMore` is `true`.
- `Comments[].ProductId` matches the `itemId` you sent. `Comments[].ShopId` identifies the shop.
- `Order` and `Product` are JSON strings inside the response. Parse them again to read the shop name and product title.

### Pricing

$0.025714 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/douyin/ec/item-comments.json`](../../../../catalog/models/douyin/ec/item-comments.json) · Store page: https://www.sandbase.ai/model/douyin/ec/item-comments
