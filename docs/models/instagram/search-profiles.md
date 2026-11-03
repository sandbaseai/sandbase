# Instagram Profile Search API: pricing, parameters and code examples

`instagram/search-profiles` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

Search public Instagram profiles by a bio or caption keyword.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/search-profiles", "query": "coffee roaster"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/search-profiles', {'query': 'coffee roaster'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/search-profiles", {
  "query": "coffee roaster"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/search-profiles", sandbase.Params{
	"query": "coffee roaster",
})
```

Same call via the path form: `POST /v1/api/instagram/search-profiles` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Bio or caption keyword/phrase to search for.  |
| `cursor` | string |  | Pagination cursor returned by a previous response.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `private`, and it is served only by a source that returns every one…  |

## Details

Returns a list of public Instagram profiles whose bio or captions match a keyword or phrase. It needs one input, `query`, such as `coffee roaster`. Each profile includes the handle, bio, follower counts, links, and flags like `verified` and `private`.

### Use cases

- Build a lead list of local businesses in a niche, such as coffee roasters, from their bio text.
- Find accounts that mention a brand, product type, or phrase in their bio for outreach.
- Compare follower counts across accounts in one niche to spot larger and smaller players.
- Collect the link-in-bio URLs of niche accounts to find their shops and ordering pages.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/search-profiles" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "coffee roaster"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Bio or caption keyword/phrase to search for. |
| `cursor` | string | No | Pagination cursor returned by a previous response. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `private`, and it is served only by a source that returns every one of |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "nextCursor": null,
    "profiles": [
      {
        "avatarUrl": "https://scontent-ord5-2.cdninstagram.com/v/t51.2885-19/236918550_117710895947947…",
        "bio": "🌍Showing you the BEST coffee scene #worldwide \n☕️Curated best coffee Branding & …",
        "bioLinks": [
          {
            "title": "",
            "url": "https://linktr.ee/roasterdaily"
          }
        ],
        "category": "Brand",
        "displayName": "Coffee Roasters & Coffee community  ®️ #roasterdaily",
        "externalUrl": "https://linktr.ee/roasterdaily",
        "followers": 306433,
        "following": 1669,
        "handle": "roasterdaily",
        "id": "7138727443",
        "isBusiness": false,
        "posts": null
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.profiles[].handle` | The Instagram username of the profile. |
| `data.profiles[].id` | The Instagram user ID as a string. |
| `data.profiles[].displayName` | The name shown on the profile. |
| `data.profiles[].bio` | The profile bio text. It can contain line breaks, emoji, and @mentions. |
| `data.profiles[].followers / data.profiles[].following` | The number of followers the profile has and the number of accounts it follows. |
| `data.profiles[].bioLinks[].url / data.profiles[].bioLinks[].title` | Each link listed in the profile bio, with its label. The title can be an empty string. |
| `data.profiles[].externalUrl` | The main external link on the profile. |
| `data.profiles[].category` | The profile category label, for example `Brand`. It is `null` when none is set. |
| `data.profiles[].verified / data.profiles[].private / data.profiles[].isBusiness` | Boolean flags for verified status, private account status, and business account status. |
| `data.nextCursor` | The cursor for the next page of results. It is `null` when there is no further page. |

### Notes

- To get the next page, pass the `nextCursor` value as `cursor` in the next request with the same `query`.
- `posts` is `null` in this response, so use a profile API to get post data for a handle. Try [Instagram Profile](/apis/instagram/profile) or [Instagram Basic Profile](/apis/instagram/basic-profile).
- Use `requireFields` with values such as `bioLinks`, `category`, `isBusiness`, or `private` when your workflow needs those fields to be present. This can change the price of the call.
- To find accounts related to a result, call [Instagram Similar Profiles](/apis/instagram/similar-profiles).

### Pricing

Billed at the actual cost of each call, about $0.0012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/instagram/search-profiles.json`](../../../catalog/models/instagram/search-profiles.json) · Store page: https://www.sandbase.ai/model/instagram/search-profiles
