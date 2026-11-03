# Weibo App AI Smart Search API: pricing, parameters and code examples

`weibo/app/ai-smart-search` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns AI smart search channel results and feed metadata from Weibo for a specified keyword query, with optional page-based pagination.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/app/ai-smart-search", "page": 1, "query": "OpenAI"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/app/ai-smart-search', {'page': 1, 'query': 'OpenAI'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/app/ai-smart-search", {
  "page": 1,
  "query": "OpenAI"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/app/ai-smart-search", sandbase.Params{
	"page": 1,
	"query": "OpenAI",
})
```

Same call via the path form: `POST /v1/api/weibo/app/ai-smart-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number, starts from 1 (default 1) default `1`; range 1– |
| `query` | string | yes | Search keyword (required)  |

## Details

Returns the Weibo app AI smart search response for a keyword. The response lists the search channels (such as 综合, 实时, 图片), the card items for the first page, and footer and share metadata. It needs a `query` and accepts an optional `page`.

### Use cases

- List the search channels Weibo offers for a keyword, with the `containerid` of each one.
- Read the `search_time` and search session IDs for a keyword query to log when a search ran.
- Check which card types and anchor IDs the app returns for a keyword, including the `ai_answer` slot.
- Build a share link for a keyword search from the `custom_share_path` value.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/app/ai-smart-search" \
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

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "channelInfo": {
    "channelConfig": {
      "channelType": "search_result",
      "menu_scheme": "sinaweibo://cardlist?containerid=100103type%3D42%26q%3DOpenAI%26t%3D1&extparam=d…",
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
            "ext": "seqid:231949943|type:200|t:1|pos:1-24-0|q:OpenAI|srid:12e6bb13aeb29c79454459cebb…",
            "fid": "100103type=200&q=OpenAI&t=1&vstyle=1",
            "lfid": "102803_ctg1_1780_-_ctg1_1780",
            "luicode": "10000512",
            "uicode": "10000003"
          }
        },
        "flowId": "100103type=1&q=OpenAI&t=1",
        "is_first_level": 1,
        "pageDataType": "flow",
        "params": {
          "dfp": "200",
          "is_container": "1",
          "pic_tab_front": 0,
          "search_mode_info": "1",
          "search_ssid": "12e6bb13aeb29c79454459cebb1646e9",
          "search_time": 1793691964,
          "search_vsid": "12e6bb13aeb29c79454459cebb1646e9",
          "searchbar_source": "discover_searchbar"
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
            "ext": "seqid:231949943|type:200|t:1|pos:1-24-0|q:OpenAI|srid:12e6bb13aeb29c79454459cebb…",
            "fid": "100103type=200&q=OpenAI&t=1&vstyle=1",
            "lfid": "102803_ctg1_1780_-_ctg1_1780",
            "luicode": "10000512",
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
        "anchorId": "1971793691964"
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
          "ext": "seqid:231949943|type:200|t:1|pos:1-24-0|q:OpenAI|srid:12e6bb13aeb29c79454459cebb…",
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
          "containerid": "100103type=200&q=OpenAI&t=1&vstyle=1",
          "custom_share_path": "http://s.weibo.com/weibo?q=OpenAI",
          "desc": "实时资讯，海量讨论",
          "icon": "http://h5.sinaimg.cn/upload/2016/07/29/557/link.png",
          "more_btns": [
            {
              "actionlog": {
                "act_code": 554,
                "ext": "seqid:231949943|type:200|t:1|pos:1-24-1|q:OpenAI|srid:12e6bb13aeb29c79454459cebb…",
                "fid": "100103type=200&q=OpenAI&t=1&vstyle=1",
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
| `channelInfo.channels[].title` | Display name of the search channel, for example 综合 (all), 实时 (real time) or 图片 (pictures). |
| `channelInfo.channels[].containerid / channelInfo.channels[].flowId` | ID of the channel's result list. It contains the channel `type` number, the query `q` and `t`. |
| `channelInfo.channels[].apiPath` | Name of the search endpoint that serves the channel. The real-time channel also has `scroll_api`. |
| `channelInfo.channels[].params.search_time` | Unix timestamp in seconds for when the search ran. |
| `channelInfo.channels[].params.search_ssid / channelInfo.channels[].params.search_vsid` | Search session IDs. They repeat across the channels of one response. |
| `channelInfo.channels[].style.flowType` | Layout of the channel, `flow` for a list or `staggered` for a two column grid. |
| `items[].category` | Kind of entry in the result list. In this response all entries are `card`. |
| `items[].data.card_type` | Numeric card type of the entry, for example `197` or `269`. |
| `items[].data.itemid` | ID of the card. The value `ai_answer` marks the AI answer slot. |
| `navigationBar.search_title[].share_data.custom_share_path` | Web search URL for the keyword on s.weibo.com. |

### Notes

- Pass the keyword in `query`. Use `page` to move through pages, starting at 1.
- The sample cards carry layout data only. This response does not show post text or user fields.
- For another way to search by keyword, try [Weibo Keyword Search](/apis/weibo/search-all).
- Call [Weibo Post Detail (App)](/apis/weibo/app/status-detail) when you have a post ID and need the full post.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Weibo Home Recommend Feed](/apis/weibo/app/home-recommend-feed): Returns recommended feed items from the Weibo app homepage, with options to paginate and specify the number of items per request.
- [Weibo Hot Search Rankings](/apis/weibo/app/hot-search): Returns current Weibo hot search rankings across various categories.
- [Weibo Hot Search Categories](/apis/weibo/app/hot-search-categories): Returns all available hot search categories from Weibo.

---
Machine-readable: [`catalog/models/weibo/app/ai-smart-search.json`](../../../../catalog/models/weibo/app/ai-smart-search.json) · Store page: https://www.sandbase.ai/model/weibo/app/ai-smart-search
