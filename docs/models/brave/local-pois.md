# Brave Local POIs API: pricing, parameters and code examples

`brave/local-pois` · data API · Brave · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.005 per call (free daily quota) · **Modes:** sync

Local POIs from Brave. Returns the official Brave API response unchanged.

## Pricing

- **$0.005 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "brave/local-pois", "ids": ["loc4DFZ5OEXSZVDUAEEDV6PMTFK6YDFANIHQIRRVKLA="]}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('brave/local-pois', {'ids': ['loc4DFZ5OEXSZVDUAEEDV6PMTFK6YDFANIHQIRRVKLA=']})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("brave/local-pois", {
  "ids": [
    "loc4DFZ5OEXSZVDUAEEDV6PMTFK6YDFANIHQIRRVKLA="
  ]
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "brave/local-pois", sandbase.Params{
	"ids": []any{"loc4DFZ5OEXSZVDUAEEDV6PMTFK6YDFANIHQIRRVKLA="},
})
```

Same call via the path form: `POST /v1/api/brave/local-pois` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `ids` | array | yes | A list of unique identifiers for the location. The ids are valid only for 8 hours.  |
| `units` | string |  | The measurement units. The following values are supported: metric - The standardized measurement system (km, celcius…) imperial - The British Imperial system of units (mile, fahrenheit…) one of: `imperial`, `metric` |
| `ui_lang` | string |  | User interface language preferred in response. Usually of the format <language_code>-<country_code>. For more, see RFC 9110 . one of: `es-AR`, `en-AU`, `de-AT`, `nl-BE`, `fr-BE`, `pt-BR`, `en-CA`, `fr-CA`, `es-CL`, `da-DK`, `fi-FI`, `fr-FR` …; default `"en-US"` |
| `search_lang` | string |  | The search language preference. The 2 or more character language code for which the search results are provided. one of: `ar`, `eu`, `bn`, `bg`, `ca`, `zh-hans`, `zh-hant`, `hr`, `cs`, `da`, `nl`, `en` …; default `"en"` |

## Details

Returns details for one or more local places (points of interest) from Brave, such as name, address, phone number, coordinates, opening hours, rating, photos and related web pages. It needs a list of location `ids` in the `ids` parameter.

### Use cases

- Show a business card with name, address, phone and opening hours for a place found in a search.
- Check which days and hours a cafe or shop is open before you send a customer there.
- Plot places on a map with `coordinates` and show their `rating` and photos.
- Collect the website and social profile links for a local business.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/brave/local-pois" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"ids": ["loc4DFZ5OEXSZVDUAEEDV6PMTFK6YDFANIHQIRRVKLA="]}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `ids` | array | Yes | A list of unique identifiers for the location. The ids are valid only for 8 hours. |
| `search_lang` | string | No | The search language preference. The 2 or more character language code for which the search results are provided. |
| `ui_lang` | string | No | User interface language preferred in response. Usually of the format <language_code>-<country_code>. For more, see RFC 9110 . |
| `units` | string | No | The measurement units. The following values are supported: metric - The standardized measurement system (km, celcius…) imperial - The British Imperial system of units (mile, fahrenheit…) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "results": [
    {
      "categories": [],
      "contact": {
        "telephone": "+12067805777"
      },
      "coordinates": [
        47.60895
      ],
      "family_friendly": true,
      "id": "loc4DFZ5OEXSZVDUAEEDV6PMTFK6YDFANIHQIRRVKLA=",
      "is_source_both": false,
      "is_source_local": false,
      "opening_hours": {
        "current_day": [
          {
            "abbr_name": "Tue",
            "closes": "17:00",
            "full_name": "Tuesday",
            "opens": "06:59"
          }
        ],
        "days": [
          [
            {
              "abbr_name": "Mon",
              "closes": "17:00",
              "full_name": "Monday",
              "opens": "06:59"
            }
          ]
        ]
      },
      "pictures": {
        "results": [
          {
            "original": "https://lh3.googleusercontent.com/p/AF1QipN6QS0pKXaJqJ7VUigWGEyXcjYJhKqayDx2TlVW…",
            "src": "https://imgs.search.brave.com/XjGqFPcOkdFwsXjUb7-etFuMZCsudU6EnuAEzElKZ1Y/rs:fit…"
          }
        ]
      },
      "postal_address": {
        "displayAddress": "94 Pike St Top floor Suite 34, Seattle, WA 98101",
        "type": "PostalAddress"
      },
      "profiles": [
        {
          "img": "https://imgs.search.brave.com/Ez_ahZzZ3ushkbmoJgmdHsAic0dvbVgEO80Y5igGQbA/rs:fit…",
          "name": "storyville.com",
          "type": "external",
          "url": "https://storyville.com/pages/pike-place-market"
        }
      ],
      "provider_url": "https://storyville.com/pages/pike-place-market"
    }
  ],
  "type": "local_pois"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `results[].title` | Name of the place. |
| `results[].postal_address.displayAddress` | Full street address as a single display string. |
| `results[].coordinates` | Latitude and longitude of the place, in that order. |
| `results[].contact.telephone` | Phone number of the place in international format. |
| `results[].opening_hours.days[] / results[].opening_hours.current_day[]` | Opening hours. Each entry has `full_name`, `abbr_name`, `opens` and `closes`. `current_day` holds the entry for the current day. |
| `results[].rating.ratingValue / results[].rating.bestRating / results[].rating.reviewCount` | Average rating, the top possible rating, and the number of reviews. `is_tripadvisor` is `true` when the rating comes from Tripadvisor. |
| `results[].profiles[].name / results[].profiles[].url` | Name and link of a web or social profile for the place, such as its website, Facebook or Instagram page. |
| `results[].pictures.results[].original / results[].pictures.results[].src` | Link to the original photo and a resized copy of it. |
| `results[].results[].title / results[].results[].url / results[].results[].description` | Web pages related to the place, with title, link and a text snippet. |
| `results[].family_friendly` | Whether the place is flagged as family friendly. |

### Notes

- Pass the location IDs in `ids` as an array. The IDs look like `loc4DFZ5OEXSZVDUAEEDV6PMTFK6YDFANIHQIRRVKLA=` and are valid only for 8 hours.
- Get location IDs from [Brave Place Search](/apis/brave/local-place-search) or [Brave Web Search](/apis/brave/web), then pass them here.
- For a text description of the same places, call [Brave POI Descriptions](/apis/brave/local-descriptions) with the same IDs.
- `search_lang`, `ui_lang` and `units` are optional. `units` accepts `metric` or `imperial`.

### Pricing

$0.005 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/brave/local-pois.json`](../../../catalog/models/brave/local-pois.json) · Store page: https://www.sandbase.ai/model/brave/local-pois
