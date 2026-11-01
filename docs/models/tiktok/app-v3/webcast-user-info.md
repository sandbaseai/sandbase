# TikTok Webcast User Information

`tiktok/app-v3/webcast-user-info` · api · TikTok

Retrieves profile information for a specified TikTok Webcast user. Queries data using either a numeric user ID or a secure user ID.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/webcast-user-info", "user_id": "7016736142473561094"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/webcast-user-info', {'user_id': '7016736142473561094'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/webcast-user-info", {
  "user_id": "7016736142473561094"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/webcast-user-info", sandbase.Params{
	"user_id": "7016736142473561094",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/webcast-user-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string |  | User uid, optional parameter, pure number, if used, please keep sec_user_id and unique_id empty. default `""` |
| `sec_user_id` | string |  | User sec_user_id default `""` |

## Details

Query Webcast user profile details on TikTok by providing `user_id` or `sec_user_id`.

### Use cases

- Inspect broadcaster account metadata for live streams.
- Look up creator information using numeric user IDs or secure IDs.
- Verify account identifiers across live webcast sessions.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/webcast-user-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | No | User uid, optional parameter, pure number, if used, please keep sec_user_id and unique_id empty. |
| `sec_user_id` | string | No | User sec_user_id |

### Notes

- When `user_id` is used, ensure `sec_user_id` and `unique_id` remain empty.
- The `user_id` parameter accepts a purely numeric string.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok LIVE Status](/model/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/model/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/model/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/webcast-user-info.json`](../../../../catalog/models/tiktok/app-v3/webcast-user-info.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/webcast-user-info
