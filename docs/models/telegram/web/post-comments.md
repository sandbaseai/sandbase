# Telegram Post Comments API: pricing, parameters and code examples

`telegram/web/post-comments` · data API · Telegram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns comments from the linked discussion group of a specified Telegram channel post. Filters include the channel username, post ID, and an optional limit.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "telegram/web/post-comments", "channel": "example", "post_id": 1}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('telegram/web/post-comments', {'channel': 'example', 'post_id': 1})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("telegram/web/post-comments", {
  "channel": "example",
  "post_id": 1
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "telegram/web/post-comments", sandbase.Params{
	"channel": "example",
	"post_id": 1,
})
```

Same call via the path form: `POST /v1/api/telegram/web/post-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Number of comments range 1–100 |
| `channel` | string | yes | Channel username; post_id: Post ID; limit: number of comments (1-100).  |
| `post_id` | integer | yes | Post ID  |

## Details

Retrieve discussion comments for a specific post using `channel` and `post_id`. Use `limit` to adjust the number of comments returned.

### Use cases

- Analyze user discussions and feedback on specific channel posts.
- Monitor linked group responses to broad channel announcements.
- Archive comment threads connected to public channel content.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/telegram/web/post-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"channel": "telegram", "post_id": 450}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `channel` | string | Yes | Channel username; post_id: Post ID; limit: number of comments (1-100). |
| `post_id` | integer | Yes | Post ID |
| `limit` | integer | No | Number of comments |

### Notes

- The `limit` parameter supports values between 1 and 100.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Telegram Batch Channel Info](/model/telegram/web/batch-channel-info): Returns basic channel profile details including title, description, and verified status for multiple public Telegram channels at once.
- [Telegram Channel Info](/model/telegram/web/channel-info): Returns public metadata for a Telegram channel, including title, description, verified status, and username, using the public web preview.
- [Telegram Channel Posts](/model/telegram/web/channel-posts): Get a public Telegram channel's recent posts: text, media, forwards, replies, link previews, reactions, views and time, with cursor pagination.

---
Machine-readable: [`catalog/models/telegram/web/post-comments.json`](../../../../catalog/models/telegram/web/post-comments.json) · Store page: https://www.sandbase.ai/model/telegram/web/post-comments
