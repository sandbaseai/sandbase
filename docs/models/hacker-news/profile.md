# Hacker News Profile API: pricing, parameters and code examples

`hacker-news/profile` · data API · Hacker News · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0015 per call · **Modes:** sync

Get a Hacker News user's public profile by username - karma, bio, and account details as clean JSON.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0015**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "hacker-news/profile", "handle": "pg"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('hacker-news/profile', {'handle': 'pg'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("hacker-news/profile", {
  "handle": "pg"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "hacker-news/profile", sandbase.Params{
	"handle": "pg",
})
```

Same call via the path form: `POST /v1/api/hacker-news/profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `handle` | string | yes | Hacker News username, e.g. "pg".  |

## Details

Returns the public profile of a Hacker News user: the username, karma score, and bio. It needs one input, the Hacker News username as `handle`.

### Use cases

- Check the karma of a Hacker News account before you trust or rank its comments.
- Show an author's bio and karma next to their posts in a dashboard.
- Confirm that a Hacker News username exists before you run further lookups.
- Track the karma of a set of well-known users over time.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/hacker-news/profile" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"handle": "pg"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `handle` | string | Yes | Hacker News username, e.g. "pg". |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "bio": "Bug fixer.",
    "karma": 157316,
    "username": "pg"
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `found` | `true` when the username exists. A lookup with no match still succeeds and returns `found: false`. |
| `data.username` | The Hacker News username of the profile. |
| `data.karma` | The karma score of the user. |
| `data.bio` | The text the user wrote in the profile's about field. |

### Notes

- Pass the username exactly as it appears on Hacker News, for example `pg`.
- Check `found` before you read `data`, because a missing user returns `found: false`.
- To find stories and comments on Hacker News, use [Hacker News Search](/apis/hacker-news/search).
- To read a specific story and its discussion, call [Hacker News Story](/apis/hacker-news/story) or [Hacker News Story Comments](/apis/hacker-news/story-comments).

### Pricing

Billed at the actual cost of each call, about $0.0015 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/hacker-news/profile.json`](../../../catalog/models/hacker-news/profile.json) · Store page: https://www.sandbase.ai/model/hacker-news/profile
