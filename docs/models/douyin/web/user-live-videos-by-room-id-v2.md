# Douyin Stream Data by Room ID (V2)

`douyin/web/user-live-videos-by-room-id-v2` · api · Douyin

Returns stream data for a specified Douyin user using a room identifier. Provide a valid room ID to inspect stream metadata and broadcast details.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/user-live-videos-by-room-id-v2", "room_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/user-live-videos-by-room-id-v2', {'room_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/user-live-videos-by-room-id-v2", {
  "room_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/user-live-videos-by-room-id-v2", sandbase.Params{
	"room_id": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/web/user-live-videos-by-room-id-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `room_id` | string | yes | Room room_id  |

## Details

This endpoint retrieves stream details for a specific user based on `room_id`. Call it to inspect broadcast metadata and session information.

### Use cases

- Retrieve broadcast details for a Douyin stream session using a room identifier.
- Track broadcaster stream performance and metadata across specific room sessions.
- Verify stream status and session details for specific user rooms.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/user-live-videos-by-room-id-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"room_id": "<room_id>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `room_id` | string | Yes | Room room_id |

### Notes

- Requires a valid `room_id` string to identify the target room.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Batch Video ID Extraction](/model/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/model/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/model/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/user-live-videos-by-room-id-v2.json`](../../../../catalog/models/douyin/web/user-live-videos-by-room-id-v2.json) · Store page: https://www.sandbase.ai/model/douyin/web/user-live-videos-by-room-id-v2
