# Bilibili Room Stream Data API: pricing, parameters and code examples

`bilibili/web/live-videos` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns stream URLs and playback connection details for a specific Bilibili broadcast room. Filter using the unique room identifier.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/web/live-videos", "room_id": "1815229528"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/web/live-videos', {'room_id': '1815229528'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/web/live-videos", {
  "room_id": "1815229528"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/web/live-videos", sandbase.Params{
	"room_id": "1815229528",
})
```

Same call via the path form: `POST /v1/api/bilibili/web/live-videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `room_id` | string | yes | Live room ID  |

## Details

Retrieve stream playback addresses and transmission parameters for a Bilibili room. Specify the target broadcast room using `room_id`.

### Use cases

- Access direct media stream links for active Bilibili broadcasts.
- Integrate Bilibili stream playback into external player interfaces.
- Inspect streaming protocol types and transmission endpoints for a room.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/live-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"room_id": "1815229528"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `room_id` | string | Yes | Live room ID |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "durl": [
      {
        "p2p_type": -1,
        "stream_type": 0,
        "url": "https://d1--ov-gotcha07.bilivideo.com/live-bvc/538254/live_1777360364_82518558.f…"
      }
    ]
  }
}
```

### Notes

- Supply the broadcast room identifier via `room_id`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Bilibili Streaming Areas](/apis/bilibili/web/all-live-areas): Returns the complete list of streaming broadcast areas and categories on Bilibili.
- [Bilibili BV to AID Converter](/apis/bilibili/web/bv-to-aid): Converts a Bilibili BV identifier to its corresponding numeric AID value.
- [Bilibili User Collection Folders](/apis/bilibili/web/collect-folders): Returns the collection folders owned by a specific Bilibili user.

---
Machine-readable: [`catalog/models/bilibili/web/live-videos.json`](../../../../catalog/models/bilibili/web/live-videos.json) · Store page: https://www.sandbase.ai/model/bilibili/web/live-videos
