# Bing Maps Maps API: pricing, parameters and code examples

`bing-maps/maps` · data API · Bing Maps · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00015 per call (free daily quota) · **Modes:** async

Search Bing Maps listings around a map center, or look up one entity by id.

## Pricing

- **$0.00015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bing-maps/maps"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bing-maps/maps', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bing-maps/maps", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bing-maps/maps", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/bing-maps/maps` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string |  | Search query. Required unless place_id is supplied.  |
| `cp` | string |  | Map center as 'latitude~longitude', such as '47.6062~-122.3321'.  |
| `count` | integer |  | Number of listings, 1-30. Default 30. range 1–30 |
| `first` | integer |  | Listing offset, 0-10,000. Default 0. range 0–10000 |
| `setlang` | string |  | Interface language such as 'en-US'.  |
| `place_id` | string |  | Native Bing Maps entity ID for a detail lookup. Required unless q is supplied.  |

## Details

Returns Bing Maps business listings for a search query near a map center. Each listing has an address, phone number, coordinates, and open state. You can also pass a `place_id` to look up one entity.

### Use cases

- Build a list of coffee shops, pharmacies, or other business types near a given latitude and longitude.
- Collect phone numbers and addresses of local businesses for a lead list.
- Plot search results on a map using the `gps_coordinates` of each listing.
- Check which nearby businesses are open right now using `open_state` and `open_hours`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bing-maps/maps" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "coffee", "cp": "47.6062~-122.3321"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `count` | integer | No | Number of listings, 1-30. Default 30. |
| `cp` | string | No | Map center as 'latitude~longitude', such as '47.6062~-122.3321'. |
| `first` | integer | No | Listing offset, 0-10,000. Default 0. |
| `place_id` | string | No | Native Bing Maps entity ID for a detail lookup. Required unless q is supplied. |
| `q` | string | No | Search query. Required unless place_id is supplied. |
| `setlang` | string | No | Interface language such as 'en-US'. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "local_results": [
    {
      "items": [
        {
          "address": "1912 Pike Pl, Seattle, WA 98101",
          "entry_type": "Business",
          "gps_coordinates": {
            "latitude": 47.610069274902344,
            "longitude": -122.34262084960938
          },
          "link": "https://www.bing.com/maps?q=Starbucks+Coffee+Company&filters=local_ypid%3A%22YNF…",
          "open_hours": "Open until 8 PM",
          "open_state": "Open",
          "phone": "(206) 448-8762",
          "place_id": "YNF9439D454244F274"
        }
      ],
      "title": "coffee"
    }
  ],
  "search_metadata": {
    "created_at": "2026-11-03 07:28:13 UTC",
    "id": "234da23691b61502af88f81d",
    "processed_at": "2026-11-03 07:28:13 UTC",
    "status": "Success",
    "total_time_taken": 0.885
  },
  "search_parameters": {
    "count": 30,
    "cp": "47.6062~-122.3321",
    "first": 0,
    "q": "coffee"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `local_results[].title` | The search term that the group of listings answers, such as `coffee`. |
| `local_results[].items[].place_id` | The Bing Maps entity ID of the listing. Pass it as `place_id` to look up that entity. |
| `local_results[].items[].address` | Street address of the listing as one text line. |
| `local_results[].items[].entry_type` | Type of entry, such as `Business`. |
| `local_results[].items[].gps_coordinates.latitude / local_results[].items[].gps_coordinates.longitude` | Decimal degree coordinates of the listing. |
| `local_results[].items[].phone` | Phone number of the listing, formatted as text. |
| `local_results[].items[].open_state / local_results[].items[].open_hours` | Whether the listing is open (`open_state`) and a short text on closing time (`open_hours`), such as `Open until 8 PM`. |
| `local_results[].items[].link` | Bing Maps URL that opens the listing. |
| `search_metadata.status` | Shows `Success` when the search finished. |
| `search_parameters.count / search_parameters.first` | The page size and offset the search used, with defaults filled in. |

### Notes

- Send either `q` or `place_id`. A search uses `q` with `cp` as the map center in the form `latitude~longitude`, such as `47.6062~-122.3321`.
- Page through results with `count` (1-30, default 30) and `first` (offset, 0-10,000).
- Take `place_id` from `local_results[].items[].place_id` to run a detail lookup on one listing.
- Timestamps in `search_metadata` use the format `2026-11-03 07:28:13 UTC`.

### Pricing

$0.00015 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/bing-maps/maps.json`](../../../catalog/models/bing-maps/maps.json) · Store page: https://www.sandbase.ai/model/bing-maps/maps
