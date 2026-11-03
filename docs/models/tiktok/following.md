# TikTok Following API: pricing, parameters and code examples

`tiktok/following` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0008 per call · **Modes:** sync

List the accounts a TikTok user follows (handle, display name, follower count, bio) by username.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0008**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/following", "handle": "stoolpresidente"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/following', {'handle': 'stoolpresidente'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/following", {
  "handle": "stoolpresidente"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/following", sandbase.Params{
	"handle": "stoolpresidente",
})
```

Same call via the path form: `POST /v1/api/tiktok/following` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Pagination cursor from a previous response.  |
| `handle` | string | yes | TikTok username without the leading @ (e.g. "stoolpresidente").  |
| `requireCursor` | boolean |  | Deprecated; send `requireFields: ["nextCursor"]` instead, which does exactly the same thing. Set true if you intend to page through results, so the request is only served by a source that can return a nextCursor. Omit…  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `secUid` or `instagramUrl`, and it is served only by a source that…  |

## Details

Returns the list of accounts a TikTok user follows. Each entry has the account's handle, display name, bio, follower count and other profile stats. The only required input is the user's `handle`, without the leading @.

### Use cases

- Map which brands, creators and media accounts a public figure follows.
- Build a lead list of accounts in a niche by reading the following list of a known account in that niche.
- Find the Instagram or YouTube links of followed accounts to match them across platforms.
- Check follower counts of followed accounts to rank them by reach.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/following" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"handle": "stoolpresidente"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `handle` | string | Yes | TikTok username without the leading @ (e.g. "stoolpresidente"). |
| `cursor` | string | No | Pagination cursor from a previous response. |
| `requireCursor` | boolean | No | Deprecated; send `requireFields: ["nextCursor"]` instead, which does exactly the same thing. Set true if you intend to page through results, so the request is only served by a source that can return a nextCursor. Omit it |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `secUid` or `instagramUrl`, and it is served only by a source that ret |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "following": [
      {
        "avatarUrl": "https://p19-common-sign.tiktokcdn-us.com/tos-useast8-avt-0068-tx2/2319d7ccb11877…",
        "bio": "Mentally at #BravoFanFest.\n🎥 Stream panels and other highlights on @Peacock!",
        "createdUtc": 1556919392,
        "displayName": "Bravo",
        "followers": 1833483,
        "following": 308,
        "handle": "bravotv",
        "id": "6685660834896626693",
        "instagramUrl": "https://www.instagram.com/bravotv",
        "likes": 150718953,
        "private": false,
        "region": "US"
      }
    ],
    "nextCursor": null
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.following[].handle / data.following[].displayName` | The account's TikTok username and its display name. |
| `data.following[].bio` | The profile bio text of the followed account. |
| `data.following[].followers / data.following[].following` | Number of followers the account has, and number of accounts it follows. |
| `data.following[].likes / data.following[].videos` | Total likes the account has received and the number of videos it has posted. |
| `data.following[].id / data.following[].secUid` | Numeric account ID as a string, and the `secUid` identifier for the account. |
| `data.following[].createdUtc` | Account creation time as a Unix timestamp in seconds. |
| `data.following[].instagramUrl / data.following[].youtubeUrl` | Instagram and YouTube links from the profile. The value is `null` when the account has none. |
| `data.following[].private / data.following[].region` | Whether the account is private, and its region code such as `US`. |
| `data.nextCursor` | Cursor for the next page. It is `null` when no further page is returned. |
| `found` | `true` when the lookup matched a user. |

### Notes

- Send `handle` without the @, for example `stoolpresidente`.
- To page through results, pass the `data.nextCursor` value as `cursor` in the next request.
- Send `requireFields: ["nextCursor"]` if you plan to page. Use `requireFields` with `secUid`, `instagramUrl` or `youtubeUrl` to force a source that returns those fields.
- `createdUtc` is in seconds since the Unix epoch.

### Pricing

Billed at the actual cost of each call, about $0.0008 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/tiktok/following.json`](../../../catalog/models/tiktok/following.json) · Store page: https://www.sandbase.ai/model/tiktok/following
