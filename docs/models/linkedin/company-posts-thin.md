# LinkedIn Company Posts (basic) API: pricing, parameters and code examples

`linkedin/company-posts-thin` · data API · LinkedIn · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

Post text and link only. No engagement counts, author details, media, or reaction breakdown - for those use linkedin.company_posts.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/company-posts-thin", "url": "https://www.linkedin.com/company/stripe"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/company-posts-thin', {'url': 'https://www.linkedin.com/company/stripe'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/company-posts-thin", {
  "url": "https://www.linkedin.com/company/stripe"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/company-posts-thin", sandbase.Params{
	"url": "https://www.linkedin.com/company/stripe",
})
```

Same call via the path form: `POST /v1/api/linkedin/company-posts-thin` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Full LinkedIn company page URL.  |
| `page` | integer |  | Page number for pagination. range 1– |

## Details

Returns a list of recent posts from a LinkedIn company page. Each post has an ID, text, creation time and link. The API needs the full company page URL in `url`.

### Use cases

- Track what a competitor's company page publishes by pulling the text of each new post.
- Collect post links from a company page to feed into a content archive or monitoring list.
- Check when a company posted about an event or announcement using the creation timestamp.
- Build a feed of company announcements that links back to the original LinkedIn posts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/company-posts-thin" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.linkedin.com/company/stripe"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Full LinkedIn company page URL. |
| `page` | integer | No | Page number for pagination. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "items": [
      {
        "createdUtc": 1793573382,
        "id": "7522792013872685056",
        "text": "Toto Wolff of the Mercedes-AMG PETRONAS Formula One Team shares how bringing an …",
        "url": "https://www.linkedin.com/posts/stripe_how-toto-wolff-built-the-most-valuable-tea…"
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `found` | `true` when the company page returned data. A lookup that finds nothing returns `false`. |
| `data.items[]` | One entry per post on the requested page. |
| `data.items[].id` | The post ID as a string of digits. The same number appears at the end of the post `url`. |
| `data.items[].text` | The post text. Long posts appear cut off in the sample, so treat this as a preview of the post body. |
| `data.items[].url` | The link to the post on LinkedIn. |
| `data.items[].createdUtc` | The post creation time as a Unix timestamp in seconds, in UTC. |

### Notes

- Copy the `url` value from the company page address in your browser, for example `https://www.linkedin.com/company/stripe`.
- Pass `page` (starting at 1) to move through more posts.
- This API returns no engagement counts, author details or media. For those fields use [LinkedIn Company Posts](/apis/linkedin/company-posts).
- To read one post in more detail, pass its link to [LinkedIn Post](/apis/linkedin/post).

### Pricing

Billed at the actual cost of each call, about $0.0012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/linkedin/company-posts-thin.json`](../../../catalog/models/linkedin/company-posts-thin.json) · Store page: https://www.sandbase.ai/model/linkedin/company-posts-thin
