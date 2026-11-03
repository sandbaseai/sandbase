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

Retrieve public profile details and verification status for a specified Telegram channel using the `channel` parameter.

### Use cases

- Check verified status and public profile details for Telegram channels.
- Display Telegram channel previews within external applications.
- Gather public metadata such as title and description from channel usernames or links.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/telegram/web/channel-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"channel": "telegram"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `channel` | string | Yes | Channel username (accepts `durov` / `@durov` / `https://t.me/durov`, normalized automatically). |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "description": "The official Telegram on Telegram. Much recursion. Very Telegram. Wow.",
  "title": "Telegram News",
  "username": "<user>",
  "verified": true
}
```

### Notes

- The `channel` parameter accepts formats such as `durov`, `@durov`, or `https://t.me/durov` and normalizes them automatically.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Telegram Batch Channel Info](/apis/telegram/web/batch-channel-info): Returns basic channel profile details including title, description, and verified status for multiple public Telegram channels at once.
- [Telegram Channel Posts](/apis/telegram/web/channel-posts): Get a public Telegram channel's recent posts: text, media, forwards, replies, link previews, reactions, views and time, with cursor pagination.
- [Telegram Channel Post Search](/apis/telegram/web/channel-search): Returns messages matching a search keyword from a specific Telegram channel.

---
Machine-readable: [`catalog/models/telegram/web/channel-info.json`](../../../../catalog/models/telegram/web/channel-info.json) · Store page: https://www.sandbase.ai/model/telegram/web/channel-info
