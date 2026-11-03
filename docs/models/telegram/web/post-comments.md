# Telegram Post Comments API: pricing, parameters and code examples

`telegram/web/post-comments` · data API · Telegram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns comments from the linked discussion group of a specified Telegram channel post. Filters include the channel username, post ID, and an optional limit.

## Pricing

- **$0.001 per call** (USD)
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

Returns comments from the linked discussion group of a Telegram channel post. It needs the channel username in `channel` and the numeric `post_id`. An optional `limit` sets how many comments to return.

### Use cases

- Read reader replies under a specific announcement post in a public channel.
- Check whether a post has any discussion before you pull its full thread.
- Collect comment text from a channel post for sentiment review.
- Pair comment results with post data from the channel to compare a post with its replies.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/telegram/web/post-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"channel": "telegram", "post_id": 450}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `channel` | string | Yes | Channel username; post_id: Post ID; limit: number of comments (1-100). |
| `post_id` | integer | Yes | Post ID |
| `limit` | integer | No | Number of comments |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "channel": "telegram",
  "comments": [],
  "mtproto_required": true,
  "note": "帖子评论需要在「设置」页启用并登录 MTProto 后端",
  "post_id": 450
}
```

### Response fields

| Field | Meaning |
|---|---|
| `channel` | The channel username that the request used. |
| `post_id` | The ID of the post that the request asked about. |
| `comments` | List of comments on the post. In the sample response it is empty `[]`. |
| `mtproto_required` | When `true`, the call needs an MTProto backend to be enabled and logged in before it can return comments. |
| `note` | Text message that explains why the result is empty. In the sample it says post comments need MTProto to be enabled and logged in on the settings page. |

### Notes

- Use the channel username without the `@` sign, for example `telegram`.
- `limit` accepts whole numbers from 1 to 100.
- Check `mtproto_required` first. If it is `true`, `comments` stays empty and `note` explains the reason.
- Get post IDs from [Telegram Channel Posts](/apis/telegram/web/channel-posts), or look up one post with [Telegram Channel Post Details](/apis/telegram/web/post-detail).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Telegram Batch Channel Info](/apis/telegram/web/batch-channel-info): Returns basic channel profile details including title, description, and verified status for multiple public Telegram channels at once.
- [Telegram Channel Info](/apis/telegram/web/channel-info): Returns public metadata for a Telegram channel, including title, description, verified status, and username, using the public web preview.
- [Telegram Channel Posts](/apis/telegram/web/channel-posts): Get a public Telegram channel's recent posts: text, media, forwards, replies, link previews, reactions, views and time, with cursor pagination.

---
Machine-readable: [`catalog/models/telegram/web/post-comments.json`](../../../../catalog/models/telegram/web/post-comments.json) · Store page: https://www.sandbase.ai/model/telegram/web/post-comments
