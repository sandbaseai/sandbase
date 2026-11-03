# WeChat Channels Stream Replay History API: pricing, parameters and code examples

`wechat-channels/v2/live-history` · data API · WeChat Channels · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns a creator's broadcast replay list, including media download URLs and decryption keys. Supports cursor pagination via a finder username.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-channels/v2/live-history", "username": "v2_060000231003b20faec8cae1811ac4d5c702ea32b0771737aa785454f7f8177114cc4d248d66@finder"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-channels/v2/live-history', {'username': 'v2_060000231003b20faec8cae1811ac4d5c702ea32b0771737aa785454f7f8177114cc4d248d66@finder'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-channels/v2/live-history", {
  "username": "v2_060000231003b20faec8cae1811ac4d5c702ea32b0771737aa785454f7f8177114cc4d248d66@finder"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-channels/v2/live-history", sandbase.Params{
	"username": "v2_060000231003b20faec8cae1811ac4d5c702ea32b0771737aa785454f7f8177114cc4d248d66@finder",
})
```

Same call via the path form: `POST /v1/api/wechat-channels/v2/live-history` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `raw` | boolean |  | Optional, default True. True=raw response; False=simplified parsed structure (recommended for media download).  |
| `flag` | integer |  | Optional fetch flag, default 12. range 0–1000 |
| `username` | string | yes | WeChat Channels finder username (`v2_…@finder` format). Example (an account with live replays): `v2_060000231003b20faec8cae1811ac4d5c702ea32b0771737aa785454f7f8177114cc4d248d66@finder` (Huxiu).  |
| `last_buffer` |  |  | Optional pagination cursor (base64), **leave empty for the first page**; when `continue_flag` is truthy, pass the previous page's `last_buffer`.  |

## Details

Fetch broadcast replay records for a creator by supplying their `username`. Output includes video download details and pagination indicators.

### Use cases

- Archive recorded stream sessions from creator channels
- Extract video URLs and decryption keys for offline storage
- Monitor broadcast history and replay availability across channels

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-channels/v2/live-history" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "v2_060000231003b20faec8cae1811ac4d5c702ea32b0771737aa785454f7f8177114cc4d248d66@finder"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | WeChat Channels finder username (`v2_…@finder` format). |
| `raw` | boolean | No | Optional, default True. |
| `flag` | integer | No | Optional fetch flag, default 12. |
| `last_buffer` | string | No | Optional pagination cursor (base64), leave empty for the first page; when `continue_flag` is truthy, pass the previous page's `last_buffer`. |

### Notes

- The required `username` must follow the `v2_...@finder` format.
- For pagination, leave `last_buffer` empty on the first call, then pass the returned cursor when continuation is indicated.
- Set `raw` to false to receive a simplified parsed structure optimized for media downloads.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [WeChat Channels ID to Username](/apis/wechat-channels/v2/channel-id-to-username): Convert a public WeChat Channels Channel ID (sph… short ID) into the finder username (v2_…@finder) required by the other WeChat Channels APIs.
- [WeChat Channels Account Info](/apis/wechat-channels/v2/channel-info): Get the public "More info" panel of a WeChat Channels account: Channel ID, IP and profile location, and verification details such as entity type, service categ…
- [WeChat Channels Collection Videos](/apis/wechat-channels/v2/collection-videos): Returns videos contained within a WeChat Channels collection using a collection ID.

---
Machine-readable: [`catalog/models/wechat-channels/v2/live-history.json`](../../../../catalog/models/wechat-channels/v2/live-history.json) · Store page: https://www.sandbase.ai/model/wechat-channels/v2/live-history
