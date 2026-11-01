# WeChat Channels In-Channel Video Search

`wechat-channels/v2/search-channel-videos` · api · WeChat Channels

Search one WeChat Channels creator's videos by keyword, within that channel only. Returns matching video IDs and titles.

## Pricing

- **$0.015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-channels/v2/search-channel-videos", "keyword": "永乐大典", "raw": false, "username": "v2_060000231003b20faec8c6e4811dc1d4c602ee30b0771bbcf220c67926bb76ab7702ac335a53@finder"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-channels/v2/search-channel-videos', {'keyword': '永乐大典', 'raw': False, 'username': 'v2_060000231003b20faec8c6e4811dc1d4c602ee30b0771bbcf220c67926bb76ab7702ac335a53@finder'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-channels/v2/search-channel-videos", {
  "keyword": "永乐大典",
  "raw": false,
  "username": "v2_060000231003b20faec8c6e4811dc1d4c602ee30b0771bbcf220c67926bb76ab7702ac335a53@finder"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-channels/v2/search-channel-videos", sandbase.Params{
	"keyword": "永乐大典",
	"raw": false,
	"username": "v2_060000231003b20faec8c6e4811dc1d4c602ee30b0771bbcf220c67926bb76ab7702ac335a53@finder",
})
```

Same call via the path form: `POST /v1/api/wechat-channels/v2/search-channel-videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `raw` | boolean |  | Optional, default True. True=raw search response; False=simplified parsed structure.  |
| `keyword` | string | yes | Keyword to search within this channel (1-100 chars)  |
| `username` | string | yes | Creator finder username (`v2_…@finder` format). E.g. `v2_060000231003b20faec8c6e4811dc1d4c602ee30b0771bbcf220c67926bb76ab7702ac335a53@finder` (People's Daily).  |

## Details

Pass a finder username and a keyword to search only that creator's published Channels videos.

### Use cases

- Find a specific video in a large channel.
- Check whether a creator has covered a topic or product.
- Build topic archives for media accounts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-channels/v2/search-channel-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "v2_060000231003b20faec8c6e4811dc1d4c602ee30b0771bbcf220c67926bb76ab7702ac335a53@finder", "keyword": "永乐大典", "raw": false}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Keyword to search within this channel (1-100 chars) |
| `username` | string | Yes | Creator finder username (`v2_…@finder` format). |
| `raw` | boolean | No | Optional, default True. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "count": 2,
  "continue_flag": 0,
  "items": [
    {
      "type": "video",
      "doc_id": "finderobjv03bpeXe0scUqXKV+shl…",
      "title": "很多人小时候都读过百科全书。明《永乐大典》被誉为“有史以来规模最大的百科全书”。它命运多舛，散佚四方，如今正被我们一点…"
    }
  ]
}
```

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [WeChat Channels ID to Username](/model/wechat-channels/v2/channel-id-to-username): Convert a public WeChat Channels Channel ID (sph… short ID) into the finder username (v2_…@finder) required by the other WeChat Channels APIs.
- [WeChat Channels Account Info](/model/wechat-channels/v2/channel-info): Get the public "More info" panel of a WeChat Channels account: Channel ID, IP and profile location, and verification details such as entity type, service categ…
- [WeChat Channels User Profile](/model/wechat-channels/v2/user-profile): Get a WeChat Channels creator's profile and stats: nickname, bio, region, follower, video, like and favorite counts, and linked accounts.

---
Machine-readable: [`catalog/models/wechat-channels/v2/search-channel-videos.json`](../../../../catalog/models/wechat-channels/v2/search-channel-videos.json) · Store page: https://www.sandbase.ai/model/wechat-channels/v2/search-channel-videos
