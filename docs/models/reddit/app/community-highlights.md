# Reddit Community Highlights API: pricing, parameters and code examples

`reddit/app/community-highlights` · data API · Reddit · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns featured highlight content for a designated Reddit community, such as popular posts and announcements, by subreddit ID. Supports optional response data formatting.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/app/community-highlights", "need_format": false, "subreddit_id": "t5_2qh0u"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/app/community-highlights', {'need_format': False, 'subreddit_id': 't5_2qh0u'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/app/community-highlights", {
  "need_format": false,
  "subreddit_id": "t5_2qh0u"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/app/community-highlights", sandbase.Params{
	"need_format": false,
	"subreddit_id": "t5_2qh0u",
})
```

Same call via the path form: `POST /v1/api/reddit/app/community-highlights` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `need_format` | boolean |  | Whether to clean and format the data default `false` |
| `subreddit_id` | string | yes | Subreddit ID starting with "t5_", can be obtained from fetch_subreddit_info endpoint  |

## Details

Retrieve highlighted content and top announcements for a specific subreddit using `subreddit_id`. Optionally clean and format the output data via `need_format`.

### Use cases

- Display pinned community announcements in custom Reddit dashboards.
- Monitor popular featured posts from designated subreddits.
- Feed curated subreddit highlight streams into moderation tools.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/app/community-highlights" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"subreddit_id": "t5_2qh0u"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `subreddit_id` | string | Yes | Subreddit ID starting with "t5_", can be obtained from fetch_subreddit_info endpoint |
| `need_format` | boolean | No | Whether to clean and format the data |

### Notes

- `subreddit_id` must start with "t5_" and can be obtained from the subreddit info endpoint.
- Set `need_format` to true to clean and format the returned data.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Reddit Subreddit Mute Status](/model/reddit/app/check-subreddit-muted): Checks whether a specified Reddit subreddit is muted by the current account using its ID.
- [Reddit App Comment Replies](/model/reddit/app/comment-replies): Returns replies and nested sub-comments under a Reddit post comment using a continuation cursor.
- [Reddit Search](/model/reddit/app/dynamic-search): Search Reddit posts, communities, comments, media and users with the Reddit app search.

---
Machine-readable: [`catalog/models/reddit/app/community-highlights.json`](../../../../catalog/models/reddit/app/community-highlights.json) · Store page: https://www.sandbase.ai/model/reddit/app/community-highlights
