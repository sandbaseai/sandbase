# Instagram User Following List API: pricing, parameters and code examples

`instagram/v3/user-following` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Returns a paginated list of accounts followed by a specified Instagram user. Supports filtering by username and custom result counts up to 100 users per request.

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v3/user-following", "username": "instagram"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v3/user-following', {'username': 'instagram'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v3/user-following", {
  "username": "instagram"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v3/user-following", sandbase.Params{
	"username": "instagram",
})
```

Same call via the path form: `POST /v1/api/instagram/v3/user-following` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number of users to fetch per request (default 12, max 100) range 1–100 |
| `max_id` | string |  | Pagination cursor, omit for first request, get from previous response `data.next_max_id`  |
| `username` | string | yes | Instagram username (required)  |

## Details

Retrieve the list of profiles that an Instagram user follows by providing their `username`. Optional parameters include `count` to control batch size and `max_id` for cursor pagination.

### Use cases

- Analyze public following lists for influencer network research.
- Inspect accounts an Instagram profile follows to detect shared interests.
- Track changes in followed profiles over time across target accounts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/user-following" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "instagram"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | Instagram username (required) |
| `count` | integer | No | Number of users to fetch per request (default 12, max 100) |
| `max_id` | string | No | Pagination cursor, omit for first request, get from previous response `data.next_max_id` |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "users": [
    {
      "full_name": "Meta AI",
      "id": "64528677628",
      "pk_id": "64528677628",
      "profile_pic_id": "3871614390308476415_64528677628",
      "profile_pic_url": "https://scontent-hou1-1.xx.fbcdn.net/m1/v/t0.65075-6/An_DmLLtCkUAG4zSiC7jef0bz7J…",
      "username": "<user>"
    }
  ]
}
```

### Notes

- `count` defaults to 12 and accepts a maximum of 100 users per call.
- Use `max_id` from the previous response `data.next_max_id` to paginate through subsequent pages.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Comment Bulk Translation](/apis/instagram/v3/bulk-translate-comments): Returns bulk translations for multiple Instagram comments using a list of comment identifiers.
- [Instagram Comment Replies (V3)](/apis/instagram/v3/comment-replies): Returns child comment replies for a specific Instagram comment using the post media ID and parent comment ID.
- [Instagram Explore Feed](/apis/instagram/v3/explore): Returns curated sectional items from the Instagram explore feed, including layout formats and feed types.

---
Machine-readable: [`catalog/models/instagram/v3/user-following.json`](../../../../catalog/models/instagram/v3/user-following.json) · Store page: https://www.sandbase.ai/model/instagram/v3/user-following
