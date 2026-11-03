# TikTok Followers API: pricing, parameters and code examples

`tiktok/followers` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0008 per call · **Modes:** sync

List the followers of a TikTok account by username, returning each follower's profile basics.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0008**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/followers", "handle": "stoolpresidente"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/followers', {'handle': 'stoolpresidente'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/followers", {
  "handle": "stoolpresidente"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/followers", sandbase.Params{
	"handle": "stoolpresidente",
})
```

Same call via the path form: `POST /v1/api/tiktok/followers` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Pagination cursor from a previous response's nextCursor, to fetch the next page of followers.  |
| `handle` | string | yes | TikTok username whose followers to list, without the @ prefix (e.g. stoolpresidente).  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `videoCount` or `secUid`, and it is served only by a source that…  |

## Details

Returns a page of followers for a TikTok account, with each follower's profile basics such as nickname, bio, region, and follower and video counts. It needs one input: the account's `handle`, without the @ prefix.

### Use cases

- Sample the followers of a large account to see what kind of audience it attracts.
- Spot follower accounts with zero videos and zero likes to estimate how many look inactive or fake.
- Build a list of follower accounts with high `followerCount` to find potential creators or partners.
- Collect `secUid` and `userId` values from followers to feed into other profile lookups.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/followers" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"handle": "stoolpresidente"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `handle` | string | Yes | TikTok username whose followers to list, without the @ prefix (e.g. stoolpresidente). |
| `cursor` | string | No | Pagination cursor from a previous response's nextCursor, to fetch the next page of followers. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `videoCount` or `secUid`, and it is served only by a source that retur |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "followers": [
      {
        "avatarUrl": "https://p19-common-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/731635406335901…",
        "bio": "",
        "createdUtc": 1703471425,
        "followerCount": 18,
        "followingCount": 64,
        "likeCount": 0,
        "nickname": "brianperry30",
        "region": "US",
        "secUid": "MS4wLjABAAAA7yz1nroIyNpNiIFoPPz6DyGBVHqiP6CXaNi1QruAcWHICikNSwxUHOzCFXgHCH5j",
        "userId": "7316353678259389483",
        "username": "brianperry30",
        "videoCount": 0
      }
    ],
    "nextCursor": null,
    "total": 4788422
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.followers[].username / data.followers[].nickname` | The follower's unique TikTok handle and the display name they chose. |
| `data.followers[].bio` | The text from the follower's profile bio. It can be an empty string. |
| `data.followers[].userId / data.followers[].secUid` | Identifiers for the follower account. `userId` is a numeric string and `secUid` is a longer encoded string. |
| `data.followers[].followerCount / data.followers[].followingCount` | How many accounts follow this follower and how many accounts this follower follows. |
| `data.followers[].likeCount / data.followers[].videoCount` | Total likes the follower's account has received and the number of videos the follower has posted. |
| `data.followers[].createdUtc` | When the follower's account was created, as a Unix timestamp in seconds. |
| `data.followers[].region` | Region code shown on the follower's profile, such as `US`. |
| `data.followers[].avatarUrl` | Link to the follower's profile picture. |
| `data.total` | Total follower count reported for the account you queried. |
| `data.nextCursor` | Cursor for the next page of followers. It is `null` when no further page is returned. |

### Notes

- Pass the username without the @ prefix, for example `stoolpresidente`.
- To get the next page, send the `nextCursor` value from the previous response as `cursor`.
- Use `requireFields` with values like `secUid` or `videoCount` if you need those fields on every follower. Naming a field can change which source serves the call and its price.
- `data.total` is the account's full follower count, so it is much larger than the number of items in one page.

### Pricing

Billed at the actual cost of each call, about $0.0008 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/tiktok/followers.json`](../../../catalog/models/tiktok/followers.json) · Store page: https://www.sandbase.ai/model/tiktok/followers
