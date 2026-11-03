# Facebook Marketplace API: pricing, parameters and code examples

`facebook/marketplace` · data API · Facebook · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

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

Returns a page of Facebook Marketplace listings that match a keyword near a latitude and longitude. Each listing includes title, price, city, photo, delivery types, and a link to the item. You send `query`, `lat`, and `lng`, and can add price, condition, delivery, recency, availability, and sort filters.

### Use cases

- Compare asking prices for used bikes within a set budget in one city.
- Track newly posted listings for a keyword by sorting with `creation_time_descend`.
- Build a deal alert that flags listings under a target `priceAmount`.
- Collect sold listings with `availability` set to `sold` to see what items sold for in an area.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/facebook/marketplace" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"lat": "30.2677", "lng": "-97.7475", "query": "bike", "priceMax": 500, "priceMin": 100}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `lat` | string | Yes | Latitude of the search location (e.g. '30.2677'). |
| `lng` | string | Yes | Longitude of the search location (e.g. '-97.7475'). |
| `query` | string | Yes | Search keyword for Marketplace listings (e.g. 'bike'). |
| `availability` | string | No | Filter by availability: available (default), sold, or all (e.g. sold). |
| `condition` | string | No | Only return listings in this condition (e.g. used_good). |
| `cursor` | string | No | Pagination cursor from a previous response to fetch the next page. |
| `dateListed` | string | No | Only return listings posted within this window (e.g. last_7_days). |
| `deliveryMethod` | string | No | Only return listings offering this delivery method (e.g. shipping). |
| `priceMax` | integer | No | Maximum listing price in whole currency units, e.g. 500 for $500. Facebook may mix in a few suggested listings outside the range. |
| `priceMin` | integer | No | Minimum listing price in whole currency units, e.g. 100 for $100. Facebook may mix in a few suggested listings outside the range. |
| `sort` | string | No | Sort order for the returned listings (e.g. price_ascend). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "hasNextPage": true,
    "listings": [
      {
        "categoryId": "1658310421102081",
        "city": "Austin",
        "cityPageId": "106224666074625",
        "createdUtc": 1788826593,
        "deliveryTypes": [
          "IN_PERSON"
        ],
        "id": "2010100319696587",
        "isHidden": false,
        "isLive": true,
        "isPending": false,
        "isSold": false,
        "listingDateText": "Listed 1 month ago",
        "locationName": "Austin, Texas"
      }
    ],
    "nextCursor": "cur_jXjcjdldJp1WvqUPdeX5sw"
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.listings[].id` | Marketplace listing ID. Use it to build the item link or to look up the listing in detail. |
| `data.listings[].title` | Title the seller gave the listing. |
| `data.listings[].priceAmount / data.listings[].priceFormatted` | Listing price as a number and as display text, for example `350` and `$350`. |
| `data.listings[].city / data.listings[].state / data.listings[].locationName` | Where the item is listed, as city, state code, and a combined place name. |
| `data.listings[].createdUtc` | Time the listing was created, as a Unix timestamp in seconds. |
| `data.listings[].listingDateText` | Relative age of the listing as shown on Facebook, for example `Listed 2 weeks ago`. |
| `data.listings[].deliveryTypes` | List of delivery options the seller offers, such as `IN_PERSON`, `PUBLIC_MEETUP`, and `DOOR_PICKUP`. |
| `data.listings[].isSold / data.listings[].isPending / data.listings[].isLive / data.listings[].isHidden` | Status flags for the listing. |
| `data.listings[].photoUrl` | URL of the main listing photo. |
| `data.listings[].url` | Direct link to the listing on Facebook Marketplace. |
| `data.hasNextPage / data.nextCursor` | `hasNextPage` shows whether more results exist. `nextCursor` is the value to send as `cursor` for the next page. |

### Notes

- To get the next page, repeat the request with `cursor` set to `data.nextCursor`. Stop when `data.hasNextPage` is `false`.
- Use the same `lat` and `lng` as a Marketplace location. [Facebook Marketplace Location Search](/apis/facebook/marketplace-location-search) can help you find coordinates for a place name.
- Call [Facebook Marketplace Item](/apis/facebook/marketplace-item) with a listing `id` to get more detail on a single listing.
- `priceMin` and `priceMax` use whole currency units. A few suggested listings outside the range can still appear.

### Pricing

Billed at the actual cost of each call, about $0.0012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/facebook/marketplace.json`](../../../catalog/models/facebook/marketplace.json) · Store page: https://www.sandbase.ai/model/facebook/marketplace
