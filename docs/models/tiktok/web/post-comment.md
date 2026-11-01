# TikTok Video Comments (Web)

`tiktok/web/post-comment` · api · TikTok

Returns user comments for a specific TikTok video using its video ID. Supports cursor-based pagination and optional region filtering.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/post-comment", "aweme_id": "7350810998023949599"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/post-comment', {'aweme_id': '7350810998023949599'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/post-comment", {
  "aweme_id": "7350810998023949599"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/post-comment", sandbase.Params{
	"aweme_id": "7350810998023949599",
})
```

Same call via the path form: `POST /v1/api/tiktok/web/post-comment` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number per page  |
| `cursor` | integer |  | Page cursor  |
| `aweme_id` | string | yes | Video id  |
| `current_region` | string |  | Current region, default is empty.  |

## Details

Query comments from a TikTok post by providing the target video identifier via `aweme_id`. Paginate through results using `cursor` and `count`.

### Use cases

- Analyze user engagement and feedback on specific video posts.
- Track popular responses and like counts on video threads.
- Collect comment histories for sentiment analysis studies.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/post-comment" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"aweme_id": "7350810998023949599"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `aweme_id` | string | Yes | Video id |
| `count` | integer | No | Number per page |
| `cursor` | integer | No | Page cursor |
| `current_region` | string | No | Current region, default is empty. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "comments": [
    {
      "author_pin": false,
      "aweme_id": "7350810998023949599",
      "create_time": 1711502748,
      "digg_count": 28860,
      "fold_status": -1,
      "reply_id": "0",
      "reply_to_reply_id": "0",
      "seeking_help_model_type": 0,
      "sort_tags": "{\"fine_sort_search_queue\":1,\"rough_sort_main_queue\":1,\"top_list\":1}",
      "status": 1,
      "share_info": {
        "desc": "୧ ׅ۫ay me𓍯’s comment: why are your eyes bleeding",
        "title": "im so sick of being tired im so tired of being sick",
        "url": "https://m.tiktok.com/v/7350810998023949599.html?_d=f0ja0akic34cb9&comment_author…"
      },
      "user": {
        "nickname": "<user>",
        "unique_id": "<user>"
      }
    }
  ]
}
```

### Notes

- Pass the video identifier to `aweme_id`.
- Control pagination using `cursor` and `count`.
- Use `current_region` to specify an optional regional context.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/model/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/model/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/model/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/post-comment.json`](../../../../catalog/models/tiktok/web/post-comment.json) · Store page: https://www.sandbase.ai/model/tiktok/web/post-comment
