# X / Twitter Community Search API: pricing, parameters and code examples

`twitter/search-communities` · data API · X (Twitter) · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0011 per call · **Modes:** sync

Search X (Twitter) communities by keyword and get their id, name, topic, and member count with cursor pagination. This is how you find a community URL to pass to twitter.community or twitter.community_tweets.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0011**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/search-communities", "query": "artificial intelligence"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/search-communities', {'query': 'artificial intelligence'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/search-communities", {
  "query": "artificial intelligence"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/search-communities", sandbase.Params{
	"query": "artificial intelligence",
})
```

Same call via the path form: `POST /v1/api/twitter/search-communities` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Keyword to match against X (Twitter) community names and topics (e.g. artificial intelligence).  |
| `cursor` | string |  | Opaque pagination cursor from a previous response's nextCursor. Omit for the first page; pass it to fetch the next page of communities.  |

## Details

Returns a list of X (Twitter) communities that match a keyword. Each result has the community id, name, topic, member count, and URL. The only required input is `query`.

### Use cases

- Find communities about a topic such as artificial intelligence and rank them by member count.
- Collect community URLs to feed into a community tweet or community info lookup.
- Build a list of communities in a niche for outreach or research.
- Filter out adult communities using the `nsfw` flag before showing results to users.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/search-communities" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "artificial intelligence"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Keyword to match against X (Twitter) community names and topics (e.g. artificial intelligence). |
| `cursor` | string | No | Opaque pagination cursor from a previous response's nextCursor. Omit for the first page; pass it to fetch the next page of communities. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "communities": [
      {
        "id": "1724390935406981529",
        "memberCount": 17280,
        "name": "Artificial Intelligence + Tech",
        "nsfw": false,
        "topic": "Artificial Intelligence",
        "url": "https://x.com/i/communities/1724390935406981529"
      }
    ],
    "nextCursor": "cur_Hri4z2wlX1vEE2iyBu6uog"
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.communities[].id` | Numeric ID of the community, returned as a string. It is also the last part of the community URL. |
| `data.communities[].name` | Display name of the community. Several communities can share the same name. |
| `data.communities[].topic` | Topic label of the community, such as `Artificial Intelligence`. |
| `data.communities[].memberCount` | Number of members in the community. |
| `data.communities[].nsfw` | `true` if the community is marked as adult content, otherwise `false`. |
| `data.communities[].url` | Full link to the community on x.com. |
| `data.nextCursor` | Cursor value for the next page of results. Pass it as `cursor` in the next request. |
| `found` | `true` when the search returned results. |

### Notes

- For the next page, repeat the same `query` and add `cursor` set to the `data.nextCursor` value from the previous response.
- Use the `id` or `url` of a result with [X (Twitter) Twitter Community](/apis/twitter/community) or [X (Twitter) Twitter Community Tweets](/apis/twitter/community-tweets).
- Results are not sorted by `memberCount`, so sort them yourself if you need the largest communities first.

### Pricing

Billed at the actual cost of each call, about $0.0011 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/twitter/search-communities.json`](../../../catalog/models/twitter/search-communities.json) · Store page: https://www.sandbase.ai/model/twitter/search-communities
