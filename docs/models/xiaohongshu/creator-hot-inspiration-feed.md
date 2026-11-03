# Xiaohongshu Hot Inspiration Feed API: pricing, parameters and code examples

`xiaohongshu/creator-hot-inspiration-feed` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get the Xiaohongshu (RedNote) creator center hot inspiration feed with cursor pagination. Use it to discover inspiration for content planning and explore further pages of creative ideas.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/creator-hot-inspiration-feed"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/creator-hot-inspiration-feed', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/creator-hot-inspiration-feed", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/creator-hot-inspiration-feed", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/xiaohongshu/creator-hot-inspiration-feed` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Leave empty for the first request. For the next page, pass the cursor value returned by the previous response.  |

## Details

Returns a page of the Xiaohongshu (RedNote) creator center hot inspiration feed. Each item is a trending topic with a title, cover image, popularity score and a deeplink for starting a new note. The only input is an optional `cursor` for paging.

### Use cases

- Pull the current trending topics to plan which subjects to post about.
- Track `score` values across repeated calls to see which hot topics gain attention.
- Collect cover images and titles of hot topics for a content idea board.
- Page through the feed with `cursor` to build a longer list of inspiration items.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/creator-hot-inspiration-feed" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | string | No | Leave empty for the first request. For the next page, pass the cursor value returned by the previous response. |

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
  "debug_id": "1f2b3982",
  "debug_info": "gAAAAABq6ZFwRZHE6PXzFAzcwFsTTt9PMmFkDzoFXtoZQtjOZZKEken4dPtnqL71RotdN8wquXDoFjiZ…",
  "msg": "成功",
  "success": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.items[].title` | Title of the hot topic, as shown in the feed. |
| `data.items[].score` | Numeric popularity value of the item. Items appear in descending order of this value in the sample. |
| `data.items[].score_text` | Display text for the score, such as `2458.7万人在看` (about 24.58 million people watching). |
| `data.items[].hot_id` | ID of the hot topic, returned as a string. |
| `data.items[].id` | Numeric ID of the feed item. |
| `data.items[].type` | Item type label. The sample items all have the value `Hot`. |
| `data.items[].cover` | URL of the cover image for the item. |
| `data.items[].deeplink` | App link (`xhsdiscover://post_new_note`) that opens the new-note editor with text prefilled for this topic. It only works inside the Xiaohongshu app. |
| `data.cursor` | Cursor value to pass as `cursor` in the next request to get the following page. |
| `data.end_flag` | Boolean that is `false` when the response is not the last page. |

### Notes

- Leave `cursor` empty on the first request. For the next page, send the `data.cursor` value from the previous response.
- Check `data.end_flag` to see whether the feed has ended.
- For a related feed, see [Xiaohongshu (RED) Creator Hot Inspiration Feed](/apis/xiaohongshu/app-v2/creator-hot-inspiration-feed) or [Xiaohongshu (RED) Inspiration Feed](/apis/xiaohongshu/app-v2/creator-inspiration-feed).
- To see what people search for, call [Xiaohongshu Hot Search](/apis/xiaohongshu/hot-search).

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/creator-hot-inspiration-feed.json`](../../../catalog/models/xiaohongshu/creator-hot-inspiration-feed.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/creator-hot-inspiration-feed
