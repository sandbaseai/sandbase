# Weibo Hot Search Rankings API: pricing, parameters and code examples

`weibo/app/hot-search` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns current Weibo hot search rankings across various categories. Supports filtering by category such as realtime trends or by city name for regional topics.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/app/hot-search", "category": "realtimehot", "count": 20, "page": 1}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/app/hot-search', {'category': 'realtimehot', 'count': 20, 'page': 1})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/app/hot-search", {
  "category": "realtimehot",
  "count": 20,
  "page": 1
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/app/hot-search", sandbase.Params{
	"category": "realtimehot",
	"count": 20,
	"page": 1,
})
```

Same call via the path form: `POST /v1/api/weibo/app/hot-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number, starts from 1 (default 1) default `1`; range 1– |
| `count` | integer |  | Items per page, default 20, max 50 default `20`; range 1–50 |
| `category` | string |  | Hot search category default `"realtimehot"` |
| `region_name` | string |  | City name for local hot search, only effective when category=region, default Beijing  |

## Details

Returns the current Weibo hot search ranking as a list of topic cards, plus the tab list for the other ranking categories. All inputs are optional: `category` picks the ranking, `region_name` picks a city, and `page` and `count` control paging.

### Use cases

- Pull the top realtime Weibo topics and store the ranked list with each topic's heat number.
- Check which topics carry a rank flag icon to see how Weibo marks them.
- Request a city ranking with `category` set to `region` and a `region_name` value to follow local topics.
- Read the `channelInfo.channels[].title` tabs to see which ranking tabs Weibo shows.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/app/hot-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `category` | string | No | Hot search category |
| `count` | integer | No | Items per page, default 20, max 50 |
| `page` | integer | No | Page number, starts from 1 (default 1) |
| `region_name` | string | No | City name for local hot search, only effective when category=region, default Beijing |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "channelInfo": {
    "channelConfig": {
      "auto_refresh_config": {
        "106003_-_type:25_-_filter_type:mineband": {
          "page_resume_expire_sec": 80000,
          "tab_and_background_expire_min": 1
        },
        "106003type=25&t=3&disable_hot=1&filter_type=fun": {
          "page_resume_expire_sec": 80000,
          "tab_and_background_expire_min": 1
        },
        "106003type=25&t=3&disable_hot=1&filter_type=gamenav": {
          "page_resume_expire_sec": 80000,
          "tab_and_background_expire_min": 1
        },
        "106003type=25&t=3&disable_hot=1&filter_type=lifenav": {
          "page_resume_expire_sec": 80000,
          "tab_and_background_expire_min": 1
        },
        "106003type=25&t=3&disable_hot=1&filter_type=realtimehot": {
          "page_resume_expire_sec": 80000,
          "tab_and_background_expire_min": 1
        },
        "106003type=25&t=3&disable_hot=1&filter_type=region": {
          "page_resume_expire_sec": 80000,
          "tab_and_background_expire_min": 1
        },
        "106003type=25&t=3&disable_hot=1&filter_type=social": {
          "page_resume_expire_sec": 80000,
          "tab_and_background_expire_min": 1
        },
        "106003type=25&t=3&disable_hot=1&filter_type=sportnav": {
          "page_resume_expire_sec": 80000,
          "tab_and_background_expire_min": 1
        }
      },
      "refresh_configs": {
        "106003_-_type:25_-_filter_type:mineband": 1,
        "106003type=25&t=3&disable_hot=1&filter_type=fun": 1,
        "106003type=25&t=3&disable_hot=1&filter_type=gamenav": 1,
        "106003type=25&t=3&disable_hot=1&filter_type=lifenav": 1,
        "106003type=25&t=3&disable_hot=1&filter_type=realtimehot": 1,
        "106003type=25&t=3&disable_hot=1&filter_type=region": 1,
        "106003type=25&t=3&disable_hot=1&filter_type=social": 1,
        "106003type=25&t=3&disable_hot=1&filter_type=sportnav": 1
      },
      "selectInfo": {
        "flowId": "106003type=25&t=3&disable_hot=1&filter_type=realtimehot",
        "pageDataType": "flow",
        "tabKey": "commonPage"
      }
    },
    "channels": [
      {
        "actionlog": {
          "act_code": 554,
          "act_type": 1,
          "ext": "seqid:17936919682050238243232|srid:56d365cce1fd9aab4fdf0021b89f242d|lcate:1001|t…",
          "fid": "106003type=25&t=3&disable_hot=1&filter_type=realtimehot",
          "lfid": "102803_ctg1_1780_-_ctg1_1780",
          "luicode": "10000512",
          "uicode": "10000011"
        },
        "apiPath": "flowpage",
        "containerid": "106003_-_type:25_-_filter_type:mineband",
        "flowId": "106003_-_type:25_-_filter_type:mineband",
        "pageDataType": "flow",
        "params": {
          "is_container": 1,
          "transType": "pageinfo"
        },
        "scheme": "sinaweibo://pageinfo?containerid=106003_-_type:25_-_filter_type:mineband&title=热…",
        "style": {
          "flowType": "flow",
          "padding": [
            0
          ]
        },
        "title": "我的",
        "titleInfo": {
          "icon": "",
          "iconDark": "",
          "style": {
            "backgroundDarkIcon": "",
            "backgroundIcon": "",
            "font": "",
            "fontSize": 15,
            "iconHeight": 24,
            "iconWidth": 24,
            "padding": [
              0
            ],
            "selectBackgroundDarkIcon": ""
          },
          "subTitle": ""
        }
      }
    ]
  },
  "config": "{}",
  "items": [
    {
      "category": "cell",
      "text": {
        "content": "实时热点，每分钟更新一次",
        "style": {
          "ellipsize": "end",
          "margin": [
            12
          ],
          "maxLines": 1,
          "textColor": "#939393",
          "textColorKey": "CommonGray93",
          "textSize": 12
        }
      },
      "type": "text"
    }
  ],
  "loadedInfo": "{}",
  "pageData": "{}",
  "pageHeader": "{}",
  "pageRefresh": "{}",
  "pageTabBar": "{}",
  "pageTitle": "{}",
  "refreshInfo": "{}"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `items[].items[].data.desc` | Text of the hot search topic, without the surrounding `#` marks. |
| `items[].items[].data.desc_extr` | Number shown next to the topic, such as `2173490`. It looks like a heat or popularity count. Some cards, such as the first pinned one, do not have it. |
| `items[].items[].data.icon` | URL of the small flag image shown beside the topic. The file name changes between topics (for example `2_0.png` and `1_0.png`). |
| `items[].items[].data.actionlog.ext` | Tracking string with `key:` (the topic with `#` marks), `pos:` and `realpos:` (position in the list) and `cate:` (category code). |
| `items[].items[].data.itemid / items[].items[].itemExt.anchorId` | Internal ID strings for the card. They repeat the position and topic key. |
| `items[].itemId` | Name of the group of cards. The topic list sits in the group with `itemId` set to `hotword`. |
| `items[].text.content` | Label text between card groups, such as the notice that the list updates every minute. |
| `channelInfo.channels[].title` | Name of each ranking tab, such as `热搜` (hot search) and `文娱` (entertainment). |
| `channelInfo.channels[].containerid` | ID of the tab. Its `filter_type=` part names the ranking, such as `realtimehot` or `fun`. |

### Notes

- Read topics from the `items` entry whose `itemId` is `hotword`. Other entries in `items` are text labels.
- The first card in the example has no `desc_extr`. Check that it exists before you read it.
- The `filter_type` values in `channelInfo.channelConfig.refresh_configs` include `realtimehot`, `fun`, `gamenav`, `lifenav`, `region`, `social` and `sportnav`. To list the categories, call [Weibo Hot Search Categories](/apis/weibo/app/hot-search-categories).
- `region_name` only takes effect when `category` is `region`.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Weibo App AI Smart Search](/apis/weibo/app/ai-smart-search): Returns AI smart search channel results and feed metadata from Weibo for a specified keyword query, with optional page-based pagination.
- [Weibo Home Recommend Feed](/apis/weibo/app/home-recommend-feed): Returns recommended feed items from the Weibo app homepage, with options to paginate and specify the number of items per request.
- [Weibo Hot Search Categories](/apis/weibo/app/hot-search-categories): Returns all available hot search categories from Weibo.

---
Machine-readable: [`catalog/models/weibo/app/hot-search.json`](../../../../catalog/models/weibo/app/hot-search.json) · Store page: https://www.sandbase.ai/model/weibo/app/hot-search
