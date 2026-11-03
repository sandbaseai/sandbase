# Tavily Site Map API: pricing, parameters and code examples

`tavily/map` · data API · Tavily · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.012 per call · **Modes:** sync

Discovers the URL structure of a target website without extracting full page content. Accepts a starting URL, maximum traversal depth, and URL discovery limits.

## Pricing

- **$0.012 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tavily/map", "limit": 10, "url": "https://static.sandbase.ai/examples/b1ca8e2d-8fe7-4358-99d8-4dac64d43e91/input/73ac2081-9c93-4d56-a0c0-0d23d590e501.com"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tavily/map', {'limit': 10, 'url': 'https://static.sandbase.ai/examples/b1ca8e2d-8fe7-4358-99d8-4dac64d43e91/input/73ac2081-9c93-4d56-a0c0-0d23d590e501.com'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tavily/map", {
  "limit": 10,
  "url": "https://static.sandbase.ai/examples/b1ca8e2d-8fe7-4358-99d8-4dac64d43e91/input/73ac2081-9c93-4d56-a0c0-0d23d590e501.com"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tavily/map", sandbase.Params{
	"limit": 10,
	"url": "https://static.sandbase.ai/examples/b1ca8e2d-8fe7-4358-99d8-4dac64d43e91/input/73ac2081-9c93-4d56-a0c0-0d23d590e501.com",
})
```

Same call via the path form: `POST /v1/api/tavily/map` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | The starting URL to map.  |
| `limit` | integer |  | Maximum number of URLs to discover. range 1–1000 |
| `max_depth` | integer |  | Maximum traversal depth from the starting URL. range 1–5 |

## Details

Returns a list of URLs found on a website, starting from the `url` you provide. It does not return page content. You can set `max_depth` (1 to 5) and `limit` (1 to 1000) to bound the crawl.

### Use cases

- Map a documentation site to see which pages exist before you pull their content.
- Build a list of page URLs on one domain to feed into a content extraction step.
- Check whether a page such as a changelog or a Markdown version of a page is reachable from the start URL.
- Compare the URL lists from two runs to spot added or removed pages.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tavily/map" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://docs.tavily.com"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | The starting URL to map. |
| `limit` | integer | No | Maximum number of URLs to discover. |
| `max_depth` | integer | No | Maximum traversal depth from the starting URL. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "base_url": "https://docs.tavily.com",
  "request_id": "fc2b750c-6921-4ef2-835a-fc35e907522f",
  "response_time": 0.07,
  "results": [
    "https://docs.tavily.com/"
  ],
  "usage": {
    "credits": 2
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `base_url` | The starting URL that was mapped, echoed back from the request. |
| `results[]` | List of discovered page URLs on the site. Each item is a full URL string. |
| `request_id` | Unique ID for this request, as a UUID string. |
| `response_time` | Time the mapping took, as a number. The response does not state the unit. |
| `usage.credits` | Number of credits this call used, as reported in the response. |

### Notes

- Only `url` is required. Add `max_depth` and `limit` to keep the result small on large sites.
- The `results` list holds plain URL strings with no titles or page text. Pass them to [Tavily URL Content Extraction](/apis/tavily/extract) to get page content.
- To find pages by topic instead of by site structure, use [Tavily Search](/apis/tavily/search).

### Pricing

$0.012 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/tavily/map.json`](../../../catalog/models/tavily/map.json) · Store page: https://www.sandbase.ai/model/tavily/map
