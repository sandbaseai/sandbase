# Instagram User Tagged Posts (V2) API: pricing, parameters and code examples

`instagram/v2/user-tagged-posts` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.003 per call (free daily quota) · **Modes:** sync

Returns posts where a specified Instagram account has been tagged by other users. Supports looking up accounts by identifier or username, with pagination handling.

## Pricing

- **$0.003 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v2/user-tagged-posts"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v2/user-tagged-posts', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v2/user-tagged-posts", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v2/user-tagged-posts", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/instagram/v2/user-tagged-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string |  | User ID (either username or user_id required)  |
| `username` | string |  | Username (either username or user_id required)  |
| `pagination_token` | string |  | Pagination token from previous response  |

## Details

Retrieve posts where an account is tagged by other users by specifying either `username` or `user_id`.

### Use cases

- Monitor user-generated content mentioning a specific profile.
- Collect posts where a brand or creator is tagged.
- Track community engagement and external media mentions.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v2/user-tagged-posts" \
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

- Either `username` or `user_id` is required to perform the request.
- Use `pagination_token` from a previous response to paginate through results.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Comment Replies (V2)](/model/instagram/v2/comment-replies): Retrieves a paginated list of replies to an Instagram comment using the post URL or shortcode and the target comment ID.
- [Instagram General Search (V2)](/model/instagram/v2/general-search): Returns Instagram search results matching a specified keyword, including media items, user profiles, and engagement statistics.
- [Instagram Hashtag Posts (V2)](/model/instagram/v2/hashtag-posts): Returns posts associated with a specific hashtag.

---
Machine-readable: [`catalog/models/instagram/v2/user-tagged-posts.json`](../../../../catalog/models/instagram/v2/user-tagged-posts.json) · Store page: https://www.sandbase.ai/model/instagram/v2/user-tagged-posts
