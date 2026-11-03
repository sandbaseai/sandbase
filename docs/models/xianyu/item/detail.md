# Xianyu Item Details API: pricing, parameters and code examples

`xianyu/item/detail` · data API · Xianyu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.028571 per call · **Modes:** sync

Get a Xianyu (Goofish) second-hand listing by item ID: title, price, description, images, seller and location.

## Pricing

- **$0.028571 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xianyu/item/detail", "itemId": "1043659406022"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xianyu/item/detail', {'itemId': '1043659406022'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xianyu/item/detail", {
  "itemId": "1043659406022"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xianyu/item/detail", sandbase.Params{
	"itemId": "1043659406022",
})
```

Same call via the path form: `POST /v1/api/xianyu/item/detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `itemId` | string | yes | A unique product identifier on Xianyu.  |

## Details

Returns one Xianyu (Goofish) second-hand listing for a given `itemId`. The response includes the description, images, category, price and coupon data, shipping origin, and a list of similar listings. The response keeps the platform's original nested structure.

### Use cases

- Pull the description, images and attribute labels of a listing to build a product catalog entry.
- Track the coupon price and promotion end time of a listing over repeated calls.
- Compare condition grades and prices across the same phone model using the similar listings list.
- Read the shipping city and province of a listing to see where the item ships from.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xianyu/item/detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"itemId": "1043659406022"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `itemId` | string | Yes | A unique product identifier on Xianyu. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "b2cBuyerDO": {
    "buyQualificationActList": [],
    "favored": "false",
    "isCollected": "false",
    "isFirstOrderUser": "false",
    "isNewUserIn7Day": "false"
  },
  "b2cDetailImageInfos": [
    {
      "heightSize": "2600",
      "major": "false",
      "type": "0",
      "url": "https://img.alicdn.com/imgextra/i4/O1CN01Hx2nMTdxhZF5HIiO_!!4611686018427385316-…",
      "widthSize": "2600"
    }
  ],
  "b2cItemDO": {
    "activityInfo": {},
    "atXGlobalCode": "digital|selectedWarehousing|c2c",
    "atmosphereTag": {
      "additionMap": {},
      "appendText": "",
      "bgColor": "#FFEEE3",
      "borderColor": "#FFEEE3",
      "iconUrl": "",
      "link": "",
      "lottieUrl": "",
      "order": "99",
      "text": "活动价",
      "textColor": "#FF4444",
      "vibeBgImgUrl": "",
      "viceIcon": ""
    },
    "b2CLogisticsInfoDO": {
      "additionMap": {},
      "area": "",
      "city": "西安",
      "price": "包邮",
      "province": "陕西",
      "shipmentsTime": "24",
      "shipmentsTimeInfo": "24小时发货"
    },
    "b2cPromotionBizConfigMap": {
      "detailBizBrandBargain": {
        "new_outlets_jhjl": {
          "androidAppVersion": "7.21.85.5",
          "atmosphereBgPic": "https://gw.alicdn.com/imgextra/i1/O1CN01E11YnU1YyfvYcmLo8_!!6000000003128-2-tps-…",
          "atmosphereBgPicWarmUp": "https://gw.alicdn.com/imgextra/i3/O1CN01dHHhaz1gAlhCXRdQv_!!6000000004102-2-tps-…",
          "atmosphereJumpUrl": "",
          "atmosphereTextPic": "https://gw.alicdn.com/imgextra/i1/O1CN012hHqlD1K28hJjIgdX_!!6000000001105-2-tps-…",
          "atmosphereTextPicWarmUp": "https://gw.alicdn.com/imgextra/i3/O1CN01ONPwrf1FBgsX0kaRQ_!!6000000000449-2-tps-…",
          "buttonBottomText": "",
          "buttonTopText": ""
        }
      },
      "detailBizCouponFxc": {
        "hangye_first_promotion": {
          "androidAppVersion": "7.21.85.5",
          "atmosphereBgPic": "https://gw.alicdn.com/imgextra/i1/O1CN01dx6GPR1gKqQQrsib2_!!6000000004124-2-tps-…",
          "atmosphereJumpUrl": "",
          "atmosphereTextPic": "https://gw.alicdn.com/imgextra/i1/O1CN019YNO2O23Btquz0poW_!!6000000007218-2-tps-…",
          "buttonBottomText": "距新人补贴结束 %s",
          "buttonTopText": "立即购买",
          "iosAppVersion": "7.21.85.5",
          "newAtmosphereBgPic": "https://gw.alicdn.com/imgextra/i3/O1CN01XVdmNB227wqMRuNPz_!!6000000007074-2-tps-…"
        }
      },
      "detailBizStrictSelection": {
        "phone_yanxuan": {
          "androidAppVersion": "7.21.85.5",
          "atmosphereBgPic": "https://gw.alicdn.com/imgextra/i1/O1CN01WPOtIU1dRJAtkBM5K_!!6000000003732-2-tps-…",
          "atmosphereJumpUrl": "",
          "atmosphereTextPic": "https://gw.alicdn.com/imgextra/i4/O1CN01UXi8KF1D6zb8qJMxB_!!6000000000168-2-tps-…",
          "buttonBottomText": "",
          "buttonTopText": "",
          "iosAppVersion": "7.21.85.5",
          "newAtmosphereBgPic": "https://gw.alicdn.com/imgextra/i3/O1CN01JK8FIn1bKJutD1qDL_!!6000000003446-2-tps-…"
        },
        "yanxuan_student": {
          "androidAppVersion": "7.21.85.5",
          "atmosphereBgPic": "https://gw.alicdn.com/imgextra/i1/O1CN01WPOtIU1dRJAtkBM5K_!!6000000003732-2-tps-…",
          "atmosphereJumpUrl": "",
          "atmosphereTextPic": "https://gw.alicdn.com/imgextra/i4/O1CN01UXi8KF1D6zb8qJMxB_!!6000000000168-2-tps-…",
          "buttonBottomText": "",
          "buttonTopText": "",
          "iosAppVersion": "7.21.85.5",
          "newAtmosphereBgPic": "https://gw.alicdn.com/imgextra/i3/O1CN01JK8FIn1bKJutD1qDL_!!6000000003446-2-tps-…"
        }
      }
    },
    "b2cPromotionPriceData": {
      "couponList": [
        {
          "action": {
            "amount": "2000",
            "null": "true",
            "type": "4"
          },
          "applied": "false",
          "bizType": "49692",
          "condition": {
            "amount": "129900",
            "null": "true",
            "type": "1"
          },
          "null": "true",
          "templateCode": "15348834688"
        }
      ],
      "detailPriceTagDesc": "",
      "discountDetail": {
        "activityId": "131767470051",
        "b2cAtmosphereDesc": "",
        "b2cAtmosphereJumpUrl": "",
        "b2cAtmosphereNewShapePic": "",
        "b2cAtmosphereNewShapePic4SuperLink": "",
        "b2cAtmospherePic": "",
        "b2cAtmosphereShapePic": "",
        "b2cAtmosphereTitleBgPic": ""
      },
      "discountDetailList": [
        {
          "activityId": "152654067790",
          "b2cAtmosphereDesc": "",
          "b2cAtmosphereJumpUrl": "",
          "b2cAtmosphereNewShapePic": "",
          "b2cAtmosphereNewShapePic4SuperLink": "",
          "b2cAtmospherePic": "",
          "b2cAtmosphereShapePic": "",
          "b2cAtmosphereTitleBgPic": ""
        }
      ],
      "discountType": "market_single_promotion",
      "haveBuyQualification": "true",
      "idlePredictPriceData": {},
      "itemId": "1095774182867",
      "minDiscountFeeStr": "20.00",
      "promotionActivityName": "活动",
      "promotionActivityType": "idle_market",
      "promotionEndTime": "1794870093000"
    },
    "benefitLabels": [
      {
        "additionMap": {},
        "bgColor": "#FFEEE3",
        "borderColor": "#F58300",
        "order": "99",
        "text": "已售33",
        "textColor": "#F58300"
      }
    ],
    "benefitTags": [],
    "browseCnt": "0",
    "categoryId": "50025386",
    "collectCnt": "0",
    "commonTags": [
      {
        "additionMap": {},
        "bgColor": "#FFEEE3",
        "borderColor": "#FFEEE3",
        "order": "2",
        "text": "券已抵20元",
        "textColor": "#FF4444",
        "trackParams": {
          "tagType": "idle_cross_shop_coupons"
        }
      }
    ]
  },
  "b2cSellerDO": {
    "aoiType": "0",
    "avgReply30dLong": "25",
    "city": "西安",
    "hasSoldNumInteger": "130927",
    "identityTags": [
      {
        "additionMap": {},
        "iconHeight": "32",
        "iconUrl": "https://gw.alicdn.com/bao/uploaded/TB1E3aKPFXXXXcKXpXXXXXXXXXX-32-32.png",
        "iconWidth": "32",
        "link": "https://h5.m.taobao.com/2shou/pd/realVerifyUrl.html?userId=2216359785956&isVerif…",
        "order": "99",
        "text": "实人认证已通过",
        "trackParams": {
          "appearTrackName": "",
          "trackCtrlName": "Button-Shiren"
        },
        "type": "1"
      }
    ],
    "idleFishCreditTag": {
      "additionMap": {},
      "iconHeight": "36",
      "iconUrl": "https://gw.alicdn.com/imgextra/i1/O1CN01YTUhW41aSHETi0kIJ_!!6000000003328-2-tps-…",
      "iconWidth": "171",
      "order": "99",
      "trackParams": {
        "pageUserId": "2216359785956",
        "sellerLevel": "5"
      }
    },
    "itemCount": "2707506",
    "lastVisitTime": "2小时前来过",
    "levelTags": [
      {
        "additionMap": {},
        "iconHeight": "36",
        "iconUrl": "https://gw.alicdn.com/imgextra/i1/O1CN01YTUhW41aSHETi0kIJ_!!6000000003328-2-tps-…",
        "iconWidth": "171",
        "order": "99",
        "trackParams": {
          "pageUserId": "2216359785956",
          "sellerLevel": "5"
        }
      }
    ],
    "nick": "天津雪球严选专营店",
    "portraitUrl": "http://img.alicdn.com/bao/uploaded/i4/O1CN01vz4x4a1trtxJ8y5X9_!!0-mtopupload.jpg",
    "publishCity": "西安"
  },
  "b2cUiIdleDetailConfigDO": {
    "enableJumpXyh": "true",
    "enableNfgcService": "true",
    "enableNfrService": "true",
    "enableSdrService": "true",
    "enableSellerVipLogo": "true",
    "enableShowBidInfo": "false",
    "enableShowOthersSellInfoGuide": "true",
    "enableShowQuickAskExp": "true",
    "enableShowSellSimple": "true",
    "extendDescItemType": "false",
    "extendPriceUnit": "false",
    "extendSellerCertificate": "false"
  },
  "bizFlagDO": {},
  "brokerDO": {},
  "buyerDO": {
    "buyQualificationActList": [],
    "favored": "false",
    "isFirstOrderUser": "false",
    "isNewUserIn7Day": "false"
  },
  "charityLuxuryDO": {},
  "commerceDO": {},
  "configInfo": {
    "hitIdleFishCreditAb": "true",
    "isFullScreen": "true",
    "isMultiPage": "true",
    "jumpXyh": "true",
    "paymentGuideMask": "false"
  },
  "dataType": "0"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `b2cItemDO.itemId` | ID of the listing returned in the item data. In the sample it differs from the requested `itemId`. |
| `b2cItemDO.desc` | Seller description text of the listing. Long text may be cut in some responses. |
| `b2cItemDO.imageInfos[].url` | Image URL of each listing photo. The entry with `major` set to `true` is the main image. `heightSize` and `widthSize` give the image size. |
| `b2cItemDO.cpvLabels[].propertyName / valueName` | Product attributes as name and value pairs, such as brand, model and storage capacity. |
| `b2cItemDO.itemCatDTO.catId` | Category ID of the listing. The same object holds the channel category IDs for each level. |
| `b2cItemDO.b2CLogisticsInfoDO.province / city / price` | Shipping origin and shipping cost label. In the sample the `price` value means free shipping. |
| `b2cItemDO.b2cPromotionPriceData.promotionPriceMin` | Lowest price after the active promotion or coupon. `promotionName` names the price type, and `promotionEndTime` is the end time in milliseconds. |
| `b2cItemDO.b2cPromotionPriceData.couponList[]` | Coupons that apply to the listing. `applied` shows whether the coupon is already applied. |
| `b2cItemDO.benefitLabels[].text` | Display labels shown on the listing, such as sold count and battery health. |
| `b2cItemDO.deepInventorySubItemList[]` | Similar listings of the same model. Each row has `subItemId`, `title`, `soldPrice`, `picUrl` and `matchedFilterOptions` for condition and storage. |

### Notes

- Get listing IDs from [Xianyu Item Search](/apis/xianyu/search/items), then pass one as `itemId`.
- `itemId` is a string of digits. Send it as a string.
- Most values in the response are strings, including numbers and booleans such as `"false"`.
- Use `subItemId` from the similar listings list as the `itemId` of a new call.

### Pricing

$0.028571 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/xianyu/item/detail.json`](../../../../catalog/models/xianyu/item/detail.json) · Store page: https://www.sandbase.ai/model/xianyu/item/detail
