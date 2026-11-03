# X / Twitter User Search API: pricing, parameters and code examples

`twitter/search-users` · data API · X (Twitter) · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00054 per call · **Modes:** sync

Search X (Twitter) accounts by keyword - the People tab of X search. Matches handles, display names, and profile bios, and returns normalized profile records with follower, following, and post counts plus cursor pagination. Use twitter.search for posts.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00054**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/search-users", "query": "ai agents"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/search-users', {'query': 'ai agents'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/search-users", {
  "query": "ai agents"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/search-users", sandbase.Params{
	"query": "ai agents",
})
```

Same call via the path form: `POST /v1/api/twitter/search-users` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Keyword to match against X (Twitter) handles, display names, and profile bios. This is the People tab of X search: pass a topic ('ai agents'), a name ('Elon Musk'), or a handle ('openai') and get back accounts, not…  |
| `cursor` | string |  | Opaque pagination cursor from a previous response's nextCursor. Omit for the first page; pass it to fetch the next page of accounts.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `location`, and it is served only by a source that returns every one…  |

## Details

Returns X (Twitter) accounts that match a keyword, like the People tab of X search. It needs one input, `query`, which can be a topic, a name, or a handle. Each account comes back with its bio, follower, following and post counts, and profile links.

### Use cases

- Build a lead list of accounts that talk about a topic, such as `ai agents`, and sort them by `followers`.
- Find the account behind a brand or person name and get its numeric `id` and `username`.
- Track new accounts in a niche by checking `createdUtc` across search results.
- Collect bios and profile URLs to review which accounts claim to work on a given subject.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/search-users" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "ai agents"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Keyword to match against X (Twitter) handles, display names, and profile bios. This is the People tab of X search: pass a topic ('ai agents'), a name ('Elon Musk'), or a handle ('openai') and get back accounts, not posts |
| `cursor` | string | No | Opaque pagination cursor from a previous response's nextCursor. Omit for the first page; pass it to fetch the next page of accounts. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `location`, and it is served only by a source that returns every one o |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "nextCursor": "cur_Vlh_zPr3gk8IXhV_RYndHg",
    "users": [
      {
        "avatarUrl": "https://pbs.twimg.com/profile_images/1878814517825572864/CjL1QsNr_normal.jpg",
        "bio": "The first #AIAgent web3 solution for Gaming & Engagement 🎮\n\nPlay #Gamety app: ht…",
        "canDm": null,
        "coverUrl": "https://pbs.twimg.com/profile_banners/1754796337399316480/1741867369",
        "createdUtc": 1707211049,
        "followers": 168259,
        "following": 106,
        "id": "1754796337399316480",
        "listedCount": null,
        "location": null,
        "name": "G-AGENTS AI💎",
        "posts": 1031
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.users[].id` | Numeric account ID as a string. Use it to identify the account in other calls. |
| `data.users[].username / data.users[].name` | `username` is the handle without the @ sign. `name` is the display name. |
| `data.users[].profileUrl` | Link to the account on x.com. |
| `data.users[].bio` | Profile bio text. It can contain line breaks, hashtags, and links. |
| `data.users[].followers / data.users[].following / data.users[].posts` | Counts of followers, accounts followed, and posts for the account. |
| `data.users[].createdUtc` | Account creation time as a Unix timestamp in seconds. |
| `data.users[].verified` | `true` if the account is marked as verified. |
| `data.users[].avatarUrl / data.users[].coverUrl` | Image URLs for the profile picture and the profile banner. |
| `data.users[].location / data.users[].canDm / data.users[].listedCount` | Optional fields. They are `null` in this response. Pass them in `requireFields` to ask for a source that returns them. |
| `data.nextCursor` | Cursor for the next page of accounts. |

### Notes

- For the next page, send the `nextCursor` value from the response as `cursor` with the same `query`.
- `requireFields` accepts `canDm`, `listedCount`, and `location`. It applies to the first page only and can change which source serves the call and its price.
- To search posts instead of accounts, use [Twitter Search Timeline](/apis/twitter/search).
- To get more detail on one account found here, call [Twitter User Profile](/apis/twitter/user-detail).

### Pricing

Billed at the actual cost of each call, about $0.00054 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/twitter/search-users.json`](../../../catalog/models/twitter/search-users.json) · Store page: https://www.sandbase.ai/model/twitter/search-users
