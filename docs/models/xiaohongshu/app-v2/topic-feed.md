# Xiaohongshu (RED) Topic Feed API: pricing, parameters and code examples

`xiaohongshu/app-v2/topic-feed` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns a list of notes listed under a specified topic page on Xiaohongshu (RED). Supports sorting options and cursor pagination using previous response indicators.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/app-v2/topic-feed", "page_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/app-v2/topic-feed', {'page_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/app-v2/topic-feed", {
  "page_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/app-v2/topic-feed", sandbase.Params{
	"page_id": "example",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/app-v2/topic-feed` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sort` | string |  | Sort type  |
| `source` | string |  | Source, default "normal"  |
| `page_id` | string | yes | Topic page ID (required), e.g. "5c1cc866febed9000184b7c1"  |
| `session_id` | string |  | Session ID, keep consistent for pagination  |
| `cursor_score` | string |  | Pagination cursor score, pass last item's cursor_score from previous response  |
| `last_note_ct` | string |  | Last note create time from previous page  |
| `last_note_id` | string |  | Last note ID from previous page  |
| `first_load_time` | string |  | First load timestamp, keep consistent for pagination  |

## Details

Query notes under a specific Xiaohongshu (RED) topic by providing `page_id`. Supports cursor pagination and custom sort options.

### Use cases

- Track posts and community discussions around a specific campaign topic.
- Monitor engagement trends and top-performing notes within a niche hashtag.
- Retrieve recent user content associated with targeted topic feeds.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/app-v2/topic-feed" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"page_id": "5c1cc866febed9000184b7c1"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `page_id` | string | Yes | Topic page ID (required), e.g. "5c1cc866febed9000184b7c1" |
| `sort` | string | No | Sort type |
| `source` | string | No | Source, default "normal" |
| `session_id` | string | No | Session ID, keep consistent for pagination |
| `cursor_score` | string | No | Pagination cursor score, pass last item's cursor_score from previous response |
| `last_note_ct` | string | No | Last note create time from previous page |
| `last_note_id` | string | No | Last note ID from previous page |
| `first_load_time` | string | No | First load timestamp, keep consistent for pagination |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "items": [
      {
        "create_time": 1770546832000,
        "desc": "宝子们！被这盏像素花灯狠狠戳中中式审美了✨ 靛蓝的亭式灯笼带着飞檐，像把江南古亭缩成掌心小物，镂空窗格透着暖黄灯火，周围粉蓝海棠开得像云絮，仿佛能闻到花香里的夜露气～ 使用104…",
        "id": "69886690000000000b010dec",
        "title": "拼豆图纸ℓ像素风“春灯海棠”ℓ国风宫灯",
        "type": "normal",
        "interaction_info": {
          "collect_count": 17331,
          "comment_count": 646,
          "like_count": 15179,
          "share_count": 3032
        },
        "note_time": {
          "create_time": 1770546832,
          "update_time": 1770546833
        },
        "share_info": {
          "content": "宝子们！被这盏像素花灯狠狠戳中中式审美了✨ 靛蓝的亭式灯笼带着飞檐，像把江南古亭缩成掌心小物，镂空窗格透着暖黄灯火，周围",
          "link": "https://www.xiaohongshu.com/discovery/item/69886690000000000b010dec?app_platform…",
          "title": "拼豆图纸ℓ像素风“春灯海棠”ℓ国风宫灯"
        },
        "topic_note_translate_info": {
          "translate_type": 2
        },
        "user": {
          "nickname": "<user>",
          "user_id": "<user>"
        }
      }
    ]
  }
}
```

### Notes

- `page_id` is required to identify the target topic page.
- Cursor pagination uses `cursor_score`, `last_note_id`, and `last_note_ct` from the previous response.
- Maintain consistent values for `session_id` and `first_load_time` across subsequent page calls.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Xiaohongshu (RED) Creator Hot Inspiration Feed](/model/xiaohongshu/app-v2/creator-hot-inspiration-feed): Retrieves creator center hot inspiration feed items with topic titles, popularity scores, and deeplinks.
- [Xiaohongshu (RED) Inspiration Feed](/model/xiaohongshu/app-v2/creator-inspiration-feed): Returns recommended inspiration feed items and trending topics from Xiaohongshu (RED).
- [Xiaohongshu (RED) Image Note Details](/model/xiaohongshu/app-v2/image-note-detail): Returns detailed information for a Xiaohongshu image note.

---
Machine-readable: [`catalog/models/xiaohongshu/app-v2/topic-feed.json`](../../../../catalog/models/xiaohongshu/app-v2/topic-feed.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/app-v2/topic-feed
