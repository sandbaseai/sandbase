# Toutiao Post Comments API: pricing, parameters and code examples

`toutiao/app/comments` · data API · Toutiao · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns user comments and interaction metrics for a specific Toutiao post. Results can be paginated through comment batches using an offset index.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "toutiao/app/comments", "group_id": "7453372680222523931", "offset": "0"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('toutiao/app/comments', {'group_id': '7453372680222523931', 'offset': '0'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("toutiao/app/comments", {
  "group_id": "7453372680222523931",
  "offset": "0"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "toutiao/app/comments", sandbase.Params{
	"group_id": "7453372680222523931",
	"offset": "0",
})
```

Same call via the path form: `POST /v1/api/toutiao/app/comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `offset` | string | yes | Offset, used for pagination, default is 0, then add 20 each time  |
| `group_id` | string | yes | Post ID, can be obtained from the link  |

## Details

Retrieve comments for a Toutiao post by passing the target post identifier in `group_id`. Paginate through sequential comment batches with `offset`.

### Use cases

- Analyze user sentiment and feedback on Toutiao content.
- Monitor engagement metrics such as digg and forward counts across post comments.
- Collect comment threads for community management workflows.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/toutiao/app/comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"group_id": "7453372680222523931", "offset": "0"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `offset` | string | Yes | Offset, used for pagination, default is 0, then add 20 each time |
| `group_id` | string | Yes | Post ID, can be obtained from the link |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": [
    {
      "cell_type": 1,
      "id": 7453426669643629364,
      "comment": {
        "bury_count": 9,
        "content_rich_span": "{\"links\":[]}",
        "create_time": 1735386148,
        "digg_count": 557,
        "forward_count": 0,
        "id": 7453426669643629364
      }
    }
  ]
}
```

### Notes

- Locate `group_id` directly in the Toutiao post URL.
- Set `offset` to 0 initially and increment by 20 for subsequent pages.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Toutiao Article Details (App)](/apis/toutiao/app/article-info): Returns details and interface settings for a specified Toutiao post.
- [Toutiao Profile User ID](/apis/toutiao/app/user-id): Resolves a Toutiao user profile URL into numeric and secure user identifiers.
- [Toutiao User Profile](/apis/toutiao/app/user-info): Get a Toutiao (Jinri Toutiao) user profile by user ID: name, bio, avatar, follower, following and like counts, and content tabs.

---
Machine-readable: [`catalog/models/toutiao/app/comments.json`](../../../../catalog/models/toutiao/app/comments.json) · Store page: https://www.sandbase.ai/model/toutiao/app/comments
