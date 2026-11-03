# AAA News Article Detail API: pricing, parameters and code examples

`aaa/news-article-detail` · data API · AAA · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Returns the full content of a specific news article identified by its URL slug. The slug is obtainable from get_news_articles results.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "aaa/news-article-detail", "slug": "national-gas-average-drops-nearly-20-cents-in-one-week"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('aaa/news-article-detail', {'slug': 'national-gas-average-drops-nearly-20-cents-in-one-week'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("aaa/news-article-detail", {
  "slug": "national-gas-average-drops-nearly-20-cents-in-one-week"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "aaa/news-article-detail", sandbase.Params{
	"slug": "national-gas-average-drops-nearly-20-cents-in-one-week",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/aaa/news-article-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `slug` | string | yes | Article URL slug (e.g. national-gas-average-drops-nearly-20-cents-in-one-week). Obtainable from get_news_articles results.  |

## Details

Returns the full text and basic metadata of one AAA news article about gasoline. It needs the article URL slug as input, such as `national-gas-average-drops-nearly-20-cents-in-one-week`.

### Use cases

- Pull the full text of an AAA gas news release to quote or summarize it in a report.
- Archive AAA news articles with their publish date and canonical link.
- Show an article page in a fuel dashboard after a user picks a headline from a list.
- Feed article text into a text analysis job that tracks how gas news is worded over time.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/aaa/news-article-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"slug": "national-gas-average-drops-nearly-20-cents-in-one-week"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `slug` | string | Yes | Article URL slug (e.g. national-gas-average-drops-nearly-20-cents-in-one-week). Obtainable from get_news_articles results. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "content": "\n<p class=\"wp-block-paragraph\">WASHINGTON, DC&nbsp;(June 4, 2026)&nbsp;&#8211;&n…",
    "date": "2026-06-04T10:27:55",
    "id": 5086,
    "link": "https://gasprices.aaa.com/national-gas-average-drops-nearly-20-cents-in-one-week…",
    "slug": "national-gas-average-drops-nearly-20-cents-in-one-week",
    "title": "National Gas Average Drops Nearly 20 Cents in One Week"
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.title` | Headline of the article. |
| `data.content` | Article body as an HTML string. It contains tags such as `<p>` and HTML entities such as `&nbsp;`, so parse or strip them before display. |
| `data.date` | Publish date and time of the article in ISO 8601 form, without a time zone offset. |
| `data.id` | Numeric ID of the article. |
| `data.slug` | URL slug of the article. It matches the `slug` you sent. |
| `data.link` | Full URL of the article on the AAA gas site. |
| `status` | Request outcome. The value is `success` for a good call. |

### Notes

- Get the `slug` from the results of [AAA News Articles](/apis/aaa/news-articles) or [AAA Search News Articles](/apis/aaa/search-news-articles).
- The `slug` is the last path segment of `data.link`.
- `data.content` is HTML, so render it as HTML or strip the tags for plain text.

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/aaa/news-article-detail.json`](../../../catalog/models/aaa/news-article-detail.json) · Store page: https://www.sandbase.ai/model/aaa/news-article-detail
