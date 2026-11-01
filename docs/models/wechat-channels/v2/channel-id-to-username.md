# WeChat Channels ID to Username

`wechat-channels/v2/channel-id-to-username` · api · WeChat Channels

Convert a public WeChat Channels Channel ID (sph… short ID) into the finder username (v2_…@finder) required by the other WeChat Channels APIs.

## Pricing

- **$0.015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-channels/v2/channel-id-to-username", "channel_id": "sphi9BjV8GK0Zsl", "raw": false}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-channels/v2/channel-id-to-username', {'channel_id': 'sphi9BjV8GK0Zsl', 'raw': False})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-channels/v2/channel-id-to-username", {
  "channel_id": "sphi9BjV8GK0Zsl",
  "raw": false
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-channels/v2/channel-id-to-username", sandbase.Params{
	"channel_id": "sphi9BjV8GK0Zsl",
	"raw": false,
})
```

Same call via the path form: `POST /v1/api/wechat-channels/v2/channel-id-to-username` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `raw` | boolean |  | Optional, default True. True=raw response; False=simplified parsed structure.  |
| `channel_id` | string | yes | Channel ID (`sph…` short ID), e.g. `sphi9BjV8GK0Zsl` (People's Daily). Must start with `sph`.  |

## Details

WeChat Channels shows a short public Channel ID (`sph…`) on profiles, but the data APIs need the internal finder username. Pass the Channel ID and get the username, nickname and bio.

### Use cases

- Resolve Channel IDs collected from profiles or links.
- First step before calling User Videos or Account Info.
- Deduplicate accounts across data sources.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-channels/v2/channel-id-to-username" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"channel_id": "sphi9BjV8GK0Zsl", "raw": false}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `channel_id` | string | Yes | Channel ID (`sph…` short ID), e.g. |
| `raw` | boolean | No | Optional, default True. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "channel_id": "sphi9BjV8GK0Zsl",
  "username": "v2_0600002310…@finder",
  "nickname": "人民日报",
  "desc": "参与、沟通、记录时代。"
}
```

### Notes

- The Channel ID must start with `sph`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [WeChat Channels Account Info](/model/wechat-channels/v2/channel-info): Get the public "More info" panel of a WeChat Channels account: Channel ID, IP and profile location, and verification details such as entity type, service categ…
- [WeChat Channels User Videos](/model/wechat-channels/v2/user-videos): Get the videos on a WeChat Channels account's homepage with descriptions, publish time, like, comment, share and favorite counts, and media download info, with…
- [WeChat Channels Video Detail](/model/wechat-channels/v2/video-detail): Get the full detail of a WeChat Channels video: description, author, engagement counts and the media URL with decode key for download.

---
Machine-readable: [`catalog/models/wechat-channels/v2/channel-id-to-username.json`](../../../../catalog/models/wechat-channels/v2/channel-id-to-username.json) · Store page: https://www.sandbase.ai/model/wechat-channels/v2/channel-id-to-username
