# Kuaishou Web User Info

`kuaishou/web/user-info` · api · Kuaishou

Returns public profile information for a specified Kuaishou web user. Supply the target user identifier to retrieve account metadata.

## Pricing

- **$0.003 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/web/user-info", "user_id": "3xz63mn6fngqtiq"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/web/user-info', {'user_id': '3xz63mn6fngqtiq'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/web/user-info", {
  "user_id": "3xz63mn6fngqtiq"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/web/user-info", sandbase.Params{
	"user_id": "3xz63mn6fngqtiq",
})
```

Same call via the path form: `POST /v1/api/kuaishou/web/user-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string | yes | 用户 ID (eid)/User ID (eid)  |

## Details

Query public user profile details from Kuaishou by passing the target `user_id` in the request.

### Use cases

- Display Kuaishou creator profile information within internal dashboards.
- Verify account details using a target creator identifier.
- Track public creator profile data over time.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/web/user-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "3xz63mn6fngqtiq"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | — |

### Notes

- The `user_id` parameter is required.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Kuaishou Web Share Short URL](/model/kuaishou/web/generate-share-short-url): Returns a shareable short URL for a specified Kuaishou video or photo post.
- [Kuaishou User ID Lookup](/model/kuaishou/web/get-user-id): Resolves a Kuaishou user ID from a provided user share link.
- [Kuaishou Web Hot List](/model/kuaishou/web/hot-list-v1): Returns the current trending hot list from Kuaishou Web.

---
Machine-readable: [`catalog/models/kuaishou/web/user-info.json`](../../../../catalog/models/kuaishou/web/user-info.json) · Store page: https://www.sandbase.ai/model/kuaishou/web/user-info
