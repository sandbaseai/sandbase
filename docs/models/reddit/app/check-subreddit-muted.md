# Reddit Subreddit Mute Status API: pricing, parameters and code examples

`reddit/app/check-subreddit-muted` · data API · Reddit · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Checks whether a specified Reddit subreddit is muted by the current account using its ID. Supports an optional flag to format the returned output.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/app/check-subreddit-muted", "subreddit_id": "t5_2qh0u"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/app/check-subreddit-muted', {'subreddit_id': 't5_2qh0u'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/app/check-subreddit-muted", {
  "subreddit_id": "t5_2qh0u"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/app/check-subreddit-muted", sandbase.Params{
	"subreddit_id": "t5_2qh0u",
})
```

Same call via the path form: `POST /v1/api/reddit/app/check-subreddit-muted` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `need_format` | boolean |  | Whether to clean and format the data  |
| `subreddit_id` | string | yes | Subreddit ID starting with "t5_", can be obtained from fetch_subreddit_info endpoint  |

## Details

Returns whether the current account has muted a given Reddit subreddit. It needs a `subreddit_id` that starts with `t5_`, such as `t5_2qh0u`.

### Use cases

- Check if a subreddit is muted before showing its posts in a custom Reddit client.
- Show a mute toggle state next to subreddit details in an account settings screen.
- Audit a list of subreddit IDs to find which ones the account has muted.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/app/check-subreddit-muted" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"subreddit_id": "t5_2qh0u"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `subreddit_id` | string | Yes | Subreddit ID starting with "t5_", can be obtained from fetch_subreddit_info endpoint |
| `need_format` | boolean | No | Whether to clean and format the data |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "subredditInfoById": {
    "__typename": "Subreddit",
    "isMuted": false
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `subredditInfoById` | Wrapper object for the subreddit that matches the requested `subreddit_id`. |
| `subredditInfoById.__typename` | Object type name. The value is `Subreddit` for a subreddit record. |
| `subredditInfoById.isMuted` | Boolean mute flag. `true` means the current account has muted this subreddit, and `false` means it has not. |

### Notes

- Get `subreddit_id` from the [Reddit App Subreddit Info](/apis/reddit/app/subreddit-info) API. The ID starts with `t5_`.
- The result applies to the account tied to the call, so the same `subreddit_id` can return different values for different accounts.
- `need_format` is optional and is a boolean. The example request omits it.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Reddit App Comment Replies](/apis/reddit/app/comment-replies): Returns replies and nested sub-comments under a Reddit post comment using a continuation cursor.
- [Reddit Community Highlights](/apis/reddit/app/community-highlights): Returns featured highlight content for a designated Reddit community, such as popular posts and announcements, by subreddit ID.
- [Reddit Search](/apis/reddit/app/dynamic-search): Search Reddit posts, communities, comments, media and users with the Reddit app search.

---
Machine-readable: [`catalog/models/reddit/app/check-subreddit-muted.json`](../../../../catalog/models/reddit/app/check-subreddit-muted.json) · Store page: https://www.sandbase.ai/model/reddit/app/check-subreddit-muted
