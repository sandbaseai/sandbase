# Weibo Comprehensive Search API: pricing, parameters and code examples

`weibo/app/search-all` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns comprehensive search results from Weibo for a specified keyword. Supports pagination and filtering by search type.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/app/search-all", "page": 1, "query": "OpenAI", "search_type": 1}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/app/search-all', {'page': 1, 'query': 'OpenAI', 'search_type': 1})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/app/search-all", {
  "page": 1,
  "query": "OpenAI",
  "search_type": 1
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/app/search-all", sandbase.Params{
	"page": 1,
	"query": "OpenAI",
	"search_type": 1,
})
```

Same call via the path form: `POST /v1/api/weibo/app/search-all` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number, starts from 1 (default 1) default `1`; range 1– |
| `query` | string | yes | Search keyword (required)  |
| `search_type` | integer |  | Search type default `1` |

## Details

Returns the Weibo app's main search results page for a keyword. The response holds the search tabs, a list of result cards (such as matching user accounts), and footer menu data. It needs a search keyword in `query`.

### Use cases

- Find which Weibo accounts the app surfaces first for a brand or product name such as `OpenAI`.
- Read the search tab list to see which result views (all results, real-time, image) exist for a keyword.
- Collect `uid` values from user cards to feed into profile lookups.
- Page through results for a topic to build a keyword research sample.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/app/search-all" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "OpenAI"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search keyword (required) |
| `page` | integer | No | Page number, starts from 1 (default 1) |
| `search_type` | integer | No | Search type |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "channelInfo": {
    "channelConfig": {
      "channelType": "search_result",
      "menu_scheme": "sinaweibo://cardlist?containerid=100103type%3D42%26q%3DOpenAI%26t%3D1&extparam=s…",
      "selectInfo": {
        "flowId": "100103type=1&q=OpenAI&t=1",
        "pageDataType": "flow",
        "tabKey": "profile"
      },
      "show_menu": 1,
      "style": {
        "backgroundColor": "#FFFFFF",
        "backgroundDarkColor": "#1E1E1E",
        "height": 42
      }
    },
    "channels": [
      {
        "ai_preload_key": "search_all_flow",
        "apiPath": "searchall",
        "appid": "100103type=1&q=OpenAI&t=1",
        "cleaned": true,
        "containerid": "100103type=1&q=OpenAI&t=1",
        "dot": {
          "request_mark_interval": 999000
        },
        "dynaConfig": {
          "bizArray": [
            "common"
          ],
          "bizType": "search",
          "enable": true
        },
        "expose": {
          "actionlog": {
            "act_code": 6688,
            "ext": "seqid:1931346883|type:1|t:1|pos:1-31-0|q:OpenAI|srid:19a3e1ec8bb8e49c4ffa8054010…",
            "fid": "100103type=1&q=OpenAI&t=1",
            "lfid": "102803_ctg1_1780_-_ctg1_1780",
            "luicode": "10000512",
            "uicode": "10000003"
          }
        },
        "flowId": "100103type=1&q=OpenAI&t=1",
        "is_first_level": 1,
        "pageDataType": "flow",
        "params": {
          "dfp": "1",
          "is_container": "1",
          "pic_tab_front": 0,
          "search_mode_info": "0",
          "search_ssid": "89fd73bcee6d72e21c1d3d8d3c5cb2e0",
          "search_time": "1769242464",
          "search_vsid": "19a3e1ec8bb8e49c4ffa805401028a0c",
          "searchbar_source": "discover_searchbar"
        }
      }
    ]
  },
  "config": "{}",
  "dsl": {
    "config": {
      "name": "dynamic",
      "version": "1643769",
      "xml": [
        {
          "bType": "default",
          "cVersion": "12.1.0",
          "name": "cardCoupon.xml",
          "signature": "f77359ae…"
        }
      ]
    },
    "version": "1643769",
    "xml": [
      {
        "layout": "%3C%3Fxml+version%3D%221.0%22+encoding%3D%22utf-8%22%3F%3E+%3CRootLayout+++++xml…",
        "name": "cardCoupon.xml"
      }
    ]
  },
  "footer": {
    "data": {
      "handler_type": 2,
      "has_post_menu": 1,
      "menus": [
        {
          "actionlog": {
            "act_code": 554,
            "ext": "seqid:1931346883|type:1|t:1|pos:1-31-2|q:OpenAI|srid:19a3e1ec8bb8e49c4ffa8054010…",
            "fid": "100103type=1&q=OpenAI&t=1",
            "lfid": "102803_ctg1_1780_-_ctg1_1780",
            "luicode": "10000512",
            "uicode": "10000003"
          },
          "button_style": "search_expand",
          "is_expand": 1,
          "name": "和当前4275人一起讨论",
          "params": {
            "align": "center",
            "bg_color": "#F4F4F4",
            "bg_color_dark": "#2C2C2C",
            "cleaned": true,
            "desc_blod": true,
            "desc_color": "#636363",
            "desc_color_dark": "#999999",
            "desc_size": 10
          },
          "pic": "https://simg.s.weibo.com/imgtool/20240424_haed.png",
          "pic_dark": "https://simg.s.weibo.com/imgtool/20240424_haed.png",
          "skip_format": 1
        }
      ],
      "type": 2
    },
    "type": "searchResult"
  },
  "globalChannelConfig": {
    "refreshInfo": {
      "refreshType": "pullArrow"
    }
  },
  "items": [
    {
      "category": "group",
      "itemId": null,
      "items": [
        {
          "category": "card",
          "data": {
            "card_type": 3,
            "cleaned": true,
            "display_arrow": 1,
            "display_type": 1,
            "elements": [
              {
                "actionlog": {
                  "act_code": 554,
                  "ext": "seqid:1931346883|type:1|t:1|pos:1-2-0|q:OpenAI|srid:19a3e1ec8bb8e49c4ffa80540102…",
                  "fid": "100103type=1&q=OpenAI&t=1",
                  "lfid": "102803_ctg1_1780_-_ctg1_1780",
                  "luicode": "10000512",
                  "uicode": "10000003"
                },
                "cleaned": true,
                "scheme": "sinaweibo://userinfo?uid=2798511294",
                "uid": "2798511294"
              }
            ],
            "foldable": true,
            "item_style": {
              "background": {
                "color": "#FFFFFF",
                "colorKey": "CommonCardBackground",
                "type": "color"
              },
              "margin": [
                0
              ],
              "padding": [
                12
              ]
            },
            "max_item_count": 5
          },
          "itemExt": {
            "anchorId": "31793691969"
          },
          "style": {
            "background": {
              "color": "#FFFFFF",
              "colorKey": "CommonCardBackground",
              "type": "color"
            },
            "margin": [
              0
            ],
            "padding": [
              12
            ]
          }
        }
      ],
      "style": {
        "background": {
          "color": "#FFFFFF",
          "colorKey": "CommonCardBackground",
          "type": "color"
        },
        "margin": [
          0
        ],
        "padding": [
          0
        ]
      },
      "type": "vertical"
    }
  ],
  "loadedInfo": "{}",
  "moreInfo": {
    "error": "网络加载失败，请稍后尝试",
    "loading": "正在加载更多",
    "moreType": "default",
    "pagingType": "cursor",
    "params": {
      "count": "10",
      "filter_label_word": "全部",
      "interval_ad_video_count": 11,
      "interval_weibo_count": 36,
      "max_id": 0,
      "page": 2,
      "page_refresh_time": 1793691969,
      "search_ssid": "89fd73bcee6d72e21c1d3d8d3c5cb2e0",
      "search_time": "1769242464",
      "search_vsid": "19a3e1ec8bb8e49c4ffa805401028a0c",
      "transparent_background_height": 0,
      "unify_new_bubble_opt": 1
    }
  },
  "navInfo": "{}",
  "navigationBar": {
    "data": {
      "title_bar_menus": [
        {
          "pic": "https://h5.sinaimg.cn/upload/1059/799/2022/03/30/share_pic.png",
          "pic_highlight": "https://h5.sinaimg.cn/upload/1059/799/2022/03/30/share_pic_hightlight.png",
          "type": "share"
        }
      ]
    },
    "search_title": [
      {
        "act_log": {
          "act_code": 1985,
          "ext": "seqid:1931346883|type:1|t:1|pos:1-31-0|q:OpenAI|srid:19a3e1ec8bb8e49c4ffa8054010…",
          "lfid": "102803_ctg1_1780_-_ctg1_1780",
          "luicode": "10000512",
          "uicode": "10000003"
        },
        "name": "share",
        "pic_height": 30,
        "pic_url": "https://simg.s.weibo.com/imgtool/20250324_0324_light_normal.png",
        "pic_url_dark": "https://simg.s.weibo.com/imgtool/20250324_0324_dark_normal.png",
        "pic_url_selected": "https://simg.s.weibo.com/imgtool/20250324_0324_light_hover.png",
        "pic_url_selected_dark": "https://simg.s.weibo.com/imgtool/20250324_0324_selected_hover_dark.png",
        "pic_width": 30,
        "scheme": "",
        "share_data": {
          "containerid": "100103type=1&q=OpenAI&t=1",
          "custom_share_path": "http://s.weibo.com/weibo?q=OpenAI",
          "desc": "实时资讯，海量讨论",
          "icon": "http://h5.sinaimg.cn/upload/2016/07/29/557/link.png",
          "more_btns": [
            {
              "actionlog": {
                "act_code": 554,
                "ext": "seqid:1931346883|type:1|t:1|pos:1-31-1|q:OpenAI|srid:19a3e1ec8bb8e49c4ffa8054010…",
                "fid": "100103type=1&q=OpenAI&t=1",
                "lfid": "102803_ctg1_1780_-_ctg1_1780",
                "luicode": "10000512",
                "uicode": "10000003"
              },
              "image_url": "https://simg.s.weibo.com/imgtool/20250630_%E5%88%86%E4%BA%AB%E6%90%9C%E7%B4%A2.p…",
              "image_url_dark": "https://simg.s.weibo.com/imgtool/20250630_%E5%88%86%E4%BA%AB%E6%90%9C%E7%B4%A2_d…",
              "name": "分享搜索",
              "params": {
                "cleaned": true,
                "scheme": "sinaweibo://sendweibo?show_keyboard=1&extparam=ann_ext%3Asearch%7Ct%3A1%7Cq%3AOp…",
                "title_max_lines": 1
              },
              "skip_format": 1,
              "type": "share_to_weibo",
              "type_description": "sousuo_share_card"
            }
          ],
          "object_id": "",
          "share_containerid": "230958type%3D1%26q%3DOpenAI",
          "share_mini": []
        },
        "type": "share"
      }
    ],
    "type": "search_default"
  },
  "pageData": "{}",
  "refreshInfo": "{}"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `items[].category` | Type of the entry. Top-level entries are `group` and hold nested entries in `items[].items[]`. Nested entries here are `card`. |
| `items[].items[].data.card_type` | Numeric card type of a result card. Use it to tell user cards from other card kinds. |
| `items[].items[].data.elements[].uid` | Weibo user ID of an account shown in a user card. |
| `items[].items[].data.elements[].scheme` | Weibo app deep link for the element. For user cards it has the form `sinaweibo://userinfo?uid=...`. |
| `items[].items[].data.max_item_count` | Maximum number of elements the card shows before it folds. The card also has `foldable` set to `true`. |
| `items[].items[].itemExt.anchorId` | Anchor ID attached to the card. |
| `channelInfo.channels[].title` | Name of a search tab. The values seen are `综合` (the all-results tab), `实时` (real-time) and `图片` (images). |
| `channelInfo.channels[].containerid` | Container ID of the tab, such as `100103type=1&q=OpenAI&t=1`. It encodes the search type in `type` and the keyword in `q`. |
| `channelInfo.channels[].params.search_time` | Search time as a Unix timestamp string. |
| `footer.data.menus[].name` | Label of a footer button. One label shows how many people are discussing the keyword. |

### Notes

- Pass the keyword in `query`. Send `page` to move through results, starting at `1`.
- The tab `containerid` values show the `type` code of each view, for example `type=1` for the all-results tab, `type=61` for real-time and `type=63` for images. The schema does not document how these map to `search_type`.
- Take a `uid` from a user card and call [Weibo User Profile Information](/apis/weibo/app/user-info) to get that account's profile.
- The response also contains layout and tracking data such as `dsl`, `style` and `actionlog`. You can ignore these for data work.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Weibo App AI Smart Search](/apis/weibo/app/ai-smart-search): Returns AI smart search channel results and feed metadata from Weibo for a specified keyword query, with optional page-based pagination.
- [Weibo Home Recommend Feed](/apis/weibo/app/home-recommend-feed): Returns recommended feed items from the Weibo app homepage, with options to paginate and specify the number of items per request.
- [Weibo Hot Search Rankings](/apis/weibo/app/hot-search): Returns current Weibo hot search rankings across various categories.

---
Machine-readable: [`catalog/models/weibo/app/search-all.json`](../../../../catalog/models/weibo/app/search-all.json) · Store page: https://www.sandbase.ai/model/weibo/app/search-all
