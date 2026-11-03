# Taobao Product Search API: pricing, parameters and code examples

`taobao/search/items` · data API · Taobao · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.028571 per call · **Modes:** sync

Search Taobao and Tmall products by keyword with titles, prices, images, sales and shop info. Sort by sales or price, filter to Tmall only and by price range.

## Pricing

- **$0.028571 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "taobao/search/items", "keyword": "蓝牙耳机"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('taobao/search/items', {'keyword': '蓝牙耳机'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("taobao/search/items", {
  "keyword": "蓝牙耳机"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "taobao/search/items", sandbase.Params{
	"keyword": "蓝牙耳机",
})
```

Same call via the path form: `POST /v1/api/taobao/search/items` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number for pagination. default `1` |
| `sort` | string |  | Sort order for the result set. one of: `_sale`, `_bid`, `bid`, `_coefp`; default `"_sale"` |
| `tmall` | boolean |  | Whether to filter results to Tmall only. default `false` |
| `keyword` | string | yes | Search keyword.  |
| `endPrice` | string |  | Maximum price filter (inclusive).  |
| `startPrice` | string |  | Minimum price filter (inclusive).  |

## Details

Returns a page of Taobao and Tmall product listings that match a keyword. Each item has a title, price, image URLs, a sales band, seller location and shop details. The only required input is `keyword`.

### Use cases

- Compare prices and sales bands for one product type, such as phone cases, across many shops.
- Track which shops and sellers rank first for a keyword sorted by sales.
- Build a catalog of product images and titles for a niche, filtered to Tmall only.
- Check how many listings match a keyword and which brands, materials and styles appear most often.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/taobao/search/items" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "手机壳"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword. |
| `endPrice` | string | No | Maximum price filter (inclusive). |
| `page` | integer | No | Page number for pagination. |
| `sort` | string | No | Sort order for the result set. |
| `startPrice` | string | No | Minimum price filter (inclusive). |
| `tmall` | boolean | No | Whether to filter results to Tmall only. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": "SUCCESS",
  "extraMap": {
    "MtopCostMillis": 91
  },
  "model": {
    "brandList": [
      {
        "brandId": 20796,
        "brandName": "\u0003欧世铭\u0003欧康胜\u0003欧易金\u0002欧潭\u0003欧皇雅\u0003欧雅琪\u0002歌姿\u0003歌朵琪\u0004步止有礼\u0002氏分\u0002汇将\u0002沁缘\u0005泮水洗青竹\u0003活水泉\u0002浩岩\u0006浩鲸智在记录\u0002浪联\u0003海易鸿\u0002涎墨\u0003润源希\u0002润…",
        "count": 0
      }
    ],
    "costMillis": 91,
    "extraMap": {
      "Endpoint": "taobao_item",
      "EndpointHost": "33.78.87.32",
      "WorldsearchIP": "33.44.173.30",
      "WorldsearchName": "worldsearch033044173030.center.na620",
      "afterSearchCostMillis": 0,
      "sp_status": "OK"
    },
    "itemList": [
      {
        "cityEn": "",
        "commentCount": "",
        "discntPriceYuan": 136.0,
        "discntRate": 10000,
        "discntType": "特价秒杀",
        "extraMap": {},
        "fahuoDsr": "490",
        "frontStock": 3587930,
        "fuwuDsr": "488",
        "hasTongkuan": false,
        "hasXiangsi": false,
        "itemGradeAvg": 0.0
      }
    ],
    "page": {
      "nextNo": 2,
      "pageNo": 1,
      "pageSize": 10,
      "prevNo": 1,
      "showBegin": 1,
      "showEnd": 3,
      "totalItems": 48989,
      "totalPages": 4899
    },
    "propertyList": [
      {
        "flag": "qp_commend",
        "pid": 28102,
        "pname": "适用品牌",
        "valueList": [
          {
            "count": 6233,
            "flag": "qp_commend",
            "vid": 30111,
            "vname": "Apple/苹果"
          }
        ]
      }
    ],
    "responseStatus": 0,
    "success": true,
    "traceList": []
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `model.itemList[].itemId` | Product ID. Use it to look up one product in other Taobao APIs. |
| `model.itemList[].itemName / itemSubName` | Listing title and the shorter selling-point line under it. The sub name can be empty. |
| `model.itemList[].priceYuanDouble / priceFen` | List price in yuan, and the same price in fen (`13600` fen is `136.0` yuan). |
| `model.itemList[].discntPriceYuan / discntType` | Discounted price in yuan and the label of the offer, such as `优惠价` or `特价秒杀`. |
| `model.itemList[].orderPayUV` | Sales band shown as text, for example `1万+`. It is a rounded label, not an exact count. |
| `model.itemList[].picUrlFull / picUrlList` | Full URL of the main image, and a list of extra image paths for the product. |
| `model.itemList[].shopId / shopName / sellerLevel` | Shop ID, shop name and the seller level number. |
| `model.itemList[].itemLoc / sellerLoc` | Province and city for the item and for the seller. Either can be an empty string. |
| `model.page.pageNo / pageSize / totalItems / totalPages` | Current page number, items per page, total matching items and total page count. |
| `model.propertyList[].pname / valueList[].vname / count` | Filter facets such as brand or material, with the number of matching items for each value. |

### Notes

- Request the next page with the `page` parameter. `model.page.nextNo` gives the next page number.
- `sort` accepts `_sale`, `_bid`, `bid` and `_coefp`. The default is `_sale`.
- Prices in `startPrice` and `endPrice` are strings and both limits are inclusive.
- Pass `itemId` to [Taobao Product Details](/apis/taobao/item/detail) for one product, or `shopId` to [Taobao Shop Product List](/apis/taobao/shop-item-list) for a full shop.

### Pricing

$0.028571 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/taobao/search/items.json`](../../../../catalog/models/taobao/search/items.json) · Store page: https://www.sandbase.ai/model/taobao/search/items
