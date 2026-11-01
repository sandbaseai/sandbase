# Douyin User Profile by Unique ID

`douyin/web/user-profile-v2` · api · Douyin

Returns profile details and compilation information for a specified Douyin user account based on their unique identifier.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/user-profile-v2", "unique_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/user-profile-v2', {'unique_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/user-profile-v2", {
  "unique_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/user-profile-v2", sandbase.Params{
	"unique_id": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/web/user-profile-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `unique_id` | string | yes | User unique_id  |

## Details

Retrieves profile and compilation details for a specified Douyin user account. Provide the account `unique_id` to look up user data.

### Use cases

- Retrieve public profile details for a Douyin account.
- Access video collection metadata associated with a user.
- Verify user account data using their unique identifier.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/user-profile-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"unique_id": "dyczxzs"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `unique_id` | string | Yes | User unique_id |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "user_info": {
    "mix_info": [
      {
        "mix_id": "7554237184270665754",
        "mix_name": "精选内容创作指南"
      }
    ]
  }
}
```

### Notes

- Supply the user's account handle or ID via the `unique_id` parameter.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Batch Video ID Extraction](/model/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/model/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/model/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/user-profile-v2.json`](../../../../catalog/models/douyin/web/user-profile-v2.json) · Store page: https://www.sandbase.ai/model/douyin/web/user-profile-v2
