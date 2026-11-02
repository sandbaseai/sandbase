# Telegram Batch Channel Info API: pricing, parameters and code examples

`telegram/web/batch-channel-info` · data API · Telegram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.012 per call (free daily quota) · **Modes:** sync

Returns basic channel profile details including title, description, and verified status for multiple public Telegram channels at once.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "telegram/web/batch-channel-info", "channels": "telegram"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('telegram/web/batch-channel-info', {'channels': 'telegram'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("telegram/web/batch-channel-info", {
  "channels": "telegram"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "telegram/web/batch-channel-info", sandbase.Params{
	"channels": "telegram",
})
```

Same call via the path form: `POST /v1/api/telegram/web/batch-channel-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `channels` | string | yes | Comma-separated channel usernames, up to 20 per request.  |

## Details

Look up public profile details for multiple Telegram channels in a single request using the `channels` parameter.

### Use cases

- Retrieve profile summaries for multiple public Telegram channels simultaneously.
- Verify whether specific Telegram channels have verified badges.
- Inspect channel descriptions and titles across a list of target usernames.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/telegram/web/batch-channel-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"channels": "telegram"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `channels` | string | Yes | Comma-separated channel usernames, up to 20 per request. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "results": [
    {
      "info": {
        "description": "The official Telegram on Telegram. Much recursion. Very Telegram. Wow.",
        "title": "Telegram News",
        "username": "<user>",
        "verified": true
      }
    }
  ]
}
```

### Notes

- Pass channel usernames as a comma-separated string to `channels`.
- Accepts up to 20 channel usernames per request.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Telegram Channel Info](/model/telegram/web/channel-info): Returns public metadata for a Telegram channel, including title, description, verified status, and username, using the public web preview.
- [Telegram Channel Posts](/model/telegram/web/channel-posts): Get a public Telegram channel's recent posts: text, media, forwards, replies, link previews, reactions, views and time, with cursor pagination.
- [Telegram Channel Post Search](/model/telegram/web/channel-search): Returns messages matching a search keyword from a specific Telegram channel.

---
Machine-readable: [`catalog/models/telegram/web/batch-channel-info.json`](../../../../catalog/models/telegram/web/batch-channel-info.json) · Store page: https://www.sandbase.ai/model/telegram/web/batch-channel-info
