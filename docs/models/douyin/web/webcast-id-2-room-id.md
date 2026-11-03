# Douyin Webcast ID to Room ID API: pricing, parameters and code examples

`douyin/web/webcast-id-2-room-id` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Converts a Douyin webcast ID into its corresponding room ID. Submit a webcast ID to retrieve the matching livestream room identifier for Douyin web workflows.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/webcast-id-2-room-id", "webcast_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/webcast-id-2-room-id', {'webcast_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/webcast-id-2-room-id", {
  "webcast_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/webcast-id-2-room-id", sandbase.Params{
	"webcast_id": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/web/webcast-id-2-room-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `webcast_id` | string | yes | Webcast id  |

## Details

This API converts a Douyin webcast ID into the livestream room ID that matches it. It needs one input, `webcast_id`, and returns a single `room_id` value.

### Use cases

- Convert a webcast ID taken from a Douyin live link into a room ID for room-based lookups.
- Store room IDs next to webcast IDs so you can match the same livestream across your own records.
- Prepare the room ID needed to request live stream data for a Douyin broadcast.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/webcast-id-2-room-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"webcast_id": "775841227732"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `webcast_id` | string | Yes | Webcast id |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "room_id": "7624919954380180276"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `room_id` | The livestream room ID that matches the submitted `webcast_id`. This is the only field in the response. |
| `room_id` | The value is a string of digits, such as `7624919954380180276`. Keep it as a string so tools do not round the long number. |
| `room_id` | Use this value as the room identifier in other Douyin live APIs that ask for a room ID. |

### Notes

- Send `webcast_id` as a string. The example value is `775841227732`.
- To get webcast IDs from live room links, call [Douyin Webcast ID Extraction](/apis/douyin/web/all-webcast-id).
- To get stream data for a room, call [Douyin Stream Data by Room ID (V2)](/apis/douyin/web/user-live-videos-by-room-id-v2) with the returned `room_id`.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Batch Video ID Extraction](/apis/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/apis/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/apis/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/webcast-id-2-room-id.json`](../../../../catalog/models/douyin/web/webcast-id-2-room-id.json) · Store page: https://www.sandbase.ai/model/douyin/web/webcast-id-2-room-id
