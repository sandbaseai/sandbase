# Facebook Ad Search

`facebook/ads-search` · api · Facebook

Search the Meta Ad Library by keyword and get matching ads (advertiser, creative text, CTA, platforms, and run dates) with cursor pagination.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0011**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "facebook/ads-search", "query": "nike"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('facebook/ads-search', {'query': 'nike'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("facebook/ads-search", {
  "query": "nike"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "facebook/ads-search", sandbase.Params{
	"query": "nike",
})
```

Same call via the path form: `POST /v1/api/facebook/ads-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Keyword to search the Meta Ad Library for (e.g. "protein powder").  |
| `adType` | string |  | Restrict to all ads (default) or only political and issue ads. one of: `all`, `political_and_issue_ads` |
| `cursor` | string |  | Opaque pagination cursor from a previous response's nextCursor.  |
| `sortBy` | string |  | Sort order: impressions (highest first, the default) or recent (most recent). one of: `impressions`, `recent` |
| `status` | string |  | Ad status filter. one of: `ALL`, `ACTIVE`, `INACTIVE`; default `"ACTIVE"` |
| `country` | string |  | Two-letter country code to scope results. Omit for all countries.  |
| `endDate` | string |  | Filter to ads with impressions on or before this date, in YYYY-MM-DD format.  |
| `mediaType` | string |  | Creative media type filter. one of: `ALL`, `IMAGE`, `VIDEO`, `MEME`, `IMAGE_AND_MEME`, `NONE` |
| `startDate` | string |  | Filter to ads with impressions on or after this date, in YYYY-MM-DD format.  |
| `searchType` | string |  | Match mode for the query: loose keyword match (keyword_unordered, the default) or exact phrase (keyword_exact_phrase). one of: `keyword_unordered`, `keyword_exact_phrase` |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `totalResults`, and it is served only by a source that returns every…  |

## Details

Search the Meta Ad Library by keyword and get matching ads (advertiser, creative text, CTA, platforms, and run dates) with cursor pagination.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/facebook/ads-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "nike", "country": "US", "searchType": "keyword_exact_phrase"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Keyword to search the Meta Ad Library for (e.g. "protein powder"). |
| `adType` | string | No | Restrict to all ads (default) or only political and issue ads. One of: `all`, `political_and_issue_ads`. |
| `country` | string | No | Two-letter country code to scope results. Omit for all countries. |
| `cursor` | string | No | Opaque pagination cursor from a previous response's nextCursor. |
| `endDate` | string | No | Filter to ads with impressions on or before this date, in YYYY-MM-DD format. |
| `mediaType` | string | No | Creative media type filter. One of: `ALL`, `IMAGE`, `VIDEO`, `MEME`, `IMAGE_AND_MEME`, `NONE`. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `totalResults`, and it is served only by a source that returns every o |
| `searchType` | string | No | Match mode for the query: loose keyword match (keyword_unordered, the default) or exact phrase (keyword_exact_phrase). One of: `keyword_unordered`, `keyword_exact_phrase`. |
| `sortBy` | string | No | Sort order: impressions (highest first, the default) or recent (most recent). One of: `impressions`, `recent`. |
| `startDate` | string | No | Filter to ads with impressions on or after this date, in YYYY-MM-DD format. |
| `status` | string | No | Ad status filter. One of: `ALL`, `ACTIVE`, `INACTIVE`. Default `"ACTIVE"`. |

### Pricing

Billed at the actual cost of each call, usually $0.0011 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/facebook/ads-search.json`](../../../catalog/models/facebook/ads-search.json) · Store page: https://www.sandbase.ai/model/facebook/ads-search
