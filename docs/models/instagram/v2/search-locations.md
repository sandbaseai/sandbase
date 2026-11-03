# Instagram Location Search API: pricing, parameters and code examples

`instagram/v2/search-locations` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Searches Instagram locations matching a specified query term. Returns a list of place candidates with their IDs, names, and Facebook place identifiers.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v2/search-locations", "keyword": "paris"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v2/search-locations', {'keyword': 'paris'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v2/search-locations", {
  "keyword": "paris"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v2/search-locations", sandbase.Params{
	"keyword": "paris",
})
```

Same call via the path form: `POST /v1/api/instagram/v2/search-locations` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | Search keyword (location name, city, etc.)  |

## Details

Look up Instagram locations by providing a location name or city query via `keyword`. The endpoint returns place metadata and identifiers for matching locations.

### Use cases

- Find location IDs for geotag research.
- Auto-complete place and city names in search interfaces.
- Match user query terms to standardized Instagram location entries.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v2/search-locations" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "paris"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword (location name, city, etc.) |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "items": [
      {
        "facebook_places_id": 1619558008055426,
        "id": "1619558008055426",
        "name": "Paris, France",
        "short_name": "Paris"
      }
    ]
  }
}
```

### Notes

- The `keyword` parameter is required and accepts a location name or city.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Comment Replies (V2)](/apis/instagram/v2/comment-replies): Retrieves a paginated list of replies to an Instagram comment using the post URL or shortcode and the target comment ID.
- [Instagram General Search (V2)](/apis/instagram/v2/general-search): Returns Instagram search results matching a specified keyword, including media items, user profiles, and engagement statistics.
- [Instagram Hashtag Posts (V2)](/apis/instagram/v2/hashtag-posts): Returns posts associated with a specific hashtag.

---
Machine-readable: [`catalog/models/instagram/v2/search-locations.json`](../../../../catalog/models/instagram/v2/search-locations.json) · Store page: https://www.sandbase.ai/model/instagram/v2/search-locations
