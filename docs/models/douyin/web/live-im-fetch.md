# Douyin Room Danmaku Parameters API: pricing, parameters and code examples

`douyin/web/live-im-fetch` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Retrieves chat and danmaku parameters for a Douyin broadcast session. Requires the target room identifier and user unique identifier.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/live-im-fetch", "room_id": "example", "user_unique_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/live-im-fetch', {'room_id': 'example', 'user_unique_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/live-im-fetch", {
  "room_id": "example",
  "user_unique_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/live-im-fetch", sandbase.Params{
	"room_id": "example",
	"user_unique_id": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/web/live-im-fetch` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `room_id` | string | yes | Live room id  |
| `user_unique_id` | string | yes | User unique ID  |

## Details

Retrieve danmaku and chat parameters for Douyin broadcasts using `room_id` and `user_unique_id`. This endpoint provides connection parameters for broadcast chat streams.

### Use cases

- Collect chat and danmaku feeds during Douyin broadcasts.
- Analyze viewer interactions and audience comments in real time.
- Monitor engagement metrics for specific broadcast rooms.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/live-im-fetch" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"room_id": "7382517534467115826", "user_unique_id": "7382524529011246630"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `room_id` | string | Yes | Live room id |
| `user_unique_id` | string | Yes | User unique ID |

### Notes

- Requires a valid `room_id` representing the broadcast room.
- Requires `user_unique_id` to establish the chat stream connection.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Batch Video ID Extraction](/apis/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/apis/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/apis/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/live-im-fetch.json`](../../../../catalog/models/douyin/web/live-im-fetch.json) · Store page: https://www.sandbase.ai/model/douyin/web/live-im-fetch
