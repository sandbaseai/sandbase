# Instagram Hashtag Recent Posts

`instagram/hashtag-recent-posts` · api · Instagram

Instagram posts published under a hashtag, newest first, read from its live chronological feed rather than a web search index. Built for monitoring: results arrive within a couple of minutes of posting, so engagement counts are usually still zero and reels do not appear (Instagram keeps those on a separate tab). For engagement-ranked results use instagram.hashtag_top_posts; for older relevance-ranked results use instagram.search_hashtag.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/hashtag-recent-posts", "hashtag": "skincare"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/hashtag-recent-posts', {'hashtag': 'skincare'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/hashtag-recent-posts", {
  "hashtag": "skincare"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/hashtag-recent-posts", sandbase.Params{
	"hashtag": "skincare",
})
```

Same call via the path form: `POST /v1/api/instagram/hashtag-recent-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Pagination cursor from a previous response's nextCursor.  |
| `hashtag` | string | yes | Hashtag to monitor, without the leading #.  |

## Details

Instagram posts published under a hashtag, newest first, read from its live chronological feed rather than a web search index. Built for monitoring: results arrive within a couple of minutes of posting, so engagement counts are usually still zero and reels do not appear (Instagram keeps those on a separate tab). For engagement-ranked results use instagram.hashtag_top_posts; for older relevance-ranked results use instagram.search_hashtag.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/hashtag-recent-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"hashtag": "skincare"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `hashtag` | string | Yes | Hashtag to monitor, without the leading #. |
| `cursor` | string | No | Pagination cursor from a previous response's nextCursor. |

### Pricing

Billed at the actual cost of each call, usually $0.0012 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/instagram/hashtag-recent-posts.json`](../../../catalog/models/instagram/hashtag-recent-posts.json) · Store page: https://www.sandbase.ai/model/instagram/hashtag-recent-posts
