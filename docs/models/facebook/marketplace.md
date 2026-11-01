# Facebook Marketplace

`facebook/marketplace` · api · Facebook

Search Facebook Marketplace listings by keyword near a location, filter by price, condition, delivery, recency, and availability, and get title, price, location, and image as normalized JSON.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "facebook/marketplace", "query": "bike", "lat": "30.2677", "lng": "-97.7475"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('facebook/marketplace', {'query': 'bike', 'lat': '30.2677', 'lng': '-97.7475'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("facebook/marketplace", {
  "query": "bike",
  "lat": "30.2677",
  "lng": "-97.7475"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "facebook/marketplace", sandbase.Params{
	"query": "bike",
	"lat": "30.2677",
	"lng": "-97.7475",
})
```

Same call via the path form: `POST /v1/api/facebook/marketplace` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `lat` | string | yes | Latitude of the search location (e.g. '30.2677').  |
| `lng` | string | yes | Longitude of the search location (e.g. '-97.7475').  |
| `sort` | string |  | Sort order for the returned listings (e.g. price_ascend). one of: `suggested`, `distance_ascend`, `creation_time_descend`, `price_ascend`, `price_descend` |
| `query` | string | yes | Search keyword for Marketplace listings (e.g. 'bike').  |
| `cursor` | string |  | Pagination cursor from a previous response to fetch the next page.  |
| `priceMax` | integer |  | Maximum listing price in whole currency units, e.g. 500 for $500. Facebook may mix in a few suggested listings outside the range. range 0– |
| `priceMin` | integer |  | Minimum listing price in whole currency units, e.g. 100 for $100. Facebook may mix in a few suggested listings outside the range. range 0– |
| `condition` | string |  | Only return listings in this condition (e.g. used_good). one of: `new`, `used_like_new`, `used_good`, `used_fair` |
| `dateListed` | string |  | Only return listings posted within this window (e.g. last_7_days). one of: `all`, `last_24_hours`, `last_7_days`, `last_30_days` |
| `availability` | string |  | Filter by availability: available (default), sold, or all (e.g. sold). one of: `available`, `sold`, `all` |
| `deliveryMethod` | string |  | Only return listings offering this delivery method (e.g. shipping). one of: `all`, `local_pickup`, `shipping` |

## Details

Search Facebook Marketplace listings by keyword near a location, filter by price, condition, delivery, recency, and availability, and get title, price, location, and image as normalized JSON.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/facebook/marketplace" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"lat": "30.2677", "lng": "-97.7475", "query": "bike", "priceMax": 500, "priceMin": 100}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `lat` | string | Yes | Latitude of the search location (e.g. '30.2677'). |
| `lng` | string | Yes | Longitude of the search location (e.g. '-97.7475'). |
| `query` | string | Yes | Search keyword for Marketplace listings (e.g. 'bike'). |
| `availability` | string | No | Filter by availability: available (default), sold, or all (e.g. sold). One of: `available`, `sold`, `all`. |
| `condition` | string | No | Only return listings in this condition (e.g. used_good). One of: `new`, `used_like_new`, `used_good`, `used_fair`. |
| `cursor` | string | No | Pagination cursor from a previous response to fetch the next page. |
| `dateListed` | string | No | Only return listings posted within this window (e.g. last_7_days). One of: `all`, `last_24_hours`, `last_7_days`, `last_30_days`. |
| `deliveryMethod` | string | No | Only return listings offering this delivery method (e.g. shipping). One of: `all`, `local_pickup`, `shipping`. |
| `priceMax` | integer | No | Maximum listing price in whole currency units, e.g. 500 for $500. Facebook may mix in a few suggested listings outside the range. |
| `priceMin` | integer | No | Minimum listing price in whole currency units, e.g. 100 for $100. Facebook may mix in a few suggested listings outside the range. |
| `sort` | string | No | Sort order for the returned listings (e.g. price_ascend). One of: `suggested`, `distance_ascend`, `creation_time_descend`, `price_ascend`, `price_descend`. |

### Pricing

Billed at the actual cost of each call, usually $0.0012 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/facebook/marketplace.json`](../../../catalog/models/facebook/marketplace.json) · Store page: https://www.sandbase.ai/model/facebook/marketplace
