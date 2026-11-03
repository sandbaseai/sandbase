# DuckDuckGo Search API: pricing, parameters and code examples

`duckduckgo/search` · data API · DuckDuckGo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.015 per call · **Modes:** sync

DuckDuckGo organic search results for a keyword, with region and safe-search options.

## Pricing

- **$0.015 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "duckduckgo/search", "q": "apple"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('duckduckgo/search', {'q': 'apple'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("duckduckgo/search", {
  "q": "apple"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "duckduckgo/search", sandbase.Params{
	"q": "apple",
})
```

Same call via the path form: `POST /v1/api/duckduckgo/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string | yes | max 500 chars  |
| `kl` | string |  | region code, e.g. us-en  |

## Details

This API returns DuckDuckGo organic search results for a keyword. Each result has a title, link, snippet and position, and the response also lists related searches. It needs a query in `q` and accepts an optional region code in `kl`.

### Use cases

- Track which pages rank for a keyword in a given region, such as `us-en`.
- Collect titles, links and snippets of top results to research a topic or a brand.
- Read `sitelinks` to see which sub-pages DuckDuckGo shows under a main result.
- Use `related_searches` to find follow-up queries for keyword research.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/duckduckgo/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "apple", "kl": "us-en"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | Yes | max 500 chars |
| `kl` | string | No | region code, e.g. us-en |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "organic_results": [
    {
      "favicon": "https://external-content.duckduckgo.com/ip3/www.apple.com.ico",
      "link": "https://www.apple.com/",
      "position": 1,
      "sitelinks": [
        {
          "link": "https://www.apple.com/shop/buy-iphone/iphone-18-pro",
          "snippet": "Get $35-$885 off a new iPhone 18 Pro or iPhone 18 Pro Max when you trade in an i…",
          "title": "Shop Iphone 18 Pro"
        }
      ],
      "snippet": "Discover the innovative world of Apple and shop everything iPhone, iPad, Apple W…",
      "title": "Apple"
    }
  ],
  "related_searches": [
    {
      "link": "https://duckduckgo.com/?q=apple%20music%20login&origin=related",
      "query": "apple music login"
    }
  ],
  "search_information": {
    "organic_results_state": "Results for exact spelling"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `organic_results[].title` | Title of the search result. |
| `organic_results[].link` | URL of the result page. |
| `organic_results[].snippet` | Short text excerpt shown under the result title. |
| `organic_results[].position` | Rank of the result in the list. The first result has `position` 1. |
| `organic_results[].favicon` | URL of the site's icon image. |
| `organic_results[].sitelinks[].title / organic_results[].sitelinks[].link / organic_results[].sitelinks[].snippet` | Title, URL and snippet of a sub-page shown under a result. Only some results have `sitelinks`. |
| `related_searches[].query` | Text of a related search suggestion. |
| `related_searches[].link` | DuckDuckGo URL that runs the related search. |
| `search_information.organic_results_state` | Short note on how the results match the query, for example `Results for exact spelling`. |

### Notes

- `q` is required and can be up to 500 characters. `kl` sets the region and language, for example `us-en`.
- The response has no pagination fields, and the request has no page parameter.
- For news articles on a topic, call [DuckDuckGo News Search](/apis/duckduckgo/news). For places, call [DuckDuckGo Maps](/apis/duckduckgo/maps).

### Pricing

$0.015 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/duckduckgo/search.json`](../../../catalog/models/duckduckgo/search.json) · Store page: https://www.sandbase.ai/model/duckduckgo/search
