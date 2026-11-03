# LinkedIn Company Posts API: pricing, parameters and code examples

`linkedin/company-posts` · data API · LinkedIn · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0029 per call · **Modes:** sync

List a LinkedIn company page's recent posts by URL: full text, canonical link, publish date, author, engagement counts with a per-reaction breakdown, and attached media.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0029**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/company-posts", "url": "https://www.linkedin.com/company/stripe"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/company-posts', {'url': 'https://www.linkedin.com/company/stripe'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/company-posts", {
  "url": "https://www.linkedin.com/company/stripe"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/company-posts", sandbase.Params{
	"url": "https://www.linkedin.com/company/stripe",
})
```

Same call via the path form: `POST /v1/api/linkedin/company-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Full LinkedIn company page URL.  |
| `limit` | integer |  | Maximum number of posts to return. default `10`; range 1–50 |
| `postedLimit` | string |  | Only return posts published within this window (default any). one of: `any`, `1h`, `24h`, `week`, `month`, `3months`, `6months`, `year` |
| `includeReposts` | boolean |  | Include reposts (posts shared without an added comment). Defaults to true; set false to exclude them.  |
| `includeQuotePosts` | boolean |  | Include quote posts (posts shared with an added comment). Defaults to true; set false to exclude them.  |

## Details

Returns a list of recent posts from a LinkedIn company page. Each post includes text, links, a publish timestamp, author details, engagement counts and attached media. It needs the full company page URL in `url`.

### Use cases

- Track what a competitor posts on LinkedIn and which posts get the most likes, comments and shares.
- Build a feed of a company's announcements for a monitoring dashboard.
- Compare reaction types across posts to see which content gets praise or empathy rather than plain likes.
- Collect post images and links from a brand page for a content audit.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/company-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.linkedin.com/company/stripe", "limit": 10}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Full LinkedIn company page URL. |
| `includeQuotePosts` | boolean | No | Include quote posts (posts shared with an added comment). Defaults to true; set false to exclude them. |
| `includeReposts` | boolean | No | Include reposts (posts shared without an added comment). Defaults to true; set false to exclude them. |
| `limit` | integer | No | Maximum number of posts to return. |
| `postedLimit` | string | No | Only return posts published within this window (default any). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "items": [
      {
        "author": {
          "id": "2135371",
          "image": "https://media.licdn.com/dms/image/v2/D560BAQE2ZfJyfn-VCg/company-logo_400_400/B5…",
          "linkedinUrl": "https://www.linkedin.com/company/stripe/",
          "name": "Stripe",
          "type": "company",
          "universalName": "stripe"
        },
        "contentAttributes": [],
        "createdUtc": 1793605643,
        "engagement": {
          "comments": 10,
          "likes": 872,
          "reactions": [],
          "shares": 29
        },
        "id": "7522927325529862144",
        "postImages": [],
        "postVideo": null,
        "repostAuthorName": "Stripe",
        "repostAuthorUniversalName": "stripe",
        "repostAuthorUrl": "https://www.linkedin.com/company/stripe/",
        "repostCreatedUtc": 1793605643,
        "shareUrl": "https://www.linkedin.com/posts/jefftitterton_congratulations-to-kimi-antonelli-o…"
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.items[].id` | ID of the post, as a string. |
| `data.items[].text` | Post text. Long posts may be shortened in the sample. |
| `data.items[].url / data.items[].shareUrl` | Link to the post on LinkedIn. |
| `data.items[].createdUtc` | Publish time as a Unix timestamp in seconds. |
| `data.items[].author.name / data.items[].author.universalName / data.items[].author.linkedinUrl` | Name, URL slug and page link of the company that published the post. |
| `data.items[].engagement.likes / data.items[].engagement.comments / data.items[].engagement.shares` | Counts of likes, comments and shares for the post. |
| `data.items[].engagement.reactions[].type / data.items[].engagement.reactions[].count` | Reaction breakdown, such as `LIKE`, `EMPATHY` or `PRAISE`, with the count for each. The list can be empty. |
| `data.items[].postImages[].url` | Link to an image attached to the post. Each image also has `width` and `height`. |
| `data.items[].contentAttributes[]` | Mentions inside the text. Each entry has a `type` such as `COMPANY_NAME` or `PROFILE_MENTION`, plus `start` and `length` for its position in `text`. |
| `data.items[].repostAuthorName / data.items[].repostAuthorUrl / data.items[].repostCreatedUtc` | Present on reposted items. They name the account tied to the repost and give a timestamp. |

### Notes

- Use the full company page URL, such as `https://www.linkedin.com/company/stripe`. Get the company page URL from [LinkedIn Company Search](/apis/linkedin/search-companies).
- Set `limit` from 1 to 50 (default 10). Use `postedLimit` to restrict posts to a time window.
- Set `includeReposts` or `includeQuotePosts` to `false` to leave those post types out.
- To read a single post in more detail, call [LinkedIn Post](/apis/linkedin/post) with the post `url`. To read its comments, call [LinkedIn Post Comments](/apis/linkedin/post-comments).

### Pricing

Billed at the actual cost of each call, about $0.0029 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/linkedin/company-posts.json`](../../../catalog/models/linkedin/company-posts.json) · Store page: https://www.sandbase.ai/model/linkedin/company-posts
