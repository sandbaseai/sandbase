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
  -d '{"model": "firecrawl/crawl", "url": "<url>", "limit": "<limit>"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('firecrawl/crawl', {'url': '<url>', 'limit': '<limit>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("firecrawl/crawl", {
  "url": "<url>",
  "limit": "<limit>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "firecrawl/crawl", sandbase.Params{
	"url": "<url>",
	"limit": "<limit>",
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

Crawl a website from a starting URL. The job finds reachable pages and returns clean markdown and metadata for each one. It runs asynchronously: submit the job, then poll for the result.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/firecrawl/crawl" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com", "limit": 2}'
```

The call returns a run `id` with status `pending`. Poll `GET https://api.sandbase.ai/v1/run/{id}` until the status is `completed`; the job result is in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Starting URL to crawl. |
| `limit` | integer | Yes | Maximum number of pages to crawl. |
| `scrapeOptions` | object | No | Options applied when scraping each page, e.g. `{"formats": ["markdown"]}`. |

### Example response

Real result for the request above, trimmed to the main fields.

```json
{
  "status": "completed",
  "total": 2,
  "completed": 2,
  "data": [
    {
      "markdown": "This domain is for use in documentation examples without needing permission. …",
      "metadata": {
        "title": "Example Domain",
        "sourceURL": "https://example.com",
        "statusCode": 200,
        "language": "en"
      }
    }
  ]
}
```

### Pricing

$0.0075 per crawled page, with a minimum of one page per job. Failed jobs are not charged.

---
Machine-readable: [`catalog/models/firecrawl/crawl.json`](../../../catalog/models/firecrawl/crawl.json) · Store page: https://www.sandbase.ai/model/firecrawl/crawl
