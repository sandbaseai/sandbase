# TikTok Shop Search Suggestions

`tiktok-shop/search-suggestions` · api · TikTok Shop

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

Get TikTok Shop search autocomplete terms for a keyword: the long-tail queries shoppers actually type, for keyword and demand research.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok-shop/search-suggestions" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "ashwagandha gummies", "country": "US"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Seed keyword to expand (e.g. ashwagandha gummies). |
| `country` | string | No | Two-letter country code of the TikTok Shop market (e.g. US). Default `"US"`. |
| `language` | string | No | Language tag for the suggestions (e.g. en-US). Default `"en-US"`. |

### Pricing

Billed at the actual cost of each call, usually $0.00095 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/tiktok-shop/search-suggestions.json`](../../../catalog/models/tiktok-shop/search-suggestions.json) · Store page: https://www.sandbase.ai/model/tiktok-shop/search-suggestions
