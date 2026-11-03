# Douyin User Profile by UID API: pricing, parameters and code examples

`douyin/web/user-profile-by-uid` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns public profile details, badge lists, and account metadata for a Douyin web user by querying their unique identifier.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/user-profile-by-uid", "uid": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/user-profile-by-uid', {'uid': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/user-profile-by-uid", {
  "uid": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/user-profile-by-uid", sandbase.Params{
	"uid": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/web/user-profile-by-uid` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | User UID  |

## Details

Retrieves Douyin web user profile data using the `uid` parameter. Use it to inspect public account badges and user information.

### Use cases

- Look up profile details for a Douyin user by user ID.
- Inspect badge lists associated with a Douyin account.
- Check Douyin user metadata for profile display.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/user-profile-by-uid" \
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
  "data": {
    "badge_image_list": [
      {
        "image_type": 1,
        "content": {
          "alternative_text": "荣誉等级0级勋章"
        }
      }
    ]
  }
}
```

### Notes

- Requires a valid Douyin user identifier in `uid`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Batch Video ID Extraction](/apis/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/apis/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/apis/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/user-profile-by-uid.json`](../../../../catalog/models/douyin/web/user-profile-by-uid.json) · Store page: https://www.sandbase.ai/model/douyin/web/user-profile-by-uid
