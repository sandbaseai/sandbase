# Instagram Hashtag Search (V2) API: pricing, parameters and code examples

`instagram/v2/search-hashtags` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.003 per call (free daily quota) · **Modes:** sync

Search for Instagram hashtags matching a given keyword query. Returns an array of matching hashtag objects containing each hashtag identifier, name, and total media count.

## Pricing

- **$0.003 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v2/search-hashtags", "keyword": "cat"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v2/search-hashtags', {'keyword': 'cat'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v2/search-hashtags", {
  "keyword": "cat"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v2/search-hashtags", sandbase.Params{
	"keyword": "cat",
})
```

Same call via the path form: `POST /v1/api/instagram/v2/search-hashtags` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | Search keyword  |

## Details

Query Instagram hashtags by passing a search term into `keyword`. The endpoint returns matching tags along with their unique IDs and media counts.

### Use cases

- Discover trending or popular Instagram hashtags related to a specific topic.
- Retrieve hashtag IDs and media counts for market research.
- Provide hashtag autocompletion within social analytics tools.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v2/search-hashtags" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "cat"}'
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
        "id": "17841562906103814",
        "media_count": 314343003,
        "name": "cat"
      }
    ]
  }
}
```

### Notes

- The `keyword` parameter is required to perform the search.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Comment Replies (V2)](/model/instagram/v2/comment-replies): Retrieves a paginated list of replies to an Instagram comment using the post URL or shortcode and the target comment ID.
- [Instagram General Search (V2)](/model/instagram/v2/general-search): Returns Instagram search results matching a specified keyword, including media items, user profiles, and engagement statistics.
- [Instagram Hashtag Posts (V2)](/model/instagram/v2/hashtag-posts): Returns posts associated with a specific hashtag.

---
Machine-readable: [`catalog/models/instagram/v2/search-hashtags.json`](../../../../catalog/models/instagram/v2/search-hashtags.json) · Store page: https://www.sandbase.ai/model/instagram/v2/search-hashtags
