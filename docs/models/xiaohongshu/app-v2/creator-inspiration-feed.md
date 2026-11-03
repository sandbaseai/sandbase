# Xiaohongshu (RED) Inspiration Feed API: pricing, parameters and code examples

`xiaohongshu/app-v2/creator-inspiration-feed` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns recommended inspiration feed items and trending topics from Xiaohongshu (RED). Supports cursor-based pagination and filtering by `tab`.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/app-v2/creator-inspiration-feed", "cursor": "", "source": "creator_center", "tab": 0}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/app-v2/creator-inspiration-feed', {'cursor': '', 'source': 'creator_center', 'tab': 0})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/app-v2/creator-inspiration-feed", {
  "cursor": "",
  "source": "creator_center",
  "tab": 0
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/app-v2/creator-inspiration-feed", sandbase.Params{
	"cursor": "",
	"source": "creator_center",
	"tab": 0,
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/app-v2/creator-inspiration-feed` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `tab` | integer |  | Tab type, default 0 default `0` |
| `cursor` | string |  | Pagination cursor, leave empty for first request, pass cursor value from previous response (e.g. "r_1", "r_2"...) default `""` |
| `source` | string |  | Source, default "creator_center" default `"creator_center"` |

## Details

Returns a page of recommended inspiration topics from the Xiaohongshu (RED) creator center. Each item has a topic name, a post count, images and deeplinks. All inputs are optional, so an empty request returns the first page.

### Use cases

- Pull topic names and post counts to see which prompts creators are using most.
- Collect `ins_id` values and deeplinks to build a content planning list.
- Page through the feed with `cursor` to build a larger set of topic ideas.
- Compare the feed across `tab` values to see which topics each tab shows.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/app-v2/creator-inspiration-feed" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | string | No | Pagination cursor, leave empty for first request, pass cursor value from previous response (e.g. "r_1", "r_2"...) |
| `source` | string | No | Source, default "creator_center" |
| `tab` | integer | No | Tab type, default 0 |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "cursor": "r_1",
    "end_flag": false,
    "inspirations": [
      {
        "btn_text": "Post Now",
        "cnt_desc": "7.6M Posted",
        "dark_icon": "https://fe-platform.xhscdn.com/platform/104101l031jm5pgtrj006g9kud0274000000000d…",
        "detail_deeplink": "xhsdiscover://nns_detail?type=inspiration&id=236297&trackId=236297&popupstyle=1&…",
        "direction": 0,
        "favor_status": 0,
        "icon": "https://fe-platform.xhscdn.com/platform/104101l031jm747g3j406g9kud0274000000000d…",
        "image": "http://ci.xiaohongshu.com/e8e4c657-5d9d-3833-84e0-c33c8f987d04?imageView2/2/w/10…",
        "ins_id": 236297,
        "ins_type": "inspiration",
        "name": "生活需要分享欲",
        "post_deeplink": "xhsdiscover://post_new_note?config=%7B%22is_from_popup%22%3Afalse%2C%22post_succ…"
      }
    ]
  },
  "debug_id": "cdf6bec5",
  "debug_info": "gAAAAABq6ZFlukGKSeHYNCq0D0juZfl3OLE1MlwrypXt_ahnRNzXUCnh-YSZv5irWphyGVw_ys9QN5-C…",
  "msg": "成功",
  "success": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.inspirations[].name` | Topic title shown to creators, in Chinese in the sample. |
| `data.inspirations[].ins_id` | Numeric ID of the inspiration item. |
| `data.inspirations[].cnt_desc` | Display text for how many posts use the topic, for example `7.6M Posted`. |
| `data.inspirations[].type / data.inspirations[].ins_type` | Kind of item. The sample shows `Topic` for `type` and `inspiration` for `ins_type`. |
| `data.inspirations[].image` | Cover image URL for the topic. |
| `data.inspirations[].icon / data.inspirations[].dark_icon` | Icon URLs for the topic. `dark_icon` is the dark mode version. |
| `data.inspirations[].detail_deeplink` | App deeplink that opens the inspiration detail page. The `id` inside it matches `ins_id`. |
| `data.inspirations[].post_deeplink` | App deeplink that opens the new note editor for this topic. |
| `data.inspirations[].btn_text` | Label of the action button, `Post Now` in the sample. |
| `data.cursor / data.end_flag` | `cursor` is the value to send for the next page. `end_flag` is `false` when more items are available. |

### Notes

- Leave `cursor` empty on the first call. Then pass `data.cursor` from the previous response, for example `r_1`.
- `source` defaults to `creator_center` and `tab` defaults to `0`.
- Deeplinks use the `xhsdiscover://` scheme and work in the Xiaohongshu app, not in a browser.
- For the posts under a topic, try [Xiaohongshu (RED) Topic Feed](/apis/xiaohongshu/app-v2/topic-feed) or [Xiaohongshu (RED) Topic Details](/apis/xiaohongshu/app-v2/topic-info).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Xiaohongshu (RED) Creator Hot Inspiration Feed](/apis/xiaohongshu/app-v2/creator-hot-inspiration-feed): Retrieves creator center hot inspiration feed items with topic titles, popularity scores, and deeplinks.
- [Xiaohongshu (RED) Image Note Details](/apis/xiaohongshu/app-v2/image-note-detail): Returns detailed information for a Xiaohongshu image note.
- [Xiaohongshu (RED) Note Comments](/apis/xiaohongshu/app-v2/note-comments): Get the comments on a Xiaohongshu note: comment text, time, likes, reply counts and location, with sorting and cursor pagination.

---
Machine-readable: [`catalog/models/xiaohongshu/app-v2/creator-inspiration-feed.json`](../../../../catalog/models/xiaohongshu/app-v2/creator-inspiration-feed.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/app-v2/creator-inspiration-feed
