# Zhihu User Followers API: pricing, parameters and code examples

`zhihu/web/user-followers` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Retrieves a paginated list of followers for a specified Zhihu user profile. Supports offset and limit parameters for browsing through follower lists.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/user-followers", "user_url_token": "<user_url_token>"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/user-followers', {'user_url_token': '<user_url_token>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/user-followers", {
  "user_url_token": "<user_url_token>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/user-followers", sandbase.Params{
	"user_url_token": "<user_url_token>",
})
```

Same call via the path form: `POST /v1/api/zhihu/web/user-followers` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | string |  | Number of users per page  |
| `offset` | string |  | Offset  |
| `user_url_token` | string | yes | User ID  |

## Details

Retrieve follower profiles for a specific Zhihu account using `user_url_token`. You can page through results using `limit` and `offset`.

### Use cases

- Track follower growth and analyze audience demographics for a Zhihu user.
- Inspect connection networks and community interactions between Zhihu accounts.
- Retrieve user lists to power follower analysis dashboards.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/user-followers" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_url_token": "<user_url_token>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_url_token` | string | Yes | User ID |
| `limit` | string | No | Number of users per page |
| `offset` | string | No | Offset |

### Notes

- Specify the user identifier using `user_url_token`.
- Paging is controlled using `limit` and `offset`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Zhihu AI Search Stream](/apis/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Answer Details](/apis/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/apis/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…

---
Machine-readable: [`catalog/models/zhihu/web/user-followers.json`](../../../../catalog/models/zhihu/web/user-followers.json) · Store page: https://www.sandbase.ai/model/zhihu/web/user-followers
