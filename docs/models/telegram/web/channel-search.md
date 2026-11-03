# Telegram Channel Post Search API: pricing, parameters and code examples

`telegram/web/channel-search` · data API · Telegram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns messages matching a search keyword from a specific Telegram channel. Filter results using channel username, query term, and result limit.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "telegram/web/channel-search", "channel": "telegram", "query": "privacy"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('telegram/web/channel-search', {'channel': 'telegram', 'query': 'privacy'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("telegram/web/channel-search", {
  "channel": "telegram",
  "query": "privacy"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "telegram/web/channel-search", sandbase.Params{
	"channel": "telegram",
	"query": "privacy",
})
```

Same call via the path form: `POST /v1/api/telegram/web/channel-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Number of hits (1-100, default 20). default `20`; range 1–100 |
| `query` | string | yes | Keyword (required).  |
| `channel` | string | yes | Channel username (required).  |

## Details

Returns messages from a public Telegram channel that match a keyword. It needs a channel username in `channel` and a search term in `query`, and takes an optional `limit`.

### Use cases

- Find channel posts that mention a product feature, such as privacy updates in the official Telegram channel.
- Pull the links and view counts of posts on one topic to compare how much attention each got.
- Collect video and link-preview posts about a keyword for a content review.
- Check how often a channel has covered a term in its recent history.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/telegram/web/channel-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"channel": "telegram", "query": "privacy"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `channel` | string | Yes | Channel username (required). |
| `query` | string | Yes | Keyword (required). |
| `limit` | integer | No | Number of hits (1-100, default 20). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "backend": "web",
  "channel": "telegram",
  "matched": 3,
  "messages": [
    {
      "author": "Telegram News",
      "channel": "telegram",
      "date": "2026-07-19T17:57:15+00:00",
      "forwarded_from": null,
      "id": 450,
      "is_forwarded": false,
      "link_preview": null,
      "media": {
        "has_unsupported": true,
        "photos": [],
        "videos": [
          {
            "duration": "0:14",
            "thumb": "https://cdn1.telesco.pe/file/ghRXw4zEVSj-LcfQyAhVPpz2VZBisrnmpWFJfVERFhfIM4tIdSz…",
            "url": "https://cdn1.telesco.pe/file/9998a6a814.mp4?token=RnY3mzsEyhcUooxfanOTo__6Mlhb_N…"
          }
        ]
      },
      "reactions": [],
      "reply_to": null,
      "text": "⭐️ Rich Text Editor. You can now create articles and long posts in a visual edit…",
      "text_html": "⭐️ <b>Rich Text Editor.</b> You can now create articles and long posts in a <b>v…"
    }
  ],
  "note": "网页预览无原生搜索，此为近期历史的尽力过滤；完整搜索需启用 MTProto 后端",
  "query": "privacy",
  "scanned": 100
}
```

### Response fields

| Field | Meaning |
|---|---|
| `matched / scanned` | `matched` is the number of messages that matched the keyword. `scanned` is the number of recent messages that were checked (100 in this response). |
| `messages[].id` | Numeric ID of the message within the channel. |
| `messages[].url` | Public `t.me` link to the message. |
| `messages[].date` | Post time as an ISO 8601 timestamp with a UTC offset. |
| `messages[].text / text_html` | Message text as plain text and as HTML. The HTML version keeps formatting such as bold tags. |
| `messages[].type` | Kind of post, such as `text` or `video`. |
| `messages[].views` | View count as a short string, for example `1.34M`. |
| `messages[].link_preview.title / link_preview.description / link_preview.url` | Title, description and target link of the web page previewed in the post. The value is `null` when the post has no preview. |
| `messages[].media.videos[].duration / media.videos[].url` | Length of an attached video and its file URL. `media.photos` lists attached photos. |
| `messages[].is_forwarded / forwarded_from / reply_to / reactions` | Whether the post was forwarded and from where, what it replies to, and its reactions. In this response these are empty, `false` or `null`. |

### Notes

- The `note` field in the response says the web preview has no native search. The API filters recent history on a best-effort basis, so older posts may not appear.
- `views` is a formatted string like `3.05M`, not a number.
- Use [Telegram Channel Posts](/apis/telegram/web/channel-posts) to read a channel's recent posts without a keyword.
- Use [Telegram Channel Post Details](/apis/telegram/web/post-detail) to look at a single post found in the results.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Telegram Batch Channel Info](/apis/telegram/web/batch-channel-info): Returns basic channel profile details including title, description, and verified status for multiple public Telegram channels at once.
- [Telegram Channel Info](/apis/telegram/web/channel-info): Returns public metadata for a Telegram channel, including title, description, verified status, and username, using the public web preview.
- [Telegram Channel Posts](/apis/telegram/web/channel-posts): Get a public Telegram channel's recent posts: text, media, forwards, replies, link previews, reactions, views and time, with cursor pagination.

---
Machine-readable: [`catalog/models/telegram/web/channel-search.json`](../../../../catalog/models/telegram/web/channel-search.json) · Store page: https://www.sandbase.ai/model/telegram/web/channel-search
