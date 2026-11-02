# Instagram Reels Search API: pricing, parameters and code examples

`instagram/v2/search-reels` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Search Instagram Reels by keyword: reel IDs, captions, creators, play, like and comment counts, with pagination.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v2/search-reels", "keyword": "openai"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v2/search-reels', {'keyword': 'openai'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v2/search-reels", {
  "keyword": "openai"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v2/search-reels", sandbase.Params{
	"keyword": "openai",
})
```

Same call via the path form: `POST /v1/api/instagram/v2/search-reels` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | Search keyword  |
| `pagination_token` | string |  | Pagination token from previous response  |

## Details

Search Instagram Reels for a keyword and get matching reels with engagement counts.

### Use cases

- Find trending reels on a topic.
- Discover creators for campaigns.
- Monitor brand mentions in short video.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v2/search-reels" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "openai"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword |
| `pagination_token` | string | No | Pagination token from previous response |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "pagination_token": "<token>",
    "items": [
      {
        "id": "3823389733213195521",
        "code": "DUPaLSGDE0B",
        "taken_at": 1770003608,
        "like_count": 20427,
        "comment_count": 217,
        "ig_play_count": 661740,
        "caption": {
          "text": "Sam Altman is pointing out a quiet shift in what actually c…"
        },
        "user": {
          "username": "<user>"
        }
      }
    ]
  }
}
```

### Notes

- Paginate with `pagination_token`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram User Profile](/model/instagram/v2/user-info): Get an Instagram user profile by username or user ID: full name, bio, website, follower, following and post counts, verification and category.
- [Get comment replies](/model/instagram/v2/comment-replies): Get list of replies to a comment Need to get comment ID from fetch_post_comments first Support pagination.
- [General search](/model/instagram/v2/general-search): Perform general search on Instagram by keyword Support pagination.

---
Machine-readable: [`catalog/models/instagram/v2/search-reels.json`](../../../../catalog/models/instagram/v2/search-reels.json) · Store page: https://www.sandbase.ai/model/instagram/v2/search-reels
