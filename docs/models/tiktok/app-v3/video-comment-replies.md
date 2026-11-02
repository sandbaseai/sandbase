# TikTok Video Comment Replies API: pricing, parameters and code examples

`tiktok/app-v3/video-comment-replies` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns reply threads for a specific comment on a TikTok video. Queries rely on the video identifier and comment identifier, with support for cursor-based pagination.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/video-comment-replies", "comment_id": "7327061675382260482", "item_id": "7326156045968067873"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/video-comment-replies', {'comment_id': '7327061675382260482', 'item_id': '7326156045968067873'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/video-comment-replies", {
  "comment_id": "7327061675382260482",
  "item_id": "7326156045968067873"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/video-comment-replies", sandbase.Params{
	"comment_id": "7327061675382260482",
	"item_id": "7326156045968067873",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/video-comment-replies` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number  |
| `cursor` | integer |  | Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response.  |
| `item_id` | string | yes | Video id  |
| `comment_id` | string | yes | Comment id  |

## Details

Retrieve replies to a specific TikTok comment by providing the target video ID in `item_id` and the comment ID in `comment_id`.

### Use cases

- Read nested comment threads under a specific TikTok video comment.
- Monitor user conversations and feedback on video discussions.
- Ingest comment reply interactions for sentiment analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/video-comment-replies" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"comment_id": "<comment_id>", "item_id": "<item_id>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `item_id` | string | Yes | Video id |
| `comment_id` | string | Yes | Comment id |
| `count` | integer | No | Number |
| `cursor` | integer | No | Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. |

### Notes

- Use `cursor` for pagination, passing 0 for the first page and the returned cursor value for subsequent pages.
- Specify `count` to limit the number of replies returned in each response.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok LIVE Status](/model/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/model/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/model/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/video-comment-replies.json`](../../../../catalog/models/tiktok/app-v3/video-comment-replies.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/video-comment-replies
