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

Look up a Douyin room ID by providing a `webcast_id`. This endpoint maps a Douyin webcast identifier to its associated livestream room ID.

### Use cases

- Resolve a webcast ID into a livestream room ID for downstream Douyin web queries.
- Normalize live broadcast identifiers across Douyin monitoring workflows.
- Match external webcast links to internal Douyin room identifiers.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/webcast-id-2-room-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"webcast_id": "<webcast_id>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `webcast_id` | string | Yes | Webcast id |

### Notes

- Requires a valid `webcast_id` string.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Batch Video ID Extraction](/model/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/model/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/model/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/webcast-id-2-room-id.json`](../../../../catalog/models/douyin/web/webcast-id-2-room-id.json) · Store page: https://www.sandbase.ai/model/douyin/web/webcast-id-2-room-id
