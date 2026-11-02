# WeChat Channels Account Info API: pricing, parameters and code examples

`wechat-channels/v2/channel-info` · data API · WeChat Channels · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Get the public "More info" panel of a WeChat Channels account: Channel ID, IP and profile location, and verification details such as entity type, service category and license numbers.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-channels/v2/channel-info", "raw": false, "username": "v2_060000231003b20faec8c6e4811dc1d4c602ee30b0771bbcf220c67926bb76ab7702ac335a53@finder"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-channels/v2/channel-info', {'raw': False, 'username': 'v2_060000231003b20faec8c6e4811dc1d4c602ee30b0771bbcf220c67926bb76ab7702ac335a53@finder'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-channels/v2/channel-info", {
  "raw": false,
  "username": "v2_060000231003b20faec8c6e4811dc1d4c602ee30b0771bbcf220c67926bb76ab7702ac335a53@finder"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-channels/v2/channel-info", sandbase.Params{
	"raw": false,
	"username": "v2_060000231003b20faec8c6e4811dc1d4c602ee30b0771bbcf220c67926bb76ab7702ac335a53@finder",
})
```

Same call via the path form: `POST /v1/api/wechat-channels/v2/channel-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `raw` | boolean |  | Optional, default True. True=raw response; False=simplified parsed structure.  |
| `username` | string | yes | WeChat Channels finder username (`v2_…@finder` format), e.g. `v2_060000231003b20faec8c6e4811dc1d4c602ee30b0771bbcf220c67926bb76ab7702ac335a53@finder` (People's Daily).  |

## Details

Pass a WeChat Channels finder username (`v2_…@finder`) and get the account's public profile details, including its Channel ID and verification information.

### Use cases

- Verify the real entity behind a Channels account before a partnership.
- Collect Channel IDs and locations for account directories.
- Combine with User Videos to build creator profiles.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-channels/v2/channel-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "v2_060000231003b20faec8c6e4811dc1d4c602ee30b0771bbcf220c67926bb76ab7702ac335a53@finder", "raw": false}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | WeChat Channels finder username (`v2_…@finder` format), e.g. |
| `raw` | boolean | No | Optional, default True. |

### Notes

- Get the finder username from a Channel ID with the Channel ID to Username API, or from WeChat search results.
- Requests with invalid parameters are still processed by WeChat and billed upstream, so validate IDs first.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [WeChat Channels ID to Username](/model/wechat-channels/v2/channel-id-to-username): Convert a public WeChat Channels Channel ID (sph… short ID) into the finder username (v2_…@finder) required by the other WeChat Channels APIs.
- [WeChat Channels User Videos](/model/wechat-channels/v2/user-videos): Get the videos on a WeChat Channels account's homepage with descriptions, publish time, like, comment, share and favorite counts, and media download info, with…
- [WeChat Channels Video Detail](/model/wechat-channels/v2/video-detail): Get the full detail of a WeChat Channels video: description, author, engagement counts and the media URL with decode key for download.

---
Machine-readable: [`catalog/models/wechat-channels/v2/channel-info.json`](../../../../catalog/models/wechat-channels/v2/channel-info.json) · Store page: https://www.sandbase.ai/model/wechat-channels/v2/channel-info
