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

Returns the public profile and activity counts of one WeChat Channels creator. You pass the creator's finder `username` (`v2_…@finder`) and get back the nickname, bio, region, avatar, video count and linked accounts.

### Use cases

- Check a creator's nickname, bio and linked official account before a partnership.
- Track how many videos a creator has published by storing `feeds_count` over time.
- Show a creator card with avatar, nickname and region in a monitoring dashboard.
- Confirm which official account is tied to a Channels account using `linked_accounts`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-channels/v2/user-profile" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "v2_060000231003b20faec8c6e4811dc1d4c602ee30b0771bbcf220c67926bb76ab7702ac335a53@finder", "raw": false}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | WeChat Channels finder username (`v2_…@finder` format). Source: the `username` field of video objects in `fetch_video_detail` / `fetch_user_videos` responses; or convert a `sph…` short ID via `fetch_channel_id_to_usernam |
| `raw` | boolean | No | Optional, default True. True=raw response; False=simplified parsed structure. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "collection_count": 7,
  "debug_id": "0ee45447",
  "debug_info": "gAAAAABq6ZEnH9WdgXsQOobpv43NXHA_0MTF9o2-BAfG8nDJo4TfZ-O1eCAXdJKShQaPk2x2_ztHBLL6…",
  "fans_count": 0,
  "fav_count": 0,
  "feeds_count": 12780,
  "forward_count": 0,
  "friend_follow_count": 0,
  "head_url": "https://wx.qlogo.cn/finderhead/ver_1/BSLohGHlzpcWnod3wUIyibfNF1kPlm3gE7XnpYdlcCv…",
  "like_count": 0,
  "linked_accounts": [
    {
      "nickname": "人民日报",
      "type": "公众号"
    }
  ],
  "live_duration_hours": 8605
}
```

### Response fields

| Field | Meaning |
|---|---|
| `nickname` | Display name of the creator. |
| `signature` | Bio text shown on the creator's profile. |
| `region` | Region shown on the profile, for example `Beijing`. |
| `feeds_count` | Number of videos on the account. The sample shows `12780`. |
| `fans_count / like_count / fav_count / forward_count / friend_follow_count` | Follower, like, favorite, forward and friend-follow counts. All are `0` in the sample, so check them against the app before relying on them. |
| `collection_count` | Number of collections on the account. The sample shows `7`. |
| `live_duration_hours` | Live stream duration value reported for the account. The sample shows `8605`. |
| `linked_accounts[].nickname / linked_accounts[].type` | Name and type of each linked account. The sample links an account of type `公众号` (official account). |
| `head_url` | URL of the creator's avatar image. |
| `verify_desc` | Verification description text. It is `null` when none is returned. |

### Notes

- Get `username` from the `username` field of video objects returned by [WeChat Channels Video Detail](/apis/wechat-channels/v2/video-detail) or [WeChat Channels User Videos](/apis/wechat-channels/v2/user-videos).
- If you only have a `sph…` short ID, convert it with [WeChat Channels ID to Username](/apis/wechat-channels/v2/channel-id-to-username) first.
- `username` must match the format `v2_<hex>@finder`.
- Set `raw` to `false` for the simplified structure shown here. The default is `true`.

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [WeChat Channels ID to Username](/apis/wechat-channels/v2/channel-id-to-username): Convert a public WeChat Channels Channel ID (sph… short ID) into the finder username (v2_…@finder) required by the other WeChat Channels APIs.
- [WeChat Channels Account Info](/apis/wechat-channels/v2/channel-info): Get the public "More info" panel of a WeChat Channels account: Channel ID, IP and profile location, and verification details such as entity type, service categ…
- [WeChat Channels In-Channel Video Search](/apis/wechat-channels/v2/search-channel-videos): Search one WeChat Channels creator's videos by keyword, within that channel only.

---
Machine-readable: [`catalog/models/wechat-channels/v2/user-profile.json`](../../../../catalog/models/wechat-channels/v2/user-profile.json) · Store page: https://www.sandbase.ai/model/wechat-channels/v2/user-profile
