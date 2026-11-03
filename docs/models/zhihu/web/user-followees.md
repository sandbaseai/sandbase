# Zhihu User Followees API: pricing, parameters and code examples

`zhihu/web/user-followees` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the list of accounts that a specific Zhihu user follows. Supports pagination through limit and offset parameters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/user-followees", "user_url_token": "<user_url_token>"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/user-followees', {'user_url_token': '<user_url_token>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/user-followees", {
  "user_url_token": "<user_url_token>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/user-followees", sandbase.Params{
	"user_url_token": "<user_url_token>",
})
```

Same call via the path form: `POST /v1/api/zhihu/web/user-followees` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | string |  | Number of users per page  |
| `offset` | string |  | Offset  |
| `user_url_token` | string | yes | User ID  |

## Details

Retrieve the list of accounts followed by a specific Zhihu user using `user_url_token`. Supports pagination via `limit` and `offset`.

### Use cases

- Inspect who a specific Zhihu user follows.
- Map user interest networks on Zhihu.
- Track following lists for account research.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/user-followees" \
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

- Identify the target account using `user_url_token`.
- Use `limit` and `offset` to page through results.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Zhihu AI Search Stream](/apis/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Answer Details](/apis/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/apis/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…

---
Machine-readable: [`catalog/models/zhihu/web/user-followees.json`](../../../../catalog/models/zhihu/web/user-followees.json) · Store page: https://www.sandbase.ai/model/zhihu/web/user-followees
