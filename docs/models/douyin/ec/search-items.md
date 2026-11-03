# Douyin Shop Product Search API: pricing, parameters and code examples

`douyin/ec/search-items` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.035714 per call · **Modes:** sync

Search products sold in Douyin shops by keyword, with price, sales and shop info; pages after the first use searchId.

## Pricing

- **$0.035714 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/ec/search-items", "keyword": "防晒霜"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/ec/search-items', {'keyword': '防晒霜'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/ec/search-items", {
  "keyword": "防晒霜"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/ec/search-items", sandbase.Params{
	"keyword": "防晒霜",
})
```

Same call via the path form: `POST /v1/api/douyin/ec/search-items` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | string |  | Page number for pagination.  |
| `keyword` | string | yes | Search keyword.  |
| `searchId` | string |  | Search ID; use the search_id value returned by the last response for subsequent pages.  |

## Details

This API searches products sold in Douyin shops by keyword. It returns a list of matching products with title, category, price, monthly sales, commission and shop info. The only required input is `keyword`.

### Use cases

- Compare prices and monthly sales of sunscreen products on Douyin Shop for a given search term.
- Find which shops sell a product type and check their shop scores.
- Collect product IDs and detail links for a category to feed a product tracking list.
- Check commission rates and creator counts to pick products for affiliate promotion.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/ec/search-items" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "防晒霜"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword. |
| `page` | string | No | Page number for pagination. |
| `searchId` | string | No | Search ID; use the search_id value returned by the last response for subsequent pages. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "extra": {
    "channel_id": "200",
    "material_type": "promotion_id",
    "recall_type": "Search",
    "search_id": "5cc89a0f6d6f25e2a230f777abb7c0e1738a5293bf29fad48e179265ec906629de617091322357ff…",
    "session_id": "2240ef2d…"
  },
  "has_more": true,
  "log_id": "2026110315320086EF1597058215346880",
  "promotions": [
    {
      "base_info": {
        "category": {
          "first_category": {
            "category_id": 1000003462,
            "category_name": "个人护理"
          },
          "fourth_category": {
            "category_id": 0,
            "category_name": ""
          },
          "leaf_layer": 3,
          "second_category": {
            "category_id": 1000003463,
            "category_name": "面部洗护"
          },
          "third_category": {
            "category_id": 1000003485,
            "category_name": "防晒霜"
          }
        },
        "detail_url": "https://haohuo.jinritemai.com/ecommerce/trade/detail/index.html?id=3851366241944…",
        "main_img": {
          "uri": "ecom-shop-material/jpeg_m_f2116c4fc8416ddd62fd6a127d888a82_sx_863881_www1024-102…",
          "url_list": [
            "https://p9-aio.ecombdimg.com/obj/ecom-shop-material/jpeg_m_f2116c4fc8416ddd62fd6…"
          ]
        },
        "price": null,
        "title": "【AK专属】【美白+防晒+隔离+保湿】高倍防晒乳持妆防水清爽四季*50g"
      },
      "product_id": "3851366241944076623",
      "promotion_id": "3851368256174686561"
    }
  ],
  "promotions_pc": null,
  "shops": null,
  "summary_authors": [],
  "summary_promotions": [
    {
      "base_model": {
        "extend_info": {
          "data_report": {
            "channel_id": "200",
            "commodity_id": "3851368256174686561",
            "first_tags": "big_promotion_11_tag",
            "log_pb": "2026110315320086EF1597058215346880",
            "material_type": "promotion_id",
            "product_id": "3851366241944076623",
            "query": "防晒霜",
            "recall_type": "Search"
          },
          "is_in_cart": false
        },
        "marketing_info": {
          "price_desc": {
            "price": {
              "decimal": "9",
              "integer": "34",
              "origin": 3490,
              "suffix": ""
            },
            "price_text": "到手价"
          }
        },
        "product_info": {
          "category": {
            "first_category": {
              "category_id": 1000003462,
              "category_name": "个人护理"
            },
            "fourth_category": {
              "category_id": 0,
              "category_name": ""
            },
            "leaf_layer": 3,
            "second_category": {
              "category_id": 1000003463,
              "category_name": "面部洗护"
            },
            "third_category": {
              "category_id": 1000003485,
              "category_name": "防晒霜"
            }
          },
          "detail_url": "https://haohuo.jinritemai.com/ecommerce/trade/detail/index.html?id=3851366241944…",
          "good_ratio": {
            "decimal": "3",
            "integer": "83",
            "origin": 83.33333333333333,
            "suffix": "%"
          },
          "main_img": {
            "uri": "ecom-shop-material/jpeg_m_f2116c4fc8416ddd62fd6a127d888a82_sx_863881_www1024-102…",
            "url_list": [
              "https://p9-aio.ecombdimg.com/obj/ecom-shop-material/jpeg_m_f2116c4fc8416ddd62fd6…"
            ]
          },
          "month_sale": {
            "origin": 1507
          },
          "month_sale_text": "月销",
          "name": "【AK专属】【美白+防晒+隔离+保湿】高倍防晒乳持妆防水清爽四季*50g",
          "product_status": {
            "check_status": 3,
            "status": 0
          }
        },
        "promotion_info": {
          "cooper_author_num": {
            "decimal": "",
            "integer": "",
            "origin": 79,
            "suffix": ""
          },
          "cos_info": {
            "cos": {
              "cos_fee": {
                "decimal": "75",
                "integer": "1",
                "origin": 175,
                "suffix": ""
              },
              "cos_ratio": {
                "decimal": "",
                "integer": "5",
                "origin": 5,
                "suffix": "%"
              }
            },
            "cos_type": 3,
            "tiered_cos_info": {}
          },
          "promotion_status": 2,
          "ticket_tip_info": {
            "type": 1
          }
        },
        "shop_info": {
          "shop_id": 298439640,
          "shop_logo": {
            "url_list": [
              "https://p6-ecom-qualification-sign.ecombdimg.com/tos-cn-i-6vegkygxbk/3663ffe5396…"
            ]
          },
          "shop_name": "娇芝妍美妆护肤优选",
          "shop_score_info": {
            "has_data": true,
            "shop_score": {
              "percentage": 0,
              "rating": "",
              "rise_than_7d_ago": 0,
              "score": 84
            }
          }
        },
        "tag_info": {
          "main_tags": [
            {
              "pic": "https://lf3-static.bytednsdoc.com/obj/eden-cn/lm-ljuhpssh/ljhwZthlaukjlkulzlp/d2…",
              "tag_type": 1,
              "text": {
                "text": ""
              },
              "type": "big_promotion_11_tag"
            }
          ],
          "second_tags": [
            {
              "border_color": "rgba(255, 51, 68, 0.25)",
              "tag_type": 2,
              "text": {
                "color": "#FF3B52",
                "text": "消费券"
              },
              "text_right": {
                "color": "#FF3B52"
              },
              "type": "big_promote_coupon"
            }
          ],
          "tag_codes": [
            "big_promotion_11_tag"
          ]
        }
      },
      "custom_model": {
        "selection_square_model": {
          "card_resource_info": {
            "CardPictureTag": {
              "tag_list": [
                {
                  "style_config": "{\"pic\":\"https://lf3-static.bytednsdoc.com/obj/eden-cn/lm-ljuhpssh/ljhwZthlaukjlk…",
                  "style_templ": 1
                }
              ]
            },
            "CardTextTag": {
              "tag_list": [
                {
                  "style_config": "{\"text\":{\"text\":\"消费券\",\"color\":\"#FF3B52\"},\"type\":\"big_promote_coupon\",\"tag_type\":…",
                  "style_templ": 1
                }
              ]
            }
          },
          "hit_ranking_list": false,
          "is_adv_approve": false,
          "recommend_reason": {
            "recommend_reason": {
              "extra": {
                "ab_tag": "",
                "alli_cate_id": "0",
                "cur_date_type": "本周榜单",
                "cur_genre_type": "直播带货",
                "cur_rank": "4",
                "cur_rank_type": "趋势榜",
                "date_type": "7d",
                "ftr_score": "0.0"
              },
              "icon": "https://lf26-cm.ecombdstatic.com/obj/cmp-ecom-alliance/iconboard.png",
              "rec_type": 2,
              "text": "防晒霜直播带货趋势榜·第4名"
            }
          },
          "sell_point": {}
        }
      },
      "product_id": "3851366241944076623",
      "promotion_id": "3851368256174686561"
    }
  ],
  "summary_shops": [],
  "total": 500
}
```

### Response fields

| Field | Meaning |
|---|---|
| `promotions[].product_id / promotions[].promotion_id` | IDs of the product and of its promotion listing. Both are long numeric strings. |
| `promotions[].base_info.title` | Product title as shown in the shop. |
| `promotions[].base_info.detail_url` | Link to the product detail page. |
| `summary_promotions[].base_model.marketing_info.price_desc.price.origin` | Price value as an integer, for example `3490` next to the display value `34.9`. The `price_text` field next to it reads `到手价`, which is the final price after discounts. |
| `summary_promotions[].base_model.product_info.month_sale.origin` | Monthly sales count for the product. `month_sale_text` holds the label `月销`. |
| `summary_promotions[].base_model.product_info.good_ratio.origin` | Good review ratio as a percentage, for example `83.33`. |
| `summary_promotions[].base_model.product_info.category.third_category.category_name` | Leaf category name of the product. The same block also has `first_category` and `second_category`. |
| `summary_promotions[].base_model.shop_info.shop_id / summary_promotions[].base_model.shop_info.shop_name` | ID and name of the shop selling the product. |
| `summary_promotions[].base_model.shop_info.shop_score_info.shop_score.score` | Score of the shop, for example `84`. |
| `summary_promotions[].base_model.promotion_info.cos_info.cos.cos_ratio.origin` | Commission ratio for the promotion, shown with suffix `%`. `cos_fee` gives the commission amount. |

### Notes

- The `promotions[].base_info.price` field is `null` in this response. Read the price from `summary_promotions[].base_model.marketing_info.price_desc`.
- For the next page, send the `extra.search_id` value from the last response as `searchId`, and set `page`. The `has_more` field shows whether more results exist.
- Use `product_id` from the results with [Douyin Shop Item Details](/apis/douyin/ec/item-detail) or [Douyin Shop Item SKUs](/apis/douyin/ec/item-skus) to get more data on one product.
- Use `shop_id` with [Douyin Shop Items](/apis/douyin/ec/shop-items) to list other products from the same shop.

### Pricing

$0.035714 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/douyin/ec/search-items.json`](../../../../catalog/models/douyin/ec/search-items.json) · Store page: https://www.sandbase.ai/model/douyin/ec/search-items
