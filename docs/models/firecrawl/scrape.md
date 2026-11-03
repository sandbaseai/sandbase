# Firecrawl Page Scraper API: pricing, parameters and code examples

`firecrawl/scrape` · data API · Firecrawl · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0075 per call (free daily quota) · **Modes:** sync

Scrapes content from target web pages with automatic handling of JavaScript rendering. Returns extracted page data based on specified formats and proxy settings.

## Pricing

- **$0.0075 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "firecrawl/scrape", "proxy": "basic", "url": "https://static.sandbase.ai/examples/b8c8d1dc-773a-4e08-adcb-eb014dd7b5eb/input/106170b7-0b8c-46ad-a429-067f9a3139ab.com"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('firecrawl/scrape', {'proxy': 'basic', 'url': 'https://static.sandbase.ai/examples/b8c8d1dc-773a-4e08-adcb-eb014dd7b5eb/input/106170b7-0b8c-46ad-a429-067f9a3139ab.com'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("firecrawl/scrape", {
  "proxy": "basic",
  "url": "https://static.sandbase.ai/examples/b8c8d1dc-773a-4e08-adcb-eb014dd7b5eb/input/106170b7-0b8c-46ad-a429-067f9a3139ab.com"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "firecrawl/scrape", sandbase.Params{
	"proxy": "basic",
	"url": "https://static.sandbase.ai/examples/b8c8d1dc-773a-4e08-adcb-eb014dd7b5eb/input/106170b7-0b8c-46ad-a429-067f9a3139ab.com",
})
```

Same call via the path form: `POST /v1/api/firecrawl/scrape` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | The HTTPS URL to scrape.  |
| `proxy` | string | yes | Proxy tier. one of: `basic`; default `"basic"` |
| `formats` | array |  | Output formats.  |

## Details

Scrape any public web page and get clean Markdown, HTML, links or a screenshot, with page metadata such as title, language and HTTP status. JavaScript-rendered pages are handled, and the `proxy` tier controls how hard-to-reach sites are fetched.

### Use cases

- Turn web pages into Markdown for LLM context or RAG.
- Extract article text without writing a parser per site.
- Capture a screenshot of a page.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/firecrawl/scrape" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com", "proxy": "basic"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `proxy` | string | Yes | Proxy tier. |
| `url` | string | Yes | The HTTPS URL to scrape. |
| `formats` | array | No | Output formats. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "markdown": "This domain is for use in documentation examples without needing permission. Thi…",
    "metadata": {
      "cacheState": "hit",
      "cachedAt": "2026-11-03T01:40:17.140Z",
      "concurrencyLimited": false,
      "contentType": "text/html; charset=utf-8",
      "favicon": "data:,",
      "language": "en",
      "proxyUsed": "basic",
      "scrapeId": "01a19f12-61d9-71bf-87c0-52a9fef97a83",
      "sourceURL": "https://example.com",
      "statusCode": 200,
      "title": "Example Domain",
      "url": "https://example.com/"
    }
  },
  "success": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.markdown` | Page content as Markdown (default format). |
| `data.html / data.links / data.screenshot` | Returned when requested in `formats`. |
| `data.metadata` | `title`, `description`, `language`, `sourceURL`, `statusCode` and `contentType` of the page. |
| `success` | `true` when the page was scraped. |

### Notes

- `proxy`: `basic` for normal sites, `stealth` for sites that block bots (slower), `auto` to retry with stealth when basic fails.
- Pages that require login or return errors fail and are not charged.

### Pricing

$0.0075 per successful call. Failed calls, including lookups whose target does not exist, are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/firecrawl/scrape.json`](../../../catalog/models/firecrawl/scrape.json) · Store page: https://www.sandbase.ai/model/firecrawl/scrape
