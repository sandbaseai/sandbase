# Xiaohongshu (RED) Inspiration Feed API: pricing, parameters and code examples

`xiaohongshu/app-v2/creator-inspiration-feed` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.015 per call (free daily quota) · **Modes:** sync

Returns recommended inspiration feed items and trending topics from Xiaohongshu (RED). Supports cursor-based pagination and filtering by `tab`.

## Pricing

- **$0.015 per call** (USD)
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

Retrieve recommended inspiration topics from Xiaohongshu (RED) using `tab`, `cursor`, and `source` parameters.

### Use cases

- Discover trending topics and content ideas for Xiaohongshu (RED).
- Track popular inspiration feed suggestions across different tabs.
- Collect topic IDs and deeplinks for automated content planning.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/app-v2/creator-inspiration-feed" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `tab` | integer | No | Tab type, default 0 |
| `cursor` | string | No | Pagination cursor, leave empty for first request, pass cursor value from previous response (e.g. "r_1", "r_2"...) |
| `source` | string | No | Source, default "creator_center" |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "inspirations": [
      {
        "btn_text": "Post Now",
        "cnt_desc": "7.1M Posted",
        "detail_deeplink": "xhsdiscover://nns_detail?type=inspiration&id=236297&trackId=236297&popupstyle=1&pageEntra…",
        "favor_status": 0,
        "ins_id": 236297,
        "ins_type": "inspiration",
        "name": "生活需要分享欲",
        "post_deeplink": "xhsdiscover://post_new_note?config=%7B%22is_from_popup%22%3Afalse%2C%22post_success_show_…",
        "type": "Topic"
      }
    ]
  }
}
```

### Notes

- Leave `cursor` empty for the initial request, then pass the cursor string from the previous response for pagination.
- The `tab` parameter defaults to 0.
- The `source` parameter defaults to creator_center.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Xiaohongshu (RED) Creator Hot Inspiration Feed](/model/xiaohongshu/app-v2/creator-hot-inspiration-feed): Retrieves creator center hot inspiration feed items with topic titles, popularity scores, and deeplinks.
- [Xiaohongshu (RED) Image Note Details](/model/xiaohongshu/app-v2/image-note-detail): Returns detailed information for a Xiaohongshu image note.
- [Xiaohongshu (RED) Note Comments](/model/xiaohongshu/app-v2/note-comments): Get the comments on a Xiaohongshu note: comment text, time, likes, reply counts and location, with sorting and cursor pagination.

---
Machine-readable: [`catalog/models/xiaohongshu/app-v2/creator-inspiration-feed.json`](../../../../catalog/models/xiaohongshu/app-v2/creator-inspiration-feed.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/app-v2/creator-inspiration-feed
