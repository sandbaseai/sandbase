# Telegram Channel Posts API: pricing, parameters and code examples

`telegram/web/channel-posts` · data API · Telegram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Get a public Telegram channel's recent posts: text, media, forwards, replies, link previews, reactions, views and time, with cursor pagination.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "telegram/web/channel-posts", "channel": "telegram", "limit": 3}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('telegram/web/channel-posts', {'channel': 'telegram', 'limit': 3})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("telegram/web/channel-posts", {
  "channel": "telegram",
  "limit": 3
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "telegram/web/channel-posts", sandbase.Params{
	"channel": "telegram",
	"limit": 3,
})
```

Same call via the path form: `POST /v1/api/telegram/web/channel-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `after` | integer |  | Pagination cursor — fetch newer posts, pass `data.pagination.after_cursor` from the previous page. default `0` |
| `limit` | integer |  | Number of posts (1-100, default 20; when >20 the server automatically pages toward older posts). default `20`; range 1–100 |
| `before` | integer |  | Pagination cursor — fetch older posts, pass `data.pagination.before_cursor` from the previous page. default `0` |
| `channel` | string | yes | Channel username (required).  |

## Details

Pass a public channel username and get its latest posts with views, reactions and link previews.

### Use cases

- Monitor announcements from crypto, news or product channels.
- Track post reach (views) over time.
- Archive channel content.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/telegram/web/channel-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"channel": "telegram", "limit": 3}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `channel` | string | Yes | Channel username (required). |
| `after` | integer | No | Pagination cursor — fetch newer posts, pass `data.pagination.after_cursor` from the previous page. |
| `limit` | integer | No | Number of posts (1-100, default 20; when >20 the server automatically pages toward older posts). |
| `before` | integer | No | Pagination cursor — fetch older posts, pass `data.pagination.before_cursor` from the previous page. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "messages": [
    {
      "id": 460,
      "date": "2026-08-26T19:12:34+00:00",
      "type": "text",
      "views": "1.68M",
      "url": "https://t.me/telegram/460",
      "text": "For all the info from today's update and a look back at 13 years of T…"
    }
  ],
  "pagination": {
    "after_cursor": 460,
    "before_cursor": 458,
    "count": 3,
    "has_more_before": true,
    "limit": 3,
    "pages_fetched": 1
  }
}
```

### Notes

- Use `before` / `after` cursors from `pagination` to page older or newer posts.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Batch channel info](/model/telegram/web/batch-channel-info): Fetch basic info (title/description/avatar/subscribers/verified) for multiple public channels concurrently.
- [Get channel info](/model/telegram/web/channel-info): Get public Telegram channel metadata: title, description, avatar, subscriber count, verified badge and media counters..
- [Search posts in a channel](/model/telegram/web/channel-search): Search posts in a channel by keyword (case-insensitive)..

---
Machine-readable: [`catalog/models/telegram/web/channel-posts.json`](../../../../catalog/models/telegram/web/channel-posts.json) · Store page: https://www.sandbase.ai/model/telegram/web/channel-posts
