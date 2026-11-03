# JD.com Product Details API: pricing, parameters and code examples

`jd/item/detail` · data API · JD.com · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.028571 per call · **Modes:** sync

Get a JD.com product by item ID: title, price, promotion price, brand, shop and images.

## Pricing

- **$0.028571 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "jd/item/detail", "itemId": "100207440191"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('jd/item/detail', {'itemId': '100207440191'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("jd/item/detail", {
  "itemId": "100207440191"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "jd/item/detail", sandbase.Params{
	"itemId": "100207440191",
})
```

Same call via the path form: `POST /v1/api/jd/item/detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `itemId` | string | yes | A unique product identifier on JD.com (item ID).  |

## Details

Returns the JD.com product page data for one item. You send the item ID as `itemId`. The response keeps the platform's original structure, including promotions, purchase buttons and page settings.

### Use cases

- Check whether the buy and add-to-cart buttons are enabled for an item.
- Collect bank and coupon promotion titles, links and end times for an item.
- Find the brand page link and customer service link for a product.
- Record the start and end times of a promotion banner with a countdown.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/jd/item/detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"itemId": "100207440191"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `itemId` | string | Yes | A unique product identifier on JD.com (item ID). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "allOverImg": "",
  "apiForbid": [
    "/urlM"
  ],
  "areaId": "1_72_55674_0",
  "bankpromo": {
    "actUrl": "https://pro.m.jd.com/mall/active/2bFsGK6W9vEd4GftT5Pow5ZtT42r/index.html?babelCh…",
    "activityId": 123125,
    "expire": 1798732799000,
    "title": "实付满1元，收货后返满1打9折券，先到先得，点击跳转活动落地页（仅app可跳转）"
  },
  "bigouinfo": "",
  "bizMsg": "",
  "bizRetCode": "",
  "bottomBar": {
    "buttonMap": {
      "addCart": {
        "enable": true,
        "link": "",
        "name": "加入购物车",
        "type": "addCart"
      },
      "buy": {
        "enable": true,
        "link": "111",
        "name": "立即购买",
        "type": "buy"
      },
      "cart": {
        "enable": true,
        "link": "",
        "name": "购物车",
        "type": "cart"
      },
      "customerService": {
        "enable": true,
        "link": "",
        "name": "客服",
        "type": "customerService"
      },
      "shop": {
        "enable": true,
        "link": "",
        "name": "店铺",
        "type": "shop"
      }
    },
    "sceneName": "正常购买",
    "sceneType": "normalPurchase"
  },
  "bottomLoginTips": {
    "bgColor": "rgba(0, 0, 0, 0.7);",
    "bgImg": "https://storage.360buyimg.com/jxfe/ppms/c/202312/08/9234b13a-021e-4b37-bc2f-6870…",
    "icon": "https://storage.360buyimg.com/jxfe/ppms/c/202312/01/f4c32592-3dc3-4326-9b65-dfd7…",
    "rightBgColor": "linear-gradient(90deg, #FF404F 0%, #FA2C19 100%);",
    "rightText": "立即登录",
    "rightTextColor": "#ffffff",
    "texts": [
      {
        "color": "#ffffff",
        "text": "登录后可查看"
      }
    ]
  },
  "bottomNav": {
    "customerServiceLink": "https://jdcs.m.jd.com/?sku=100207440191&entry=m_item",
    "enable": true,
    "executorCode": "normalBuy",
    "left": {
      "backgroundColor": "linear-gradient(135deg,#f2140c,#f2270c 70%,#f24d0c);",
      "enable": true,
      "eventId": 2,
      "eventUrl": "",
      "subText": "",
      "text": "加入购物车",
      "textColor": "",
      "type": "left"
    },
    "popup": {
      "content": "",
      "leftButton": "",
      "rightButton": "",
      "title": ""
    },
    "right": {
      "backgroundColor": "linear-gradient(135deg,#ffba0d,#ffc30d 69%,#ffcf0d);",
      "enable": true,
      "eventId": 3,
      "eventUrl": "//trade.m.jd.com/pay?sceneval=2&scene=jd&isCanEdit=1&EncryptInfo=&from=m_inter_d…",
      "subText": "",
      "text": "立即购买",
      "textColor": "",
      "type": "right"
    },
    "tips": {
      "amsg": "",
      "amsgUrl": "",
      "backgroupColor": "",
      "text": "",
      "textColor": ""
    },
    "viewId": "normalBuy",
    "viewName": "正常购买"
  },
  "channelInfo": {
    "address": false,
    "bottomButtonTip": "",
    "descDetailNotLinkTip": "",
    "forbidConfig": {
      "adKey": false,
      "addressFloor": false,
      "askFloor": false,
      "bloodSugar": false,
      "bookIntroduction": false,
      "bottomButton": false,
      "bottomButtonTip": "",
      "businessEntry": false,
      "bybtBannerLink": false,
      "carSubscript": false,
      "colorSwitchFloor": false,
      "commentFloor": false
    },
    "isShortItem": false,
    "shortItemType": "",
    "sourceType": "m-item"
  },
  "channelManage": {
    "enable": false
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `errCode / msg / bizMsg` | Status of the lookup. `errCode` is `"0"` in this response, and the message fields are empty. |
| `bankpromo.title` | Text of the bank promotion shown on the item. In this response it describes a coupon returned after the order is received. |
| `bankpromo.actUrl / bankpromo.activityId` | Link to the promotion page and the numeric ID of the promotion. |
| `bankpromo.expire` | End time of the bank promotion, as a 13-digit millisecond timestamp. |
| `bottomBar.buttonMap.addCart.enable / bottomBar.buttonMap.buy.enable` | Whether the add-to-cart and buy buttons are enabled for this item. |
| `bottomBar.sceneType` | Purchase scene of the item. The value `normalPurchase` means a normal purchase, and `sceneName` gives the display name. |
| `commonInfo.brandUrl` | Link to the brand page for this item. |
| `commonInfo.wqAddrDefault` | Default delivery address used for the lookup. It is a pipe-separated string with the area ID, region names, street address and coordinates. |
| `bottomNav.customerServiceLink` | Customer service link for the item. The `sku` query value is the item ID. |
| `newBanner.fData.bannerName / newBanner.fData.countDown.startTime / newBanner.fData.countDown.endTime` | Name of the promotion banner and the start and end times of its countdown, as millisecond timestamps. |

### Notes

- Get `itemId` from [JD.com Product Search](/apis/jd/search/items) or [JD.com Shop Products](/apis/jd/shop/items). The example ID is `100207440191`.
- Many fields describe page layout and feature switches, such as `floorForbids`, `floorSwitch` and `channelInfo`. Skip them if you only need product and promotion data.
- Text values such as promotion titles and button names are in Chinese.
- For reviews call [JD.com Product Comments](/apis/jd/item/comments). For detail images call [JD.com Product Description Images](/apis/jd/item/description-images).

### Pricing

$0.028571 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/jd/item/detail.json`](../../../../catalog/models/jd/item/detail.json) · Store page: https://www.sandbase.ai/model/jd/item/detail
