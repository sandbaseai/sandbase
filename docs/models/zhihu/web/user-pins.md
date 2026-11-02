# Zhihu User Pins API: pricing, parameters and code examples

`zhihu/web/user-pins` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of pins or moments posted by a specific Zhihu user. Supports pagination controls using offset and limit parameters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/user-pins", "user_url_token": "<user_url_token>"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/user-pins', {'user_url_token': '<user_url_token>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/user-pins", {
  "user_url_token": "<user_url_token>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/user-pins", sandbase.Params{
	"user_url_token": "<user_url_token>",
})
```

Same call via the path form: `POST /v1/api/zhihu/web/user-pins` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | string |  | Number of pins per page  |
| `offset` | string |  | Offset  |
| `user_url_token` | string | yes | User ID  |

## Details

Retrieve a list of pins and moments for a target Zhihu account by specifying `user_url_token`. Pagination is supported through `limit` and `offset`.

### Use cases

- Display a timeline of pins and short posts from a Zhihu creator profile.
- Track recent thoughts and moments shared by selected Zhihu users.
- Archive historical user pins using paginated requests.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/user-pins" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_url_token": "<user_url_token>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_url_token` | string | Yes | User ID |
| `limit` | string | No | Number of pins per page |
| `offset` | string | No | Offset |

### Notes

- Pass the user identifier in `user_url_token`.
- Control pagination using `limit` and `offset`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Zhihu AI Search Stream](/model/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Answer Details](/model/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/model/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…

---
Machine-readable: [`catalog/models/zhihu/web/user-pins.json`](../../../../catalog/models/zhihu/web/user-pins.json) · Store page: https://www.sandbase.ai/model/zhihu/web/user-pins
