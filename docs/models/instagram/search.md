# Instagram Search

`instagram/search` · api · Instagram

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

Search Instagram for users, hashtags, or places by keyword and get matching results with names, counts, and links.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "nasa"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Keyword to search Instagram for; one or more words without special punctuation (e.g. coffee roastery). |
| `limit` | integer | No | Maximum number of results to return (1-20, default 20). |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `postsCount`, and it is served only by a source that returns every one |
| `type` | string | No | What to search for: user profiles, hashtags, or places (e.g. hashtag). One of: `user`, `hashtag`, `place`. Default `"user"`. |

### Pricing

Billed at the actual cost of each call, usually $0.0036 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/instagram/search.json`](../../../catalog/models/instagram/search.json) · Store page: https://www.sandbase.ai/model/instagram/search
