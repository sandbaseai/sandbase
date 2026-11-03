# Firecrawl URL Discovery API: pricing, parameters and code examples

`firecrawl/map` · data API · Firecrawl · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0075 per call (free daily quota) · **Modes:** sync

Discovers and returns URLs found across a target website. Provide an HTTPS target address and define the maximum link count to map site pages.

## Pricing

- **$0.0075 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "firecrawl/map", "url": "https://docs.firecrawl.dev", "limit": 10}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('firecrawl/map', {'url': 'https://docs.firecrawl.dev', 'limit': 10})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("firecrawl/map", {
  "url": "https://docs.firecrawl.dev",
  "limit": 10
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "firecrawl/map", sandbase.Params{
	"url": "https://docs.firecrawl.dev",
	"limit": 10,
})
```

Same call via the path form: `POST /v1/api/firecrawl/map` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | The HTTPS URL to map.  |
| `limit` | integer | yes | Maximum number of links to discover. range 1–100000 |

## Details

Returns a list of URLs found on a website, each with its page title and sometimes a short description. You send an HTTPS site address in `url` and the maximum number of links to return in `limit`.

### Use cases

- List the pages of a documentation site before deciding which ones to scrape.
- Build a sitemap of a domain for a search index or content audit.
- Find localized versions of pages by reading the language prefix in each URL, such as `/es/` or `/ja/`.
- Check which API reference or guide pages exist on a site.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/firecrawl/map" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://docs.firecrawl.dev", "limit": 10}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `limit` | integer | Yes | Maximum number of links to discover. |
| `url` | string | Yes | The HTTPS URL to map. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "id": "01a1a053-d7e1-737d-a1a5-342cf89669af",
  "links": [
    {
      "title": "Obtener el estado de la captura por lotes - Firecrawl Docs",
      "url": "https://docs.firecrawl.dev/es/api-reference/endpoint/batch-scrape-get"
    }
  ],
  "success": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `success` | Shows whether the mapping call worked. The value is `true` when it did. |
| `id` | Identifier of this mapping result, in UUID-style format. |
| `links[]` | List of discovered pages. The list holds up to `limit` entries. |
| `links[].url` | Full address of the discovered page. |
| `links[].title` | Title of the page, in the language of that page. |
| `links[].description` | Short summary of the page. Only some links include this field. |

### Notes

- Set `limit` between `1` and `100000`. The request needs both `url` and `limit`.
- Use `url` with the `https://` prefix, for example `https://docs.firecrawl.dev`.
- To read the content of a discovered page, pass its `links[].url` to [Firecrawl Page Scraper](/apis/firecrawl/scrape). For many pages at once, use [Firecrawl Batch Scrape](/apis/firecrawl/batch/scrape).
- Check for `links[].description` before using it, since it does not appear on every link.

### Pricing

$0.0075 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/firecrawl/map.json`](../../../catalog/models/firecrawl/map.json) · Store page: https://www.sandbase.ai/model/firecrawl/map
