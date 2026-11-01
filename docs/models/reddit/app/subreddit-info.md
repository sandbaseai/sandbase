# Reddit App Subreddit Info

`reddit/app/subreddit-info` · api · Reddit

Returns detailed metadata for a Reddit subreddit, such as rules, descriptions, and app installations. Look up data by subreddit name with optional response formatting.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/app/subreddit-info"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/app/subreddit-info', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/app/subreddit-info", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/app/subreddit-info", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/reddit/app/subreddit-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `need_format` | boolean |  | Whether to clean and format the data default `false` |
| `subreddit_name` | string |  | Subreddit name (without r/ prefix), e.g., "pics", "funny", "AskReddit" default `"pics"` |

## Details

Retrieve detailed community information and metadata using `subreddit_name`. Use `need_format` to clean and format the returned payload.

### Use cases

- Look up metadata and app installations for a specific subreddit.
- Inspect community rules and subscriber statistics across communities.
- Check subreddit configuration details before building automated workflows.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/app/subreddit-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `need_format` | boolean | No | Whether to clean and format the data |
| `subreddit_name` | string | No | Subreddit name (without r/ prefix), e.g., "pics", "funny", "AskReddit" |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "subredditInfoByName": {
    "devvit": {
      "installations": [
        {
          "app": {
            "name": "spazdeko"
          }
        }
      ]
    }
  }
}
```

### Notes

- Supply `subreddit_name` without the 'r/' prefix, such as 'pics' or 'funny'.
- Set `need_format` to true to clean and format the output data.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Reddit Subreddit Mute Status](/model/reddit/app/check-subreddit-muted): Checks whether a specified Reddit subreddit is muted by the current account using its ID.
- [Reddit App Comment Replies](/model/reddit/app/comment-replies): Returns replies and nested sub-comments under a Reddit post comment using a continuation cursor.
- [Reddit Community Highlights](/model/reddit/app/community-highlights): Returns featured highlight content for a designated Reddit community, such as popular posts and announcements, by subreddit ID.

---
Machine-readable: [`catalog/models/reddit/app/subreddit-info.json`](../../../../catalog/models/reddit/app/subreddit-info.json) · Store page: https://www.sandbase.ai/model/reddit/app/subreddit-info
