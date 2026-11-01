# Bilibili Live Room Details

`bilibili/web/live-room-detail` · api · Bilibili

Returns detailed metadata and status information for a specified Bilibili live broadcast room based on the provided room identifier.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/web/live-room-detail", "room_id": "22816111"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/web/live-room-detail', {'room_id': '22816111'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/web/live-room-detail", {
  "room_id": "22816111"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/web/live-room-detail", sandbase.Params{
	"room_id": "22816111",
})
```

Same call via the path form: `POST /v1/api/bilibili/web/live-room-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `room_id` | string | yes | Live room ID  |

## Details

Retrieve detailed live stream information for a specific Bilibili room by providing the target `room_id`.

### Use cases

- Monitor the status of a specific Bilibili live room.
- Retrieve stream metadata for display in external dashboards.
- Verify live room availability before directing viewers.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/live-room-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"room_id": "22816111"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `room_id` | string | Yes | Live room ID |

### Notes

- Provide the target live broadcast identifier using `room_id`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Bilibili Streaming Areas](/model/bilibili/web/all-live-areas): Returns the complete list of streaming broadcast areas and categories on Bilibili.
- [Bilibili BV to AID Converter](/model/bilibili/web/bv-to-aid): Converts a Bilibili BV identifier to its corresponding numeric AID value.
- [Bilibili User Collection Folders](/model/bilibili/web/collect-folders): Returns the collection folders owned by a specific Bilibili user.

---
Machine-readable: [`catalog/models/bilibili/web/live-room-detail.json`](../../../../catalog/models/bilibili/web/live-room-detail.json) · Store page: https://www.sandbase.ai/model/bilibili/web/live-room-detail
