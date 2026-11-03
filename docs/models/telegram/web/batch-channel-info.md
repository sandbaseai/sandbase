# Telegram Batch Channel Info API: pricing, parameters and code examples

`telegram/web/batch-channel-info` · data API · Telegram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Returns basic channel profile details including title, description, and verified status for multiple public Telegram channels at once.

## Pricing

- **$0.008 per call** (USD)
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

Returns public profile details for up to 20 Telegram channels in one call. You pass a comma-separated list of channel usernames in `channels`. Each result holds the title, description, photo, verified flag and subscriber and media counts.

### Use cases

- Check the verified status and subscriber counts of a list of competitor channels in one request.
- Build a directory of channels with titles, descriptions and profile photos from a list of usernames.
- Validate a list of channel usernames and spot which ones return no profile data.
- Track how channel subscriber counts and media totals compare across a group of channels.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/telegram/web/batch-channel-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"channels": "telegram"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `channels` | string | Yes | Comma-separated channel usernames, up to 20 per request. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "count": 1,
  "results": [
    {
      "channel": "telegram",
      "info": {
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
      "ok": true
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `count` | Number of channels in the `results` list. |
| `results[].channel` | The username you asked for, as sent in the request. |
| `results[].ok` | `true` when the lookup for this channel worked. |
| `results[].info.title` | Display name of the channel. |
| `results[].info.username` | Channel username without the `@`. |
| `results[].info.description` | Channel bio text. |
| `results[].info.verified` | `true` when the channel has the verified badge. |
| `results[].info.subscribers / results[].info.counters.subscribers` | Subscriber count as a short text string, such as `9.2M`. It is not an exact number. |
| `results[].info.counters.photos / results[].info.counters.videos / results[].info.counters.links` | Counts of photos, videos and links shared in the channel, returned as strings. |
| `results[].info.photo` | URL of the channel profile picture. |

### Notes

- Send usernames without the `@`, separated by commas, for example `telegram,durov`. The limit is 20 per request.
- Check `results[].ok` for each channel, since results are returned per channel.
- Counts such as `subscribers` are abbreviated strings, so parse values like `9.2M` before you do math.
- For one channel, use [Telegram Channel Info](/apis/telegram/web/channel-info). To read posts next, call [Telegram Channel Posts](/apis/telegram/web/channel-posts).

### Pricing

$0.008 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Telegram Channel Info](/apis/telegram/web/channel-info): Returns public metadata for a Telegram channel, including title, description, verified status, and username, using the public web preview.
- [Telegram Channel Posts](/apis/telegram/web/channel-posts): Get a public Telegram channel's recent posts: text, media, forwards, replies, link previews, reactions, views and time, with cursor pagination.
- [Telegram Channel Post Search](/apis/telegram/web/channel-search): Returns messages matching a search keyword from a specific Telegram channel.

---
Machine-readable: [`catalog/models/telegram/web/batch-channel-info.json`](../../../../catalog/models/telegram/web/batch-channel-info.json) · Store page: https://www.sandbase.ai/model/telegram/web/batch-channel-info
