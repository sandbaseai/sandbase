# Telegram Channel Post Details

`telegram/web/post-detail` · api · Telegram

Retrieves details for a single public Telegram channel post parsed from the web embed view. Provide the channel username and post ID to view reactions and post data.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "telegram/web/post-detail", "channel": "durov", "post_id": 510}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('telegram/web/post-detail', {'channel': 'durov', 'post_id': 510})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("telegram/web/post-detail", {
  "channel": "durov",
  "post_id": 510
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "telegram/web/post-detail", sandbase.Params{
	"channel": "durov",
	"post_id": 510,
})
```

Same call via the path form: `POST /v1/api/telegram/web/post-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `channel` | string | yes | Channel username (required).  |
| `post_id` | integer | yes | Post ID (required, auto-incremented integer within the channel).  |

## Details

This endpoint returns details for a specific post in a public channel using `channel` and `post_id`.

### Use cases

- Monitor reaction metrics on individual channel posts.
- Retrieve public message metadata by post ID.
- Track engagement levels across specific channel announcements.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/telegram/web/post-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"channel": "durov", "post_id": 510}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `channel` | string | Yes | Channel username (required). |
| `post_id` | integer | Yes | Post ID (required, auto-incremented integer within the channel). |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "reactions": [
    {
      "count": "8.24K"
    }
  ]
}
```

### Notes

- `channel` requires the public channel username.
- `post_id` is an auto-incremented integer representing the post within the channel.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Telegram Batch Channel Info](/model/telegram/web/batch-channel-info): Returns basic channel profile details including title, description, and verified status for multiple public Telegram channels at once.
- [Telegram Channel Info](/model/telegram/web/channel-info): Returns public metadata for a Telegram channel, including title, description, verified status, and username, using the public web preview.
- [Telegram Channel Posts](/model/telegram/web/channel-posts): Get a public Telegram channel's recent posts: text, media, forwards, replies, link previews, reactions, views and time, with cursor pagination.

---
Machine-readable: [`catalog/models/telegram/web/post-detail.json`](../../../../catalog/models/telegram/web/post-detail.json) · Store page: https://www.sandbase.ai/model/telegram/web/post-detail
