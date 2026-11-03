# X / Twitter Following API: pricing, parameters and code examples

`twitter/following` · data API · X (Twitter) · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00045 per call · **Modes:** sync

List the accounts a public X (Twitter) account follows by username with cursor pagination. Limit is a per-page maximum; follow the response's nextCursor for more.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00045**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/following", "username": "nasa"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/following', {'username': 'nasa'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/following", {
  "username": "nasa"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/following", sandbase.Params{
	"username": "nasa",
})
```

Same call via the path form: `POST /v1/api/twitter/following` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Accepted but does not change the page: every call returns one full native page of followed accounts (about 50), never trimmed, so follow nextCursor to continue exactly where this response ended. default `200`; range 1–100000 |
| `cursor` | string |  | Opaque pagination cursor from a previous response's nextCursor. Omit for the first page; pass it to fetch the next page of followed accounts.  |
| `username` | string | yes | The X (Twitter) username to fetch the following list for, without the @ prefix (e.g. elonmusk).  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `location`, and it is served only by a source that returns every one…  |

## Details

Returns the accounts that a public X (Twitter) account follows, one page at a time. You pass the account `username` without the @ prefix. Each item has the followed account's profile basics and follower counts.

### Use cases

- Map which accounts a brand or agency account follows to see its peers and partners.
- Build a list of followed accounts to check who a public figure pays attention to.
- Collect the `id` values of followed accounts and look up their full profiles or posts.
- Compare the following lists of two accounts to find shared interests.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/following" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": 200, "username": "nasa"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | The X (Twitter) username to fetch the following list for, without the @ prefix (e.g. elonmusk). |
| `cursor` | string | No | Opaque pagination cursor from a previous response's nextCursor. Omit for the first page; pass it to fetch the next page of followed accounts. |
| `limit` | integer | No | Accepted but does not change the page: every call returns one full native page of followed accounts (about 50), never trimmed, so follow nextCursor to continue exactly where this response ended. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `location`, and it is served only by a source that returns every one o |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "items": [
      {
        "avatarUrl": "https://pbs.twimg.com/profile_images/3468011581/efb985f24af0a814a722457a768f3cc5…",
        "bio": "The official X account for the NASA Hubble Space Telescope, managed and operated…",
        "createdUtc": 1204834502,
        "followers": 8894641,
        "following": 44,
        "id": "14091091",
        "name": "Hubble",
        "posts": 8503,
        "username": "NASAHubble"
      }
    ],
    "nextCursor": "cur_W0kxlUWcLC2JYpqfMFBqDw"
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.items[].username / data.items[].name` | The handle and display name of the followed account. |
| `data.items[].id` | The numeric ID of the followed account, returned as a string. |
| `data.items[].bio` | The profile bio text. Some accounts have no `bio`, and the key is then missing. |
| `data.items[].followers / data.items[].following` | How many accounts follow the followed account, and how many accounts it follows. |
| `data.items[].posts` | The post count of the followed account. |
| `data.items[].createdUtc` | When the followed account was created, as a Unix timestamp in seconds (UTC). |
| `data.items[].avatarUrl` | The URL of the profile image of the followed account. |
| `data.nextCursor` | Cursor for the next page. Pass it as `cursor` in the next request. |
| `found` | `true` when the account was found. |

### Notes

- Use the handle without the @ prefix, for example `nasa`.
- `limit` does not change the page size. Each call returns one full page of about 50 accounts, so follow `nextCursor` to continue.
- For the first page, omit `cursor`. For later pages, pass the `nextCursor` value from the previous response unchanged.
- To list the accounts that follow this account instead, call [X / Twitter Followers](/apis/twitter/followers).

### Pricing

Billed at the actual cost of each call, about $0.00045 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/twitter/following.json`](../../../catalog/models/twitter/following.json) · Store page: https://www.sandbase.ai/model/twitter/following
