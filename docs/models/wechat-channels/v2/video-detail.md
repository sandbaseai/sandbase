# WeChat Channels Video Detail

`wechat-channels/v2/video-detail` · api · WeChat Channels

Get the full detail of a WeChat Channels video: description, author, engagement counts and the media URL with decode key for download. Look up by object ID, export ID or share URL.

## Pricing

- **$0.015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-channels/v2/video-detail", "object_id": "15026240326408735234", "raw": false}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-channels/v2/video-detail', {'object_id': '15026240326408735234', 'raw': False})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-channels/v2/video-detail", {
  "object_id": "15026240326408735234",
  "raw": false
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-channels/v2/video-detail", sandbase.Params{
	"object_id": "15026240326408735234",
	"raw": false,
})
```

Same call via the path form: `POST /v1/api/wechat-channels/v2/video-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `raw` | boolean |  | Optional, default True. True=raw response; False=simplified parsed structure (recommended for media download).  |
| `export_id` |  |  | Second priority, optional. `exportId` from search results (must start with `export/`). Search results often only carry `exportId` without a plain object_id — pass export_id directly in that case (it expires, use it…  |
| `object_id` |  |  | Highest priority, optional. Video objectId (numeric), e.g. `14941130915890399732`. Obtainable from the video `id` of `fetch_user_videos` / `fetch_collection_videos`.  |
| `share_url` |  |  | Last, optional. Channels share URL (`https://weixin.qq.com/sph/…`), e.g. `https://weixin.qq.com/sph/AH3sCoIPhH`. Used only when both object_id and export_id are empty.  |
| `object_nonce_id` |  |  | Optional. `feedNonceId` (numeric) from search results, pairs with the above to improve hit rate.  |

## Details

Pass a Channels video `object_id`, `export_id` or share URL and get the video detail, including the `media` address and `decode_key` needed to download it.

### Use cases

- Download and archive Channels videos.
- Get full details for videos found in search.
- Track engagement on a specific video.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-channels/v2/video-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"object_id": "15026240326408735234", "raw": false}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `raw` | boolean | No | Optional, default True. |
| `export_id` | string | No | Second priority, optional. |
| `object_id` | string | No | Highest priority, optional. |
| `share_url` | string | No | Last, optional. |
| `object_nonce_id` | string | No | Optional. |

### Notes

- Priority when several inputs are given: `object_id` > `export_id` > `share_url`.
- Requests with invalid parameters are still processed by WeChat and billed upstream.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [WeChat Channels ID to Username](/model/wechat-channels/v2/channel-id-to-username): Convert a public WeChat Channels Channel ID (sph… short ID) into the finder username (v2_…@finder) required by the other WeChat Channels APIs.
- [WeChat Channels Account Info](/model/wechat-channels/v2/channel-info): Get the public "More info" panel of a WeChat Channels account: Channel ID, IP and profile location, and verification details such as entity type, service categ…
- [WeChat Channels User Videos](/model/wechat-channels/v2/user-videos): Get the videos on a WeChat Channels account's homepage with descriptions, publish time, like, comment, share and favorite counts, and media download info, with…

---
Machine-readable: [`catalog/models/wechat-channels/v2/video-detail.json`](../../../../catalog/models/wechat-channels/v2/video-detail.json) · Store page: https://www.sandbase.ai/model/wechat-channels/v2/video-detail
