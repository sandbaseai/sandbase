# X / Twitter Followers API: pricing, parameters and code examples

`twitter/followers` · data API · X (Twitter) · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00045 per call · **Modes:** sync

Fetch the follower list of any public X (Twitter) account by username with cursor pagination. Limit is a per-page maximum and a native page holds up to 200 accounts; follow the response's nextCursor for more.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00045**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/followers", "username": "nasa"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/followers', {'username': 'nasa'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/followers", {
  "username": "nasa"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/followers", sandbase.Params{
	"username": "nasa",
})
```

Same call via the path form: `POST /v1/api/twitter/followers` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Accepted but does not change the page: every call returns one full native page of followers (up to 200, depending on the source), never trimmed, so follow nextCursor to continue exactly where this response ended. default `200`; range 1–100000 |
| `cursor` | string |  | Opaque pagination cursor from a previous response's nextCursor. Omit for the first page; pass it to fetch the next page of followers.  |
| `username` | string | yes | The X (Twitter) username to fetch followers for, without the @ prefix (e.g. elonmusk).  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `bio`, and it is served only by a source that returns every one of…  |

## Details

Returns a page of accounts that follow a public X (Twitter) user. It needs the `username` of the account, without the @ prefix. Each page holds up to 200 accounts and comes with a cursor for the next page.

### Use cases

- Build a list of accounts that follow a brand or agency account to review its audience.
- Find large or verified followers of a competitor account for outreach.
- Export follower IDs and usernames to track who joins an account's audience between two runs.
- Check which followers are located in a given place by reading the `location` text.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/followers" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": 200, "username": "nasa"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | The X (Twitter) username to fetch followers for, without the @ prefix (e.g. elonmusk). |
| `cursor` | string | No | Opaque pagination cursor from a previous response's nextCursor. Omit for the first page; pass it to fetch the next page of followers. |
| `limit` | integer | No | Accepted but does not change the page: every call returns one full native page of followers (up to 200, depending on the source), never trimmed, so follow nextCursor to continue exactly where this response ended. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `bio`, and it is served only by a source that returns every one of the |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "items": [
      {
        "avatarUrl": "https://pbs.twimg.com/profile_images/1697749409851985920/HbrI04tM_normal.jpg",
        "createdUtc": 1240523610,
        "followers": 41933593,
        "id": "34743251",
        "location": "Earth",
        "name": "SpaceX",
        "username": "SpaceX",
        "verified": true
      }
    ],
    "nextCursor": "cur_S42qvQ9PIxL0rN8yJt8zUg"
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.items[]` | One follower account per row. |
| `data.items[].id` | The follower's numeric account ID, returned as a string. |
| `data.items[].username / data.items[].name` | The follower's handle and display name. |
| `data.items[].followers` | How many followers this follower account has. |
| `data.items[].verified` | `true` when the follower account is marked as verified. |
| `data.items[].location` | The free-text location the follower set on their profile. It can be empty or not a real place. |
| `data.items[].createdUtc` | When the follower account was created, as a Unix timestamp in seconds. |
| `data.items[].avatarUrl` | Link to the follower's profile image. |
| `data.nextCursor` | Cursor to pass as `cursor` to get the next page of followers. |
| `found` | `true` when the account was found. |

### Notes

- Pass `username` without the @ prefix, for example `nasa`.
- `limit` does not change the page size. Each call returns one full native page, so pass `data.nextCursor` as `cursor` to continue where the last page ended.
- Omit `cursor` for the first page. Treat cursor values as opaque strings.
- To list only verified followers, use [X (Twitter) Verified Followers](/apis/twitter/verified-followers). To list the accounts a user follows, use [X / Twitter Following](/apis/twitter/following).

### Pricing

Billed at the actual cost of each call, about $0.00045 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/twitter/followers.json`](../../../catalog/models/twitter/followers.json) · Store page: https://www.sandbase.ai/model/twitter/followers
