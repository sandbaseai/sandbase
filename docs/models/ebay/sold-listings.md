# eBay Sold Listings API: pricing, parameters and code examples

`ebay/sold-listings` · data API · eBay · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.003 per call · **Modes:** sync

Retrieve recently sold eBay listings for any keyword with optional price-range, condition, category, sold-date, and sort filters, page by page (sold price, sale date, condition, seller, item details); ideal for pricing research.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.003**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "ebay/sold-listings", "query": "iphone 13 pro"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('ebay/sold-listings', {'query': 'iphone 13 pro'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("ebay/sold-listings", {
  "query": "iphone 13 pro"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "ebay/sold-listings", sandbase.Params{
	"query": "iphone 13 pro",
})
```

Same call via the path form: `POST /v1/api/ebay/sold-listings` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | 1-based results page. Use with hasMore in the output to paginate, and keep query, filters, and limit the same while walking pages, because limit sets the page size. default `1`; range 1– |
| `site` | string |  | eBay country site to search. Sold-listing coverage is currently US only. one of: `ebay.com`; default `"ebay.com"` |
| `sort` | string |  | Result sort order; omitted means ended_recently (e.g. price_high sorts by highest sold price plus shipping first). one of: `ended_recently`, `price_low`, `price_high` |
| `limit` | integer |  | Maximum number of results to return (1-60, default 25). default `25`; range 1–60 |
| `query` | string | yes | Search keyword for sold items (e.g. iphone 13 pro).  |
| `seller` | string |  | Not supported by the current sources: a request that sets it is refused without charge.  |
| `endDate` | string |  | Only return listings sold on or before this date, inclusive, in YYYY-MM-DD format (e.g. 2026-09-15). This bound is applied to each page after it is fetched, so a page can hold fewer than limit listings, or none, while…  |
| `maxPrice` | number |  | Optional maximum sold price in the site currency (e.g. 500). range 0– |
| `minPrice` | number |  | Optional minimum sold price in the site currency (e.g. 200). range 0– |
| `condition` | string |  | Item condition filter (e.g. used). one of: `any`, `new`, `used`; default `"any"` |
| `startDate` | string |  | Only return listings sold on or after this date, inclusive, in YYYY-MM-DD format (e.g. 2026-09-01).  |
| `categoryId` | string |  | Optional numeric eBay category id to search within (e.g. 9355 for Cell Phones & Smartphones, 9394 for Cell Phone Accessories).  |
| `listingType` | string |  | Restrict to a listing format; omit or use all for both (e.g. auction for auction sales only). one of: `all`, `auction`, `buy_it_now` |
| `freeShipping` | boolean |  | Not supported by the current sources: only false (no filter) is accepted; true is refused without charge.  |
| `returnsAccepted` | boolean |  | Not supported by the current sources: only false (no filter) is accepted; true is refused without charge.  |

## Details

Retrieve recently sold eBay listings for any keyword with optional price-range, condition, category, sold-date, and sort filters, page by page (sold price, sale date, condition, seller, item details); ideal for pricing research.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "ebay/sold-listings", "sort": "ended_recently", "limit": 10, "query": "iphone 13 pro"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search keyword for sold items (e.g. iphone 13 pro). |
| `categoryId` | string | No | Optional numeric eBay category id to search within (e.g. 9355 for Cell Phones & Smartphones, 9394 for Cell Phone Accessories). |
| `condition` | string | No | Item condition filter (e.g. used). One of: `any`, `new`, `used`. Default `"any"`. |
| `endDate` | string | No | Only return listings sold on or before this date, inclusive, in YYYY-MM-DD format (e.g. 2026-09-15). This bound is applied to each page after it is fetched, so a page can hold fewer than limit listings, or none, while ha |
| `freeShipping` | boolean | No | Not supported by the current sources: only false (no filter) is accepted; true is refused without charge. |
| `limit` | integer | No | Maximum number of results to return (1-60, default 25). |
| `listingType` | string | No | Restrict to a listing format; omit or use all for both (e.g. auction for auction sales only). One of: `all`, `auction`, `buy_it_now`. |
| `maxPrice` | number | No | Optional maximum sold price in the site currency (e.g. 500). |
| `minPrice` | number | No | Optional minimum sold price in the site currency (e.g. 200). |
| `page` | integer | No | 1-based results page. Use with hasMore in the output to paginate, and keep query, filters, and limit the same while walking pages, because limit sets the page size. Default `1`. |
| `returnsAccepted` | boolean | No | Not supported by the current sources: only false (no filter) is accepted; true is refused without charge. |
| `seller` | string | No | Not supported by the current sources: a request that sets it is refused without charge. |
| `site` | string | No | eBay country site to search. Sold-listing coverage is currently US only. One of: `ebay.com`. Default `"ebay.com"`. |
| `sort` | string | No | Result sort order; omitted means ended_recently (e.g. price_high sorts by highest sold price plus shipping first). One of: `ended_recently`, `price_low`, `price_high`. |
| `startDate` | string | No | Only return listings sold on or after this date, inclusive, in YYYY-MM-DD format (e.g. 2026-09-01). |

### Pricing

Billed at the actual cost of each call, about $0.003 per request. A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/ebay/sold-listings.json`](../../../catalog/models/ebay/sold-listings.json) · Store page: https://www.sandbase.ai/model/ebay/sold-listings
