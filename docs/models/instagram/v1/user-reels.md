# Instagram User Reels (V1) API: pricing, parameters and code examples

`instagram/v1/user-reels` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a paginated list of Instagram Reels associated with a specific user account. Supports custom page sizes and cursor-based navigation.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v1/user-reels", "user_id": "25025320"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v1/user-reels', {'user_id': '25025320'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v1/user-reels", {
  "user_id": "25025320"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v1/user-reels", sandbase.Params{
	"user_id": "25025320",
})
```

Same call via the path form: `POST /v1/api/instagram/v1/user-reels` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Count per page, default 12 default `12`; range 1–50 |
| `max_id` | string |  | Pagination cursor, omit for first request  |
| `user_id` | string | yes | Instagram user ID  |

## Details

Access Reels media items for an Instagram profile using `user_id`. Manage pagination across results with `max_id` and `count`.

### Use cases

- Review Reels content from a target creator profile.
- Track engagement indicators such as comment counts across an account's Reels.
- Index video media associated with a specific Instagram user.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v1/user-reels" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "25025320"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | Instagram user ID |
| `count` | integer | No | Count per page, default 12 |
| `max_id` | string | No | Pagination cursor, omit for first request |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "items": [
    {
      "media": {
        "caption_is_edited": false,
        "coauthor_producer_can_see_organic_insights": false,
        "comment_count": 18380,
        "device_timestamp": 1790870048722622,
        "disable_caption_and_comment": false,
        "filter_type": 0
      }
    }
  ]
}
```

### Notes

- Use `max_id` as the pagination cursor after the initial request.
- The `count` parameter defaults to 12 items per page.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Cities by Country](/apis/instagram/v1/cities): Returns a list of Instagram cities and regions for a specified country code.
- [Instagram Hashtag Posts (V1)](/apis/instagram/v1/hashtag-posts): Returns public Instagram posts associated with a specific hashtag.
- [Instagram Location Details (V1)](/apis/instagram/v1/location-info): Returns detailed metadata and profile information for a specified Instagram location using its unique identifier.

---
Machine-readable: [`catalog/models/instagram/v1/user-reels.json`](../../../../catalog/models/instagram/v1/user-reels.json) · Store page: https://www.sandbase.ai/model/instagram/v1/user-reels
