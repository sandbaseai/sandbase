# Reddit App User Profile API: pricing, parameters and code examples

`reddit/app/user-profile` · data API · Reddit · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns detailed profile information for a specified Reddit app user by username. Supports an optional flag to clean and format the output data.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/app/user-profile", "username": "spez"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/app/user-profile', {'username': 'spez'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/app/user-profile", {
  "username": "spez"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/app/user-profile", sandbase.Params{
	"username": "spez",
})
```

Same call via the path form: `POST /v1/api/reddit/app/user-profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `username` | string | yes | Reddit username (without u/ prefix)  |
| `need_format` | boolean |  | Whether to clean and format the data default `false` |

## Details

Retrieve detailed profile information for a Reddit account using the `username` parameter. You can optionally set `need_format` to format the returned data.

### Use cases

- Inspect public Reddit account profile details and moderation records.
- Verify user identities and profile metadata across community platforms.
- Retrieve formatted user information for analytics dashboards.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/app/user-profile" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "spez"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | Reddit username (without u/ prefix) |
| `need_format` | boolean | No | Whether to clean and format the data |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "redditorInfoByName": {
    "profile": {
      "moderatorsInfo": {
        "edges": [
          {
            "node": {
              "id": "t2_1w72"
            }
          }
        ]
      }
    }
  }
}
```

### Notes

- Provide `username` without the `u/` prefix.
- Set `need_format` to true to clean and format the response data.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Reddit Subreddit Mute Status](/model/reddit/app/check-subreddit-muted): Checks whether a specified Reddit subreddit is muted by the current account using its ID.
- [Reddit App Comment Replies](/model/reddit/app/comment-replies): Returns replies and nested sub-comments under a Reddit post comment using a continuation cursor.
- [Reddit Community Highlights](/model/reddit/app/community-highlights): Returns featured highlight content for a designated Reddit community, such as popular posts and announcements, by subreddit ID.

---
Machine-readable: [`catalog/models/reddit/app/user-profile.json`](../../../../catalog/models/reddit/app/user-profile.json) · Store page: https://www.sandbase.ai/model/reddit/app/user-profile
