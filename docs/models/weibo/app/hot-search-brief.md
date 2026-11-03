# Weibo Hot search brief API: pricing, parameters and code examples

`weibo/app/hot-search-brief` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get hot search brief on Weibo. Returns the platform data as structured JSON.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/app/hot-search-brief"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/app/hot-search-brief', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/app/hot-search-brief", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/app/hot-search-brief", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/weibo/app/hot-search-brief` with the body above minus `model`.

## Details

Returns the Weibo app search result page for the query "热搜简报" (hot search brief). It takes no input parameters. The response holds the search channel tabs, page menus, and a list of card items for the page layout.

### Use cases

- Read the search channel tabs (综合, 智搜, 实时) and their container IDs to see how Weibo structures this search page.
- Collect the card item IDs from the brief page to track which cards Weibo shows for this query.
- Pull the share button and menu data to build a link or share card for the hot search brief page.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/app/hot-search-brief" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "channelInfo": {
    "channelConfig": {
      "channelType": "search_result",
      "menu_scheme": "sinaweibo://cardlist?containerid=100103type%3D42%26q%3D%E7%83%AD%E6%90%9C%E7%AE%…",
      "selectInfo": [],
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
        "appid": "100103type=1&q=热搜简报&t=911",
        "cleaned": true,
        "containerid": "100103type=1&q=热搜简报&t=911",
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
            "ext": "seqid:489468554|type:200|t:911|pos:1-24-0|q:热搜简报|srid:2b9d72a3193b472b12f90ea03c…",
            "fid": "100103type=200&q=%E7%83%AD%E6%90%9C%E7%AE%80%E6%8A%A5&t=911&vstyle=1",
            "lfid": "102803_ctg1_1780_-_ctg1_1780",
            "luicode": "10001344",
            "uicode": "10000003"
          }
        },
        "flowId": "100103type=1&q=热搜简报&t=911",
        "is_first_level": 1,
        "pageDataType": "flow",
        "params": {
          "dfp": "200",
          "is_container": "1",
          "pic_tab_front": 0,
          "search_mode_info": "1",
          "search_ssid": "2b9d72a3193b472b12f90ea03cf710e4",
          "search_time": 1793691973,
          "search_vsid": "2b9d72a3193b472b12f90ea03cf710e4"
        }
      }
    ]
  },
  "config": "{}",
  "footer": {
    "data": {
      "handler_type": 2,
      "has_post_menu": 1,
      "menus": [
        {
          "actionlog": {
            "act_code": 554,
            "ext": "seqid:489468554|type:200|t:911|pos:1-24-0|q:热搜简报|srid:2b9d72a3193b472b12f90ea03c…",
            "fid": "100103type=200&q=%E7%83%AD%E6%90%9C%E7%AE%80%E6%8A%A5&t=911&vstyle=1",
            "lfid": "102803_ctg1_1780_-_ctg1_1780",
            "luicode": "10001344",
            "uicode": "10000003"
          },
          "button_style": "search_expand",
          "duration": 3000,
          "is_expand": 1,
          "name": "有问题尽管问我",
          "params": {
            "align": "center",
            "bg_color": "#F4F4F4",
            "bg_color_dark": "#2C2C2C",
            "cleaned": true,
            "disable_count": false,
            "is_interrupt": 0,
            "pic_height": 26,
            "pic_width": 26
          },
          "pic": "https://simg.s.weibo.com/imgtool/20251127_chat_icon.png",
          "pic_dark": "https://simg.s.weibo.com/imgtool/20251127_chat_icon_dark.png"
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
      "category": "card",
      "data": {
        "backgroundColor": "#EEEEEE",
        "backgroundDarkColor": "#151515",
        "card_type": 197,
        "height": 1,
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
            0
          ]
        },
        "openurl": "",
        "padding": [
          0
        ]
      },
      "itemExt": {
        "anchorId": "1971793691973"
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
          0
        ]
      }
    }
  ],
  "loadedInfo": "{}",
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
          "ext": "seqid:489468554|type:200|t:911|pos:1-24-0|q:热搜简报|srid:2b9d72a3193b472b12f90ea03c…",
          "lfid": "102803_ctg1_1780_-_ctg1_1780",
          "luicode": "10001344",
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
          "containerid": "100103type=200&q=%E7%83%AD%E6%90%9C%E7%AE%80%E6%8A%A5&t=911&vstyle=1",
          "custom_share_path": "https://m.s.weibo.com/applink/go2?noclose=1&url=sinaweibo%3A//searchall%3Fcontai…",
          "desc": "",
          "icon": "https://simg.s.weibo.com/zhisou/sharecard_image_0.png",
          "more_btns": [
            {
              "actionlog": {
                "act_code": 554,
                "ext": "seqid:489468554|type:200|t:911|pos:1-24-1|q:热搜简报|srid:2b9d72a3193b472b12f90ea03c…",
                "fid": "100103type=200&q=%E7%83%AD%E6%90%9C%E7%AE%80%E6%8A%A5&t=911&vstyle=1",
                "lfid": "102803_ctg1_1780_-_ctg1_1780",
                "luicode": "10001344",
                "uicode": "10000003"
              },
              "image_url": "https://simg.s.weibo.com/imgtool/20250630_%E5%88%86%E4%BA%AB%E6%90%9C%E7%B4%A2.p…",
              "image_url_dark": "https://simg.s.weibo.com/imgtool/20250630_%E5%88%86%E4%BA%AB%E6%90%9C%E7%B4%A2_d…",
              "name": "分享搜索",
              "params": {
                "cleaned": true,
                "scheme": "sinaweibo://sendweibo?show_keyboard=1&extparam=ann_ext%3Asearch%7Ct%3A911%7Cq%3A…",
                "title_max_lines": 1
              },
              "skip_format": 1,
              "type": "share_to_weibo",
              "type_description": "sousuo_share_card"
            }
          ],
          "object_id": "",
          "share_containerid": "23296496eb0729de2b6f002d3393c07af0bc82",
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
| `channelInfo.channels[].title` | Name of the search tab, such as `综合`, `智搜` or `实时`. |
| `channelInfo.channels[].containerid` | Container ID of the tab. It encodes the search type (`type=1`, `type=261`, `type=61`), the query `q` and `t=911`. |
| `channelInfo.channels[].pageDataType` | How the tab loads its content, for example `flow` or `wbox`. |
| `channelInfo.channels[].scroll_api` | Name of the API path the tab scrolls through. The real-time tab shows `search/realtime`. |
| `channelInfo.channels[].params.search_time` | Time of the search as a Unix timestamp in seconds. |
| `items[].category` | Type of the page item. The visible items use `card`. |
| `items[].data.card_type` | Numeric card type, such as `197` or `269`. Cards of type `197` have no content and act as spacers or anchors. |
| `items[].data.itemid / items[].itemExt.anchorId` | ID of the card on the page. |
| `footer.data.menus[].name` | Label of a footer button, such as `分享` (share). The `params.count` field holds a number shown with the button. |
| `navigationBar.search_title[].share_data.containerid` | Container ID used to share this search page. |

### Notes

- The request takes no parameters. Send an empty JSON object `{}`.
- The list of brief cards in `items` is trimmed to layout data here. For ranked hot search topics, call [Weibo Hot Search Rankings](/apis/weibo/app/hot-search) next.
- To browse hot search groups, use [Weibo Hot Search Categories](/apis/weibo/app/hot-search-categories).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/weibo/app/hot-search-brief.json`](../../../../catalog/models/weibo/app/hot-search-brief.json) · Store page: https://www.sandbase.ai/model/weibo/app/hot-search-brief
