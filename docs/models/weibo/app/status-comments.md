# Weibo Post Comments (App) API: pricing, parameters and code examples

`weibo/app/status-comments` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the first-level comments for a designated post or video on Weibo. Supports sorting options and cursor-based pagination for browsing discussion threads.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/app/status-comments", "max_id": null, "sort_type": "0", "status_id": "5258708168476831"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/app/status-comments', {'max_id': None, 'sort_type': '0', 'status_id': '5258708168476831'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/app/status-comments", {
  "max_id": null,
  "sort_type": "0",
  "status_id": "5258708168476831"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/app/status-comments", sandbase.Params{
	"max_id": nil,
	"sort_type": "0",
	"status_id": "5258708168476831",
})
```

Same call via the path form: `POST /v1/api/weibo/app/status-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `max_id` |  |  | Pagination cursor, don't pass for first request, use returned max_id for subsequent requests  |
| `sort_type` | string |  | Comment sort type default `"0"` |
| `status_id` | string | yes | Post ID or Video ID (required)  |

## Details

Returns the first-level comments under a Weibo post or video, along with a pagination cursor. It needs the post or video ID as `status_id`.

### Use cases

- Collect the top-level comments under a Weibo post to review how readers respond.
- Page through a long comment thread with the returned `max_id` cursor.
- Read the comment timestamps and floor numbers to see when a discussion was active.
- Check the comment count and author tags in `analysis_extra` for a quick per-comment summary.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/app/status-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"status_id": "5258708168476831"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `status_id` | string | Yes | Post ID or Video ID (required) |
| `max_id` | string | No | Pagination cursor, don't pass for first request, use returned max_id for subsequent requests |
| `sort_type` | string | No | Comment sort type |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "config": "{}",
  "items": [
    {
      "category": "detail",
      "data": {
        "tip_biz_type": 0,
        "tip_icon": "https://d.sinaimg.cn/prd/100/1985/2025/09/24/icon.png",
        "tip_icon_dark": "https://d.sinaimg.cn/prd/100/1985/2025/09/24/icon_dark.png",
        "tip_msg": "查看我的铁粉关系 查看详情",
        "tip_scheme": "sinaweibo://cardlist?containerid=231093_-_bigfans&extparam=7480401147",
        "tip_state": 0,
        "tip_struct": [
          {
            "color": "#507DAF",
            "color_dark": "#6290C3",
            "title": "查看详情"
          }
        ],
        "tip_type": 3
      },
      "type": "comment_header_tip"
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
      "lastAdInterval": 10,
      "max_id": 138889559850779,
      "max_id_type": 0,
      "recommend_max_id": 0,
      "recommend_page": 0
    }
  },
  "pageData": "{}"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `items[]` | List of cards on the page. The first card can be a header tip and the rest are comments. Check `type` to tell them apart. |
| `items[].type` | Card kind. `comment` marks a comment card and `comment_header_tip` marks a notice shown above the comments. |
| `items[].data.created_at` | Time the comment was posted, as text such as `Sun Jan 25 16:55:24 +0800 2026`. |
| `items[].data.floor_number` | Floor number of the comment in the thread. |
| `items[].data.analysis_extra` | Pipe-separated text with `author_uid`, `mid` (the post ID), `page`, `index` and `comment_count`. |
| `items[].data.comment_bubble.name / items[].data.comment_bubble.id` | Name and ID of the bubble style attached to the comment, for example `金粉专属`. |
| `items[].data.disable_reply` | Flag for whether replies are turned off for this comment. `0` is the value in this response. |
| `moreInfo.params.max_id` | Cursor for the next page. Pass it as `max_id` in the next request. |
| `moreInfo.params.count` | Number of items per page, `20` in this response. |
| `moreInfo.pagingType` | Paging style. The value `cursor` means pages are fetched with a cursor. |

### Notes

- Leave out `max_id` on the first call. For later pages, copy the value from `moreInfo.params.max_id`.
- `status_id` is the numeric post or video ID, such as `5258708168476831`. It also appears as `mid` inside `analysis_extra`.
- The response mixes card types in `items`. Filter on `type` equal to `comment` to keep only comments.
- To get the post itself, call [Weibo Post Detail (App)](/apis/weibo/app/status-detail).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Weibo App AI Smart Search](/apis/weibo/app/ai-smart-search): Returns AI smart search channel results and feed metadata from Weibo for a specified keyword query, with optional page-based pagination.
- [Weibo Home Recommend Feed](/apis/weibo/app/home-recommend-feed): Returns recommended feed items from the Weibo app homepage, with options to paginate and specify the number of items per request.
- [Weibo Hot Search Rankings](/apis/weibo/app/hot-search): Returns current Weibo hot search rankings across various categories.

---
Machine-readable: [`catalog/models/weibo/app/status-comments.json`](../../../../catalog/models/weibo/app/status-comments.json) · Store page: https://www.sandbase.ai/model/weibo/app/status-comments
