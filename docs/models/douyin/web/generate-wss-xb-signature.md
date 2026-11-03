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

This endpoint produces an xb signature required for Douyin web barrage stream connections. Supply `room_id`, `user_agent`, and `user_unique_id` to obtain the signature value.

### Use cases

- Obtaining signature parameters for web barrage connections.
- Connecting to Douyin chat streams with valid browser headers.
- Authenticating WebSocket sessions using a room identifier.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/generate-wss-xb-signature" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"room_id": "7382517534467115826", "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0", "user_unique_id": "7382524529011246630"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `room_id` | string | Yes | Room ID |
| `user_agent` | string | Yes | User browser agent |
| `user_unique_id` | string | Yes | User unique ID |

### Notes

- `room_id` is required to specify the target room.
- Supply `user_agent` corresponding to the client browser environment.
- `user_unique_id` represents the unique viewer identifier.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Batch Video ID Extraction](/apis/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/apis/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/apis/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/generate-wss-xb-signature.json`](../../../../catalog/models/douyin/web/generate-wss-xb-signature.json) · Store page: https://www.sandbase.ai/model/douyin/web/generate-wss-xb-signature
