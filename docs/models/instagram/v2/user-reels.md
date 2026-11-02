# Instagram User Reels (V2) API: pricing, parameters and code examples

`instagram/v2/user-reels` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Returns a list of Reels from an Instagram account by username or user ID. Supports cursor-based pagination to browse past video content.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v2/user-reels"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v2/user-reels', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v2/user-reels", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v2/user-reels", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/instagram/v2/user-reels` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string |  | User ID (either username or user_id required)  |
| `username` | string |  | Username (either username or user_id required)  |
| `pagination_token` | string |  | Pagination token from previous response  |

## Details

Retrieve reels posted by an Instagram profile using `username` or `user_id`. Supports `pagination_token` to navigate through subsequent pages of results.

### Use cases

- Browse recent video reels from a specific creator profile.
- Monitor new reel posts across tracked Instagram accounts.
- Ingest Instagram reels metadata into content archives.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v2/user-reels" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | No | User ID (either username or user_id required) |
| `username` | string | No | Username (either username or user_id required) |
| `pagination_token` | string | No | Pagination token from previous response |

### Notes

- Provide either `username` or `user_id` to query an account.
- Pass `pagination_token` from a previous response to fetch additional pages.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Comment Replies (V2)](/model/instagram/v2/comment-replies): Retrieves a paginated list of replies to an Instagram comment using the post URL or shortcode and the target comment ID.
- [Instagram General Search (V2)](/model/instagram/v2/general-search): Returns Instagram search results matching a specified keyword, including media items, user profiles, and engagement statistics.
- [Instagram Hashtag Posts (V2)](/model/instagram/v2/hashtag-posts): Returns posts associated with a specific hashtag.

---
Machine-readable: [`catalog/models/instagram/v2/user-reels.json`](../../../../catalog/models/instagram/v2/user-reels.json) · Store page: https://www.sandbase.ai/model/instagram/v2/user-reels
