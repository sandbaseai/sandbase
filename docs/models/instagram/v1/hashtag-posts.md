# Instagram Hashtag Posts (V1) API: pricing, parameters and code examples

`instagram/v1/hashtag-posts` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns public Instagram posts associated with a specific hashtag. Filter by hashtag name and paginate through media results using a cursor.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v1/hashtag-posts", "hashtag": "veganrecipes"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v1/hashtag-posts', {'hashtag': 'veganrecipes'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v1/hashtag-posts", {
  "hashtag": "veganrecipes"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v1/hashtag-posts", sandbase.Params{
	"hashtag": "veganrecipes",
})
```

Same call via the path form: `POST /v1/api/instagram/v1/hashtag-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `hashtag` | string | yes | Hashtag name (without #)  |
| `end_cursor` | string |  | Pagination cursor, omit for first request  |

## Details

Retrieve media posts tagged with a target topic by providing `hashtag`. Subsequent pages can be queried by supplying `end_cursor`.

### Use cases

- Track media content and trends around specific topic tags.
- Collect public image and video posts for brand campaigns.
- Aggregate user posts associated with event hashtags.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v1/hashtag-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"hashtag": "openai"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `hashtag` | string | Yes | Hashtag name (without #) |
| `end_cursor` | string | No | Pagination cursor, omit for first request |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "hashtag": {
      "edge_hashtag_to_media": {
        "edges": [
          {
            "node": {
              "__typename": "GraphImage",
              "accessibility_caption": "Photo by Aliança News on October 06, 2026. May be a meme of text.",
              "display_url": "https://scontent-dfw6-2.cdninstagram.com/v/t51.82787-15/839441193_18136625092601…",
              "id": "4001955501160418113",
              "taken_at_timestamp": 1791290300
            }
          }
        ]
      }
    }
  }
}
```

### Notes

- Provide `hashtag` without the leading '#' symbol.
- Use `end_cursor` for pagination, omitting it on the initial request.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Cities by Country](/model/instagram/v1/cities): Returns a list of Instagram cities and regions for a specified country code.
- [Instagram Location Details (V1)](/model/instagram/v1/location-info): Returns detailed metadata and profile information for a specified Instagram location using its unique identifier.
- [Instagram Location Posts (V1)](/model/instagram/v1/location-posts): Returns posts tagged at a designated location.

---
Machine-readable: [`catalog/models/instagram/v1/hashtag-posts.json`](../../../../catalog/models/instagram/v1/hashtag-posts.json) · Store page: https://www.sandbase.ai/model/instagram/v1/hashtag-posts
