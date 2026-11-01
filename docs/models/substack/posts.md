# Substack Posts

`substack/posts` · api · Substack

Pull posts from any Substack publication by its URL, or pass a single post URL (…/p/slug) to fetch just that one article. Returns title, subtitle, publish date, paywall status, word count, engagement (reactions, comments, restacks), author profile, publication details, the full article body as text, HTML and Markdown, and optional comment threads.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0444**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "substack/posts", "url": "https://www.astralcodexten.com"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('substack/posts', {'url': 'https://www.astralcodexten.com'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("substack/posts", {
  "url": "https://www.astralcodexten.com"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "substack/posts", sandbase.Params{
	"url": "https://www.astralcodexten.com",
})
```

Same call via the path form: `POST /v1/api/substack/posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Either a Substack publication URL / custom domain to fetch its recent posts (e.g. https://www.astralcodexten.com), OR a single post URL to fetch just that one article with full content (e.g.…  |
| `limit` | integer |  | Maximum number of recent posts to return when given a publication URL (1-100, default 25); ignored for a single post URL, which always returns that one post. You are billed per post returned, so a lower limit costs less. range 1–100 |
| `endDate` | string |  | Only return posts published on or before this date, format YYYY-MM-DD (e.g. 2024-12-31). Applied within the most recent 'limit' posts scanned.  |
| `onlyFree` | boolean |  | Return only free (non-paywalled) posts (e.g. true). default `false` |
| `startDate` | string |  | Only return posts published on or after this date, format YYYY-MM-DD (e.g. 2024-01-01). Applied within the most recent 'limit' posts scanned, so raise 'limit' to reach older date ranges.  |
| `contentType` | string |  | Restrict to a single post type, or 'all' (e.g. newsletter). one of: `all`, `newsletter`, `podcast`, `thread`; default `"all"` |
| `maxComments` | integer |  | Maximum comments collected per post when 'includeComments' is true (0-500, default 20). Costs nothing extra (e.g. 50). range 0–500 |
| `minComments` | integer |  | Only return posts with at least this many comments (e.g. 10). range 0– |
| `minReactions` | integer |  | Only return posts with at least this many reactions (e.g. 100). range 0– |
| `minWordCount` | integer |  | Only return posts with at least this many words, which filters out short notes and announcements (e.g. 1000). range 0– |
| `includeContent` | boolean |  | Include the full article body as text, HTML and Markdown. Set false for metadata only, which is faster (e.g. false). default `true` |
| `includeComments` | boolean |  | Include public comment threads and their direct replies on each post (e.g. true). default `false` |

## Details

Pull posts from any Substack publication by its URL, or pass a single post URL (…/p/slug) to fetch just that one article. Returns title, subtitle, publish date, paywall status, word count, engagement (reactions, comments, restacks), author profile, publication details, the full article body as text, HTML and Markdown, and optional comment threads.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/substack/posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.astralcodexten.com", "limit": 3}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Either a Substack publication URL / custom domain to fetch its recent posts (e.g. https://www.astralcodexten.com), OR a single post URL to fetch just that one article with full content (e.g. https://www.astralcodexten.co |
| `contentType` | string | No | Restrict to a single post type, or 'all' (e.g. newsletter). One of: `all`, `newsletter`, `podcast`, `thread`. Default `"all"`. |
| `endDate` | string | No | Only return posts published on or before this date, format YYYY-MM-DD (e.g. 2024-12-31). Applied within the most recent 'limit' posts scanned. |
| `includeComments` | boolean | No | Include public comment threads and their direct replies on each post (e.g. true). Default `false`. |
| `includeContent` | boolean | No | Include the full article body as text, HTML and Markdown. Set false for metadata only, which is faster (e.g. false). Default `true`. |
| `limit` | integer | No | Maximum number of recent posts to return when given a publication URL (1-100, default 25); ignored for a single post URL, which always returns that one post. You are billed per post returned, so a lower limit costs less. |
| `maxComments` | integer | No | Maximum comments collected per post when 'includeComments' is true (0-500, default 20). Costs nothing extra (e.g. 50). |
| `minComments` | integer | No | Only return posts with at least this many comments (e.g. 10). |
| `minReactions` | integer | No | Only return posts with at least this many reactions (e.g. 100). |
| `minWordCount` | integer | No | Only return posts with at least this many words, which filters out short notes and announcements (e.g. 1000). |
| `onlyFree` | boolean | No | Return only free (non-paywalled) posts (e.g. true). Default `false`. |
| `startDate` | string | No | Only return posts published on or after this date, format YYYY-MM-DD (e.g. 2024-01-01). Applied within the most recent 'limit' posts scanned, so raise 'limit' to reach older date ranges. |

### Pricing

Billed at the actual cost of each call, usually $0.0444 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/substack/posts.json`](../../../catalog/models/substack/posts.json) · Store page: https://www.sandbase.ai/model/substack/posts
