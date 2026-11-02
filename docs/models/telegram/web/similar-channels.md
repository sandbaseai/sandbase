# Telegram Similar Channels API: pricing, parameters and code examples

`telegram/web/similar-channels` · data API · Telegram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns Telegram's official similar channel recommendations based on a specified channel username for channel discovery and audience research.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "telegram/web/similar-channels", "channel": "telegram"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('telegram/web/similar-channels', {'channel': 'telegram'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("telegram/web/similar-channels", {
  "channel": "telegram"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "telegram/web/similar-channels", sandbase.Params{
	"channel": "telegram",
})
```

Same call via the path form: `POST /v1/api/telegram/web/similar-channels` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `channel` | string | yes | Channel username.  |

## Details

Look up similar channel recommendations directly from Telegram by supplying the target username via `channel`.

### Use cases

- Discover related Telegram channels within the same topic or niche.
- Research competitor channel networks and linked communities.
- Automate channel discovery feeds based on official recommendations.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/telegram/web/similar-channels" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"channel": "telegram"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `channel` | string | Yes | Channel username. |

### Notes

- Pass the Telegram channel username using the `channel` parameter.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Telegram Batch Channel Info](/model/telegram/web/batch-channel-info): Returns basic channel profile details including title, description, and verified status for multiple public Telegram channels at once.
- [Telegram Channel Info](/model/telegram/web/channel-info): Returns public metadata for a Telegram channel, including title, description, verified status, and username, using the public web preview.
- [Telegram Channel Posts](/model/telegram/web/channel-posts): Get a public Telegram channel's recent posts: text, media, forwards, replies, link previews, reactions, views and time, with cursor pagination.

---
Machine-readable: [`catalog/models/telegram/web/similar-channels.json`](../../../../catalog/models/telegram/web/similar-channels.json) · Store page: https://www.sandbase.ai/model/telegram/web/similar-channels
