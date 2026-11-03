# TikTok Shop Search Suggestions API: pricing, parameters and code examples

`tiktok-shop/search-suggestions` · data API · TikTok Shop · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00095 per call · **Modes:** sync

Get TikTok Shop search autocomplete terms for a keyword: the long-tail queries shoppers actually type, for keyword and demand research.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00095**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok-shop/search-suggestions", "query": "ashwagandha gummies"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok-shop/search-suggestions', {'query': 'ashwagandha gummies'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok-shop/search-suggestions", {
  "query": "ashwagandha gummies"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok-shop/search-suggestions", sandbase.Params{
	"query": "ashwagandha gummies",
})
```

Same call via the path form: `POST /v1/api/tiktok-shop/search-suggestions` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Seed keyword to expand (e.g. ashwagandha gummies).  |
| `country` | string |  | Two-letter country code of the TikTok Shop market (e.g. US). default `"US"` |
| `language` | string |  | Language tag for the suggestions (e.g. en-US). default `"en-US"` |

## Details

This API returns TikTok Shop search autocomplete suggestions for a seed keyword. It needs a `query` and can also take a `country` code and a `language` tag.

### Use cases

- Expand a product keyword such as `ashwagandha gummies` into the long-tail searches shoppers type.
- Find product angles to test, such as a suggestion that adds a buyer group or a brand name.
- Build keyword lists for TikTok Shop listing titles and product research.
- Compare suggestions for the same seed keyword across different markets by changing `country`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok-shop/search-suggestions" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "ashwagandha gummies", "country": "US"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Seed keyword to expand (e.g. ashwagandha gummies). |
| `country` | string | No | Two-letter country code of the TikTok Shop market (e.g. US). |
| `language` | string | No | Language tag for the suggestions (e.g. en-US). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "suggestions": [
      "ashwagandha gummies"
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.suggestions[]` | Autocomplete terms for the seed keyword, as plain strings. Each string is a search phrase that can include the seed keyword plus extra words, such as `ashwagandha gummies for men`. |
| `data.suggestions[0]` | In this response, the first suggestion repeats the seed keyword exactly. |
| `found` | Boolean flag. It is `true` when the lookup returned data. |

### Notes

- The response is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.
- `country` defaults to `US` and `language` defaults to `en-US`.
- To see products for a suggested phrase, pass it to [TikTok Shop Search](/apis/tiktok-shop/search).
- To browse the category tree, use [TikTok Shop Categories](/apis/tiktok-shop/categories).

### Pricing

Billed at the actual cost of each call, about $0.00095 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/tiktok-shop/search-suggestions.json`](../../../catalog/models/tiktok-shop/search-suggestions.json) · Store page: https://www.sandbase.ai/model/tiktok-shop/search-suggestions
