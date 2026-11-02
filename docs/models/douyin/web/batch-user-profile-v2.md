# Douyin Batch User Profile (V2) API: pricing, parameters and code examples

`douyin/web/batch-user-profile-v2` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.15 per call · **Modes:** sync

Retrieves user profile details in batches for up to 50 Douyin accounts at once. Pass comma-separated secure user identifiers to return account data.

## Pricing

- **$0.15 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/batch-user-profile-v2", "sec_user_ids": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/batch-user-profile-v2', {'sec_user_ids': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/batch-user-profile-v2", {
  "sec_user_ids": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/batch-user-profile-v2", sandbase.Params{
	"sec_user_ids": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/web/batch-user-profile-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sec_user_ids` | string | yes | User sec_user_id list, separated by commas, up to 50  |

## Details

Retrieves public profile details for multiple Douyin accounts in a single request. Provide a comma-separated list of account identifiers in `sec_user_ids`.

### Use cases

- Retrieve profiles for multiple Douyin creators in a single query.
- Monitor public account metadata across lists of Douyin users.
- Enrich creator rosters with batch profile data.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/batch-user-profile-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sec_user_ids": "<sec_user_ids>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sec_user_ids` | string | Yes | User sec_user_id list, separated by commas, up to 50 |

### Notes

- Accepts a comma-separated list of up to 50 `sec_user_ids`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Batch Video ID Extraction](/model/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/model/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/model/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/batch-user-profile-v2.json`](../../../../catalog/models/douyin/web/batch-user-profile-v2.json) · Store page: https://www.sandbase.ai/model/douyin/web/batch-user-profile-v2
