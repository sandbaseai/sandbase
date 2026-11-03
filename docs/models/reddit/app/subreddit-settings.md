# Reddit App Subreddit Settings API: pricing, parameters and code examples

`reddit/app/subreddit-settings` · data API · Reddit · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns settings and configuration details for a specified Reddit subreddit, including posting rules, flair settings, and moderation configurations.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/app/subreddit-settings", "need_format": false, "subreddit_id": "t5_2qh0u"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/app/subreddit-settings', {'need_format': False, 'subreddit_id': 't5_2qh0u'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/app/subreddit-settings", {
  "need_format": false,
  "subreddit_id": "t5_2qh0u"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/app/subreddit-settings", sandbase.Params{
	"need_format": false,
	"subreddit_id": "t5_2qh0u",
})
```

Same call via the path form: `POST /v1/api/reddit/app/subreddit-settings` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `need_format` | boolean |  | Whether to clean and format the data default `false` |
| `subreddit_id` | string | yes | Subreddit ID with format starting with t5_, e.g., "t5_2qh0u" (can be obtained from the fetch_subreddit_info endpoint)  |

## Details

Retrieve community configuration and moderation rules by specifying a `subreddit_id`.

### Use cases

- Inspect posting rules and flair configurations for a community.
- Review subreddit moderation and permission settings.
- Audit community operational settings across multiple subreddits.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/app/subreddit-settings" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"subreddit_id": "t5_2qh0u"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `subreddit_id` | string | Yes | Subreddit ID with format starting with t5_, e.g., "t5_2qh0u" (can be obtained from the fetch_subreddit_info endpoint) |
| `need_format` | boolean | No | Whether to clean and format the data |

### Notes

- The `subreddit_id` must start with the t5_ prefix, such as t5_2qh0u.
- Set `need_format` to true to return cleaned and formatted data.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Reddit Subreddit Mute Status](/apis/reddit/app/check-subreddit-muted): Checks whether a specified Reddit subreddit is muted by the current account using its ID.
- [Reddit App Comment Replies](/apis/reddit/app/comment-replies): Returns replies and nested sub-comments under a Reddit post comment using a continuation cursor.
- [Reddit Community Highlights](/apis/reddit/app/community-highlights): Returns featured highlight content for a designated Reddit community, such as popular posts and announcements, by subreddit ID.

---
Machine-readable: [`catalog/models/reddit/app/subreddit-settings.json`](../../../../catalog/models/reddit/app/subreddit-settings.json) · Store page: https://www.sandbase.ai/model/reddit/app/subreddit-settings
