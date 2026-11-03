# WeChat Channels User Profile API: pricing, parameters and code examples

`wechat-channels/v2/user-profile` · data API · WeChat Channels · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Get a WeChat Channels creator's profile and stats: nickname, bio, region, follower, video, like and favorite counts, and linked accounts.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-channels/v2/user-profile", "raw": false, "username": "v2_060000231003b20faec8c6e4811dc1d4c602ee30b0771bbcf220c67926bb76ab7702ac335a53@finder"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-channels/v2/user-profile', {'raw': False, 'username': 'v2_060000231003b20faec8c6e4811dc1d4c602ee30b0771bbcf220c67926bb76ab7702ac335a53@finder'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-channels/v2/user-profile", {
  "raw": false,
  "username": "v2_060000231003b20faec8c6e4811dc1d4c602ee30b0771bbcf220c67926bb76ab7702ac335a53@finder"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-channels/v2/user-profile", sandbase.Params{
	"raw": false,
	"username": "v2_060000231003b20faec8c6e4811dc1d4c602ee30b0771bbcf220c67926bb76ab7702ac335a53@finder",
})
```

Same call via the path form: `POST /v1/api/wechat-channels/v2/user-profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `raw` | boolean |  | Optional, default True. True=raw response; False=simplified parsed structure.  |
| `username` | string | yes | WeChat Channels finder username (`v2_…@finder` format). Source: the `username` field of video objects in `fetch_video_detail` / `fetch_user_videos` responses; or convert a `sph…` short ID via…  |

## Details

Pass a finder username (`v2_…@finder`) and get the creator's homepage profile and interaction statistics.

### Use cases

- Vet Channels creators before partnerships.
- Track creator growth.
- Combine with User Videos for full creator reports.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-channels/v2/user-profile" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "v2_060000231003b20faec8c6e4811dc1d4c602ee30b0771bbcf220c67926bb76ab7702ac335a53@finder", "raw": false}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | WeChat Channels finder username (`v2_…@finder` format). |
| `raw` | boolean | No | Optional, default True. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "username": "v2_0600002310…@finder",
  "nickname": "人民日报",
  "signature": "参与、沟通、记录时代。",
  "region": "Beijing",
  "fans_count": 0,
  "feeds_count": 12331,
  "like_count": 0,
  "fav_count": 0,
  "forward_count": 0,
  "collection_count": 7
}
```

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [WeChat Channels ID to Username](/apis/wechat-channels/v2/channel-id-to-username): Convert a public WeChat Channels Channel ID (sph… short ID) into the finder username (v2_…@finder) required by the other WeChat Channels APIs.
- [WeChat Channels Account Info](/apis/wechat-channels/v2/channel-info): Get the public "More info" panel of a WeChat Channels account: Channel ID, IP and profile location, and verification details such as entity type, service categ…
- [WeChat Channels In-Channel Video Search](/apis/wechat-channels/v2/search-channel-videos): Search one WeChat Channels creator's videos by keyword, within that channel only.

---
Machine-readable: [`catalog/models/wechat-channels/v2/user-profile.json`](../../../../catalog/models/wechat-channels/v2/user-profile.json) · Store page: https://www.sandbase.ai/model/wechat-channels/v2/user-profile
