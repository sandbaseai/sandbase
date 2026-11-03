# Telegram Channel Posts API: pricing, parameters and code examples

`telegram/web/channel-posts` · data API · Telegram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get a public Telegram channel's recent posts: text, media, forwards, replies, link previews, reactions, views and time, with cursor pagination.

## Pricing

- **$0.001 per call** (USD)
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

Returns recent posts from a public Telegram channel, plus basic channel info. Each post has text, media, link preview, reactions, views and a timestamp. The only required input is the channel `username`.

### Use cases

- Monitor a news or product channel for new announcements and read the linked blog posts from `link_preview`.
- Compare `views` across recent posts to see which posts reach the most readers.
- Archive a channel by paging back through posts and saving `text_html`, photo URLs and video URLs.
- Read the subscriber count and verified flag of a channel together with its latest posts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/telegram/web/channel-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"channel": "telegram", "limit": 3}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `channel` | string | Yes | Channel username (required). |
| `after` | integer | No | Pagination cursor — fetch newer posts, pass `data.pagination.after_cursor` from the previous page. |
| `before` | integer | No | Pagination cursor — fetch older posts, pass `data.pagination.before_cursor` from the previous page. |
| `limit` | integer | No | Number of posts (1-100, default 20; when >20 the server automatically pages toward older posts). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "channel": "telegram",
  "channel_info": {
    "counters": {
      "links": "378",
      "photos": "16",
      "subscribers": "9.2M",
      "videos": "228"
    },
    "description": "The official Telegram on Telegram. Much recursion. Very Telegram. Wow.",
    "photo": "https://cdn1.telesco.pe/file/hnmFZVV6A1_vjW41WnRQI9LiY1404GFwcfT_HbWGXlPkZCJQr6y…",
    "subscribers": "9.2M",
    "title": "Telegram News",
    "username": "telegram",
    "verified": true
  },
  "messages": [
    {
      "author": "Telegram News",
      "channel": "telegram",
      "date": "2026-08-26T19:12:34+00:00",
      "forwarded_from": null,
      "id": 460,
      "is_forwarded": false,
      "link_preview": {
        "description": "Introducing Welcome Messages to greet new members of groups or channels, Buttons…",
        "site_name": "Telegram",
        "title": "Welcome Messages, Buttons in Messages and Signed Gifts",
        "url": "https://telegram.org/blog/welcome-messages-buttons-TG-13"
      },
      "media": {
        "has_unsupported": false,
        "photos": [],
        "videos": []
      },
      "reactions": [],
      "reply_to": null,
      "text": "For all the info from today's update and a look back at 13 years of Telegram fea…",
      "text_html": "For all the info from today's update and a look back at <b>13 years of Telegram …"
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

### Response fields

| Field | Meaning |
|---|---|
| `messages[].id` | Numeric ID of the post inside the channel. Posts with higher IDs are newer. |
| `messages[].date` | Time the post was published, in ISO 8601 format with a UTC offset. |
| `messages[].type` | Kind of post, such as `text`, `video` or `photo`. |
| `messages[].text / messages[].text_html` | The post body as plain text, and as HTML with tags for bold text and links. |
| `messages[].url` | Public `t.me` link to the post. |
| `messages[].views` | View count as a short string such as `2.29M`, not an exact number. |
| `messages[].link_preview.title / messages[].link_preview.description / messages[].link_preview.url` | Title, summary and target URL of the web page previewed under the post. The value is `null` when the post has no preview. |
| `messages[].media.photos[] / messages[].media.videos[]` | Photo URLs, and video objects with `url`, `thumb` and `duration`. `media.has_unsupported` is `true` when the post has media that is not listed. |
| `messages[].is_forwarded / messages[].forwarded_from / messages[].reply_to` | Show whether the post was forwarded, where it came from, and which post it replies to. These are `null` or `false` when they do not apply. |
| `channel_info.title / channel_info.subscribers / channel_info.verified` | Channel display name, subscriber count as a short string, and whether the channel has a verified badge. |

### Notes

- Pass the channel name without the `@` sign as `channel`, for example `telegram`.
- To load older posts, pass `pagination.before_cursor` as `before`. To load newer posts, pass `pagination.after_cursor` as `after`.
- `pagination.has_more_before` tells you if older posts remain. `limit` accepts 1 to 100.
- For full channel metadata, call [Telegram Channel Info](/apis/telegram/web/channel-info). To find posts by keyword, call [Telegram Channel Post Search](/apis/telegram/web/channel-search).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Batch channel info](/apis/telegram/web/batch-channel-info): Fetch basic info (title/description/avatar/subscribers/verified) for multiple public channels concurrently.
- [Get channel info](/apis/telegram/web/channel-info): Get public Telegram channel metadata: title, description, avatar, subscriber count, verified badge and media counters..
- [Search posts in a channel](/apis/telegram/web/channel-search): Search posts in a channel by keyword (case-insensitive)..

---
Machine-readable: [`catalog/models/telegram/web/channel-posts.json`](../../../../catalog/models/telegram/web/channel-posts.json) · Store page: https://www.sandbase.ai/model/telegram/web/channel-posts
