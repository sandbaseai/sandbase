# Xianyu Item Search API: pricing, parameters and code examples

`xianyu/search/items` · data API · Xianyu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.028571 per call · **Modes:** sync

Search Xianyu (Goofish) second-hand listings by keyword, sorted by activity, recency, seller credit or price.

## Pricing

- **$0.028571 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xianyu/search/items", "keyword": "iphone 15"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xianyu/search/items', {'keyword': 'iphone 15'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xianyu/search/items", {
  "keyword": "iphone 15"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xianyu/search/items", sandbase.Params{
	"keyword": "iphone 15",
})
```

Same call via the path form: `POST /v1/api/xianyu/search/items` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | string |  | Page number for pagination. The first page is 1.  |
| `sort` | string |  | Sort order for Xianyu search results. one of: `active`, `recent`, `credit`, `price_asc`, `price_desc`, `price_drop`, `newest`; default `"active"` |
| `keyword` | string | yes | Search keyword.  |

## Details

Returns Xianyu (Goofish) second-hand search results for a keyword. The response also carries filter options and paging info. It needs a `keyword`, and you can add `page` and `sort`.

### Use cases

- Track asking prices for a model such as iPhone 15 by sorting with `price_asc` or `price_desc`.
- Find newly listed or newly price-cut items for a keyword by using the `newest` or `price_drop` sort.
- Read the total match count and price range for a keyword to size a resale market.
- Build a search page that reuses the storage, price and publish-time filter options.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xianyu/search/items" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "iphone 15"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword. |
| `page` | string | No | Page number for pagination. The first page is 1. |
| `sort` | string | No | Sort order for Xianyu search results. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "appBar": {},
  "division": {},
  "extraFilterValue": {
    "divisionList": [],
    "hideExcludeMultiPlacesSellers": "true"
  },
  "filterPanelDO": [
    {
      "cardData": {
        "propId": "quickFilter",
        "propName": "快捷筛选",
        "req": "true",
        "value": [
          {
            "selected": "false",
            "trackParams": {
              "id": "personal",
              "index": "0-0",
              "name": "个人闲置",
              "trackCtrlName": "FilterQik",
              "type": "5"
            },
            "valueId": "filterPersonal",
            "valueName": "个人闲置"
          }
        ]
      },
      "cardType": "3081"
    }
  ],
  "filterSheetDO": {
    "useFilterSheet": "true"
  },
  "flexFilter": {
    "data": [
      {
        "element": [
          {
            "data": {
              "initIndex": "0",
              "trackDO": {
                "arg1": "Button-SortChose",
                "args": {
                  "name": "排序",
                  "spm": "a2170.8011571.sortchose.1"
                },
                "page": "Page_xySearchResult"
              },
              "valueList": [
                {
                  "trackDO": {
                    "arg1": "Button-SortTogether",
                    "args": {
                      "name": "综合",
                      "spm": "a2170.8011571.sorttogether.1"
                    },
                    "page": "Page_xySearchResult"
                  },
                  "valueName": "综合"
                }
              ]
            },
            "filterType": "SortSingleChoiceList"
          }
        ],
        "name": "sorter",
        "property": {
          "style": "flex_1"
        }
      }
    ],
    "property": {},
    "protocol": "MultiLevelFilterBar"
  },
  "needDecryptKeys": [
    "resultList.data.item.main.exContent.jump2XianYuHao.clickParam.args.user_id"
  ],
  "relateResultPrefixBar": [],
  "resultInfo": {
    "enableGraphSearchResPageStyleUpdated": "true",
    "forceUseTppRepair": "false",
    "hasNextPage": "true",
    "hidePriceFilter": "false",
    "loadingTextList": [
      "宝贝正在来..."
    ],
    "maxPrice": "",
    "minPrice": "",
    "screenAdapter": "false",
    "scrollParams": {
      "androidSpeed": "middle",
      "androidUseNew": "false",
      "iOSSpeed": "middle",
      "iOSSpeedCoeff": "1",
      "iOSUseNew": "false"
    },
    "searchResControlFields": {
      "backupType": "",
      "channelCateLevel1Id": "126866987",
      "hasItems": "true",
      "maxPrice": "1150000",
      "minPrice": "100",
      "nextPage": "true",
      "numFound": "800000",
      "rn": "73476ae22a674fb518ddf0f2fcf35e43",
      "searchId": "b28b319b0be2f7928182b80634234c3e",
      "sellingOrder": "800000+",
      "similar": "false",
      "srpFeedsItemsDataEmpty": "false"
    },
    "showLoginGuideBar": "true",
    "singleControl": "false"
  },
  "resultList": [
    {
      "data": {
        "item": {
          "main": {
            "clickParam": {
              "arg1": "Item",
              "args": {
                "CoinPay_Morediscount": "false",
                "HideUserInfo": "false",
                "abid": "290827",
                "biz_type": "item",
                "bucketid": "26",
                "cCatId": "126862528",
                "card_type": "idlefish_search_item_fy26",
                "catId": "50025386"
              },
              "page": "Page_xySearchResult"
            },
            "exContent": {
              "area": "河南",
              "detailPageType": "detailCommonBuy",
              "detailParams": {
                "imageInfos": "[{\"extraInfo\":{\"raw\":\"true\",\"isT\":\"false\",\"lFileId\":\"1555008861091202001\",\"isH\":…",
                "isVideo": "false",
                "itemId": "1091554621744",
                "itemType": "detailCommonBuy",
                "picHeight": "1920",
                "picWidth": "1440",
                "postInfo": "包邮",
                "soldPrice": "3100"
              },
              "dislikeFeedback": {
                "clickParam": {
                  "arg1": "DisLikePanel",
                  "args": {
                    "bizType": "item",
                    "itemId": "1091554621744",
                    "itemPosition": "1",
                    "keyword": "iphone 15",
                    "picHeight": "218.0",
                    "picWicth": "164.0",
                    "referPage": "Page_xySearchResult_FindSimilar"
                  },
                  "page": "Page_xySearchResult"
                },
                "dislikeStyle": "dislikeStyle202304",
                "itemPicUrl": "http://img.alicdn.com/bao/uploaded/i3/O1CN01EB7LXMgUG3C2vHAO~livephoto~_!!461168…",
                "moreList": [
                  {
                    "apiParams": {
                      "actType": "fakePrice",
                      "extra": "UUIk4pShX1p+W//LBB5LpQ==",
                      "queryWord": "iphone 15",
                      "scene": "Page_xySearchResult",
                      "targetId": "1091554621744",
                      "targetIndex": "1",
                      "targetType": "item"
                    },
                    "clickParam": {
                      "arg1": "DisLikeItemMore",
                      "args": {
                        "actType": "fakePrice",
                        "bizType": "item",
                        "index": "1",
                        "itemId": "1091554621744",
                        "itemPosition": "1",
                        "keyword": "iphone 15",
                        "name": "虚假价格",
                        "picHeight": "218.0"
                      },
                      "page": "Page_xySearchResult"
                    },
                    "icon": "https://img.alicdn.com/imgextra/i4/O1CN01AeEtqS1cxXCmlX2IC_!!6000000003667-2-tps…",
                    "index": "1",
                    "text": "虚假价格"
                  }
                ],
                "showList": [
                  {
                    "apiParams": {
                      "actType": "dislikeGoods",
                      "extra": "UUIk4pShX1p+W//LBB5LpQ==",
                      "queryWord": "iphone 15",
                      "scene": "Page_xySearchResult",
                      "targetId": "1091554621744",
                      "targetIndex": "1",
                      "targetType": "item"
                    },
                    "clickParam": {
                      "arg1": "DisLikeItemFirst",
                      "args": {
                        "actType": "dislikeGoods",
                        "bizType": "item",
                        "index": "1",
                        "itemId": "1091554621744",
                        "itemPosition": "1",
                        "keyword": "iphone 15",
                        "name": "不喜欢该商品",
                        "picHeight": "218.0"
                      },
                      "page": "Page_xySearchResult"
                    },
                    "icon": "https://gw.alicdn.com/imgextra/i2/O1CN01nEHAUr1bTw528ELSv_!!6000000003467-2-tps-…",
                    "index": "1",
                    "text": "不喜欢该商品"
                  }
                ],
                "similarTargetUrl": "https://h5.m.goofish.com/wow/moyu/moyu-project/idle-photo-search/pages/home?kun=…",
                "targetUrl": "https://h5.m.goofish.com/wow/moyu/moyu-project/idle-negative-feedback-layer/page…"
              },
              "fishTagCustomParam": {
                "feedStyle202208": "1",
                "feedStyle202304": "1"
              },
              "fishTags": {
                "r2": {
                  "config": {
                    "delimiterColor": "#D6D6D6",
                    "delimiterHeight": "10",
                    "delimiterMarginBottom": "3",
                    "delimiterMarginLeft": "4.5",
                    "delimiterMarginRight": "4.5",
                    "delimiterMarginTop": "3",
                    "delimiterPosition": "between",
                    "delimiterWidth": "0.5"
                  },
                  "tagList": [
                    {
                      "data": {
                        "color": "#868999",
                        "content": "Apple/苹果",
                        "labelId": "38",
                        "lineHeight": "1.5",
                        "marginLeft": "0",
                        "marginRight": "0",
                        "size": "12",
                        "type": "text"
                      },
                      "utParams": {
                        "arg1": "4_tag_r2_38",
                        "args": {
                          "LabelSystem2.0": "1",
                          "content": "Apple/苹果"
                        }
                      }
                    }
                  ]
                },
                "r3": {
                  "config": {
                    "mutualLabelBizGroup": "false"
                  },
                  "tagList": [
                    {
                      "data": {
                        "color": "#FF4444",
                        "content": "已降50元",
                        "labelId": "1181",
                        "lineHeight": "1.3",
                        "marginLeft": "4",
                        "size": "12",
                        "type": "text"
                      },
                      "utParams": {
                        "arg1": "4_tag_r3_1181",
                        "args": {
                          "LabelSystem2.0": "1",
                          "content": "已降50元"
                        }
                      }
                    }
                  ]
                },
                "r5": {
                  "config": {
                    "mutualLabelBizGroup": "false"
                  },
                  "tagList": [
                    {
                      "data": {
                        "bold": "true",
                        "color": "#0DAEFF",
                        "content": "包邮",
                        "labelId": "2061",
                        "lineHeight": "1.33",
                        "marginRight": "6",
                        "size": "12",
                        "type": "text"
                      },
                      "utParams": {
                        "arg1": "4_tag_r5_2061",
                        "args": {
                          "LabelSystem2.0": "1",
                          "content": "包邮"
                        }
                      }
                    }
                  ]
                }
              },
              "hideUserInfo": "false",
              "isAliMaMaAD": "false"
            },
            "targetUrl": "fleamarket://awesome_detail?itemId=1091554621744&hitNativeDetail=true&flutter=tr…"
          }
        },
        "template": {
          "name": "idlefish_search_item_fy26",
          "url": "https://dinamicx.alibabausercontent.com/pub/idlefish_search_item_fy26/1787565234…",
          "version": "1787565234836"
        },
        "templateSingle": {
          "name": "idlefish_search_item_single_column_fy26",
          "url": "https://dinamicx.alibabausercontent.com/pub/idlefish_search_item_single_column_f…",
          "version": "1782441925368"
        }
      },
      "style": "flow",
      "type": "DX"
    }
  ],
  "resultPrefixBar": [
    {
      "data": {
        "item": {
          "main": {
            "clickParam": {
              "arg1": "ZXFestCoupon",
              "args": {
                "amount": "1820000",
                "claimMode": "SYNC",
                "displayMode": "MULTI_COUPON",
                "fuxi_task_id": "71786",
                "isFilterChecked": "false",
                "phrase": "Apply",
                "showToast": "false",
                "templateId": "882"
              },
              "page": "Page_xySearchResult"
            },
            "exContent": {
              "amount": "1820000",
              "claimMode": "SYNC",
              "displayCopyWriting": "多张限时优惠券待领取",
              "displayMode": "MULTI_COUPON",
              "displayVoucherTagText": "多张限时优惠券待领取",
              "displayVoucherValueText": "",
              "extraParam": {
                "activityId": "104859",
                "asac": "3A25C016K6IB5AKX6CQJFP",
                "benefitsParams": [
                  {
                    "idleOliverBenefitCode": "1048599357"
                  }
                ]
              },
              "filterChecked": "false"
            }
          }
        },
        "template": {
          "name": "idlefish_search_filter_redpacket_v2",
          "url": "https://dinamicx.alibabausercontent.com/pub/idlefish_search_filter_redpacket_v2/…",
          "version": "1788748802115"
        }
      },
      "style": "list",
      "type": "DX"
    }
  ],
  "tabList": [
    {
      "apiName": "mtop.taobao.idlemtopsearch.search",
      "apiVersion": "1.0",
      "searchTabType": "SEARCH_TAB_MAIN",
      "showName": "全部"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `resultInfo.hasNextPage` | Shows whether more result pages exist for this search. The value is the string `true` or `false`. |
| `resultInfo.searchResControlFields.numFound` | Number of matching listings found for the keyword. The value `800000` appears alongside `sellingOrder` of `800000+`, so treat large counts as approximate. |
| `resultInfo.searchResControlFields.minPrice / maxPrice` | Lowest and highest price among the matching listings, as strings. Units are not stated in the response. |
| `resultInfo.searchResControlFields.searchId` | Identifier for this search request. |
| `resultInfo.searchResControlFields.channelCateLevel1Id` | ID of the top-level category that the search matched. |
| `filterPanelDO[].cardData.propName` | Display name of a filter group, such as quick filters, price or publish time. Names are in Chinese. |
| `filterPanelDO[].cardData.value[].valueId / valueName` | ID and label of each option inside a filter group, such as `1` for items published within 1 day. |
| `flexFilter.data[].element[].data.valueList[].valueName` | Label of each sort or filter button, such as most recently active or newly reduced price. |
| `flexFilter.data[].element[].data.pvTermList[].vname` | Value of a product attribute filter, such as the storage sizes `256GB`, `128GB` and `64GB`. |

### Notes

- Pass `page` as a string. The first page is `1`. Check `resultInfo.hasNextPage` before you request the next page.
- `sort` accepts `active` (default), `recent`, `credit`, `price_asc`, `price_desc`, `price_drop` and `newest`.
- The response keeps the platform's original structure and Chinese labels. The trimmed sample shows filter and paging data, so look for the listing entries under `resultList`.
- To read one listing in full, call [Xianyu Item Details](/apis/xianyu/item/detail).

### Pricing

$0.028571 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/xianyu/search/items.json`](../../../../catalog/models/xianyu/search/items.json) · Store page: https://www.sandbase.ai/model/xianyu/search/items
