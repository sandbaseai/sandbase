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

Returns Telegram's similar channel recommendations for one channel, using the channel username in `channel`. The response can also carry an `mtproto_required` flag and a `note` when recommendations are not available for the request.

### Use cases

- Find channels related to a given channel when you research a topic or niche.
- Build a list of neighbouring channels around a competitor's channel.
- Feed seed usernames into a channel discovery workflow and collect the recommended channels from `similar`.
- Check whether a channel returns recommendations before you add it to a monitoring list.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/telegram/web/similar-channels" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"channel": "telegram"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `channel` | string | Yes | Channel username. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "channel": "telegram",
  "mtproto_required": true,
  "note": "相似频道推荐需要在「设置」页启用并登录 MTProto 后端",
  "similar": []
}
```

### Response fields

| Field | Meaning |
|---|---|
| `channel` | The channel username the request was made for. It repeats the `channel` input. |
| `similar` | List of recommended channels. It is an empty list in the sample response, so check its length before you read items. |
| `mtproto_required` | Boolean flag. When it is `true`, the response says recommendations need an MTProto backend that is not active for this request. |
| `note` | Short text that explains the `mtproto_required` flag. In the sample it says similar channel recommendations need MTProto to be enabled and logged in on the Settings page. |

### Notes

- Send the channel username as `channel`, for example `telegram`.
- If `mtproto_required` is `true` and `similar` is empty, the call returned no recommendations. Read `note` for the reason.
- To get profile details for a channel you found, call [Telegram Channel Info](/apis/telegram/web/channel-info). To read its recent posts, call [Telegram Channel Posts](/apis/telegram/web/channel-posts).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Telegram Batch Channel Info](/apis/telegram/web/batch-channel-info): Returns basic channel profile details including title, description, and verified status for multiple public Telegram channels at once.
- [Telegram Channel Info](/apis/telegram/web/channel-info): Returns public metadata for a Telegram channel, including title, description, verified status, and username, using the public web preview.
- [Telegram Channel Posts](/apis/telegram/web/channel-posts): Get a public Telegram channel's recent posts: text, media, forwards, replies, link previews, reactions, views and time, with cursor pagination.

---
Machine-readable: [`catalog/models/telegram/web/similar-channels.json`](../../../../catalog/models/telegram/web/similar-channels.json) · Store page: https://www.sandbase.ai/model/telegram/web/similar-channels
