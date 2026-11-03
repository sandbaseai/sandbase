# Instagram Search API: pricing, parameters and code examples

`instagram/search` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0036 per call · **Modes:** sync

Search Instagram for users, hashtags, or places by keyword and get matching results with names, counts, and links.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0036**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/search", "query": "nasa"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/search', {'query': 'nasa'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/search", {
  "query": "nasa"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/search", sandbase.Params{
	"query": "nasa",
})
```

Same call via the path form: `POST /v1/api/instagram/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `type` | string |  | What to search for: user profiles, hashtags, or places (e.g. hashtag). one of: `user`, `hashtag`, `place`; default `"user"` |
| `limit` | integer |  | Maximum number of results to return (1-20, default 20). range 1–20 |
| `query` | string | yes | Keyword to search Instagram for; one or more words without special punctuation (e.g. coffee roastery).  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `postsCount`, and it is served only by a source that returns every…  |

## Details

This API searches Instagram by keyword and returns a list of matching results. Each result has a name, handle, ID, profile image, and link. It needs a `query`, and you can set `type` to `user`, `hashtag`, or `place`.

### Use cases

- Find the official Instagram account for a brand or organization by searching its name.
- Build a list of candidate accounts for a topic, then check which ones are verified.
- Turn a keyword into Instagram user IDs and handles to feed into profile or post lookups.
- Add an account search box to a tool that links to each profile page.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "nasa"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Keyword to search Instagram for; one or more words without special punctuation (e.g. coffee roastery). |
| `limit` | integer | No | Maximum number of results to return (1-20, default 20). |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `postsCount`, and it is served only by a source that returns every one |
| `type` | string | No | What to search for: user profiles, hashtags, or places (e.g. hashtag). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "items": [
      {
        "bio": "",
        "followers": 0,
        "following": 0,
        "handle": "nasa",
        "id": "528817151",
        "image": "https://instagram.fsjc1-4.fna.fbcdn.net/v/t51.2885-19/29090066_159271188110124_1…",
        "name": "NASA",
        "postsCount": null,
        "url": "https://www.instagram.com/nasa/",
        "verified": true
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.items[].handle` | The account username, without the @ sign. |
| `data.items[].name` | The display name shown on the profile. |
| `data.items[].id` | The numeric Instagram ID of the account, returned as a string. |
| `data.items[].url` | Link to the profile page on Instagram. |
| `data.items[].verified` | `true` when the account has the verified badge. |
| `data.items[].image` | URL of the profile picture. |
| `data.items[].followers / data.items[].following` | Follower and following counts. In this sample response they are `0` for every result, so do not rely on them for ranking. |
| `data.items[].bio` | Profile biography text. It is an empty string in this sample response. |
| `data.items[].postsCount` | Number of posts on the account. It is `null` in this sample response. |
| `found` | `true` when the search returned results. |

### Notes

- Results are in `data.items`. A search with no match still succeeds and returns `found: false`.
- Use `limit` (1 to 20) to cap the number of results. There is no page parameter.
- `postsCount` came back as `null` in this sample. Pass `requireFields: ["postsCount"]` to route to a source that returns it. This can raise the price of the call.
- For full profile details, take the `handle` or `id` and call [Instagram Profile](/apis/instagram/profile) or [Instagram User Profile by ID](/apis/instagram/v1/user-info-by-id).

### Pricing

Billed at the actual cost of each call, about $0.0036 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/instagram/search.json`](../../../catalog/models/instagram/search.json) · Store page: https://www.sandbase.ai/model/instagram/search
