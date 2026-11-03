# Substack Posts API: pricing, parameters and code examples

`substack/posts` · data API · Substack · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0444 per call · **Modes:** sync

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

Returns recent posts from a Substack publication, or one article when you pass a post URL. Each post includes title, subtitle, engagement counts, author and publication details, and the article body as text, HTML and Markdown. The only required input is `url`.

### Use cases

- Track engagement on each new post of a newsletter by comparing `reactionCount`, `commentCount` and `restackCount`.
- Build a text archive of a publication by saving the `markdown` or `text` of each post.
- Find long, free posts from a writer by filtering on `wordcount` and `isPaid`.
- Collect reader discussion on a single article by setting `includeComments` to true.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/substack/posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.astralcodexten.com", "limit": 3}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Either a Substack publication URL / custom domain to fetch its recent posts (e.g. https://www.astralcodexten.com), OR a single post URL to fetch just that one article with full content (e.g. https://www.astralcodexten.co |
| `contentType` | string | No | Restrict to a single post type, or 'all' (e.g. newsletter). |
| `endDate` | string | No | Only return posts published on or before this date, format YYYY-MM-DD (e.g. 2024-12-31). Applied within the most recent 'limit' posts scanned. |
| `includeComments` | boolean | No | Include public comment threads and their direct replies on each post (e.g. true). |
| `includeContent` | boolean | No | Include the full article body as text, HTML and Markdown. Set false for metadata only, which is faster (e.g. false). |
| `limit` | integer | No | Maximum number of recent posts to return when given a publication URL (1-100, default 25); ignored for a single post URL, which always returns that one post. You are billed per post returned, so a lower limit costs less. |
| `maxComments` | integer | No | Maximum comments collected per post when 'includeComments' is true (0-500, default 20). Costs nothing extra (e.g. 50). |
| `minComments` | integer | No | Only return posts with at least this many comments (e.g. 10). |
| `minReactions` | integer | No | Only return posts with at least this many reactions (e.g. 100). |
| `minWordCount` | integer | No | Only return posts with at least this many words, which filters out short notes and announcements (e.g. 1000). |
| `onlyFree` | boolean | No | Return only free (non-paywalled) posts (e.g. true). |
| `startDate` | string | No | Only return posts published on or after this date, format YYYY-MM-DD (e.g. 2024-01-01). Applied within the most recent 'limit' posts scanned, so raise 'limit' to reach older date ranges. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "items": [
      {
        "authorHandle": "astralcodexten",
        "authorImage": "https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/http…",
        "authorName": "Scott Alexander",
        "authorUrl": "https://substack.com/@astralcodexten",
        "commentCount": 244,
        "comments": [],
        "contentStatus": "full",
        "createdUtc": 1793595877,
        "description": "...",
        "hasVoiceover": true,
        "html": "<p>This is the weekly visible open thread. Post about anything you want, ask ran…",
        "image": "https://substack-post-media.s3.amazonaws.com/public/images/9d8ea239-2d80-4635-9f…"
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.items[].title / subtitle / description` | Post headline, subtitle and short summary. The summary or subtitle can be a literal `...` when the author set none. |
| `data.items[].url / slug / postId` | Public post URL, the URL slug, and the numeric post ID as a string. |
| `data.items[].createdUtc / updatedUtc` | Creation and last update time as Unix timestamps in seconds. |
| `data.items[].postType` | Type of post, such as `newsletter`. |
| `data.items[].isPaid` | `true` if the post is paywalled, `false` if it is free. |
| `data.items[].wordcount` | Number of words in the post. |
| `data.items[].reactionCount / commentCount / replyCount / restackCount` | Engagement counts for the post: reactions, comments, replies and restacks. |
| `data.items[].text / html / markdown` | Article body in plain text, HTML and Markdown. These fields appear when `includeContent` is true, and can be missing on some items. |
| `data.items[].authorName / authorHandle / authorUrl` | Author display name, Substack handle and profile URL. |
| `data.items[].publication.name / subdomain / customDomain` | Name of the publication, its Substack subdomain and its custom domain. |

### Notes

- Pass a publication URL or custom domain to get recent posts. Pass a post URL ending in `/p/slug` to get one article.
- Use `limit` (1-100) to set how many recent posts to return. The date filters apply only within the most recent `limit` posts, so raise `limit` to reach older posts.
- `comments` is an empty list unless you set `includeComments` to true. `maxComments` sets the cap per post (0-500).
- `contentStatus` shows `full` when the full body was returned. `podcastUrl` links to an audio file for the post.

### Pricing

Billed at the actual cost of each call, about $0.0444 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/substack/posts.json`](../../../catalog/models/substack/posts.json) · Store page: https://www.sandbase.ai/model/substack/posts
