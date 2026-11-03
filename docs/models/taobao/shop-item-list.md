# Taobao Shop Product List API: pricing, parameters and code examples

`taobao/shop-item-list` · data API · Taobao · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.028571 per call · **Modes:** sync

Get products from a Taobao or Tmall shop using both seller or user ID and shop ID, with page-based pagination and sorting by sales, new arrivals, credit, or price. Use it to browse a known shop catalog.

## Pricing

- **$0.028571 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "taobao/shop-item-list", "userId": "1659916565", "shopId": "103710607"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('taobao/shop-item-list', {'userId': '1659916565', 'shopId': '103710607'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("taobao/shop-item-list", {
  "userId": "1659916565",
  "shopId": "103710607"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "taobao/shop-item-list", sandbase.Params{
	"userId": "1659916565",
	"shopId": "103710607",
})
```

Same call via the path form: `POST /v1/api/taobao/shop-item-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number for pagination. default `1` |
| `sort` | string |  | Sort order for the result set. one of: `sales-des`, `new-des`, `credit-des`, `price-asc`, `price-des`; default `"sales-des"` |
| `shopId` | string | yes | Unique shop identifier on Taobao/Tmall (shop ID).  |
| `userId` | string | yes | Shop identifier. Also known as Seller ID or User ID (they refer to the same value).  |

## Details

Returns one page of products from a Taobao or Tmall shop, plus shop details such as the shop name and service scores. It needs the seller ID (`userId`) and the shop ID (`shopId`). You can sort by sales, new arrivals, credit, or price.

### Use cases

- Pull the full catalog of a competitor shop and compare discount prices across pages.
- Track how a shop's product list changes by calling it with `sort` set to `new-des`.
- Check a shop's delivery, description and service scores before you source from it.
- Build a list of product categories a shop sells in using the category ID fields.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/taobao/shop-item-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"userId": "1659916565", "shopId": "103710607"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `shopId` | string | Yes | Unique shop identifier on Taobao/Tmall (shop ID). |
| `userId` | string | Yes | Shop identifier. Also known as Seller ID or User ID (they refer to the same value). |
| `page` | integer | No | Page number for pagination. |
| `sort` | string | No | Sort order for the result set. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "httpData": {
    "breadcrumbModuleResponse": {
      "breadcrumbList": [
        {
          "href": "https://taobao.com/",
          "name": "首页"
        }
      ],
      "success": true
    },
    "itemListModuleResponse": {
      "itemList": [
        {
          "areaLimit": false,
          "backCatId": 50012587,
          "backCatIdL1": 50008090,
          "commentCount": "8万+",
          "commentTagList": [],
          "currencySymbol": "฿",
          "discntPriceYuan": 52.94,
          "discntType": "品牌巨惠"
        }
      ],
      "page": {
        "hideTotalCount": "100",
        "nextNo": 2,
        "pageNo": 1,
        "pageSize": 60,
        "prevNo": 1,
        "showBegin": 1,
        "showEnd": 3,
        "totalCount": 262
      },
      "pageUrlFollow": false,
      "success": true
    },
    "metaModuleResponse": {
      "description": "欢迎光临-图拉斯旗舰店，淘宝网Taobao为你提供最新商品图片、价格、品牌、评价、折扣等信息，有问题可直接咨询商家！淘宝Taobao/天猫Tmall数亿热销好货…",
      "keyword": "图拉斯旗舰店",
      "linkList": [
        {
          "href": "https://taobao.com103710607.htm",
          "rel": "canonical"
        }
      ],
      "robots": "index,follow",
      "success": true,
      "title": "图拉斯旗舰店 - 淘宝网|Taobao - 天猫|Tmall"
    },
    "pageABTestModuleResponse": {
      "abTag": 0,
      "aeAsoTag": 0,
      "featureGrayResultMap": {
        "AUTO_LOGIN_GUIDE": {
          "bucketId": 0,
          "extProperties": {},
          "hit": true
        },
        "LOGIN_GUIDE": {
          "bucketId": 0,
          "extProperties": {},
          "hit": true
        }
      },
      "success": true
    },
    "pageSimplifiedModuleResponse": {
      "simplified": false,
      "simplifiedType": "NO_SIMPLIFIED",
      "success": false,
      "userId": "2223250982130"
    },
    "seoCommonBannerResponse": {
      "color": "#FC385B",
      "pcBanner": "https://img.alicdn.com/imgextra/i1/O1CN01v7EvqI29IfUrgeUNc_!!6000000008045-1-tps…",
      "success": true,
      "targetURl": "https://huodong.taobao.com/wow/a/act/tao/dailygroup/23509/24308/wupr?spm=a2141.2…"
    },
    "shopListModuleResponse": {
      "shopList": [
        {
          "deliverScore": "4.9",
          "descriptionMatchScore": "4.8",
          "picUrl": "//img.alicdn.com/imgextra/i2/1659916565/O1CN01CtYGJ01yMpFkZsjho_!!1659916565.jpg",
          "sellerId": 1659916565,
          "serviceScore": "4.8",
          "shopId": 103710607,
          "shopName": "图拉斯旗舰店"
        }
      ],
      "success": true
    },
    "statusCode": 0,
    "success": true
  },
  "pageData": {
    "client": "pc",
    "currentPath": "https://taobao.com",
    "currentUrl": "https://taobao.com103710607.htm",
    "detailUrl": "https://taobao.com/item/",
    "env": "production",
    "host": "pagehandler-handler.tmg-wormhole-n",
    "isBase64On": true,
    "keyword": "图拉斯旗舰店",
    "locale": "zh-tw",
    "loginGuideHit": true,
    "pageConfig": {
      "pageVersion": ""
    },
    "pageUrlFollow": false
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `httpData.itemListModuleResponse.itemList[]` | The products on the current page. Each entry holds the price, discount type, category IDs and review count of one product. |
| `httpData.itemListModuleResponse.itemList[].discntPriceYuan` | The discounted price of the product. Read it together with `currencySymbol`, which can show a symbol such as `฿`. |
| `httpData.itemListModuleResponse.itemList[].discntType` | The discount label for the product, for example `特价秒杀` or `品牌巨惠`. |
| `httpData.itemListModuleResponse.itemList[].commentCount` | The review count as text. Large values are shortened, for example `8万+`. |
| `httpData.itemListModuleResponse.itemList[].backCatId / backCatIdL1` | The product's category ID and its top-level category ID. |
| `httpData.itemListModuleResponse.page.totalCount` | The total number of products in the shop. |
| `httpData.itemListModuleResponse.page.pageNo / pageSize / nextNo / prevNo` | The current page number, the page size, and the numbers of the next and previous pages. |
| `httpData.shopListModuleResponse.shopList[].shopName` | The shop's display name. |
| `httpData.shopListModuleResponse.shopList[].sellerId / shopId` | The numeric seller ID and shop ID of the shop. |
| `httpData.shopListModuleResponse.shopList[].deliverScore / descriptionMatchScore / serviceScore` | The shop's delivery, description match and service scores, returned as text. |

### Notes

- Send `page` with the value of `nextNo` to get the next page. Compare `totalCount` with `pageSize` to see how many pages exist.
- `sort` accepts `sales-des` (default), `new-des`, `credit-des`, `price-asc` and `price-des`.
- Each item in `itemList` in this sample does not include a product ID or title. Use [Taobao Product Search](/apis/taobao/search/items) to find a product, then [Taobao Product Details](/apis/taobao/item/detail) for more on it.
- The `httpData` blocks other than `itemListModuleResponse` and `shopListModuleResponse` hold page metadata, such as breadcrumbs, banners and A/B test flags.

### Pricing

$0.028571 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/taobao/shop-item-list.json`](../../../catalog/models/taobao/shop-item-list.json) · Store page: https://www.sandbase.ai/model/taobao/shop-item-list
