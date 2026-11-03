# DataForSEO OnPage Content Parsing API: pricing, parameters and code examples

`dataforseo/v3/on_page/content_parsing/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00015 per call · **Modes:** sync

Parses and returns structured on-page content directly from a specified webpage URL. Inspect page elements, headings, text blocks, and page layout details for SEO analysis.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00015**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/on_page/content_parsing/live", "disable_cookie_popup": true, "enable_javascript": true, "markdown_view": true, "url": "https://static.sandbase.ai/examples/dc72bbe8-ff8a-43f6-a42a-a3161c329d91/input/fad85338-69fb-47a8-b4aa-2440d6455215.bin"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/on_page/content_parsing/live', {'disable_cookie_popup': True, 'enable_javascript': True, 'markdown_view': True, 'url': 'https://static.sandbase.ai/examples/dc72bbe8-ff8a-43f6-a42a-a3161c329d91/input/fad85338-69fb-47a8-b4aa-2440d6455215.bin'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/on_page/content_parsing/live", {
  "disable_cookie_popup": true,
  "enable_javascript": true,
  "markdown_view": true,
  "url": "https://static.sandbase.ai/examples/dc72bbe8-ff8a-43f6-a42a-a3161c329d91/input/fad85338-69fb-47a8-b4aa-2440d6455215.bin"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/on_page/content_parsing/live", sandbase.Params{
	"disable_cookie_popup": true,
	"enable_javascript": true,
	"markdown_view": true,
	"url": "https://static.sandbase.ai/examples/dc72bbe8-ff8a-43f6-a42a-a3161c329d91/input/fad85338-69fb-47a8-b4aa-2440d6455215.bin",
})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/on_page/content_parsing/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string |  | Page URL.  |

## Details

Parses structured content elements directly from a target webpage. Useful for auditing on-page text, headings, and structure.

### Use cases

- Analyze on-page text and heading structures for SEO audits.
- Extract raw page content elements for natural language processing.
- Inspect content layout and metadata directly from target URLs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/on_page/content_parsing/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.python.org/"}'
```

### Parameters

The JSON body is forwarded to the upstream endpoint (one task per call). Fields used above:

| Name | Description |
|---|---|
| `url` | Page URL. |

### Pricing

Billed at the actual cost of each call, about $0.00015 for the request above. The cost grows with the number of rows, targets or pages a call returns. Failed calls are not charged. Searches with no results are billed at their actual cost.

### Related APIs

- [DataForSEO Backlinks Anchors](/apis/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/apis/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/apis/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/on_page/content_parsing/live.json`](../../../../../../catalog/models/dataforseo/v3/on_page/content_parsing/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/on_page/content_parsing/live
