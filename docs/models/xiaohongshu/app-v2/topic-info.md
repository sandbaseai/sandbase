# Xiaohongshu (RED) Topic Details API: pricing, parameters and code examples

`xiaohongshu/app-v2/topic-info` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns topic page details such as topic name, view count, discussion count, and share info by topic page ID. Supports passing optional context like source note ID.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/app-v2/topic-info", "note_id": "", "page_id": "5c1cc866febed9000184b7c1", "source": "normal"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/app-v2/topic-info', {'note_id': '', 'page_id': '5c1cc866febed9000184b7c1', 'source': 'normal'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/app-v2/topic-info", {
  "note_id": "",
  "page_id": "5c1cc866febed9000184b7c1",
  "source": "normal"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/app-v2/topic-info", sandbase.Params{
	"note_id": "",
	"page_id": "5c1cc866febed9000184b7c1",
	"source": "normal",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/app-v2/topic-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `source` | string |  | Source, default "normal" default `"normal"` |
| `note_id` | string |  | Source note ID, pass when jumping from note to topic (optional) default `""` |
| `page_id` | string | yes | Topic page ID (required), e.g. "5c1cc866febed9000184b7c1"  |

## Details

Returns details for one Xiaohongshu (RED) topic page, including its name, view count, discussion count, share card and a few sample users. It needs the topic page ID as `page_id`. You can also pass `note_id` and `source` as context.

### Use cases

- Read the view and discussion totals for a hashtag topic such as `新年` to compare how much attention topics get.
- Collect the share title, link and cover image of a topic to build a link preview.
- Store the topic name with its `topic_id` to match topic pages to your own tracking list.
- Check which sort tabs a topic page offers before you fetch its notes.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/app-v2/topic-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"page_id": "5c1cc866febed9000184b7c1"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `page_id` | string | Yes | Topic page ID (required), e.g. "5c1cc866febed9000184b7c1" |
| `note_id` | string | No | Source note ID, pass when jumping from note to topic (optional) |
| `source` | string | No | Source, default "normal" |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "business_type": 0,
    "custom_tabs": [],
    "feedShowType": "2",
    "followed": false,
    "inside_deeplink": "xhsdiscover://topic/v2/5c1cc866febed9000184b7c1",
    "middle_lane_list": [],
    "moduleId": "0",
    "page_id": "5c1cc866febed9000184b7c1",
    "page_info": {
      "banner": "",
      "desc": "",
      "discussNum": 2330307,
      "discuss_comment_num": 36351380,
      "discuss_comment_num_text": "999万+",
      "name": "新年",
      "topic_translate_info": {
        "translate_type": 2
      },
      "viewNum": 7705118072,
      "view_num_text": "999万+"
    },
    "page_type": "topic",
    "post_deeplink": "xhsdiscover://post_new_note?page=%7B%22page_type%22%3A%22albums%22%7D&source=%7B…",
    "post_option": {
      "default_link": "xhsdiscover://post_new_note?source=%7B%22type%22%3A%22pages%22%2C%22ids%22%3A%22…",
      "func_items": [
        {
          "link": "xhsdiscover://post_new_note?source=%7B%22type%22%3A%22pages%22%2C%22ids%22%3A%22…",
          "title": "Choose from Album"
        }
      ]
    }
  },
  "debug_id": "762109a8",
  "debug_info": "gAAAAABq6ZFtotwmW7U6uFyOoDDeZr9ax0lIvRIbTulQ1cieFB1UjIpDjpxrjvCyh0iXAeX_Jfs5blmq…",
  "msg": "成功",
  "success": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.page_info.name` | Topic name, for example `新年`. |
| `data.page_info.viewNum / data.page_info.view_num_text` | Total view count as a number, and the same count as a short display text such as `999万+`. |
| `data.page_info.discussNum` | Number of discussions on the topic, as a number. |
| `data.page_info.discuss_comment_num / data.page_info.discuss_comment_num_text` | Discussion comment count as a number, and as a short display text. |
| `data.page_id / data.topic_id / data.topic_long_id` | Identifiers of the topic. `page_id` echoes the requested topic page ID. `topic_id` and `topic_long_id` are two other ID forms for the same topic. |
| `data.share_info.title / data.share_info.desc / data.share_info.link` | Title, description text and web link used when the topic is shared. |
| `data.share_info.image / data.share_info.outside_image` | Image URLs for the share card inside the app and for sharing outside the app. |
| `data.tabs[].name / data.tabs[].value` | Sort tabs on the topic page. `value` is `trend` for Hottest and `time` for Latest. |
| `data.users[].id / data.users[].nickname / data.users[].image` | User ID, display name and avatar URL of users shown on the topic page. |
| `data.inside_deeplink` | App deeplink that opens the topic page in the Xiaohongshu app. |

### Notes

- `page_id` is a 24-character hex string, such as `5c1cc866febed9000184b7c1`. The deeplink in `data.inside_deeplink` also contains it.
- Pass `note_id` only when you reach the topic from a note. It is optional.
- To list the notes under a topic, call [Xiaohongshu (RED) Topic Feed](/apis/xiaohongshu/app-v2/topic-feed).
- Counts such as `viewNum` are plain numbers. The `_text` fields are shortened display strings.

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Xiaohongshu (RED) Creator Hot Inspiration Feed](/apis/xiaohongshu/app-v2/creator-hot-inspiration-feed): Retrieves creator center hot inspiration feed items with topic titles, popularity scores, and deeplinks.
- [Xiaohongshu (RED) Inspiration Feed](/apis/xiaohongshu/app-v2/creator-inspiration-feed): Returns recommended inspiration feed items and trending topics from Xiaohongshu (RED).
- [Xiaohongshu (RED) Image Note Details](/apis/xiaohongshu/app-v2/image-note-detail): Returns detailed information for a Xiaohongshu image note.

---
Machine-readable: [`catalog/models/xiaohongshu/app-v2/topic-info.json`](../../../../catalog/models/xiaohongshu/app-v2/topic-info.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/app-v2/topic-info
