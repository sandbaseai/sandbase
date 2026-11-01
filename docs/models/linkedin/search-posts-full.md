# LinkedIn Post Search (full)

`linkedin/search-posts-full` · api · LinkedIn

Search public LinkedIn posts with rich author, engagement, attachment, and poll details.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.004**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/search-posts-full", "query": "artificial intelligence"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/search-posts-full', {'query': 'artificial intelligence'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/search-posts-full", {
  "query": "artificial intelligence"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/search-posts-full", sandbase.Params{
	"query": "artificial intelligence",
})
```

Same call via the path form: `POST /v1/api/linkedin/search-posts-full` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sort` | string |  | Order results by search relevance or publication date. one of: `relevance`, `date`; default `"relevance"` |
| `limit` | integer |  | Maximum number of posts to return (1-100, default 10). The upper bound is one LinkedIn search page. default `10`; range 1–100 |
| `query` | string | yes | LinkedIn post search query, including quoted terms or Boolean operators accepted by LinkedIn search.  |
| `authorUrls` | array |  | Only return posts authored by these LinkedIn profile or company URLs.  |
| `datePosted` | string |  | Only return posts published within this relative time window. Last-hour and windows beyond one month route to the provider that supports them. one of: `last-hour`, `last-day`, `last-week`, `last-month`, `last-three-months`, `last-six-months`, `last-year`; default `"last-day"` |
| `contentType` | string |  | Only return posts carrying this content type. one of: `all`, `videos`, `images`, `jobs`, `live-videos`, `documents`, `collaborative-articles` |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `attachmentType` or `pollOptions`, and it is served only by a source…  |
| `authorKeywords` | string |  | Only return posts whose author profile headline or job title contains at least one of these keywords.  |
| `authorIndustryIds` | array |  | Only return posts by authors associated with these LinkedIn industry IDs.  |
| `authorCompanyNames` | array |  | Only return posts by people associated with these company names.  |
| `mentioningMemberUrls` | array |  | Only return posts mentioning these LinkedIn member profile URLs.  |

## Details

Search public LinkedIn posts with rich author, engagement, attachment, and poll details.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/search-posts-full" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sort": "relevance", "limit": 10, "query": "artificial intelligence", "datePosted": "last-week"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | LinkedIn post search query, including quoted terms or Boolean operators accepted by LinkedIn search. |
| `authorCompanyNames` | array | No | Only return posts by people associated with these company names. |
| `authorIndustryIds` | array | No | Only return posts by authors associated with these LinkedIn industry IDs. |
| `authorKeywords` | string | No | Only return posts whose author profile headline or job title contains at least one of these keywords. |
| `authorUrls` | array | No | Only return posts authored by these LinkedIn profile or company URLs. |
| `contentType` | string | No | Only return posts carrying this content type. One of: `all`, `videos`, `images`, `jobs`, `live-videos`, `documents`, `collaborative-articles`. |
| `datePosted` | string | No | Only return posts published within this relative time window. Last-hour and windows beyond one month route to the provider that supports them. One of: `last-hour`, `last-day`, `last-week`, `last-month`, `last-three-month |
| `limit` | integer | No | Maximum number of posts to return (1-100, default 10). The upper bound is one LinkedIn search page. |
| `mentioningMemberUrls` | array | No | Only return posts mentioning these LinkedIn member profile URLs. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `attachmentType` or `pollOptions`, and it is served only by a source t |
| `sort` | string | No | Order results by search relevance or publication date. One of: `relevance`, `date`. Default `"relevance"`. |

### Pricing

Billed at the actual cost of each call, usually $0.004 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/linkedin/search-posts-full.json`](../../../catalog/models/linkedin/search-posts-full.json) · Store page: https://www.sandbase.ai/model/linkedin/search-posts-full
