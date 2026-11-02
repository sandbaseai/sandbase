# Douyin Web User Information API: pricing, parameters and code examples

`douyin/web/query-user` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns basic profile information for a Douyin web user account. The endpoint accepts a ttwid cookie string in the request body to retrieve account details.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/query-user"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/query-user', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/query-user", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/query-user", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/web/query-user` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `body` | string |  | User ttwid cookie. Obtain it by calling `/api/v1/douyin/web/generate_ttwid`.  |

## Details

Retrieve basic profile information for a Douyin account using web credentials. Supply the user ttwid cookie in the `body` parameter.

### Use cases

- Look up basic profile details for a Douyin web user.
- Inspect account information associated with a web session.
- Integrate Douyin user profile verification into web applications.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/query-user" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `body` | string | No | User ttwid cookie. |

### Notes

- Pass the ttwid cookie in `body`, which can be obtained by calling `/api/v1/douyin/web/generate_ttwid`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Batch Video ID Extraction](/model/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/model/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/model/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/query-user.json`](../../../../catalog/models/douyin/web/query-user.json) · Store page: https://www.sandbase.ai/model/douyin/web/query-user
