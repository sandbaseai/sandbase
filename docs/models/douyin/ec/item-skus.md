# Douyin Shop Item SKUs API: pricing, parameters and code examples

`douyin/ec/item-skus` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.035714 per call · **Modes:** sync

Get the SKU list of a Douyin shop product by item ID: variant options with price and stock.

## Pricing

- **$0.035714 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/ec/item-skus", "itemId": "3734619545235751048"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/ec/item-skus', {'itemId': '3734619545235751048'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/ec/item-skus", {
  "itemId": "3734619545235751048"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/ec/item-skus", sandbase.Params{
	"itemId": "3734619545235751048",
})
```

Same call via the path form: `POST /v1/api/douyin/ec/item-skus` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `itemId` | string | yes | The unique ID of the item on Douyin E-commerce.  |

## Details

Returns SKU and product page data for one Douyin Shop item. You send the item ID as `itemId`. The response includes the title, category, price, images, product attributes and a sample of buyer comments.

### Use cases

- Check the current price of a Douyin Shop product from its item ID.
- Collect the category path and brand attributes of a product for catalog matching.
- Download the main image and detail images of a product for listing comparison.
- Read the top comment tags and sample reviews of a product to see what buyers say.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/ec/item-skus" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"itemId": "3734619545235751048"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `itemId` | string | Yes | The unique ID of the item on Douyin E-commerce. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "category": {
    "firstCName": "个人护理",
    "firstCid": 1000003462,
    "fourthCName": "",
    "fourthCid": 0,
    "secondCName": "面部洗护",
    "secondCid": 1000003463,
    "thirdCName": "防晒霜",
    "thirdCid": 1000003485
  },
  "description": "",
  "detail_info": {
    "ai_question": null,
    "detail_config": [
      {
        "main_content": [
          {
            "content": [
              "售卖价，由商家依照《价格法》规定的定价原则及定价依据通过商家后台页面自主填写（适用政府指导价或者政府定价除外），如商品未通过商家后台参加促销活动（如优惠券、满减…"
            ],
            "default_show": false,
            "links": [
              {
                "key": "抖音电商平台价格标签说明",
                "link": "https://school.jinritemai.com/doudian/web/article/aHzox7KpPT94"
              }
            ],
            "title": "价格说明",
            "type": 0
          }
        ],
        "main_title": "",
        "main_type": 0
      }
    ],
    "detail_imgs": [
      {
        "height": 1262,
        "uri": "ecom-shop-material/jpeg_m_7a451b88b93bf8db3dfc0ec3c89386aa_sx_420641_www790-1262",
        "url_list": [
          "https://p3-item.ecombdimg.com/img/ecom-shop-material/jpeg_m_7a451b88b93bf8db3dfc…"
        ],
        "width": 790
      }
    ],
    "detail_imgs_new": [
      {
        "image": {
          "height": 1262,
          "uri": "ecom-shop-material/jpeg_m_7a451b88b93bf8db3dfc0ec3c89386aa_sx_420641_www790-1262",
          "url_list": [
            "https://p3-item.ecombdimg.com/img/ecom-shop-material/jpeg_m_7a451b88b93bf8db3dfc…"
          ],
          "width": 790
        },
        "pic_type": "pic"
      }
    ],
    "jump_url": "sslocal://webcast_lynxview?type=popup&url=https%3A%2F%2Flf-webcast-sourcecdn-tos…",
    "product_format": [
      {
        "format": [
          {
            "message": [
              {
                "desc": "JIAOCHAN/娇婵"
              }
            ],
            "name": "品牌",
            "pic_urls": null,
            "property_id": "1687"
          }
        ],
        "media_elements": null
      }
    ],
    "tag_card": null,
    "title_image": {
      "height": 21,
      "uri": "tos-cn-i-5mmsx3fupr/product_detail_head.png",
      "url_list": [
        "http://p26-item.ecombdimg.com/tos-cn-i-5mmsx3fupr/product_detail_head.png~tplv-5…"
      ],
      "width": 149
    }
  },
  "id": "3734619545235751048",
  "mainImg": "https://p9-aio.ecombdimg.com/obj/ecom-shop-material/jpeg_m_e0dd74cc60c22ee927610…",
  "name": "【美白+补水+隔离+防晒乳】四效合一SPF50+PA++++防水(试用七天)",
  "originalPrice": 3990,
  "price_source": "buyin_pack_detail",
  "price_verified": 3990,
  "promotion_h5": {
    "basic_info_data": {
      "bottom_label_list": [
        {
          "coms": [
            {
              "border_radius": "",
              "height": 13,
              "margin": "0 4px 0 0",
              "type": "icon",
              "url": "https://p26-item.ecombdimg.com/img/tos-cn-i-5mmsx3fupr/year_rank_icon.png~tplv-5…"
            }
          ],
          "label_type": 70,
          "link_info": {
            "link": "sslocal://webcast_lynxview?url=https%3A%2F%2Flf-dy-sourcecdn-tos.bytegecko.com%2…"
          },
          "render_type": 0
        }
      ],
      "price_info": {
        "price": {
          "min_price": "3?",
          "suffix": "起"
        }
      },
      "product_id": "3734619545235751048",
      "title_info": {
        "title": "【美白+补水+隔离+防晒乳】四效合一SPF50+PA++++防水(试用七天)"
      }
    },
    "collapse_detail": false,
    "comment_data": {
      "buyer_show": {
        "title_bar": {
          "link": "aweme://ecom_buyer_show?title=%E4%B9%B0%E5%AE%B6%E7%A7%80&product_id=37346195452…"
        }
      },
      "good_comment": {
        "comment_list": [
          {
            "avatar": "https://p3-ecom-commentpic.byteimg.com/tos-cn-i-fceoirpogb/229c77efc170705f8a6aa…",
            "comment_id": "3651490945721270571",
            "content": "用了两瓶了，第二次回购，真心好用，推荐给大家。扫码是正品，超赞！",
            "name": "淡**z",
            "tag_list": [
              {}
            ]
          }
        ],
        "media_list": [
          {
            "image_info": {
              "thumbnail": "https://p3-product-comment-sign.byteimg.com/tos-cn-i-8y5sebgt5i/fe48be9f083d4e82…",
              "url": "https://p3-product-comment-sign.byteimg.com/tos-cn-i-8y5sebgt5i/fe48be9f083d4e82…"
            },
            "type": 1,
            "video_info": {}
          }
        ],
        "tag_list": [
          {
            "num": 206,
            "sentiment": 1,
            "text": "回头客"
          }
        ],
        "title_bar": {
          "link": "sslocal://ec_goods_comment/?comment_entrance=product_flow_page&product_id=373461…",
          "sum": 4268
        }
      },
      "good_evaluation": {},
      "shop_extra_comment": {
        "title_bar": {}
      },
      "style_type": 0
    },
    "footer_data": {
      "big_button_list": [
        {
          "bg_color": "#FE2C550D",
          "button_status": "normal",
          "button_type": -3,
          "sub_text_info": {},
          "text_info": {
            "color": "#FE2C55",
            "content": "加入购物车"
          }
        }
      ],
      "small_button_list": [
        {
          "icon_url": "https://lf3-static.bytednsdoc.com/obj/eden-cn/ljylttvjl_lmp/ljhwZthlaukjlkulzlp/…",
          "name": "店铺"
        }
      ]
    },
    "head_figure_data": {
      "container_size": 0,
      "media_list": [
        {
          "content_list": [
            {
              "combination_info": {
                "combination_jump": {}
              },
              "height": 0,
              "url": "https://p3-item.ecombdimg.com/img/ecom-shop-material/jpeg_m_e0dd74cc60c22ee92761…",
              "width": 0
            }
          ],
          "name": "商品",
          "type": "image"
        }
      ],
      "style_type": 0
    },
    "init_popup_data": {
      "find_sim": {}
    },
    "pack_detail": {
      "style_type": 0
    },
    "page_data": {},
    "product_support_info_data": {
      "header_content": {
        "background": "#FFFFFF",
        "content_color": "#161823",
        "service_tag": {}
      },
      "logistics_content": {
        "content_list": [
          {
            "coms": [
              {
                "border_radius": "",
                "type": "icon",
                "url": "https://lf3-static.bytednsdoc.com/obj/eden-cn/rjhw.ajbkvyweh7tvjl/ljhwZthlaukjlk…"
              }
            ],
            "label_type": 0,
            "link": "sslocal://webcast_lynxview?add_safe_area_height=0&gravity=bottom&height_percent=…"
          }
        ],
        "title": "物流"
      },
      "safety_content": {
        "content_list": [
          {
            "coms": [
              {
                "text": "运费险",
                "type": "text"
              }
            ],
            "label_type": 1,
            "render_type": 0
          }
        ],
        "safety_popup_content": [
          {
            "content": "发货90天内退/换货，使用上门取件可享3公斤内免运费，使用快递柜或驿站邮寄可享1公斤内免运费。若选择自行寄回，享受和上门取件同样的免运费金额，需上传真实的运单号…",
            "left_icon": "http://p3-item.ecombdimg.com/tos-cn-i-5mmsx3fupr/second_page_priority_icon_blue.…",
            "title": "运费险",
            "url": "sslocal://webcast_webview?radius=20&up_height_percent=73&up_offset_height=400&up…"
          }
        ],
        "service_type": "2,6,9,10"
      }
    },
    "redirect_location_v2": "",
    "shop_coupon_data": {},
    "shop_info": {
      "basic_info": {
        "account_url": "",
        "background": "",
        "brand_icon": "",
        "grade_info": {
          "is_new_style": true,
          "score": 4.8
        },
        "new_brand_icon": "",
        "shop_extra_info": null,
        "shop_icon_list": null,
        "shop_link_button": {
          "background": "#FE2C55FF",
          "link": "sslocal://goods/store?entrance_location=product_detail_live&pass_through_api=%7B…",
          "text": "进店逛逛"
        }
      },
      "style_type": 0
    }
  },
  "salePrice": 3990,
  "sellNum": 63976
}
```

### Response fields

| Field | Meaning |
|---|---|
| `id` | The item ID of the product. It matches the `itemId` you sent. |
| `name` | The product title shown on the Douyin Shop page. |
| `originalPrice / price_verified` | Price values for the item, both `3990` in the example. The response does not label the unit. |
| `price_source` | A label for where the verified price came from, for example `buyin_pack_detail`. |
| `mainImg` | URL of the main product image. |
| `category.firstCName / secondCName / thirdCName / fourthCName` | Category names from level 1 to level 4, in Chinese. An empty string means the item has no level at that depth. |
| `category.firstCid / secondCid / thirdCid / fourthCid` | Numeric category IDs that match the category names. `0` means the level is not used. |
| `detail_info.product_format[].format[].name` | The name of a product attribute, such as brand or target group. The value is in `message[].desc`. |
| `detail_info.detail_imgs[].url_list` | Image URLs for the product detail page. Each image has more than one URL, plus `width` and `height`. |
| `promotion_h5.comment_data.good_comment.tag_list[].text / num` | A buyer comment tag and the number next to it, such as `回头客` with `206`. |
| `promotion_h5.comment_data.good_comment.comment_list[].content` | The text of a sample buyer comment. Each comment also has `comment_id`, a masked `name` and an `avatar` URL. |

### Notes

- `itemId` is a numeric string, such as `3734619545235751048`. The same value comes back in `id` and in `promotion_h5.basic_info_data.product_id`.
- Text fields such as `name`, category names and comments are in Chinese.
- The comments in this response are only a sample. Call [Douyin Shop Item Comments](/apis/douyin/ec/item-comments) for the full comment list.
- Call [Douyin Shop Item Details](/apis/douyin/ec/item-detail) for other product page data. Use [Douyin Shop Product Search](/apis/douyin/ec/search-items) to look for item IDs.

### Pricing

$0.035714 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/douyin/ec/item-skus.json`](../../../../catalog/models/douyin/ec/item-skus.json) · Store page: https://www.sandbase.ai/model/douyin/ec/item-skus
