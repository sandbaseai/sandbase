# Facebook Marketplace Item API: pricing, parameters and code examples

`facebook/marketplace-item` · data API · Facebook · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

Fetch full details for a single Facebook Marketplace listing by ID or URL (title, price, location, photos, and attributes) as normalized JSON.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "facebook/marketplace-item"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('facebook/marketplace-item', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("facebook/marketplace-item", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "facebook/marketplace-item", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/facebook/marketplace-item` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string |  | Facebook Marketplace item ID.  |
| `url` | string |  | Facebook Marketplace item URL.  |

## Details

Returns the details of one Facebook Marketplace listing as JSON. You pass either the item `id` or the item `url`. The response includes the title, price, location, photos, seller, and item attributes.

### Use cases

- Track the asking price and sold status of a specific listing over time.
- Pull photos, description, and attributes of a listing into a resale or price comparison tool.
- Check whether a seller has a rating and how many ratings they have before you rank listings.
- Map a listing to its coordinates to group items by area.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/facebook/marketplace-item" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.facebook.com/marketplace/item/1656586118821988/"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string | No | Facebook Marketplace item ID. |
| `url` | string | No | Facebook Marketplace item URL. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "attributes": [
      {
        "label": "Used - Good",
        "name": "Condition",
        "value": "used_good"
      }
    ],
    "categoryId": "1658310421102081",
    "creationTime": "2026-05-15T16:57:39.000Z",
    "currency": "USD",
    "deliveryTypes": [
      "IN_PERSON"
    ],
    "description": "Was going to hang on to this one bc I absolutely love how it looks, but the 20” …",
    "id": "1656586118821988",
    "isBuyNowEnabled": false,
    "isHidden": false,
    "isLive": true,
    "isPending": false,
    "isShippingOffered": false
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.title / data.description` | Listing title and the seller's description text. |
| `data.priceAmount / data.currency / data.priceFormatted` | Asking price as a number, its currency code, and the display string such as `$220`. |
| `data.strikethroughPriceFormatted` | The earlier price shown crossed out, as a display string. It is `$380` in this listing. |
| `data.isSold / data.isPending / data.isLive / data.isHidden` | Flags for the current state of the listing. |
| `data.locationText / data.latitude / data.longitude` | Place name of the listing and its coordinates. |
| `data.attributes[].name / data.attributes[].label / data.attributes[].value` | Item attributes such as Condition, Bicycle Type, and Material. `label` is the display text and `value` is the raw value. |
| `data.photos[].url / data.photos[].width / data.photos[].height` | Photo link with its width and height. |
| `data.seller.name / data.seller.rating / data.seller.ratingCount` | Seller name, rating value, and the number of ratings. |
| `data.creationTime / data.listingDateText` | Creation time as an ISO 8601 timestamp and the relative listing text such as `Listed 5 months ago`. |
| `data.deliveryTypes / data.isShippingOffered / data.isBuyNowEnabled` | How the item can be handed over and whether shipping or buy now is offered. |

### Notes

- Send either `id` or `url`. The `id` is the number at the end of the item URL, for example `1656586118821988`.
- The response has a top-level `found` flag. It is `true` when the listing was found.
- To find listing IDs first, use [Facebook Marketplace](/apis/facebook/marketplace). To find a location to search in, use [Facebook Marketplace Location Search](/apis/facebook/marketplace-location-search).

### Pricing

Billed at the actual cost of each call, about $0.0012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/facebook/marketplace-item.json`](../../../catalog/models/facebook/marketplace-item.json) · Store page: https://www.sandbase.ai/model/facebook/marketplace-item
