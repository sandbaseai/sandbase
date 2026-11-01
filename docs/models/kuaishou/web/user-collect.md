# Kuaishou User Favorites

`kuaishou/web/user-collect` · api · Kuaishou

Retrieves the list of collected or favorited items for a specified Kuaishou account. Supports pagination through cursor tokens to browse older entries.

## Pricing

- **$0.015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/web/user-collect", "user_id": "3795214411"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/web/user-collect', {'user_id': '3795214411'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/web/user-collect", {
  "user_id": "3795214411"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/web/user-collect", sandbase.Params{
	"user_id": "3795214411",
})
```

Same call via the path form: `POST /v1/api/kuaishou/web/user-collect` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `pcursor` | string |  | 作品游标/Post cursor  |
| `user_id` | string | yes | 用户 ID (eid)/User ID (eid)  |

## Details

Retrieve favorite items for an account by providing `user_id`. Use `pcursor` to navigate across paginated result sets.

### Use cases

- Inspect publicly favorited videos from a specific Kuaishou profile.
- Track content preferences and saved media for audience research.
- Collect favorited video lists for archival and monitoring tasks.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/web/user-collect" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "3795214411"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | — |
| `pcursor` | string | No | — |

### Notes

- Requires `user_id` to identify the account.
- Pass `pcursor` to paginate through subsequent pages of results.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Kuaishou Web Share Short URL](/model/kuaishou/web/generate-share-short-url): Returns a shareable short URL for a specified Kuaishou video or photo post.
- [Kuaishou User ID Lookup](/model/kuaishou/web/get-user-id): Resolves a Kuaishou user ID from a provided user share link.
- [Kuaishou Web Hot List](/model/kuaishou/web/hot-list-v1): Returns the current trending hot list from Kuaishou Web.

---
Machine-readable: [`catalog/models/kuaishou/web/user-collect.json`](../../../../catalog/models/kuaishou/web/user-collect.json) · Store page: https://www.sandbase.ai/model/kuaishou/web/user-collect
