# Douyin Batch User Profile API: pricing, parameters and code examples

`douyin/web/batch-user-profile-v1` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Retrieves public profile information for multiple Douyin accounts in a single request. Specify up to 10 user IDs to return user details in batch.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/batch-user-profile-v1", "sec_user_ids": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/batch-user-profile-v1', {'sec_user_ids': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/batch-user-profile-v1", {
  "sec_user_ids": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/batch-user-profile-v1", sandbase.Params{
	"sec_user_ids": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/web/batch-user-profile-v1` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sec_user_ids` | string | yes | User sec_user_id list, separated by commas, up to 10  |

## Details

Use this endpoint to look up profile data for multiple Douyin creators at once by passing `sec_user_ids`.

### Use cases

- Retrieve profile metadata for a list of Douyin creators simultaneously.
- Monitor multiple user accounts without calling single-profile endpoints individually.
- Enrich internal creator records with batch Douyin user information.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/batch-user-profile-v1" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sec_user_ids": "MS4wLjABAAAANXSltcLCzDGmdNFI2Q_QixVTr67NiYzjKOIP5s03CAE,MS4wLjABAAAAW9FWcqS7RdQAWPd2AA5fL_ilmqsIFUCQ_Iym6Yh9_cUa6ZRqVLjVQSUjlHrfXY1Y"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sec_user_ids` | string | Yes | User sec_user_id list, separated by commas, up to 10 |

### Notes

- `sec_user_ids` accepts a comma-separated list of user identifiers.
- A single request supports a maximum of 10 user IDs.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Batch Video ID Extraction](/apis/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/apis/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/apis/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/batch-user-profile-v1.json`](../../../../catalog/models/douyin/web/batch-user-profile-v1.json) · Store page: https://www.sandbase.ai/model/douyin/web/batch-user-profile-v1
