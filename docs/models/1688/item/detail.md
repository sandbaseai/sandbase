# 1688 Product Details API: pricing, parameters and code examples

`1688/item/detail` · data API · 1688 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get a 1688 wholesale product by item ID: images, video, SKU options and prices, tiered pricing, minimum order, seller and shop details.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "1688/item/detail", "itemId": "1046925823679"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('1688/item/detail', {'itemId': '1046925823679'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("1688/item/detail", {
  "itemId": "1046925823679"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "1688/item/detail", sandbase.Params{
	"itemId": "1046925823679",
})
```

Same call via the path form: `POST /v1/api/1688/item/detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `itemId` | string | yes | A unique product identifier on 1688.  |

## Details

This API returns the full detail record for one 1688 wholesale product. It needs the 1688 item ID in the `itemId` parameter. The response includes attributes, coupons, delivery and buyer protection, and images.

### Use cases

- Pull the product images and `attribute.propsList` specs to build a listing in your own catalog.
- Check the delivery location, shipping fee and promised dispatch time before you source a product.
- Read the buyer protection services on a product to compare suppliers.
- Collect the SKU weights to estimate shipping weight per variant.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/1688/item/detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"itemId": "1046925823679"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `itemId` | string | Yes | A unique product identifier on 1688. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "attribute": {
    "offerId": 1046925823679,
    "propUrl": "https://air.1688.com/pages/od/1688-drawer-layout/dx4c1wsd4/index.html?spm=a26g8.…",
    "propsList": [
      {
        "name": "芯片类型",
        "show": false,
        "value": "杰理"
      }
    ],
    "title": "属性"
  },
  "coupon": {
    "bgColor": "#ff0e31",
    "buttonName": "",
    "couponInfoList": [
      {
        "buttonName": "领券",
        "displayType": "text",
        "extraInfo": {
          "uiType": "COIN_POINT_ACTIVITY"
        },
        "name": "元宝抵扣",
        "promotionItems": [
          {
            "actionName": "立即领取",
            "applied": false,
            "canApply": true,
            "creatorId": 2216226597326,
            "detail": "元宝可抵1%（100元宝等于1元）",
            "discountFee": "0.27",
            "extendDetail": "",
            "label": "元宝可抵1%"
          }
        ],
        "rankValue": 100,
        "summary": "null",
        "type": "COIN_POINT_ACTIVITY",
        "uiType": "COIN_POINT_ACTIVITY"
      }
    ],
    "couponList": [
      {
        "couponContent": "元宝可抵1%",
        "couponType": "COIN_POINT_ACTIVITY"
      }
    ],
    "couponRuleLink": "https://rulechannel.1688.com/1688?type=detail&ruleId=20002183&cId=31#/rule/detai…",
    "couponRuleLinkText": "新人专享玩法说明 >",
    "linkUrl": "https://cybert.m.1688.com/43ohz283.html?sceneName=chimera_16527",
    "offerId": 1046925823679,
    "onHandPrice": {
      "ext": "起",
      "unit": "￥"
    },
    "pageName": "Page_GetCoupon",
    "style": {
      "arrowsImg": "https://img.alicdn.com/tfs/TB19FQtP4D1gK0jSZFsXXbldVXa-26-44.png",
      "textColor": "#FF4000"
    },
    "tagShareModel": {
      "bizType": "offer",
      "originalUrl": "http://m.1688.com/offer/1046925823679.html?rpg-cnt=share.offerDetail&offerId=104…",
      "pageContent": {
        "businessId": 1046925823679
      },
      "sceneType": "od_promotion_tag",
      "shareContent": "我在1688发现了一个很赞的商品，快来看看吧！",
      "sharePicUrl": "https://cbu01.alicdn.com/img/ibank/O1CN0181MUa31mQErz5zMgR_!!2206588314948-0-C2M…",
      "shareTitle": "德国柏林之音2026新款夹耳式不入耳骨传导运动长续航无线蓝牙耳机"
    }
  },
  "delivery": {
    "amount": 1,
    "buyerProtectionModel": [
      {
        "bigLogo": "https://img.alicdn.com/imgextra/i2/O1CN01ZvNktK1ywYCPcwtcR_!!6000000006643-2-tps…",
        "enabled": true,
        "extendInfo": {
          "odSpecialStyle": "{\"priority\":1001,\"type\":\"base\"}"
        },
        "hugeLogo": "https://img.alicdn.com/imgextra/i1/O1CN0138HBhh1XF2x7LMeaO_!!6000000002893-2-tps…",
        "largeLogo": "https://img.alicdn.com/imgextra/i3/O1CN01pBIjwH238Eli04JFY_!!6000000007210-2-tps…",
        "littleLogo": "https://img.alicdn.com/imgextra/i1/O1CN01lJPwkj1fLTR8Rgu7r_!!6000000003990-2-tps…",
        "logicGroupId": "yxpzbf",
        "logo": "https://img.alicdn.com/imgextra/i4/O1CN015dO1Li1KiHE0brm3j_!!6000000001197-2-tps…",
        "middleLogo": "https://img.alicdn.com/imgextra/i3/O1CN01pbZ3Ke1FsHnlmAwRl_!!6000000000542-2-tps…",
        "moreHugeLogo": "https://img.alicdn.com/imgextra/i4/O1CN015dO1Li1KiHE0brm3j_!!6000000001197-2-tps…",
        "productPage": "https://pages-fast.1688.com/wow/cbu/default/defaultv1/TQCfKypffJ/index.html?wh_p…",
        "serviceCode": "yxpzbf"
      }
    ],
    "buyerProtectionScene": "dsc",
    "deliveryLimit": 1,
    "deliveryLimitTimeModel": {
      "attrs": {
        "logisticsTimeServiceType": "yjf",
        "offerUnit": "条",
        "ptsOfferStepModels": [
          {
            "selected": false,
            "selectedEndQuantity": 5,
            "selectedPtsOfferTagModel": {
              "agreeDeliveryHours": 24,
              "disabled": false,
              "required": false,
              "selected": false,
              "serviceCode": "essxsfh",
              "serviceName": "24小时发货"
            },
            "selectedStartQuantity": 1
          }
        ]
      },
      "expectSendHour": 3,
      "expectTimeDesc": "预计3小时发货，承诺24小时发货",
      "limitTimeDay": 1,
      "limitTimeDesc": "常发圆通快递",
      "offerId": 1046925823679,
      "orderCntLevelText": "5条以内",
      "textColor": "#22AC60",
      "trimTextPrefix": true
    },
    "deliveryLimitTxt": "常发圆通快递",
    "freeEndAmount": -1,
    "hideDeliveryTime": false,
    "hideLogisticsClick": false,
    "isNew": true,
    "isOptimalLogisticsOffer": true,
    "jicai": ""
  },
  "description": {
    "detailUrl": "https://itemcdn.tmall.com/1688offer/icoss1922697650890e6fcacb2a9101",
    "isUseNewDetail": true
  },
  "images": [
    {
      "fullPathImageURI": "https://cbu01.alicdn.com/img/ibank/O1CN0181MUa31mQErz5zMgR_!!2206588314948-0-C2M…",
      "imageURI": "img/ibank/O1CN0181MUa31mQErz5zMgR_!!2206588314948-0-C2M.jpg",
      "searchImageURI": "https://cbu01.alicdn.com/img/ibank/O1CN0181MUa31mQErz5zMgR_!!2206588314948-0-C2M…",
      "size220x220ImageURI": "https://cbu01.alicdn.com/img/ibank/O1CN0181MUa31mQErz5zMgR_!!2206588314948-0-C2M…",
      "size310x310ImageURI": "https://cbu01.alicdn.com/img/ibank/O1CN0181MUa31mQErz5zMgR_!!2206588314948-0-C2M…",
      "summImageURI": "https://cbu01.alicdn.com/img/ibank/O1CN0181MUa31mQErz5zMgR_!!2206588314948-0-C2M…"
    }
  ],
  "item": {
    "addCartUrl": "",
    "aggregatePromotionInfo": [],
    "applyCouponUrl": "https://h5.m.taobao.com/app/1688activity/pages/odlottery/index.html?sceneType=co…",
    "businessType": "default",
    "canApplyChtCoupon": true,
    "companyName": "深圳市聚声源电子商务有限公司",
    "consignOffer": false,
    "defaultOfferImg": "https://cbu01.alicdn.com/img/ibank/O1CN0181MUa31mQErz5zMgR_!!2206588314948-0-C2M…",
    "isChtOffer": false,
    "isFavoriteOffer": false,
    "offerId": "1046925823679",
    "offerTitle": "德国柏林之音2026新款夹耳式不入耳骨传导运动长续航无线蓝牙耳机"
  },
  "mainPic": {
    "dpzh_Type": "dpzh",
    "hasAdditionComponent": false,
    "isPrivacy": false,
    "liveInfoModel": {},
    "offerId": "1046925823679",
    "offerImages": [
      {
        "imgUrl": "https://cbu01.alicdn.com/img/ibank/O1CN0181MUa31mQErz5zMgR_!!2206588314948-0-C2M…",
        "type": "normal",
        "typeDes": "主图"
      }
    ],
    "offerImgList": [
      "https://cbu01.alicdn.com/img/ibank/O1CN0181MUa31mQErz5zMgR_!!2206588314948-0-C2M…"
    ],
    "offerInfoModel": {
      "isFav": false,
      "offerId": 1046925823679,
      "price": "26.80-22.10",
      "title": "德国柏林之音2026新款夹耳式不入耳骨传导运动长续航无线蓝牙耳机"
    },
    "processingActivityImg": "",
    "sellerUserId": 2216226597326,
    "skuImages": [
      {
        "imgUrl": "https://cbu01.alicdn.com/img/ibank/O1CN01FP9Hu623zMS62CnLg_!!2216226597326-0-cib…",
        "name": "【升级版丨空洞黑】环绕9D音效★物理降噪★双核双芯片低延迟",
        "type": "sku"
      }
    ],
    "trackInfo": {
      "expoData": "object_type@video^bizScene@offerDetail^object_id@426470435520^offerId@1046925823…",
      "uiTrackInfo": {
        "od_live_click": {
          "args": {
            "offerId": "1046925823679"
          }
        },
        "videoPlay": {
          "args": {
            "bizScene": "offerDetail",
            "expoData": "object_type@video^bizScene@offerDetail^object_id@426470435520^offerId@1046925823…",
            "fromSource": "offerDetail",
            "offerId": "1046925823679",
            "videoId": "426470435520"
          }
        }
      }
    }
  },
  "order": {
    "coord": {
      "atmosphere": "normal",
      "business": "default",
      "channel": "dsc",
      "role": "defaultBuyer",
      "scene": "default",
      "useCase": "1688wap"
    },
    "sceneList": [
      {
        "sceneKey": "order",
        "sceneName": "批发",
        "sceneTextColor": "#888888",
        "sceneTextSize": 15,
        "wapUrl": "https://m.1688.com/offer/1046925823679.html?urlParam=sk%3dorder&sk=order"
      }
    ],
    "selectedScene": {
      "sceneKey": "order",
      "sceneName": "批发",
      "sceneTextColor": "#222222",
      "sceneTextSize": 16
    }
  },
  "price": {
    "activityModel": {
      "activityId": "null",
      "beforePro": false,
      "countdown": "null"
    },
    "alipayIntegralInfo": {
      "originalOrderPrice": {
        "addCartParam": {
          "cartType": ""
        },
        "beginNum": 1,
        "canBookedAmount": 29204,
        "flow": "general",
        "mixParam": {
          "mixAmount": 200,
          "mixBegin": 0,
          "mixNum": 6,
          "shopMixNum": 2147483647,
          "supportMix": true
        },
        "saledCount": 749,
        "skuParam": {
          "skuPriceType": "rangePrice",
          "skuRangePrices": [
            {
              "beginAmount": "1",
              "price": "26.80"
            }
          ]
        }
      }
    },
    "bigPromotion": false,
    "bigPromotionInfo": {
      "bigPromotionCountdown": -1,
      "bigPromotionStatus": "NONE",
      "burstBeginTime": -1,
      "burstEndTime": -1,
      "preheatTime": -1,
      "promotionResources": {}
    },
    "channel": "dsc",
    "displayType": "normal-range",
    "extraInfo": {
      "isPlusOffer": false
    },
    "isBmPrice": false,
    "isHpDz": false,
    "isPlusPrice": false,
    "isPrivatePrice": false,
    "isVipPrice": false
  },
  "service": {
    "newOdFlag": true,
    "offerId": 1046925823679,
    "service1": "品质不符包赔",
    "service2": "7天无理由退货",
    "service3": "严选晚发必赔",
    "serviceDesc": [
      {
        "priority": 1001,
        "serviceCode": "yxpzbf",
        "serviceName": "品质不符包赔",
        "styleType": "base",
        "textColor": "#222222",
        "type": "protect"
      }
    ],
    "serviceDetail": [
      {
        "description": "“品质不符包赔”服务是指当买家在1688x严选购买带有<span style=\"color:#BC8136;\">“品质不符包赔”</span>标识的商品后，依照…",
        "priority": 1001,
        "serviceCode": "yxpzbf",
        "serviceLink": "https://pages-fast.1688.com/wow/cbu/default/defaultv1/TQCfKypffJ/index.html?wh_p…",
        "serviceName": "品质不符包赔",
        "styleType": "base"
      }
    ],
    "serviceUrl": "https://air.1688.com/app/ctf-m-page/address-manage/safe-buy-popup.html?spm=defwo…"
  },
  "skuCore": null,
  "specs": {
    "loginUserId": 0,
    "useCase": "1688wap"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `attribute.offerId` | The numeric 1688 item ID. It matches the `itemId` you sent. |
| `attribute.propsList[].name / attribute.propsList[].value` | One product attribute per row, such as chip type or battery life. `name` is the attribute label and `value` is its setting. Both are returned in Chinese. |
| `images[].fullPathImageURI` | Full URL of a product image. Other keys in the same row hold resized versions, such as `size220x220ImageURI` and `size310x310ImageURI`. |
| `description.detailUrl` | URL of the product's long description content. |
| `coupon.couponInfoList[].name` | Name of an available promotion or coupon. `promotionItems[].detail` explains the offer and `promotionItems[].discountFee` gives its discount value. |
| `coupon.tagShareModel.shareTitle` | The product title as shown when a user shares the product. `sharePicUrl` is the share image. |
| `delivery.location` | The place the goods ship from, given as province and city. |
| `delivery.postFeeValue / delivery.postFree` | `postFeeValue` is the shipping fee amount. `postFree` is a flag that says whether shipping is free. |
| `delivery.deliveryLimitTimeModel.expectTimeDesc` | Text that states the expected and promised dispatch time. `limitTimeDesc` names the usual courier. |
| `delivery.protectionInfos[].serviceName` | Name of a buyer protection service on this product. `description` explains its terms. |
| `delivery.skuWeight` | Map of SKU ID to weight. Each key is a SKU ID and each value is the weight for that SKU. |

### Notes

- Take the item ID from a 1688 product link. If you only have a URL, call [1688 Product Details by URL](/apis/1688/item/detail-by-url).
- Many text values are in Chinese. Some descriptions contain HTML tags such as `<span>`.
- For the long description images, call [1688 Product Description Images](/apis/1688/item/description-images). For shipping costs to an address, call [1688 Product Shipping Fee](/apis/1688/item/shipping).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/1688/item/detail.json`](../../../../catalog/models/1688/item/detail.json) · Store page: https://www.sandbase.ai/model/1688/item/detail
