# Weibo User Timeline API: pricing, parameters and code examples

`weibo/app/user-timeline` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get the posts on a Weibo user's timeline: text, publish time, region, images and repost, comment and like counts, with page and month filters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/app/user-timeline", "filter_type": "all", "month": null, "page": 1, "uid": "7648703289"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/app/user-timeline', {'filter_type': 'all', 'month': None, 'page': 1, 'uid': '7648703289'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/app/user-timeline", {
  "filter_type": "all",
  "month": null,
  "page": 1,
  "uid": "7648703289"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/app/user-timeline", sandbase.Params{
	"filter_type": "all",
	"month": nil,
	"page": 1,
	"uid": "7648703289",
})
```

Same call via the path form: `POST /v1/api/weibo/app/user-timeline` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | User ID (required)  |
| `page` | integer |  | Page number, starts from 1 (default 1) default `1`; range 1– |
| `month` |  |  | Time filter parameter, format YYYYMMDD (only used when filter_type=month)  |
| `filter_type` | string |  | Filter type (default "all") default `"all"` |

## Details

Returns a page of posts from a Weibo user's timeline. Each post carries its text, publish time, region, images and repost, comment and like counts. You pass the user ID as `uid`, and you can set `page`, `filter_type` and `month` to narrow the results.

### Use cases

- Track what a brand, media outlet or public figure posts on Weibo.
- Compare like counts across an account's recent posts to see which ones drew the most reaction.
- Collect the images and check-in places attached to a user's posts.
- Pull a single month of an account's posts with `filter_type` set to `month`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/app/user-timeline" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "7648703289"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | User ID (required) |
| `filter_type` | string | No | Filter type (default "all") |
| `month` | string | No | Time filter parameter, format YYYYMMDD (only used when filter_type=month) |
| `page` | integer | No | Page number, starts from 1 (default 1) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "config": "{}",
  "dsl": {
    "config": {
      "name": "dynamic",
      "version": "1643769",
      "xml": [
        {
          "bType": "profile",
          "cVersion": "13.3.4",
          "name": "profile_dyna_avatars.xml",
          "signature": "dec06681…"
        }
      ]
    },
    "version": "1643769",
    "xml": [
      {
        "layout": "%3C%3Fxml+version%3D%221.0%22+encoding%3D%22utf-8%22%3F%3E+%3CRootLayout+xmlns%3…",
        "name": "profile_dyna_avatars.xml"
      }
    ]
  },
  "items": [
    {
      "category": "card",
      "data": {
        "card_type": 216,
        "filter_scheme": "sinaweibo://wbaction_filterdialog?select_containerid=1076037648703289_-_WEIBO_SE…",
        "left_hint": [
          {
            "content": "全部微博(1136)",
            "style": {
              "textColor": "#ff828282",
              "textSize": 13
            },
            "type": "text"
          }
        ],
        "openurl": "",
        "right_filter": [
          {
            "iconUrl": "https://d.sinaimg.cn/prd/1059/799/2025/06/20/shaixuan.png",
            "style": {
              "darkMode": "urlAppend",
              "height": 15,
              "width": 15
            },
            "type": "icon"
          }
        ]
      },
      "itemExt": {
        "anchorId": "2161793691976"
      },
      "style": {
        "margin": [
          0.0
        ],
        "padding": [
          0.0
        ]
      }
    }
  ],
  "loadedInfo": "{}",
  "moreInfo": {
    "autoLoadMoreIndex": 10,
    "error": "网络加载失败，请稍后尝试",
    "loading": "正在加载更多",
    "moreType": "default",
    "pagingType": "cursor",
    "params": {
      "count": 20,
      "max_id": 0,
      "page": 2
    }
  },
  "navInfo": "{}",
  "pageData": "{}",
  "refreshInfo": "{}"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `items[].category` | Type of each entry. `card` is a header block with the filter and post count, and `feed` is an actual post. |
| `items[].data.left_hint[].content` | Label on the header card that shows the total post count for the account, for example `全部微博(1136)`. |
| `items[].data.attitudes_count` | Like count of the post. |
| `items[].data.bmiddle_pic` | URL of the medium-size image attached to the post, when it has one. |
| `items[].data.annotations[].place.title / items[].data.annotations[].place.poiid` | Name and ID of the place tagged on the post. The `type` next to them is `checkin` in the sample. |
| `items[].data.analysis_extra` | Pipe-separated string of key:value pairs. It includes `ouid`, the user ID of the account that owns the timeline. |
| `items[].itemExt.anchorId / items[].itemExt.extraItemId` | ID of the feed entry. It joins the timeline container ID and the post ID with `_-_`. |
| `moreInfo.params.page / moreInfo.params.count / moreInfo.params.max_id` | Paging values for the next request. In the sample, `page` is 2 and `count` is 20. |
| `moreInfo.pagingType` | Paging style the response reports. The sample returns `cursor`. |

### Notes

- The first item in `items` is a `card` with the filter and total post count. Posts are the items where `category` is `feed`.
- Set `page` to get later pages. It starts at 1. `moreInfo.params.page` shows the next page number.
- To filter by month, set `filter_type` to `month` and pass `month` as `YYYYMMDD`. `month` is ignored for other filter types.
- Use [Weibo User Profile Information](/apis/weibo/app/user-info) for the account's profile, and [Weibo Post Comments (App)](/apis/weibo/app/status-comments) for comments on a post.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [AI Smart Search](/apis/weibo/app/ai-smart-search): App Ai Smart Search provides a focused capability for applications, automation, and data workflows.
- [Get home recommend feed](/apis/weibo/app/home-recommend-feed): Get the home recommend feed from Weibo.
- [Get hot search](/apis/weibo/app/hot-search): Get Weibo hot search ranking, supports multiple categories.

---
Machine-readable: [`catalog/models/weibo/app/user-timeline.json`](../../../../catalog/models/weibo/app/user-timeline.json) · Store page: https://www.sandbase.ai/model/weibo/app/user-timeline
