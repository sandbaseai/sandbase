# WeChat Channels Video Share URL API: pricing, parameters and code examples

`wechat-channels/v2/video-share-url` · data API · WeChat Channels · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns the share URL for a specific WeChat Channels video using its numeric object ID. Supports both raw and simplified parsed response formats.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-channels/v2/video-share-url", "object_id": "14941130915890399732"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-channels/v2/video-share-url', {'object_id': '14941130915890399732'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-channels/v2/video-share-url", {
  "object_id": "14941130915890399732"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-channels/v2/video-share-url", sandbase.Params{
	"object_id": "14941130915890399732",
})
```

Same call via the path form: `POST /v1/api/wechat-channels/v2/video-share-url` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `raw` | boolean |  | Optional, default True. True=raw response; False=simplified parsed structure.  |
| `object_id` | string | yes | Video objectId (numeric), e.g. `14941130915890399732`. From the video `id` of `fetch_user_videos` / `fetch_video_detail`.  |

## Details

Returns the public share URL for a WeChat Channels video. It needs the numeric `object_id` of the video and returns a short `weixin.qq.com/sph/...` link.

### Use cases

- Build a list of shareable links for videos you collected from a channel.
- Add a clickable WeChat Channels link to a report or spreadsheet that already holds video IDs.
- Check that a video `object_id` still resolves to a link before you publish it elsewhere.
- Send a share link to a user from an app that tracks WeChat Channels videos.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-channels/v2/video-share-url" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"object_id": "14941130915890399732"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `object_id` | string | Yes | Video objectId (numeric), e.g. `14941130915890399732`. From the video `id` of `fetch_user_videos` / `fetch_video_detail`. |
| `raw` | boolean | No | Optional, default True. True=raw response; False=simplified parsed structure. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "baseResponse": {
    "errMsg": {
      "pbRequestMsgInfo": null,
      "string": ""
    },
    "pbRequestMsgInfo": null,
    "ret": 0
  },
  "debug_id": "af3be523",
  "debug_info": "gAAAAABq6ZEqPk4z1vRiD4BkXYJ1vs5NqAg3czDYG8Tn1QYQUux9zbT-rgf724H9718E0u-cGQlmdi1c…",
  "feedH5Url": "https://weixin.qq.com/sph/An9q68ZQCn",
  "pbRequestMsgInfo": null,
  "urlList": [
    {
      "feedH5Url": "https://weixin.qq.com/sph/An9q68ZQCn",
      "objectId": 14941130915890399732,
      "pbRequestMsgInfo": null
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `feedH5Url` | The share URL for the video. It is a short `https://weixin.qq.com/sph/...` link. |
| `urlList[].feedH5Url` | The same share URL, returned inside a list of results. |
| `urlList[].objectId` | The numeric video ID that the URL belongs to. It matches the `object_id` you sent. |
| `baseResponse.ret` | Status code of the lookup. `0` means the call succeeded in this response. |
| `baseResponse.errMsg.string` | Error message text. It is empty when the call succeeds. |
| `debug_id` | Short identifier for this response. Useful when you report a problem. |

### Notes

- Get `object_id` from the video `id` returned by [WeChat Channels User Videos](/apis/wechat-channels/v2/user-videos) or [WeChat Channels Video Detail](/apis/wechat-channels/v2/video-detail).
- `object_id` must be digits only, up to 32 characters. Send it as a string.
- `raw` defaults to `true`, which returns the full structure shown here. Set it to `false` for a simplified parsed structure.
- In `urlList[]`, `objectId` is a number, while the request `object_id` is a string.

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [WeChat Channels ID to Username](/apis/wechat-channels/v2/channel-id-to-username): Convert a public WeChat Channels Channel ID (sph… short ID) into the finder username (v2_…@finder) required by the other WeChat Channels APIs.
- [WeChat Channels Account Info](/apis/wechat-channels/v2/channel-info): Get the public "More info" panel of a WeChat Channels account: Channel ID, IP and profile location, and verification details such as entity type, service categ…
- [WeChat Channels Collection Videos](/apis/wechat-channels/v2/collection-videos): Returns videos contained within a WeChat Channels collection using a collection ID.

---
Machine-readable: [`catalog/models/wechat-channels/v2/video-share-url.json`](../../../../catalog/models/wechat-channels/v2/video-share-url.json) · Store page: https://www.sandbase.ai/model/wechat-channels/v2/video-share-url
