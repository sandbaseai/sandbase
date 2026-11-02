# WeChat Channels Collection Videos API: pricing, parameters and code examples

`wechat-channels/v2/collection-videos` · data API · WeChat Channels · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns videos contained within a WeChat Channels collection using a collection ID. Provides video media URLs, decryption keys, and pagination cursors.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-channels/v2/collection-videos", "topic_id": "<topic_id>"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-channels/v2/collection-videos', {'topic_id': '<topic_id>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-channels/v2/collection-videos", {
  "topic_id": "<topic_id>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-channels/v2/collection-videos", sandbase.Params{
	"topic_id": "<topic_id>",
})
```

Same call via the path form: `POST /v1/api/wechat-channels/v2/collection-videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `raw` | boolean |  | Optional, default True. True=raw response; False=simplified parsed structure (recommended for media download).  |
| `topic` |  |  | Collection name (optional, improves hit rate)  |
| `topic_id` | string | yes | Collection ID (numeric, from topic_id of fetch_user_collections)  |
| `username` |  |  | Optional, creator finder username (`v2_…@finder` format), improves hit rate.  |
| `topic_type` | integer |  | Optional, collection type, default 16 (align with the collection's `topic_type` from `fetch_user_collections`). range 0–1000 |
| `last_buffer` |  |  | Optional pagination cursor (base64), **leave empty for the first page**; when `down_continue` is truthy, pass the previous page's `last_buffer`.  |

## Details

Fetch all videos listed in a specific WeChat Channels collection by providing `topic_id`. Supports cursor-based pagination via `last_buffer`.

### Use cases

- List all videos organized within a specific creator collection.
- Obtain media download URLs and decryption keys for collection videos.
- Paginate through extended multi-video collections using cursor buffers.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-channels/v2/collection-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"topic_id": "<topic_id>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `topic_id` | string | Yes | Collection ID (numeric, from topic_id of fetch_user_collections) |
| `raw` | boolean | No | Optional, default True. |
| `topic` | string | No | Collection name (optional, improves hit rate) |
| `username` | string | No | Optional, creator finder username (`v2_…@finder` format), improves hit rate. |
| `topic_type` | integer | No | Optional, collection type, default 16 (align with the collection's `topic_type` from `fetch_user_collections`). |
| `last_buffer` | string | No | Optional pagination cursor (base64), leave empty for the first page; when `down_continue` is truthy, pass the previous page's `last_buffer`. |

### Notes

- Obtain `topic_id` and `topic_type` from user collection lookups.
- Leave `last_buffer` empty for the first page and pass the returned buffer when further pages exist.
- Set `raw` to false to receive a simplified structure formatted for media downloads.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [WeChat Channels ID to Username](/model/wechat-channels/v2/channel-id-to-username): Convert a public WeChat Channels Channel ID (sph… short ID) into the finder username (v2_…@finder) required by the other WeChat Channels APIs.
- [WeChat Channels Account Info](/model/wechat-channels/v2/channel-info): Get the public "More info" panel of a WeChat Channels account: Channel ID, IP and profile location, and verification details such as entity type, service categ…
- [WeChat Channels Stream Detail](/model/wechat-channels/v2/live-detail): Returns live-room details including anchor info, status, online count, and replay data using a live ID.

---
Machine-readable: [`catalog/models/wechat-channels/v2/collection-videos.json`](../../../../catalog/models/wechat-channels/v2/collection-videos.json) · Store page: https://www.sandbase.ai/model/wechat-channels/v2/collection-videos
