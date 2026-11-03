# Taobao Product Reviews API: pricing, parameters and code examples

`taobao/item/reviews` · data API · Taobao · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.028571 per call · **Modes:** sync

Get Taobao and Tmall product reviews by item ID with pagination, sorted by latest or default, for customer feedback analysis.

## Pricing

- **$0.028571 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "taobao/item/reviews", "itemId": "920640959876"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('taobao/item/reviews', {'itemId': '920640959876'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("taobao/item/reviews", {
  "itemId": "920640959876"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "taobao/item/reviews", sandbase.Params{
	"itemId": "920640959876",
})
```

Same call via the path form: `POST /v1/api/taobao/item/reviews` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number for pagination. default `1` |
| `itemId` | string | yes | Unique product identifier on Taobao/Tmall (item ID).  |
| `orderType` | string |  | Sort order for the result set. one of: `feedbackdate`, `general`; default `"feedbackdate"` |

## Details

This API returns customer reviews for a Taobao or Tmall product. It needs the product `itemId`, and it returns one page of reviews with review text, buyer SKU, photos, and summary counts.

### Use cases

- Read the newest buyer feedback on a Taobao listing to spot new complaints.
- Count how often review tags such as battery life or delivery speed come up for a product.
- Collect review photos to see how buyers use or receive an item.
- Compare reviews across SKU variants to find which version buyers praise or criticize.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/taobao/item/reviews" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"itemId": "920640959876"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `itemId` | string | Yes | Unique product identifier on Taobao/Tmall (item ID). |
| `orderType` | string | No | Sort order for the result set. |
| `page` | integer | No | Page number for pagination. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "comments": [
    {
      "append": null,
      "appendCanExplainable": false,
      "appendList": [],
      "auction": {
        "aucNumId": "920640959876",
        "auctionPic": "",
        "link": "//item.taobao.com/auction/item_detail.htm?item_num_id=920640959876",
        "sku": "套餐类型:官方标配;颜色分类:【经典款·BC1lite】星际黑●全景空间音效●舒适佩戴",
        "thumbnail": "",
        "title": ""
      },
      "award": "",
      "bidPriceMoney": null,
      "buyAmount": 0,
      "content": "该用户觉得商品非常好，给出5星好评",
      "creditFraudRule": 0,
      "date": "2026年11月03日 15:28",
      "dayAfterConfirm": 0,
      "enableSNS": false
    }
  ],
  "currentPageNum": 1,
  "hasAppendCount": 700,
  "hasMediaCount": 2000,
  "hasNextPage": true,
  "keywords": [
    {
      "count": "354",
      "labelId": "2079958979-11",
      "type": "1",
      "word": "续航能力强"
    }
  ],
  "maxPage": 50,
  "qnaDisabled": true,
  "total": 20000,
  "totalFuzzy": "2万+",
  "watershed": 100
}
```

### Response fields

| Field | Meaning |
|---|---|
| `comments[].content` | Text of the review. |
| `comments[].date` | Review time as a text string, for example `2026年11月03日 15:28`. |
| `comments[].auction.sku` | The SKU the buyer purchased, with package type and color options. |
| `comments[].rateId` | Unique ID of the review. |
| `comments[].photos[].url / comments[].photos[].thumbnail` | Links to the full image and the small thumbnail attached to the review. The links start with `//`. The list is empty when the review has no photos. |
| `comments[].user.nick` | Masked buyer nickname. `comments[].user.anony` shows whether the review is anonymous. |
| `comments[].likeCount / comments[].useful` | Counts of likes and useful votes on the review. |
| `keywords[].word / keywords[].count` | Review tag text and the number of reviews that mention it. |
| `total / totalFuzzy` | Total number of reviews as a number and as a short text such as `2万+`. |
| `currentPageNum / maxPage / hasNextPage` | Pagination state: the current page, the last page number, and whether another page exists. |

### Notes

- Use the `page` parameter to move through results. Check `hasNextPage` in each response before you ask for the next page.
- `orderType` accepts `feedbackdate` (default) or `general`.
- Get the `itemId` from the product search or product detail APIs, such as [Taobao Product Search](/apis/taobao/search/items) or [Taobao Product Details](/apis/taobao/item/detail).
- For buyer questions about the same product, call [Taobao Product Questions](/apis/taobao/item/questions).

### Pricing

$0.028571 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/taobao/item/reviews.json`](../../../../catalog/models/taobao/item/reviews.json) · Store page: https://www.sandbase.ai/model/taobao/item/reviews
