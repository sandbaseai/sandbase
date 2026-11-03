# Telegram Channel Info API: pricing, parameters and code examples

`telegram/web/channel-info` · data API · Telegram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns public metadata for a Telegram channel, including title, description, verified status, and username, using the public web preview.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "telegram/web/channel-info", "channel": "telegram"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('telegram/web/channel-info', {'channel': 'telegram'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("telegram/web/channel-info", {
  "channel": "telegram"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "telegram/web/channel-info", sandbase.Params{
	"channel": "telegram",
})
```

Same call via the path form: `POST /v1/api/telegram/web/channel-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `channel` | string | yes | Channel username (accepts `durov` / `@durov` / `https://t.me/durov`, normalized automatically).  |

## Details

Returns public metadata for a Telegram channel: title, description, username, verified flag, profile photo URL and subscriber and media counts. It needs one input, the `channel` username, link or @handle.

### Use cases

- Check whether a Telegram channel is verified before you add it to a monitoring list.
- Show a channel card with its title, photo and subscriber count inside your own app.
- Track the subscriber count of a channel by calling the API on a schedule and storing the result.
- Resolve a `https://t.me/` link into a clean username and title.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/telegram/web/channel-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"channel": "telegram"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `channel` | string | Yes | Channel username (accepts `durov` / `@durov` / `https://t.me/durov`, normalized automatically). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
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
}
```

### Response fields

| Field | Meaning |
|---|---|
| `title` | Display name of the channel, such as `Telegram News`. |
| `username` | Channel username without the `@` sign. |
| `description` | Public description text shown on the channel page. |
| `verified` | `true` when the channel shows as verified. |
| `subscribers / counters.subscribers` | Subscriber count as a short string such as `9.2M`. Both fields hold the same value in this response. |
| `counters.photos / counters.videos / counters.links` | Counts of photos, videos and links shared in the channel, returned as strings. |
| `photo` | URL of the channel profile picture. |

### Notes

- Pass `channel` as `durov`, `@durov` or `https://t.me/durov`. The API normalizes all three.
- Counts are returned as strings and may be abbreviated, for example `9.2M`. Parse them before you do math.
- To read the channel's messages, call [Telegram Channel Posts](/apis/telegram/web/channel-posts) next.
- To look up many channels in one call, use [Telegram Batch Channel Info](/apis/telegram/web/batch-channel-info).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Telegram Batch Channel Info](/apis/telegram/web/batch-channel-info): Returns basic channel profile details including title, description, and verified status for multiple public Telegram channels at once.
- [Telegram Channel Posts](/apis/telegram/web/channel-posts): Get a public Telegram channel's recent posts: text, media, forwards, replies, link previews, reactions, views and time, with cursor pagination.
- [Telegram Channel Post Search](/apis/telegram/web/channel-search): Returns messages matching a search keyword from a specific Telegram channel.

---
Machine-readable: [`catalog/models/telegram/web/channel-info.json`](../../../../catalog/models/telegram/web/channel-info.json) · Store page: https://www.sandbase.ai/model/telegram/web/channel-info
