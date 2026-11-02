# Instagram User Followers (V3) API: pricing, parameters and code examples

`instagram/v3/user-followers` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Returns a list of followers for a specified Instagram account. Supports pagination cursors and limits up to 100 users per request.

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v3/user-followers", "username": "instagram"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v3/user-followers', {'username': 'instagram'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v3/user-followers", {
  "username": "instagram"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v3/user-followers", sandbase.Params{
	"username": "instagram",
})
```

Same call via the path form: `POST /v1/api/instagram/v3/user-followers` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number of users to fetch per request (default 12, max 100) range 1–100 |
| `max_id` | string |  | Pagination cursor, omit for first request, get from previous response `data.next_max_id`  |
| `username` | string | yes | Instagram username (required)  |

## Details

Retrieve the follower list for an Instagram profile specified by `username`.

### Use cases

- Audit follower profiles for target Instagram accounts.
- Analyze audience demographics and follower growth.
- Collect profile IDs and usernames for network analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/user-followers" \
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
      "full_name": "nebulosa🎀",
      "id": "45901571201",
      "pk_id": "45901571201",
      "profile_pic_id": "3984758658198814100_45901571201",
      "profile_pic_url": "https://instagram.fpit1-1.fna.fbcdn.net/v/t51.82787-19/806299292_180740922805312…",
      "username": "<user>"
    }
  ]
}
```

### Notes

- Set `count` between 12 and 100 to adjust the batch size.
- Pass `max_id` from the previous response `data.next_max_id` to page through subsequent results.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Comment Bulk Translation](/model/instagram/v3/bulk-translate-comments): Returns bulk translations for multiple Instagram comments using a list of comment identifiers.
- [Instagram Comment Replies (V3)](/model/instagram/v3/comment-replies): Returns child comment replies for a specific Instagram comment using the post media ID and parent comment ID.
- [Instagram Explore Feed](/model/instagram/v3/explore): Returns curated sectional items from the Instagram explore feed, including layout formats and feed types.

---
Machine-readable: [`catalog/models/instagram/v3/user-followers.json`](../../../../catalog/models/instagram/v3/user-followers.json) · Store page: https://www.sandbase.ai/model/instagram/v3/user-followers
