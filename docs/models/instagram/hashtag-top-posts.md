# Instagram Hashtag Top Posts

`instagram/hashtag-top-posts` · api · Instagram

Instagram's own top-ranked posts for a hashtag, read from its live hashtag feed rather than a web search index, with view, like, and comment counts. Reels-heavy and engagement-ranked, so it answers what is performing on a tag right now. For older relevance-ranked results with date and media-type filters use instagram.search_hashtag; for the chronological feed use instagram.hashtag_recent_posts.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0011**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/hashtag-top-posts", "hashtag": "skincare"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/hashtag-top-posts', {'hashtag': 'skincare'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/hashtag-top-posts", {
  "hashtag": "skincare"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/hashtag-top-posts", sandbase.Params{
	"hashtag": "skincare",
})
```

Same call via the path form: `POST /v1/api/instagram/hashtag-top-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Pagination cursor from a previous response's nextCursor.  |
| `hashtag` | string | yes | Hashtag to fetch, without the leading #.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `soundTitle`, and it is served only by a source that returns every…  |

## Details

Instagram's own top-ranked posts for a hashtag, read from its live hashtag feed rather than a web search index, with view, like, and comment counts. Reels-heavy and engagement-ranked, so it answers what is performing on a tag right now. For older relevance-ranked results with date and media-type filters use instagram.search_hashtag; for the chronological feed use instagram.hashtag_recent_posts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/hashtag-top-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"hashtag": "skincare"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `hashtag` | string | Yes | Hashtag to fetch, without the leading #. |
| `cursor` | string | No | Pagination cursor from a previous response's nextCursor. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `soundTitle`, and it is served only by a source that returns every one |

### Pricing

Billed at the actual cost of each call, usually $0.0011 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/instagram/hashtag-top-posts.json`](../../../catalog/models/instagram/hashtag-top-posts.json) · Store page: https://www.sandbase.ai/model/instagram/hashtag-top-posts
