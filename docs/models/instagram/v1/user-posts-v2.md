# Instagram User Posts (V1, V2)

`instagram/v1/user-posts-v2` · api · Instagram

Returns a paginated list of media posts for a specified Instagram account. Filter by user ID with support for custom page limits and cursor-based navigation.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v1/user-posts-v2", "user_id": "25025320"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v1/user-posts-v2', {'user_id': '25025320'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v1/user-posts-v2", {
  "user_id": "25025320"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v1/user-posts-v2", sandbase.Params{
	"user_id": "25025320",
})
```

Same call via the path form: `POST /v1/api/instagram/v1/user-posts-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Count per page, default 12 default `12`; range 1–50 |
| `user_id` | string | yes | Instagram user ID  |
| `end_cursor` | string |  | Pagination cursor, omit for first request  |

## Details

Retrieve timeline posts for a specific profile by supplying `user_id`. Use `count` and `end_cursor` to paginate through historic media results.

### Use cases

- Retrieve recent timeline posts and reels from a target Instagram profile.
- Paginate through an account historical media library for content analysis.
- Extract post media details including display URLs and media preview data.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v1/user-posts-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "25025320"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | Instagram user ID |
| `count` | integer | No | Count per page, default 12 |
| `end_cursor` | string | No | Pagination cursor, omit for first request |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "user": {
      "edge_owner_to_timeline_media": {
        "edges": [
          {
            "node": {
              "__typename": "GraphVideo",
              "display_url": "https://scontent-cdg4-1.cdninstagram.com/v/t51.82787-15/830594125_18798964129001…",
              "id": "3998430248382584993",
              "like_and_view_counts_disabled": false,
              "media_preview": "ABgq58LngDmums2JgXPVRtP4dP0xUY0uJectke//ANarMdusYwMke5zUvUaKmd3U4YnnP8h7D+dFWZIFYZ6H2oqLF…",
              "product_type": "clips"
            }
          }
        ]
      }
    }
  }
}
```

### Notes

- Set `count` to customize the number of posts returned per page, defaulting to 12.
- Pass `end_cursor` to retrieve subsequent pages of results, or omit it for the initial call.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Cities by Country](/model/instagram/v1/cities): Returns a list of Instagram cities and regions for a specified country code.
- [Instagram Hashtag Posts (V1)](/model/instagram/v1/hashtag-posts): Returns public Instagram posts associated with a specific hashtag.
- [Instagram Location Details (V1)](/model/instagram/v1/location-info): Returns detailed metadata and profile information for a specified Instagram location using its unique identifier.

---
Machine-readable: [`catalog/models/instagram/v1/user-posts-v2.json`](../../../../catalog/models/instagram/v1/user-posts-v2.json) · Store page: https://www.sandbase.ai/model/instagram/v1/user-posts-v2
