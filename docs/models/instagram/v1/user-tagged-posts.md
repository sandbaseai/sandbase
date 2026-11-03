# Instagram User Tagged Posts (V1) API: pricing, parameters and code examples

`instagram/v1/user-tagged-posts` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns posts where a specific user is tagged by other accounts. Supports result limits and pagination through a cursor parameter.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v1/user-tagged-posts", "user_id": "25025320"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v1/user-tagged-posts', {'user_id': '25025320'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v1/user-tagged-posts", {
  "user_id": "25025320"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v1/user-tagged-posts", sandbase.Params{
	"user_id": "25025320",
})
```

Same call via the path form: `POST /v1/api/instagram/v1/user-tagged-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Count per page, default 12 default `12`; range 1–50 |
| `user_id` | string | yes | Instagram user ID  |
| `end_cursor` | string |  | Pagination cursor, omit for first request  |

## Details

Retrieve photos and posts where an account is tagged using `user_id`. Supports pagination via `end_cursor`.

### Use cases

- Monitor user-generated content and brand mentions across tagged media.
- Display community posts that feature a specific Instagram creator or account.
- Archive media items where a specified profile is identified.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v1/user-tagged-posts" \
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
      "edge_user_to_photos_of_you": {
        "edges": [
          {
            "node": {
              "__typename": "GraphImage",
              "accessibility_caption": "Photo by LUCAS RAMOS MENDES ® in Florianópolis, Santa Catarina with @instagram, @faber_ca…",
              "display_url": "https://scontent-phl2-1.cdninstagram.com/v/t51.82787-15/621585839_18092087866989…",
              "id": "2251138696266127152",
              "taken_at_timestamp": 1582576666
            }
          }
        ]
      }
    }
  }
}
```

### Notes

- The `count` parameter defaults to 12 items per page.
- Omit `end_cursor` for the initial request, then pass the cursor returned by previous responses for subsequent pages.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Cities by Country](/apis/instagram/v1/cities): Returns a list of Instagram cities and regions for a specified country code.
- [Instagram Hashtag Posts (V1)](/apis/instagram/v1/hashtag-posts): Returns public Instagram posts associated with a specific hashtag.
- [Instagram Location Details (V1)](/apis/instagram/v1/location-info): Returns detailed metadata and profile information for a specified Instagram location using its unique identifier.

---
Machine-readable: [`catalog/models/instagram/v1/user-tagged-posts.json`](../../../../catalog/models/instagram/v1/user-tagged-posts.json) · Store page: https://www.sandbase.ai/model/instagram/v1/user-tagged-posts
