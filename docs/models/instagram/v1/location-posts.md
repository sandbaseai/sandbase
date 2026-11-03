# Instagram Location Posts (V1) API: pricing, parameters and code examples

`instagram/v1/location-posts` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns posts tagged at a designated location. Supports sorting by top or latest posts alongside cursor-based pagination.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v1/location-posts", "location_id": "703457703"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v1/location-posts', {'location_id': '703457703'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v1/location-posts", {
  "location_id": "703457703"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v1/location-posts", sandbase.Params{
	"location_id": "703457703",
})
```

Same call via the path form: `POST /v1/api/instagram/v1/location-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `tab` | string |  | Sorting method, ranked(top)/recent(latest) default `"ranked"` |
| `end_cursor` | string |  | Pagination cursor, omit for first request  |
| `location_id` | string | yes | Location ID  |

## Details

Fetch media items tagged at a specific place using `location_id`. You can also configure the sort order using `tab`.

### Use cases

- Discover trending posts associated with a specific venue or city.
- Monitor recent user content tagged at a retail storefront.
- Analyze location-tagged media feeds for regional social research.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v1/location-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"location_id": "703457703"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `location_id` | string | Yes | Location ID |
| `tab` | string | No | Sorting method, ranked(top)/recent(latest) |
| `end_cursor` | string | No | Pagination cursor, omit for first request |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "edges": [
    {
      "node": {
        "carousel_media": [
          {
            "carousel_parent_id": "3956906345903348188_6169608598",
            "id": "3956905332562451903_6169608598",
            "media_type": 1,
            "user": {
              "id": "6169608598"
            }
          }
        ]
      }
    }
  ]
}
```

### Notes

- `location_id` is required to identify the target place.
- `tab` supports "ranked" for top posts and "recent" for latest posts.
- `end_cursor` provides pagination; omit it on the initial request.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Cities by Country](/apis/instagram/v1/cities): Returns a list of Instagram cities and regions for a specified country code.
- [Instagram Hashtag Posts (V1)](/apis/instagram/v1/hashtag-posts): Returns public Instagram posts associated with a specific hashtag.
- [Instagram Location Details (V1)](/apis/instagram/v1/location-info): Returns detailed metadata and profile information for a specified Instagram location using its unique identifier.

---
Machine-readable: [`catalog/models/instagram/v1/location-posts.json`](../../../../catalog/models/instagram/v1/location-posts.json) · Store page: https://www.sandbase.ai/model/instagram/v1/location-posts
