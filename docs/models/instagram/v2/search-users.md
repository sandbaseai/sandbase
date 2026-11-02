# Instagram User Search (V2) API: pricing, parameters and code examples

`instagram/v2/search-users` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.003 per call (free daily quota) · **Modes:** sync

Searches for Instagram users matching a specified keyword. Returns a list of user accounts including user IDs, usernames, full names, and profile picture URLs.

## Pricing

- **$0.003 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v2/search-users", "keyword": "openai"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v2/search-users', {'keyword': 'openai'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v2/search-users", {
  "keyword": "openai"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v2/search-users", sandbase.Params{
	"keyword": "openai",
})
```

Same call via the path form: `POST /v1/api/instagram/v2/search-users` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | Search keyword  |

## Details

Query Instagram user profiles by supplying a search query via `keyword`. The endpoint returns matching user accounts along with basic profile metadata.

### Use cases

- Find Instagram account IDs and usernames matching a query string.
- Look up public user profile pictures and display names.
- Power user search and account discovery workflows.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v2/search-users" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "openai"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "items": [
      {
        "full_name": "OpenAI",
        "id": "45374573700",
        "profile_pic_id": "3973928817672774008",
        "profile_pic_url": "https://scontent-cph2-1.cdninstagram.com/v/t51.82787-19/788716177_18115256264517…",
        "unseen_count": 0,
        "username": "<user>"
      }
    ]
  }
}
```

### Notes

- The `keyword` parameter is required to perform the user search query.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Comment Replies (V2)](/model/instagram/v2/comment-replies): Retrieves a paginated list of replies to an Instagram comment using the post URL or shortcode and the target comment ID.
- [Instagram General Search (V2)](/model/instagram/v2/general-search): Returns Instagram search results matching a specified keyword, including media items, user profiles, and engagement statistics.
- [Instagram Hashtag Posts (V2)](/model/instagram/v2/hashtag-posts): Returns posts associated with a specific hashtag.

---
Machine-readable: [`catalog/models/instagram/v2/search-users.json`](../../../../catalog/models/instagram/v2/search-users.json) · Store page: https://www.sandbase.ai/model/instagram/v2/search-users
