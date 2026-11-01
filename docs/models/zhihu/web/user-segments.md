# Zhihu User Highlighted Segments

`zhihu/web/user-segments` · api · Zhihu

Returns highlighted text segments and line comments for a specified Zhihu member. Supports filtering by content type along with offset pagination.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/user-segments", "user_url_token": "<user_url_token>"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/user-segments', {'user_url_token': '<user_url_token>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/user-segments", {
  "user_url_token": "<user_url_token>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/user-segments", sandbase.Params{
	"user_url_token": "<user_url_token>",
})
```

Same call via the path form: `POST /v1/api/zhihu/web/user-segments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | string |  | Number per page  |
| `offset` | string |  | Offset  |
| `content_type` | string |  | Content type, all for all  |
| `user_url_token` | string | yes | MUST be the user's **member hash id** (e.g. c72367...), not the url_token  |

## Details

Fetch highlighted segments and line comments left by a member using their member hash ID in `user_url_token`.

### Use cases

- Review highlighted text quotes and inline comments from a target member.
- Filter member segment interactions across specific content types.
- Paginate through public line commentary history for community research.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/user-segments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_url_token": "<user_url_token>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_url_token` | string | Yes | MUST be the user's member hash id (e.g. c72367...), not the url_token |
| `limit` | string | No | Number per page |
| `offset` | string | No | Offset |
| `content_type` | string | No | Content type, all for all |

### Notes

- `user_url_token` must be the user's member hash ID rather than their standard profile URL token.
- Use `limit` and `offset` to page through results.
- Set `content_type` to "all" to include all supported content types.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Zhihu AI Search Stream](/model/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Answer Details](/model/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/model/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…

---
Machine-readable: [`catalog/models/zhihu/web/user-segments.json`](../../../../catalog/models/zhihu/web/user-segments.json) · Store page: https://www.sandbase.ai/model/zhihu/web/user-segments
