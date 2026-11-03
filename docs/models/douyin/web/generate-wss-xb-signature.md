# Douyin Barrage WSS XB Signature API: pricing, parameters and code examples

`douyin/web/generate-wss-xb-signature` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a signed xb parameter for Douyin web barrage WebSocket connections using a specified room ID, user browser agent, and unique user identifier.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/generate-wss-xb-signature", "room_id": "example", "user_agent": "example", "user_unique_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/generate-wss-xb-signature', {'room_id': 'example', 'user_agent': 'example', 'user_unique_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/generate-wss-xb-signature", {
  "room_id": "example",
  "user_agent": "example",
  "user_unique_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/generate-wss-xb-signature", sandbase.Params{
	"room_id": "example",
	"user_agent": "example",
	"user_unique_id": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/web/generate-wss-xb-signature` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `room_id` | string | yes | Room ID  |
| `user_agent` | string | yes | User browser agent  |
| `user_unique_id` | string | yes | User unique ID  |

## Details

Returns a signature string for a Douyin live room barrage (danmaku) WebSocket connection. It needs a `room_id`, a browser `user_agent` string, and a `user_unique_id`.

### Use cases

- Sign a Douyin live room WebSocket URL before you open the barrage stream.
- Generate a signature for each viewer identity when you run several chat listeners.
- Pair the signature with the same `user_agent` you send in your WebSocket headers.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/generate-wss-xb-signature" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"room_id": "7382517534467115826", "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0", "user_unique_id": "7382524529011246630"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `room_id` | string | Yes | Room ID |
| `user_agent` | string | Yes | User browser agent |
| `user_unique_id` | string | Yes | User unique ID |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "x_bogus": "6kux4VFjvCR1Mnox"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `x_bogus` | The signature string. The response holds only this one key, and its value is a short string such as `6kux4VFjvCR1Mnox`. |
| `x_bogus` | The value is built from the `room_id`, `user_agent`, and `user_unique_id` you sent. A different input set gives a different signature. |
| `x_bogus` | Use this value as the xb signature in the barrage WebSocket connection for that room. |

### Notes

- If you only have a webcast ID, convert it to a `room_id` with [Douyin Webcast ID to Room ID](/apis/douyin/web/webcast-id-2-room-id).
- Use the same `user_agent` and `user_unique_id` in the WebSocket connection that you used to create the signature.
- Call [Douyin Room Danmaku Parameters](/apis/douyin/web/live-im-fetch) to get more parameters for the barrage connection.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Batch Video ID Extraction](/apis/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/apis/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/apis/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/generate-wss-xb-signature.json`](../../../../catalog/models/douyin/web/generate-wss-xb-signature.json) · Store page: https://www.sandbase.ai/model/douyin/web/generate-wss-xb-signature
