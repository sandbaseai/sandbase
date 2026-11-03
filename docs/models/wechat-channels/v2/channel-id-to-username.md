# WeChat Channels ID to Username API: pricing, parameters and code examples

`wechat-channels/v2/channel-id-to-username` · data API · WeChat Channels · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Convert a public WeChat Channels Channel ID (sph… short ID) into the finder username (v2_…@finder) required by the other WeChat Channels APIs.

## Pricing

- **$0.01 per call** (USD)
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

This API takes a public WeChat Channels Channel ID (the short `sph…` ID) and returns the matching finder username (`v2_…@finder`). The response also includes the account nickname and bio.

### Use cases

- Convert Channel IDs collected from profiles or shared links into finder usernames.
- Get the `username` value you need before calling an account or video API for the same channel.
- Check which account sits behind a Channel ID by reading its `nickname` and `desc`.
- Match accounts from different sources by storing the `channel_id` and `username` pair.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-channels/v2/channel-id-to-username" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"channel_id": "sphi9BjV8GK0Zsl", "raw": false}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `channel_id` | string | Yes | Channel ID (`sph…` short ID), e.g. `sphi9BjV8GK0Zsl` (People's Daily). Must start with `sph`. |
| `raw` | boolean | No | Optional, default True. True=raw response; False=simplified parsed structure. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "channel_id": "sphi9BjV8GK0Zsl",
  "debug_id": "8b961260",
  "debug_info": "gAAAAABq6ZEeqTsKRQM1orP1An49kNtr_AbW7D7g90AVBCP1iJ6dpfwofN36FsORnSGOQ3Vo_qtnu_GC…",
  "desc": "参与、沟通、记录时代。",
  "nickname": "人民日报",
  "username": "v2_060000231003b20faec8c6e4811dc1d4c602ee30b0771bbcf220c67926bb76ab7702ac335a53@…"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `username` | The finder username for the channel, in the form `v2_…@finder`. Pass this value to the other WeChat Channels APIs that ask for a username. |
| `channel_id` | The Channel ID you sent, returned unchanged. |
| `nickname` | The display name of the account, for example `人民日报`. |
| `desc` | The account bio text shown on the channel profile. |
| `debug_id / debug_info` | Diagnostic values attached to the response. You do not need them to use the username. |

### Notes

- Take the `channel_id` from a channel profile. It must start with `sph` and can be up to 64 characters.
- With `raw` set to `false`, the response is the simplified structure shown here. `raw` defaults to `true`.
- Next, call [WeChat Channels User Videos](/apis/wechat-channels/v2/user-videos) or [WeChat Channels Account Info](/apis/wechat-channels/v2/channel-info) with the returned `username`.
- The `username` is a long string, so copy it in full.

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [WeChat Channels Account Info](/apis/wechat-channels/v2/channel-info): Get the public "More info" panel of a WeChat Channels account: Channel ID, IP and profile location, and verification details such as entity type, service categ…
- [WeChat Channels User Videos](/apis/wechat-channels/v2/user-videos): Get the videos on a WeChat Channels account's homepage with descriptions, publish time, like, comment, share and favorite counts, and media download info, with…
- [WeChat Channels Video Detail](/apis/wechat-channels/v2/video-detail): Get the full detail of a WeChat Channels video: description, author, engagement counts and the media URL with decode key for download.

---
Machine-readable: [`catalog/models/wechat-channels/v2/channel-id-to-username.json`](../../../../catalog/models/wechat-channels/v2/channel-id-to-username.json) · Store page: https://www.sandbase.ai/model/wechat-channels/v2/channel-id-to-username
