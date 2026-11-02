# Douyin User Stream Information by UID API: pricing, parameters and code examples

`douyin/web/user-live-info-by-uid` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Retrieves stream session information and broadcast metadata for a Douyin user based on their unique identifier. Accepts a user UID to return stream scene and logging data.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/user-live-info-by-uid", "uid": "7673500446660873006"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/user-live-info-by-uid', {'uid': '7673500446660873006'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/user-live-info-by-uid", {
  "uid": "7673500446660873006"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/user-live-info-by-uid", sandbase.Params{
	"uid": "7673500446660873006",
})
```

Same call via the path form: `POST /v1/api/douyin/web/user-live-info-by-uid` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | User UID  |

## Details

This endpoint retrieves Douyin user broadcast information using a specified `uid`. It returns session identifiers and scene metadata linked to the account.

### Use cases

- Check broadcast status details for a specific Douyin account.
- Track streaming session logs and scene identifiers by user identifier.
- Integrate Douyin creator broadcast data into monitoring dashboards.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/user-live-info-by-uid" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "92769419069"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | User UID |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": [
    {
      "log_id": "20261006204105F5A3868EFFBE457E1D1B",
      "scene_id": 253
    }
  ]
}
```

### Notes

- `uid` is required to identify the target Douyin account.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Batch Video ID Extraction](/model/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/model/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/model/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/user-live-info-by-uid.json`](../../../../catalog/models/douyin/web/user-live-info-by-uid.json) · Store page: https://www.sandbase.ai/model/douyin/web/user-live-info-by-uid
