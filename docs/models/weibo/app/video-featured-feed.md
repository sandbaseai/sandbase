# Weibo Featured Video Feed API: pricing, parameters and code examples

`weibo/app/video-featured-feed` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns featured video feed cards from the Weibo video section. Supports pagination using page numbers to browse recommended multimedia posts.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/app/video-featured-feed"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/app/video-featured-feed', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/app/video-featured-feed", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/app/video-featured-feed", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/weibo/app/video-featured-feed` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` |  |  | Page number, don't pass for first page, pass "2" for second page, and so on  |

## Details

Returns a page of featured video cards from the Weibo video section. The `page` input is optional, and you can leave it out to get the first page.

### Use cases

- Collect the post IDs of featured Weibo videos to feed into a video or post detail lookup.
- Track which cluster names appear in the featured video feed over time.
- Build a list of author user IDs whose posts show up in the featured feed.
- Page through the feed to sample the recommended video posts shown to Weibo app users.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/app/video-featured-feed" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `page` | string | No | Page number, don't pass for first page, pass "2" for second page, and so on |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "config": "{}",
  "items": [
    {
      "category": "card",
      "data": {
        "actionlog": {
          "act_code": "8257",
          "act_type": 1,
          "ext": "index:1|mid:5283691653236513|miduid:7236453246|page:1|recom_code:null|hot_reques…",
          "fid": "231643_11_5030",
          "uicode": "10000838"
        },
        "analysis_extra": "index:1|mid:5283691653236513|miduid:7236453246|page:1|recom_code:null|hot_reques…",
        "auto_play_config": {
          "condition": {
            "type": "best_match"
          },
          "group_id": "",
          "play_rule": "step"
        },
        "card_type": 231,
        "grid_group": 0,
        "hide_flag": 0,
        "icon": "https://d.sinaimg.cn/prd/103/2043/2026/04/02/jingxuanbikan.png",
        "image_scale": 0.0
      },
      "itemExt": {
        "anchorId": "5283691653236513"
      },
      "style": {
        "grid": true,
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
  "moreInfo": {
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
  "pageData": "{}",
  "pageRefresh": "{}",
  "pageTabBar": "{}",
  "refreshInfo": "{}"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `items[].category` | Type of the feed entry. All entries in the sample are `card`. |
| `items[].itemExt.anchorId` | ID of the post behind the card. It matches the `mid` value in the `actionlog.ext` string. |
| `items[].data.actionlog.ext / items[].data.analysis_extra` | Pipe-separated tracking string. It holds the card position (`index`), post ID (`mid`), author user ID (`miduid`), `page`, `cluster_id` and `cluster_name`. |
| `items[].data.card_type` | Numeric card type. The sample cards all use `231`. |
| `items[].data.icon` | URL of the badge image shown on the card. |
| `items[].data.auto_play_config` | Autoplay settings for the card, including the `play_rule` and the `condition.type`. |
| `items[].data.hide_flag` | Flag for hiding the card. It is `0` in the sample. |
| `moreInfo.params.page` | Page number to request next. It is `2` after the first page. |
| `moreInfo.params.count / moreInfo.params.max_id` | Page size (`20` in the sample) and cursor value (`0` in the sample) for the next request. |
| `moreInfo.pagingType` | Paging style reported by the feed. The sample value is `cursor`. |

### Notes

- Omit `page` for the first page. Pass `"2"` for the second page, and so on.
- The cards carry only IDs and tracking data. Take the post ID from `items[].itemExt.anchorId` and call [Weibo Video Detail](/apis/weibo/app/video-detail) or [Weibo Post Detail (App)](/apis/weibo/app/status-detail) for the content.
- The author user ID is the `miduid` value inside `items[].data.actionlog.ext`. Pass it to [Weibo User Profile Information](/apis/weibo/app/user-info) to look up the author.
- The `config`, `loadedInfo`, `pageData`, `pageRefresh`, `pageTabBar` and `refreshInfo` keys return the string `{}` in the sample.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Weibo App AI Smart Search](/apis/weibo/app/ai-smart-search): Returns AI smart search channel results and feed metadata from Weibo for a specified keyword query, with optional page-based pagination.
- [Weibo Home Recommend Feed](/apis/weibo/app/home-recommend-feed): Returns recommended feed items from the Weibo app homepage, with options to paginate and specify the number of items per request.
- [Weibo Hot Search Rankings](/apis/weibo/app/hot-search): Returns current Weibo hot search rankings across various categories.

---
Machine-readable: [`catalog/models/weibo/app/video-featured-feed.json`](../../../../catalog/models/weibo/app/video-featured-feed.json) · Store page: https://www.sandbase.ai/model/weibo/app/video-featured-feed
