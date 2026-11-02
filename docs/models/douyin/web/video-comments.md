# Douyin Video Comments (Web) API: pricing, parameters and code examples

`douyin/web/video-comments` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns comments for a specific Douyin video using its video ID. Supports pagination controls via cursor and item count parameters.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/video-comments", "aweme_id": "7372484719365098803", "count": 20, "cursor": 0}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/video-comments', {'aweme_id': '7372484719365098803', 'count': 20, 'cursor': 0})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/video-comments", {
  "aweme_id": "7372484719365098803",
  "count": 20,
  "cursor": 0
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/video-comments", sandbase.Params{
	"aweme_id": "7372484719365098803",
	"count": 20,
	"cursor": 0,
})
```

Same call via the path form: `POST /v1/api/douyin/web/video-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number default `20` |
| `cursor` | integer |  | Cursor default `0` |
| `aweme_id` | string | yes | Video id  |

## Details

Retrieve comments for a specific Douyin video by providing the target `aweme_id`. Supports pagination using `cursor` and `count` parameters.

### Use cases

- Analyze audience feedback and sentiment on specific video posts.
- Extract top comment interactions and like counts for performance review.
- Monitor user discussions and engagement patterns over time.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/video-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"aweme_id": "7372484719365098803"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `aweme_id` | string | Yes | Video id |
| `count` | integer | No | Number |
| `cursor` | integer | No | Cursor |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "comments": [
    {
      "aweme_id": "7372484719365098803",
      "content_type": 3,
      "create_time": 1716559306,
      "digg_count": 1932,
      "ip_label": "<user>",
      "label_type": -1,
      "reply_id": "0",
      "reply_to_reply_id": "0",
      "sort_tags": "{\"top_list\":1}",
      "status": 1,
      "user": {
        "close_friend_type": 0,
        "nickname": "<user>",
        "short_id": "<user>",
        "status": 1
      }
    }
  ]
}
```

### Notes

- Specify the target video using the required `aweme_id` parameter.
- Manage response pagination using the `cursor` and `count` parameters.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Batch Video ID Extraction](/model/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/model/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/model/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/video-comments.json`](../../../../catalog/models/douyin/web/video-comments.json) · Store page: https://www.sandbase.ai/model/douyin/web/video-comments
