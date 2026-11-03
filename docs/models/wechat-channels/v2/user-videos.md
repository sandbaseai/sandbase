# WeChat Channels User Videos API: pricing, parameters and code examples

`wechat-channels/v2/user-videos` · data API · WeChat Channels · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Get the videos on a WeChat Channels account's homepage with descriptions, publish time, like, comment, share and favorite counts, and media download info, with cursor pagination.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-channels/v2/user-videos", "raw": false, "username": "v2_060000231003b20faec8c6e4811dc1d4c602ee30b0771bbcf220c67926bb76ab7702ac335a53@finder"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-channels/v2/user-videos', {'raw': False, 'username': 'v2_060000231003b20faec8c6e4811dc1d4c602ee30b0771bbcf220c67926bb76ab7702ac335a53@finder'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-channels/v2/user-videos", {
  "raw": false,
  "username": "v2_060000231003b20faec8c6e4811dc1d4c602ee30b0771bbcf220c67926bb76ab7702ac335a53@finder"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-channels/v2/user-videos", sandbase.Params{
	"raw": false,
	"username": "v2_060000231003b20faec8c6e4811dc1d4c602ee30b0771bbcf220c67926bb76ab7702ac335a53@finder",
})
```

Same call via the path form: `POST /v1/api/wechat-channels/v2/user-videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `raw` | boolean |  | Optional, default True. True=raw response; False=simplified parsed structure (recommended for media download).  |
| `username` | string | yes | WeChat Channels finder username (`v2_…@finder` format), e.g. `v2_060000231003b20faec8c6e4811dc1d4c602ee30b0771bbcf220c67926bb76ab7702ac335a53@finder` (People's Daily). See `fetch_channel_info` / `fetch_video_detail` /…  |
| `last_buffer` |  |  | Optional pagination cursor (base64). **Leave empty for the first page**; when `up_continue` in the response is truthy, pass the previous page's `last_buffer` to get the next page. (base64 contains `+//=` characters,…  |

## Details

Pass a finder username (`v2_…@finder`) and get the account's latest videos. Each video includes engagement counts and a `media` object for download and decryption.

### Use cases

- Monitor new videos from creators or brands.
- Benchmark engagement across a creator's recent posts.
- Archive Channels videos.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-channels/v2/user-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "v2_060000231003b20faec8c6e4811dc1d4c602ee30b0771bbcf220c67926bb76ab7702ac335a53@finder", "raw": false}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | WeChat Channels finder username (`v2_…@finder` format), e.g. |
| `raw` | boolean | No | Optional, default True. |
| `last_buffer` | string | No | Optional pagination cursor (base64). |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "username": "v2_0600002310…@finder",
  "nickname": "人民日报",
  "count": 15,
  "up_continue": 0,
  "last_buffer": "<cursor for next page>",
  "videos": [
    {
      "id": "15026163526991350303",
      "create_time": 1791258278,
      "like_count": 754,
      "comment_count": 27,
      "forward_count": 571,
      "fav_count": 1716,
      "description": "很多人小时候都读过百科全书。明《永乐大典》被誉为“有史以来规模最大的百科全书”。它命运多舛，散佚四…",
      "media": {
        "url": "https://finder.video.qq.com/…",
        "decode_key": "<key>"
      }
    }
  ]
}
```

### Notes

- When `up_continue` is truthy, pass `last_buffer` from the response to get the next page.
- Convert a public Channel ID (`sph…`) to a username with the Channel ID to Username API.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [WeChat Channels ID to Username](/apis/wechat-channels/v2/channel-id-to-username): Convert a public WeChat Channels Channel ID (sph… short ID) into the finder username (v2_…@finder) required by the other WeChat Channels APIs.
- [WeChat Channels Account Info](/apis/wechat-channels/v2/channel-info): Get the public "More info" panel of a WeChat Channels account: Channel ID, IP and profile location, and verification details such as entity type, service categ…
- [WeChat Channels Video Detail](/apis/wechat-channels/v2/video-detail): Get the full detail of a WeChat Channels video: description, author, engagement counts and the media URL with decode key for download.

---
Machine-readable: [`catalog/models/wechat-channels/v2/user-videos.json`](../../../../catalog/models/wechat-channels/v2/user-videos.json) · Store page: https://www.sandbase.ai/model/wechat-channels/v2/user-videos
