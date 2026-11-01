# Reddit Subreddit Mute Status

`reddit/app/check-subreddit-muted` · api · Reddit

Checks whether a specified Reddit subreddit is muted by the current account using its ID. Supports an optional flag to format the returned output.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/app/check-subreddit-muted", "subreddit_id": "<subreddit_id>"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/app/check-subreddit-muted', {'subreddit_id': '<subreddit_id>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/app/check-subreddit-muted", {
  "subreddit_id": "<subreddit_id>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/app/check-subreddit-muted", sandbase.Params{
	"subreddit_id": "<subreddit_id>",
})
```

Same call via the path form: `POST /v1/api/reddit/app/check-subreddit-muted` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `need_format` | boolean |  | Whether to clean and format the data  |
| `subreddit_id` | string | yes | Subreddit ID starting with "t5_", can be obtained from fetch_subreddit_info endpoint  |

## Details

Inspects whether an account has muted a specific subreddit by providing `subreddit_id`. An optional `need_format` parameter controls data formatting.

### Use cases

- Verify mute status for a target subreddit on the active account.
- Filter out muted subreddit feeds in custom client applications.
- Display mute preferences alongside subreddit details.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/app/check-subreddit-muted" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"subreddit_id": "<subreddit_id>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `subreddit_id` | string | Yes | Subreddit ID starting with "t5_", can be obtained from fetch_subreddit_info endpoint |
| `need_format` | boolean | No | Whether to clean and format the data |

### Notes

- `subreddit_id` must start with "t5_" and can be obtained from the subreddit info endpoint.
- `need_format` specifies whether to clean and format the returned data.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Reddit App Comment Replies](/model/reddit/app/comment-replies): Returns replies and nested sub-comments under a Reddit post comment using a continuation cursor.
- [Reddit Community Highlights](/model/reddit/app/community-highlights): Returns featured highlight content for a designated Reddit community, such as popular posts and announcements, by subreddit ID.
- [Reddit Search](/model/reddit/app/dynamic-search): Search Reddit posts, communities, comments, media and users with the Reddit app search.

---
Machine-readable: [`catalog/models/reddit/app/check-subreddit-muted.json`](../../../../catalog/models/reddit/app/check-subreddit-muted.json) · Store page: https://www.sandbase.ai/model/reddit/app/check-subreddit-muted
