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

Use this endpoint to extract web content from a target `url` using a designated `proxy` tier and optional output `formats`.

### Use cases

- Extract clean page content from JavaScript-heavy websites.
- Convert target web pages into specific structured formats.
- Retrieve website data via automated scraping proxies.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/firecrawl/scrape" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "<url>", "proxy": "basic"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | The HTTPS URL to scrape. |
| `proxy` | string | Yes | Proxy tier. |
| `formats` | array | No | Output formats. |

### Notes

- Requires an HTTPS link passed to the `url` parameter.
- The `proxy` parameter accepts the value `basic`.

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/firecrawl/scrape.json`](../../../catalog/models/firecrawl/scrape.json) · Store page: https://www.sandbase.ai/model/firecrawl/scrape
