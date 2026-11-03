# Xiaohongshu (RED) Creator Hot Inspiration Feed API: pricing, parameters and code examples

`xiaohongshu/app-v2/creator-hot-inspiration-feed` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Retrieves creator center hot inspiration feed items with topic titles, popularity scores, and deeplinks. Supports pagination using a cursor parameter.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/app-v2/creator-hot-inspiration-feed", "cursor": "股票"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/app-v2/creator-hot-inspiration-feed', {'cursor': '股票'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/app-v2/creator-hot-inspiration-feed", {
  "cursor": "股票"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/app-v2/creator-hot-inspiration-feed", sandbase.Params{
	"cursor": "股票",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/app-v2/creator-hot-inspiration-feed` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Pagination cursor, leave empty for first request, pass cursor value from previous response (e.g. "1", "2"...) default `""` |

## Details

Returns a list of hot topic items from the Xiaohongshu creator center inspiration feed. Each item has a title, a popularity score, a cover image and a deeplink that opens the note editor. The only input is an optional `cursor` for paging.

### Use cases

- Pull the current hot topics to plan which subjects to post about.
- Rank topics by `score` to see which ones draw the most viewers right now.
- Store `hot_id` values over time to track how long a topic stays on the feed.
- Collect `deeplink` values to open the note editor with a topic already filled in.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/app-v2/creator-hot-inspiration-feed" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | string | No | Pagination cursor, leave empty for first request, pass cursor value from previous response (e.g. "1", "2"...) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "cursor": "1",
    "end_flag": false,
    "items": [
      {
        "cover": "http://ci.xiaohongshu.com/spectrum/1040g34o3272om05f6e105n4sr354lit78622ql0?imag…",
        "deeplink": "xhsdiscover://post_new_note?attach=%7B%22note_text_v2%22%3A%7B%22content%22%3A%2…",
        "hot_id": "3996295",
        "id": 57994307,
        "score": 24586676,
        "score_text": "2458.7万人在看",
        "title": "恋与深空完美仿生人男友上线",
        "type": "Hot"
      }
    ]
  },
  "debug_id": "eababa7b",
  "debug_info": "gAAAAABq6ZFkRQEbcBCctDAMK3J0oEyPAgVrZj_bFHxE0tt6kYeBkrcWvdZVXOD8ziTED6bBPm7B7iof…",
  "msg": "成功",
  "success": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.items[].title` | Topic title shown in the feed, in Chinese. |
| `data.items[].score` | Numeric popularity score for the topic. Higher values mean more people are watching. |
| `data.items[].score_text` | Display version of the popularity, for example `2458.7万人在看`. |
| `data.items[].hot_id / data.items[].id` | Identifiers for the hot topic and for the feed item. `hot_id` is a string and `id` is a number. |
| `data.items[].deeplink` | A `xhsdiscover://post_new_note` link with the topic text URL-encoded in the `attach` parameter. It opens the new note screen in the app. |
| `data.items[].cover` | URL of the cover image for the topic. |
| `data.items[].type` | Item type. The sample items all return `Hot`. |
| `data.cursor` | Cursor value returned with this page. Pass it as `cursor` to request the next page. |
| `data.end_flag` | Boolean. It is `false` while the response is not marked as the last page. |

### Notes

- Leave `cursor` empty on the first call. For later pages, send the `data.cursor` value from the previous response, such as `1` or `2`.
- Check `data.end_flag` to see whether the feed has ended.
- `deeplink` values only work inside the Xiaohongshu app. Decode the `attach` parameter to read the topic text.
- For a different set of suggested topics, call [Xiaohongshu (RED) Inspiration Feed](/apis/xiaohongshu/app-v2/creator-inspiration-feed).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Xiaohongshu (RED) Inspiration Feed](/apis/xiaohongshu/app-v2/creator-inspiration-feed): Returns recommended inspiration feed items and trending topics from Xiaohongshu (RED).
- [Xiaohongshu (RED) Image Note Details](/apis/xiaohongshu/app-v2/image-note-detail): Returns detailed information for a Xiaohongshu image note.
- [Xiaohongshu (RED) Note Comments](/apis/xiaohongshu/app-v2/note-comments): Get the comments on a Xiaohongshu note: comment text, time, likes, reply counts and location, with sorting and cursor pagination.

---
Machine-readable: [`catalog/models/xiaohongshu/app-v2/creator-hot-inspiration-feed.json`](../../../../catalog/models/xiaohongshu/app-v2/creator-hot-inspiration-feed.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/app-v2/creator-hot-inspiration-feed
