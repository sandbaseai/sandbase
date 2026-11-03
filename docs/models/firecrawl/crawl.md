# Firecrawl Crawl API: pricing, parameters and code examples

`firecrawl/crawl` · data API · Firecrawl · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.0075 per run, depending on parameters · **Modes:** async

Crawl an entire website starting from a URL. Discovers and scrapes all reachable pages, returning clean markdown for each. Runs asynchronously — submit the job, then poll for results.

## Pricing

- Depends on parameters ().

| parameters | USD |
|---|---|
| defaults | 0.0075 |

Formula: `Math.max(1.0, Math.max((output.completed ?? 0) * 1.0, len(output.data ?? []) * 1.0)) * 0.0075`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "firecrawl/crawl", "url": "https://example.com", "limit": 2}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('firecrawl/crawl', {'url': 'https://example.com', 'limit': 2})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("firecrawl/crawl", {
  "url": "https://example.com",
  "limit": 2
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "firecrawl/crawl", sandbase.Params{
	"url": "https://example.com",
	"limit": 2,
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/firecrawl/crawl` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | The starting URL to crawl.  |
| `limit` | integer | yes | Maximum number of pages to crawl. range 1–10000 |
| `scrapeOptions` | object |  | Options passed to the scraper for each page.  |

## Details

Crawls a website from a starting URL and returns the content of each page it finds as markdown, plus page metadata. It needs a `url` and a `limit` for the maximum number of pages. The job runs asynchronously, so you submit it and then poll for the result.

### Use cases

- Copy the pages of a documentation site into markdown files for a search index or an LLM knowledge base.
- Pull the text of a company site to summarize its products and pricing pages.
- Snapshot a site's content on a schedule so you can compare versions over time.
- Collect page text from a small site to check language and content type across all its pages.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/firecrawl/crawl" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com", "limit": 2}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `limit` | integer | Yes | Maximum number of pages to crawl. |
| `url` | string | Yes | The starting URL to crawl. |
| `scrapeOptions` | object | No | Options passed to the scraper for each page. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "completed": 2,
  "completedAt": "2026-11-03T07:33:32.633Z",
  "createdAt": "2026-11-03T07:33:31.620Z",
  "creditsUsed": 2,
  "data": [
    {
      "markdown": "This domain is for use in documentation examples without needing permission. Thi…",
      "metadata": {
        "cacheState": "hit",
        "cachedAt": "2026-11-03T07:33:19.669Z",
        "contentType": "text/html; charset=utf-8",
        "creditsUsed": 1,
        "favicon": "data:,",
        "language": "en",
        "proxyUsed": "basic",
        "scrapeId": "01a1a053-d857-759b-8946-800c1acf51cf"
      },
      "warning": "This scrape job was throttled at your current concurrency limit. If you'd like t…"
    }
  ],
  "duration": 1.013,
  "expiresAt": "2026-11-04T07:33:41.000Z",
  "status": "completed",
  "success": true,
  "total": 2
}
```

### Response fields

| Field | Meaning |
|---|---|
| `status / success` | `status` shows the job state, such as `completed`. `success` is a boolean for the request. |
| `total / completed` | `total` is the number of pages found for the job. `completed` is the number of pages finished so far. |
| `data[].markdown` | The page content converted to markdown. |
| `data[].metadata.language / data[].metadata.contentType` | The page language code (for example `en`) and the content type of the response (for example `text/html; charset=utf-8`). |
| `data[].metadata.scrapeId` | An ID for the scrape of that single page. |
| `data[].metadata.cacheState / data[].metadata.cachedAt` | `cacheState` shows whether the page came from a cache (for example `hit`). `cachedAt` is the ISO timestamp of the cached copy. |
| `data[].metadata.creditsUsed / creditsUsed` | Credits used for one page and for the whole job. |
| `data[].warning` | An optional message on a page, such as a note that the scrape was throttled. It appears only on some items. |
| `createdAt / completedAt / expiresAt` | ISO 8601 UTC timestamps for when the job started, when it finished, and when the result expires. |
| `duration` | How long the job took. The value in the example is `1.013`. |

### Notes

- Poll `GET /v1/run/{id}` until `status` is `completed`, then read the result from `outputs[0].data`.
- Set `limit` between 1 and 10000 to cap the number of pages crawled.
- Set `scrapeOptions.formats` to choose the output formats: `markdown`, `html`, `rawHtml`, `links` or `screenshot`.
- To scrape one known page, use [Firecrawl Page Scraper](/apis/firecrawl/scrape). To list a site's URLs without content, use [Firecrawl URL Discovery](/apis/firecrawl/map).

### Pricing

Billed at the actual cost of each call, about $0.0075 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/firecrawl/crawl.json`](../../../catalog/models/firecrawl/crawl.json) · Store page: https://www.sandbase.ai/model/firecrawl/crawl
