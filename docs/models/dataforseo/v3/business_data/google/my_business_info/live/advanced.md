# DataForSEO Google Business Listing Info API: pricing, parameters and code examples

`dataforseo/v3/business_data/google/my_business_info/live/advanced` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0054 per call · **Modes:** sync

Returns comprehensive Google Business Profile data, including local listing details, customer reviews, ratings, and business attributes for targeted locations.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0054**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/business_data/google/my_business_info/live/advanced"}'
```

**Python** ([sdk/python](../../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/business_data/google/my_business_info/live/advanced', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/business_data/google/my_business_info/live/advanced", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/business_data/google/my_business_info/live/advanced", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/business_data/google/my_business_info/live/advanced` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string |  | Search query.  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |

## Details

Returns the Google Business Profile for one place, found by a search query and a location. It needs a `keyword` (the business name), a `location_code` and a `language_code`.

### Use cases

- Look up the address, category and Google ID of a named business before adding it to a CRM.
- Check which accessibility features a venue lists on its Google profile.
- Compare how the same business is categorized across different locations or languages.
- Build a link to the Google Maps page for a business from its `cid`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/business_data/google/my_business_info/live/advanced" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "The Metropolitan Museum of Art", "location_code": 2840, "language_code": "en"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | No | Search query. |
| `language_code` | string | No | Language code, e.g. "en". |
| `location_code` | integer | No | Location code, e.g. 2840 for the United States. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "status_code": 20000,
  "status_message": "Ok.",
  "tasks": [
    {
      "data": {
        "api": "business_data",
        "device": "desktop",
        "function": "my_business_info",
        "keyword": "The Metropolitan Museum of Art",
        "language_code": "en",
        "location_code": 2840,
        "os": "windows",
        "se": "google"
      },
      "id": "11030828-2190-0572-0000-fe67064bd604",
      "path": [
        "v3"
      ],
      "result": [
        {
          "check_url": "https://www.google.com/maps?cid=4264808743088595450&hl=en&gl=US",
          "datetime": "2026-11-03 08:28:54 +00:00",
          "item_types": [
            "google_business_info"
          ],
          "items": [
            {
              "additional_categories": [
                "Arts organization"
              ],
              "address": "1000 5th Ave, New York, NY 10028",
              "address_info": {
                "address": "1000 5th Ave",
                "borough": "Manhattan",
                "city": "New York",
                "country_code": "US",
                "region": "New York",
                "zip": "10028"
              },
              "attributes": {
                "available_attributes": {
                  "accessibility": [
                    "has_assisted_listening_devices"
                  ]
                },
                "unavailable_attributes": null
              },
              "book_online_url": null,
              "category": "Art museum",
              "category_ids": null,
              "cid": "4264808743088595450"
            }
          ],
          "items_count": 1,
          "keyword": "The Metropolitan Museum of Art",
          "language_code": "en",
          "location_code": 2840
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "8.0274 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "8.0415 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].cid` | Google customer ID of the business as a string. It also appears in `check_url`. |
| `tasks[].result[].check_url` | Google Maps link for the listing, built from the `cid`. |
| `tasks[].result[].items[].category` | Main category of the business, such as `Art museum`. |
| `tasks[].result[].items[].additional_categories[]` | Other categories listed for the business. |
| `tasks[].result[].items[].address` | Full street address as one string. |
| `tasks[].result[].items[].address_info.city / region / zip / country_code` | Address split into parts: city, region, ZIP code and country code. |
| `tasks[].result[].items[].attributes.available_attributes` | Attributes the business has, grouped by topic. For example, `accessibility` lists items like `has_wheelchair_accessible_entrance`. |
| `tasks[].result[].items[].attributes.unavailable_attributes` | Attributes the business does not have. It is `null` when none are listed. |
| `tasks[].result[].items_count` | Number of listings returned for the query. |
| `tasks[].result[].datetime` | Time the result was produced, in UTC. |

### Notes

- Use the business name as `keyword`. `location_code` `2840` is the United States.
- Some fields, such as `book_online_url` and `category_ids`, can be `null` when the profile has no value.
- The response wraps results in `tasks[]`. Read the listing from `tasks[].result[].items[]`.
- Check `status_code` (`20000` means Ok) at the top level and inside each task.

### Pricing

Billed at the actual cost of each call, about $0.0054 for the request above. Failed calls are not charged.

### Related APIs

- [DataForSEO Backlinks Anchors](/apis/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/apis/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/apis/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/business_data/google/my_business_info/live/advanced.json`](../../../../../../../../catalog/models/dataforseo/v3/business_data/google/my_business_info/live/advanced.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/business_data/google/my_business_info/live/advanced
