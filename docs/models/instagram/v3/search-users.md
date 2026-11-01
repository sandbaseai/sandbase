# Instagram User Search (V3)

`instagram/v3/search-users` · api · Instagram

Searches for Instagram accounts matching a keyword query and returns user profiles including account IDs, full names, and usernames.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v3/search-users", "query": "openai"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v3/search-users', {'query': 'openai'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v3/search-users", {
  "query": "openai"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v3/search-users", sandbase.Params{
	"query": "openai",
})
```

Same call via the path form: `POST /v1/api/instagram/v3/search-users` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Search keyword  |
| `rank_token` | string |  | Rank token from previous search response for pagination  |

## Details

Search for Instagram user accounts using `query` to return matching profile summaries and basic account information.

### Use cases

- Discover Instagram user profiles matching brand names or keywords.
- Retrieve account identifiers and usernames for profile lookup workflows.
- Navigate through multiple pages of search results using rank tokens.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/search-users" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "openai"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search keyword |
| `rank_token` | string | No | Rank token from previous search response for pagination |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "items": [
    {
      "full_name": "OpenAI",
      "id": "45374573700",
      "profile_pic_url": "https://instagram.flas1-2.fna.fbcdn.net/v/t51.82787-19/788716177_181152562645177…",
      "username": "<user>"
    }
  ]
}
```

### Notes

- Pass `rank_token` from a prior response to handle pagination.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Comment Bulk Translation](/model/instagram/v3/bulk-translate-comments): Returns bulk translations for multiple Instagram comments using a list of comment identifiers.
- [Instagram Comment Replies (V3)](/model/instagram/v3/comment-replies): Returns child comment replies for a specific Instagram comment using the post media ID and parent comment ID.
- [Instagram Explore Feed](/model/instagram/v3/explore): Returns curated sectional items from the Instagram explore feed, including layout formats and feed types.

---
Machine-readable: [`catalog/models/instagram/v3/search-users.json`](../../../../catalog/models/instagram/v3/search-users.json) · Store page: https://www.sandbase.ai/model/instagram/v3/search-users
