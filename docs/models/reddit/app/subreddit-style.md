# Reddit Subreddit Rules and Style Info API: pricing, parameters and code examples

`reddit/app/subreddit-style` · data API · Reddit · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns rules, styling details, and moderator information for a designated Reddit subreddit. Accepts the subreddit name and an optional formatting toggle.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/app/subreddit-style"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/app/subreddit-style', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/app/subreddit-style", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/app/subreddit-style", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/reddit/app/subreddit-style` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `need_format` | boolean |  | Whether to clean and format the data default `false` |
| `subreddit_name` | string |  | Subreddit name default `"pics"` |

## Details

Retrieve rule specifications and community styling data for a target subreddit using `subreddit_name`. Set `need_format` to format and clean the returned payload.

### Use cases

- Inspect subreddit guidelines and configuration rules.
- Extract community moderator lists and identifiers.
- Retrieve subreddit style information for custom viewing interfaces.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/app/subreddit-style" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `need_format` | boolean | No | Whether to clean and format the data |
| `subreddit_name` | string | No | Subreddit name |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "subredditInfoByName": {
    "moderatorsInfo": {
      "edges": [
        {
          "node": {
            "id": "t2_2fpn"
          }
        }
      ]
    }
  }
}
```

### Notes

- Set `need_format` to true to return cleaned and formatted data.
- Specify the target community using `subreddit_name`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Reddit Subreddit Mute Status](/model/reddit/app/check-subreddit-muted): Checks whether a specified Reddit subreddit is muted by the current account using its ID.
- [Reddit App Comment Replies](/model/reddit/app/comment-replies): Returns replies and nested sub-comments under a Reddit post comment using a continuation cursor.
- [Reddit Community Highlights](/model/reddit/app/community-highlights): Returns featured highlight content for a designated Reddit community, such as popular posts and announcements, by subreddit ID.

---
Machine-readable: [`catalog/models/reddit/app/subreddit-style.json`](../../../../catalog/models/reddit/app/subreddit-style.json) · Store page: https://www.sandbase.ai/model/reddit/app/subreddit-style
