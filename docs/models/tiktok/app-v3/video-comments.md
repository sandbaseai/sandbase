# TikTok Video Comments (App V3) API: pricing, parameters and code examples

`tiktok/app-v3/video-comments` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns comments for a specific TikTok video using its video ID. Includes comment engagement metrics, timestamps, author details, and supports pagination controls.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/video-comments", "aweme_id": "7350810998023949599"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/video-comments', {'aweme_id': '7350810998023949599'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/video-comments", {
  "aweme_id": "7350810998023949599"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/video-comments", sandbase.Params{
	"aweme_id": "7350810998023949599",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/video-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number default `20` |
| `cursor` | integer |  | Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. default `0` |
| `aweme_id` | string | yes | Video id  |

## Details

Retrieve user comments for a single video by providing the target video identifier in `aweme_id`. Supports paginating through comment lists via `cursor` and `count`.

### Use cases

- Analyze audience reactions and engagement on specific TikTok videos.
- Monitor community discussions and sentiment around branded content.
- Extract top comments and interaction metrics for post performance reports.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/video-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"aweme_id": "7350810998023949599"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `aweme_id` | string | Yes | Video id |
| `count` | integer | No | Number |
| `cursor` | integer | No | Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "comments": [
    {
      "author_pin": false,
      "aweme_id": "7350810998023949599",
      "create_time": 1711502748,
      "digg_count": 28839,
      "fold_status": -1,
      "reply_id": "0",
      "reply_to_reply_id": "0",
      "seeking_help_model_type": 0,
      "sort_tags": "{\"fine_sort_search_queue\":1,\"rough_sort_main_queue\":1,\"top_list\":1}",
      "status": 1,
      "share_info": {
        "desc": "୧ ׅ۫ay me𓍯’s comment: why are your eyes bleeding",
        "title": "im so sick of being tired im so tired of being sick",
        "url": "https://www.tiktok.com/@jennmelon/video/7350810998023949599?_d=eg2364aic36c1d&_r…"
      },
      "user": {
        "apple_account": 0,
        "authority_status": 0,
        "aweme_count": 0,
        "comment_filter_status": 0,
        "create_time": 0,
        "favoriting_count": 0
      }
    }
  ]
}
```

### Notes

- Set `cursor` to 0 for the first page, then use the cursor value returned in the response for subsequent pages.
- Use `aweme_id` to specify the target video ID.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok LIVE Status](/apis/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/apis/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/apis/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/video-comments.json`](../../../../catalog/models/tiktok/app-v3/video-comments.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/video-comments
