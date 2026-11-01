# WeChat Channels Stream Detail

`wechat-channels/v2/live-detail` · api · WeChat Channels

Returns live-room details including anchor info, status, online count, and replay data using a live ID. Allows switching between raw and parsed output formats.

## Pricing

- **$0.015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-channels/v2/live-detail", "live_id": "2078950291205875194"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-channels/v2/live-detail', {'live_id': '2078950291205875194'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-channels/v2/live-detail", {
  "live_id": "2078950291205875194"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-channels/v2/live-detail", sandbase.Params{
	"live_id": "2078950291205875194",
})
```

Same call via the path form: `POST /v1/api/wechat-channels/v2/live-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `raw` | boolean |  | Optional, default True. True=raw response; False=simplified parsed structure.  |
| `scene` | integer |  | Optional, entry scene, default 5. range 0–1000 |
| `live_id` | string | yes | Live ID (numeric). Source: replay items of `fetch_live_history`, live entry, or live share. E.g. `2078950291205875194`.  |
| `finder_username` |  |  | Optional, anchor finder username (`v2_…@finder` format), improves hit rate. E.g. `v2_060000231003b20faec8cae1811ac4d5c702ea32b0771737aa785454f7f8177114cc4d248d66@finder` (Huxiu).  |

## Details

Retrieve detailed room metrics, anchor information, and replay availability by passing a target `live_id` and optional `finder_username`.

### Use cases

- Inspect anchor information and real-time room status.
- Check online viewer counts during an active session.
- Retrieve replay details from completed broadcasts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-channels/v2/live-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"live_id": "<live_id>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `live_id` | string | Yes | Live ID (numeric). |
| `raw` | boolean | No | Optional, default True. |
| `scene` | integer | No | Optional, entry scene, default 5. |
| `finder_username` | string | No | Optional, anchor finder username (`v2_…@finder` format), improves hit rate. |

### Notes

- Set `raw` to false to obtain a simplified parsed response instead of the raw payload.
- Providing `finder_username` alongside `live_id` improves lookup accuracy.
- The `live_id` can be obtained from broadcast history items, entry points, or share links.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [WeChat Channels ID to Username](/model/wechat-channels/v2/channel-id-to-username): Convert a public WeChat Channels Channel ID (sph… short ID) into the finder username (v2_…@finder) required by the other WeChat Channels APIs.
- [WeChat Channels Account Info](/model/wechat-channels/v2/channel-info): Get the public "More info" panel of a WeChat Channels account: Channel ID, IP and profile location, and verification details such as entity type, service categ…
- [WeChat Channels Collection Videos](/model/wechat-channels/v2/collection-videos): Returns videos contained within a WeChat Channels collection using a collection ID.

---
Machine-readable: [`catalog/models/wechat-channels/v2/live-detail.json`](../../../../catalog/models/wechat-channels/v2/live-detail.json) · Store page: https://www.sandbase.ai/model/wechat-channels/v2/live-detail
