# Weibo Post Reposts API: pricing, parameters and code examples

`weibo/app/status-reposts` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of reposts for a specified Weibo post or video. Output includes repost details and engagement metrics with pagination support.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/app/status-reposts", "max_id": null, "status_id": "5016922058656962"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/app/status-reposts', {'max_id': None, 'status_id': '5016922058656962'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/app/status-reposts", {
  "max_id": null,
  "status_id": "5016922058656962"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/app/status-reposts", sandbase.Params{
	"max_id": nil,
	"status_id": "5016922058656962",
})
```

Same call via the path form: `POST /v1/api/weibo/app/status-reposts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `max_id` |  |  | Pagination cursor, don't pass for first request, use returned max_id for subsequent requests  |
| `status_id` | string | yes | Post ID or Video ID (required)  |

## Details

Returns a list of reposts for one Weibo post or video. It needs the `status_id` of the original post, and returns each repost as an item with engagement counts and display settings, plus cursor paging info.

### Use cases

- Count how many reposts a Weibo post has received and inspect each repost entry.
- Page through every repost of a post to map how the post spread.
- Check the like counts on reposts to find reposts that drew engagement.
- Group reposts by the `appid` value to see which client apps people used to share.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/app/status-reposts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"status_id": "5016922058656962"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `status_id` | string | Yes | Post ID or Video ID (required) |
| `max_id` | string | No | Pagination cursor, don't pass for first request, use returned max_id for subsequent requests |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "config": "{}",
  "items": [
    {
      "category": "detail",
      "data": {
        "ad_marked": false,
        "analysis_extra": "mblog_rt_mid:5016922058656962",
        "annotations": [
          {
            "mapi_request": true
          }
        ],
        "appid": 2830606,
        "attitudes_animation": 1,
        "attitudes_count": 0,
        "attitudes_status": 0,
        "bottom_bar_dyna": {
          "cell_item": {
            "category": "dynamic",
            "itemExt": {
              "bizType": "common"
            },
            "type": "detailBottomBarDefaultButtonStyle"
          }
        }
      },
      "type": "forward"
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
      "lastAdInterval": 16,
      "max_id_type": 0,
      "page": 2
    }
  },
  "pageData": "{}"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `items[]` | One entry per repost. Each entry has a `category`, a `type` and a `data` object. |
| `items[].type` | Kind of entry. The value `forward` marks a repost. |
| `items[].category` | Entry group. The value `detail` appears for repost entries. |
| `items[].data.attitudes_count` | Number of likes on the repost. |
| `items[].data.analysis_extra` | Tracking string that includes `mblog_rt_mid:` followed by the ID of the original post. |
| `items[].data.appid` | Numeric ID of the app used to create the repost. |
| `items[].data.ad_marked` | Boolean that shows whether the repost is marked as an ad. |
| `moreInfo.pagingType` | Paging style. The value `cursor` means pages follow a cursor. |
| `moreInfo.params.count` | Page size hint, shown as `20` in this response. |
| `moreInfo.params.page` | Page number the server reports for the next load. |

### Notes

- Take `status_id` from a post or video ID, for example the `mblog_rt_mid` value in a response. You can also get it from [Weibo Post Detail (App)](/apis/weibo/app/status-detail).
- Leave `max_id` out on the first request. For later pages, pass the returned `max_id`.
- The `data` object of each item holds the full repost record. The trimmed example shows only a few of its keys.
- To read replies on the original post instead, call [Weibo Post Comments (App)](/apis/weibo/app/status-comments).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Weibo App AI Smart Search](/apis/weibo/app/ai-smart-search): Returns AI smart search channel results and feed metadata from Weibo for a specified keyword query, with optional page-based pagination.
- [Weibo Home Recommend Feed](/apis/weibo/app/home-recommend-feed): Returns recommended feed items from the Weibo app homepage, with options to paginate and specify the number of items per request.
- [Weibo Hot Search Rankings](/apis/weibo/app/hot-search): Returns current Weibo hot search rankings across various categories.

---
Machine-readable: [`catalog/models/weibo/app/status-reposts.json`](../../../../catalog/models/weibo/app/status-reposts.json) · Store page: https://www.sandbase.ai/model/weibo/app/status-reposts
