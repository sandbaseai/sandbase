# Reddit User Public Trophies API: pricing, parameters and code examples

`reddit/app/user-trophies` · data API · Reddit · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns a list of public trophies and achievements for a specified Reddit account. Users can supply a username and optionally request cleaned, formatted data.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/app/user-trophies", "username": "spez"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/app/user-trophies', {'username': 'spez'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/app/user-trophies", {
  "username": "spez"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/app/user-trophies", sandbase.Params{
	"username": "spez",
})
```

Same call via the path form: `POST /v1/api/reddit/app/user-trophies` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `username` | string | yes | Reddit username (without u/ prefix)  |
| `need_format` | boolean |  | Whether to clean and format the data  |

## Details

Retrieve the public achievements and trophies earned by a Reddit user by specifying their `username`.

### Use cases

- Display user badges and achievements in community profiles.
- Inspect Reddit account milestones and historical participation awards.
- Verify account authenticity and longevity using public trophy records.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/app/user-trophies" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "<username>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | Reddit username (without u/ prefix) |
| `need_format` | boolean | No | Whether to clean and format the data |

### Notes

- Provide the `username` without the u/ prefix.
- Set `need_format` to true to receive cleaned and formatted response data.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Reddit Subreddit Mute Status](/model/reddit/app/check-subreddit-muted): Checks whether a specified Reddit subreddit is muted by the current account using its ID.
- [Reddit App Comment Replies](/model/reddit/app/comment-replies): Returns replies and nested sub-comments under a Reddit post comment using a continuation cursor.
- [Reddit Community Highlights](/model/reddit/app/community-highlights): Returns featured highlight content for a designated Reddit community, such as popular posts and announcements, by subreddit ID.

---
Machine-readable: [`catalog/models/reddit/app/user-trophies.json`](../../../../catalog/models/reddit/app/user-trophies.json) · Store page: https://www.sandbase.ai/model/reddit/app/user-trophies
