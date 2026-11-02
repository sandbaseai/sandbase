# Douyin UID to Sec User ID API: pricing, parameters and code examples

`douyin/web/encrypt-uid-to-sec-user-id` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Converts a standard Douyin user UID into an encrypted sec_user_id. It takes a short_id value and returns the corresponding secure identifier.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/encrypt-uid-to-sec-user-id", "uid": "92769419069"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/encrypt-uid-to-sec-user-id', {'uid': '92769419069'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/encrypt-uid-to-sec-user-id", {
  "uid": "92769419069"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/encrypt-uid-to-sec-user-id", sandbase.Params{
	"uid": "92769419069",
})
```

Same call via the path form: `POST /v1/api/douyin/web/encrypt-uid-to-sec-user-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | User uid, which is the short_id of the Douyin number  |

## Details

Retrieve the encrypted secure user identifier for Douyin profiles by providing a target `uid`.

### Use cases

- Convert standard Douyin short IDs into secure identifiers.
- Prepare secure user identifiers required by Douyin web endpoints.
- Resolve user identifiers across profile-related lookup workflows.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/encrypt-uid-to-sec-user-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "92769419069"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | User uid, which is the short_id of the Douyin number |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "sec_user_id": "<user>"
}
```

### Notes

- The `uid` parameter expects the user UID, which corresponds to the short_id of the Douyin number.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Batch Video ID Extraction](/model/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/model/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/model/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/encrypt-uid-to-sec-user-id.json`](../../../../catalog/models/douyin/web/encrypt-uid-to-sec-user-id.json) · Store page: https://www.sandbase.ai/model/douyin/web/encrypt-uid-to-sec-user-id
