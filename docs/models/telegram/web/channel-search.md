# Telegram Channel Post Search

`telegram/web/channel-search` · api · Telegram

Returns messages matching a search keyword from a specific Telegram channel. Filter results using channel username, query term, and result limit.

## Pricing

- **$0.0015 per call** (USD)
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

Search for messages within a target Telegram channel matching a `query` string using the channel username in `channel`.

### Use cases

- Search channel history for specific topic mentions or announcements.
- Locate media posts matching specific keyword queries within a channel.
- Track historical coverage of particular terms across a channel feed.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/telegram/web/channel-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"channel": "telegram", "query": "privacy"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Keyword (required). |
| `channel` | string | Yes | Channel username (required). |
| `limit` | integer | No | Number of hits (1-100, default 20). |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "messages": [
    {
      "author": "Telegram News",
      "date": "2026-07-19T17:57:15+00:00",
      "id": 450,
      "text": "⭐️ Rich Text Editor. You can now create articles and long posts in a visual editor that s…",
      "text_html": "⭐️ Rich Text Editor. You can now create articles and long posts in a visual editor that s…",
      "type": "video",
      "url": "https://t.me/telegram/450",
      "views": "1.25M"
    }
  ]
}
```

### Notes

- Accepts a `limit` between 1 and 100 hits, with a default of 20.
- Keyword matching through `query` is case-insensitive.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Telegram Batch Channel Info](/model/telegram/web/batch-channel-info): Returns basic channel profile details including title, description, and verified status for multiple public Telegram channels at once.
- [Telegram Channel Info](/model/telegram/web/channel-info): Returns public metadata for a Telegram channel, including title, description, verified status, and username, using the public web preview.
- [Telegram Channel Posts](/model/telegram/web/channel-posts): Get a public Telegram channel's recent posts: text, media, forwards, replies, link previews, reactions, views and time, with cursor pagination.

---
Machine-readable: [`catalog/models/telegram/web/channel-search.json`](../../../../catalog/models/telegram/web/channel-search.json) · Store page: https://www.sandbase.ai/model/telegram/web/channel-search
