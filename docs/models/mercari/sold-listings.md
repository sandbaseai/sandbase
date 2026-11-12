# Mercari Sold Listings API: pricing, parameters and code examples

`mercari/sold-listings` · data API · Mercari · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

Search Mercari US or Japan sold listings by keyword with optional price-range, condition, category, brand, and sort filters, page by page, with the total result count; ideal for resale pricing research. The sold price is the final price after any accepted offer; it does not include buyer fees, and whether shipping is included depends on the listing's shipping terms. Rows carry no sale date: call mercari.product for soldUtc (US only).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "mercari/sold-listings", "query": "nike air jordan 1"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('mercari/sold-listings', {'query': 'nike air jordan 1'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("mercari/sold-listings", {
  "query": "nike air jordan 1"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "mercari/sold-listings", sandbase.Params{
	"query": "nike air jordan 1",
})
```

Same call via the path form: `POST /v1/api/mercari/sold-listings` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sort` | string |  | Result order; omitted means Mercari's default (most recently sold first for a US sold search). most_liked is Japan only; recently_sold is US only (e.g. price_desc). one of: `relevance`, `newest`, `price_asc`, `price_desc`, `most_liked`, `recently_sold` |
| `query` | string | yes | Search keyword (e.g. nike air jordan 1). Japanese terms return far more in Japan, though Latin brand and model names work.  |
| `cursor` | string |  | Pagination cursor: pass the previous response's nextCursor with the same query and filters; omit for the first page.  |
| `brandId` | string |  | Mercari brand id, or several separated by commas; the US and Japan use separate ids (e.g. 319 for Apple in the US). Every US row carries its brandId.  |
| `country` | string |  | Mercari marketplace: us (mercari.com, USD) or jp (jp.mercari.com, JPY). one of: `us`, `jp`; default `"us"` |
| `maxPrice` | integer |  | Highest sold price to include, in whole units of the country's currency (e.g. 300). range 0– |
| `minPrice` | integer |  | Lowest sold price to include, in whole units of the country's currency (US dollars or yen) (e.g. 50). range 0– |
| `condition` | array |  | Only listings in any of these condition grades (e.g. ["new", "like_new"]). worn is Japan only.  |
| `categoryId` | string |  | Mercari category id, or several separated by commas; the US and Japan use separate ids and a parent id includes its children (e.g. 778 for US cell phones and smartphones). Every row carries its categoryId.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `categories`, and it is served only by a source that returns every…  |

## Details

Search Mercari US or Japan sold listings by keyword with optional price-range, condition, category, brand, and sort filters, page by page, with the total result count; ideal for resale pricing research. The sold price is the final price after any accepted offer; it does not include buyer fees, and whether shipping is included depends on the listing's shipping terms. Rows carry no sale date: call mercari.product for soldUtc (US only).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "mercari/sold-listings", "query": "nike air jordan 1"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search keyword (e.g. nike air jordan 1). Japanese terms return far more in Japan, though Latin brand and model names work. |
| `brandId` | string | No | Mercari brand id, or several separated by commas; the US and Japan use separate ids (e.g. 319 for Apple in the US). Every US row carries its brandId. |
| `categoryId` | string | No | Mercari category id, or several separated by commas; the US and Japan use separate ids and a parent id includes its children (e.g. 778 for US cell phones and smartphones). Every row carries its categoryId. |
| `condition` | array | No | Only listings in any of these condition grades (e.g. ["new", "like_new"]). worn is Japan only. |
| `country` | string | No | Mercari marketplace: us (mercari.com, USD) or jp (jp.mercari.com, JPY). One of: `us`, `jp`. Default `"us"`. |
| `cursor` | string | No | Pagination cursor: pass the previous response's nextCursor with the same query and filters; omit for the first page. |
| `maxPrice` | integer | No | Highest sold price to include, in whole units of the country's currency (e.g. 300). |
| `minPrice` | integer | No | Lowest sold price to include, in whole units of the country's currency (US dollars or yen) (e.g. 50). |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `categories`, and it is served only by a source that returns every one |
| `sort` | string | No | Result order; omitted means Mercari's default (most recently sold first for a US sold search). most_liked is Japan only; recently_sold is US only (e.g. price_desc). One of: `relevance`, `newest`, `price_asc`, `price_desc |

### Pricing

Billed at the actual cost of each call, about $0.0012 per request. A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/mercari/sold-listings.json`](../../../catalog/models/mercari/sold-listings.json) · Store page: https://www.sandbase.ai/model/mercari/sold-listings
