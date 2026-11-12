# IKEA Search API: pricing, parameters and code examples

`ikea/search` · data API · IKEA · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00085 per call · **Modes:** sync

Search IKEA's US store by keyword and get title, price, rating, and image for each product in one normalized response.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00085**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "ikea/search", "query": "bookshelf"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('ikea/search', {'query': 'bookshelf'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("ikea/search", {
  "query": "bookshelf"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "ikea/search", sandbase.Params{
	"query": "bookshelf",
})
```

Same call via the path form: `POST /v1/api/ikea/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | 1-based results page of 24 products. Each page is billed as one request. default `1`; range 1–100 |
| `query` | string | yes | Search keywords, e.g. "bookshelf" or "desk".  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `memberOffer`, and it is served only by a source that returns every…  |

## Details

Search IKEA's US store by keyword and get title, price, rating, and image for each product in one normalized response.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "ikea/search", "query": "bookshelf"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search keywords, e.g. "bookshelf" or "desk". |
| `page` | integer | No | 1-based results page of 24 products. Each page is billed as one request. Default `1`. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `memberOffer`, and it is served only by a source that returns every on |

### Pricing

Billed at the actual cost of each call, about $0.00085 per request. A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/ikea/search.json`](../../../catalog/models/ikea/search.json) · Store page: https://www.sandbase.ai/model/ikea/search
