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

Retrieve a shareable link for a WeChat Channels video by supplying its `object_id`. Use the optional `raw` parameter to toggle between full and simplified response schemas.

### Use cases

- Retrieve public sharing links for specific WeChat Channels videos.
- Direct users to native WeChat Channels video content via external platforms.
- Automate the collection of video URLs for reporting and distribution workflows.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-channels/v2/video-share-url" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"object_id": "14941130915890399732"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `object_id` | string | Yes | Video objectId (numeric), e.g. |
| `raw` | boolean | No | Optional, default True. |

### Notes

- Find `object_id` from the video `id` returned by user video lists or video detail endpoints.
- Set `raw` to false for a simplified parsed structure, or true (default) for the raw response.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [WeChat Channels ID to Username](/apis/wechat-channels/v2/channel-id-to-username): Convert a public WeChat Channels Channel ID (sph… short ID) into the finder username (v2_…@finder) required by the other WeChat Channels APIs.
- [WeChat Channels Account Info](/apis/wechat-channels/v2/channel-info): Get the public "More info" panel of a WeChat Channels account: Channel ID, IP and profile location, and verification details such as entity type, service categ…
- [WeChat Channels Collection Videos](/apis/wechat-channels/v2/collection-videos): Returns videos contained within a WeChat Channels collection using a collection ID.

---
Machine-readable: [`catalog/models/wechat-channels/v2/video-share-url.json`](../../../../catalog/models/wechat-channels/v2/video-share-url.json) · Store page: https://www.sandbase.ai/model/wechat-channels/v2/video-share-url
