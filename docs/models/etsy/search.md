# Etsy Search API: pricing, parameters and code examples

`etsy/search` · data API · Etsy · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0009 per call · **Modes:** sync

Search Etsy listings by keyword, the same results an Etsy search or /market page shows, with optional sort, price range and page, and get title, price, original price, image, shop, rating and ad flag for each listing in one normalized response.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0009**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "etsy/search", "query": "cover letter template"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('etsy/search', {'query': 'cover letter template'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("etsy/search", {
  "query": "cover letter template"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "etsy/search", sandbase.Params{
	"query": "cover letter template",
})
```

Same call via the path form: `POST /v1/api/etsy/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | 1-based results page. Each page is billed as one request. default `1`; range 1–250 |
| `sort` | string |  | Result order: relevance (Etsy's own order, the default), newest, price_low, or price_high. one of: `relevance`, `newest`, `price_low`, `price_high`; default `"relevance"` |
| `query` | string | yes | Search keywords, e.g. "cover letter template". For an Etsy /market page, pass its words: https://www.etsy.com/market/habit_tracker_2027 is the query "habit tracker 2027".  |
| `maxPrice` | number |  | Optional maximum listing price, in USD. range 0– |
| `minPrice` | number |  | Optional minimum listing price, in USD. range 0– |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `rating`, and it is served only by a source that returns every one…  |

## Details

Search Etsy listings by keyword, the same results an Etsy search or /market page shows, with optional sort, price range and page, and get title, price, original price, image, shop, rating and ad flag for each listing in one normalized response.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "etsy/search", "query": "cover letter template"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search keywords, e.g. "cover letter template". For an Etsy /market page, pass its words: https://www.etsy.com/market/habit_tracker_2027 is the query "habit tracker 2027". |
| `maxPrice` | number | No | Optional maximum listing price, in USD. |
| `minPrice` | number | No | Optional minimum listing price, in USD. |
| `page` | integer | No | 1-based results page. Each page is billed as one request. Default `1`. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `rating`, and it is served only by a source that returns every one of  |
| `sort` | string | No | Result order: relevance (Etsy's own order, the default), newest, price_low, or price_high. One of: `relevance`, `newest`, `price_low`, `price_high`. |

### Pricing

Billed at the actual cost of each call, about $0.0009 per request. A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/etsy/search.json`](../../../catalog/models/etsy/search.json) · Store page: https://www.sandbase.ai/model/etsy/search
