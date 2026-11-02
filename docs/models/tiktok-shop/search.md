# TikTok Shop Search API: pricing, parameters and code examples

`tiktok-shop/search` · data API · TikTok Shop · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00095 per call · **Modes:** sync

Search TikTok Shop products by keyword across 15 countries: price, sales, rating, and seller info per product, in one normalized response.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00095**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok-shop/search", "query": "phone case"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok-shop/search', {'query': 'phone case'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok-shop/search", {
  "query": "phone case"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok-shop/search", sandbase.Params{
	"query": "phone case",
})
```

Same call via the path form: `POST /v1/api/tiktok-shop/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum products to return, honoured on US searches up to 30. Other countries and larger values return every product TikTok Shop gives for the query, typically about 30 and occasionally more than 50. The price per call… range 1– |
| `query` | string | yes | Search keyword for TikTok Shop products (e.g. wireless earbuds).  |
| `country` | string |  | Country code of the TikTok Shop market to search (e.g. US). one of: `US`, `VN`, `TH`, `PH`, `MY`, `ID`, `GB`, `SG`, `ES`, `MX`, `DE`, `IT` …; default `"US"` |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `currency`, and it is served only by a source that returns every one…  |

## Details

Search TikTok Shop products by keyword across 15 countries: price, sales, rating, and seller info per product, in one normalized response.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok-shop/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": 3, "query": "phone case"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search keyword for TikTok Shop products (e.g. wireless earbuds). |
| `country` | string | No | Country code of the TikTok Shop market to search (e.g. US). One of: `US`, `VN`, `TH`, `PH`, `MY`, `ID`, `GB`, `SG`, `ES`, `MX`, `DE`, `IT`. Default `"US"`. |
| `limit` | integer | No | Maximum products to return, honoured on US searches up to 30. Other countries and larger values return every product TikTok Shop gives for the query, typically about 30 and occasionally more than 50. The price per call i |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `currency`, and it is served only by a source that returns every one o |

### Pricing

Billed at the actual cost of each call, usually $0.00095 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/tiktok-shop/search.json`](../../../catalog/models/tiktok-shop/search.json) · Store page: https://www.sandbase.ai/model/tiktok-shop/search
