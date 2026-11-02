# Douyin User Profile by Short ID API: pricing, parameters and code examples

`douyin/web/user-profile-by-short-id` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Retrieves Douyin web user profile details using an account short ID. Returns profile metadata, title information, and engagement counters.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/user-profile-by-short-id", "short_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/user-profile-by-short-id', {'short_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/user-profile-by-short-id", {
  "short_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/user-profile-by-short-id", sandbase.Params{
	"short_id": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/web/user-profile-by-short-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `short_id` | string | yes | User Short ID  |

## Details

Query Douyin web user profiles by passing a target account's `short_id`. The endpoint returns profile information and associated metadata.

### Use cases

- Look up Douyin account profiles using a user short ID.
- Retrieve profile status and engagement counters for specific accounts.
- Inspect web user account metadata for analytics workflows.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/user-profile-by-short-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"short_id": "2941976066"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `short_id` | string | Yes | User Short ID |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "data": [
      {
        "like_count": 0,
        "mosaic_status": 0,
        "status": 4,
        "status_str": "4",
        "title": "动物作者分享",
        "user_count_str": "0"
      }
    ]
  }
}
```

### Notes

- Requires `short_id` as the primary lookup parameter.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Batch Video ID Extraction](/model/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/model/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/model/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/user-profile-by-short-id.json`](../../../../catalog/models/douyin/web/user-profile-by-short-id.json) · Store page: https://www.sandbase.ai/model/douyin/web/user-profile-by-short-id
