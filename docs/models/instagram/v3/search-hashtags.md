# Instagram Hashtag Search (V3)

`instagram/v3/search-hashtags` · api · Instagram

Searches Instagram hashtags by keyword and returns matching hashtag names, IDs, and media counts. Supports pagination via rank tokens.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v3/search-hashtags", "query": "openai"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v3/search-hashtags', {'query': 'openai'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v3/search-hashtags", {
  "query": "openai"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v3/search-hashtags", sandbase.Params{
	"query": "openai",
})
```

Same call via the path form: `POST /v1/api/instagram/v3/search-hashtags` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Search keyword  |
| `rank_token` | string |  | Rank token from previous search response for pagination  |

## Details

Search Instagram hashtags matching a keyword using `query`. Returns hashtag metadata including media counts, with support for pagination via `rank_token`.

### Use cases

- Look up hashtag popularity and media counts.
- Discover relevant hashtags based on search terms.
- Collect hashtag IDs for social media monitoring workflows.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/search-hashtags" \
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
  "hashtags": [
    {
      "id": "17841553213093056",
      "media_count": 2319697,
      "name": "openai"
    }
  ]
}
```

### Notes

- Use `rank_token` from a previous response to paginate through additional results.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Comment Bulk Translation](/model/instagram/v3/bulk-translate-comments): Returns bulk translations for multiple Instagram comments using a list of comment identifiers.
- [Instagram Comment Replies (V3)](/model/instagram/v3/comment-replies): Returns child comment replies for a specific Instagram comment using the post media ID and parent comment ID.
- [Instagram Explore Feed](/model/instagram/v3/explore): Returns curated sectional items from the Instagram explore feed, including layout formats and feed types.

---
Machine-readable: [`catalog/models/instagram/v3/search-hashtags.json`](../../../../catalog/models/instagram/v3/search-hashtags.json) · Store page: https://www.sandbase.ai/model/instagram/v3/search-hashtags
