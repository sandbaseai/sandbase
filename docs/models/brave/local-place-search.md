# Brave Place Search API: pricing, parameters and code examples

`brave/local-place-search` · data API · Brave · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.005 per call (free daily quota) · **Modes:** sync

Place Search from Brave. Returns the official Brave API response unchanged.

## Pricing

- **$0.005 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "brave/local-place-search"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('brave/local-place-search', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("brave/local-place-search", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "brave/local-place-search", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/brave/local-place-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string |  | Query string to search for points of interest in an area. If no q is provided, the endpoint will return general points of interest in the given area. default `""` |
| `count` | integer |  | Number of results to return. The maximum is 100. default `20`; range 1–100 |
| `units` | string |  | Units of measurement for distance values: metric is kilometres, imperial is miles. one of: `imperial`, `metric`; default `"metric"` |
| `geoloc` | string |  | Optional geolocation of the user in the format <latitude>x<longitude> . Used to calculate distance values in results.  |
| `radius` | number |  | Search radius bias around the given coordinates, in meters. NOTE : This is not strictly the radius of the search (nor the resulting radius of the results), but rather a bias towards results that are closer to the given… range 0– |
| `country` | string |  | Two-letter country code (ISO 3166-1 alpha-2) to scope the search. one of: `AR`, `AU`, `AT`, `BE`, `BR`, `CA`, `CL`, `DK`, `FI`, `FR`, `DE`, `GR` …; default `"US"` |
| `ui_lang` | string |  | User interface language for the response. Usually <language>-<region> . one of: `es-AR`, `en-AU`, `de-AT`, `nl-BE`, `fr-BE`, `pt-BR`, `en-CA`, `fr-CA`, `es-CL`, `da-DK`, `fi-FI`, `fr-FR` …; default `"en-US"` |
| `latitude` | number |  | Latitude of the geographical coordinates. range -90–90 |
| `location` | string |  | Location string to search for points of interest in an area. This is alternative to the latitude and longitude parameters. For locations in US prefer the form <city> <state> <country name> , ie. san francisco ca united…  |
| `longitude` | number |  | Longitude of the geographical coordinates. range -180–180 |
| `safesearch` | string |  | Safe search level for the query results. one of: `off`, `moderate`, `strict`; default `"strict"` |
| `spellcheck` | boolean |  | Whether to apply spellcheck before executing the search. default `true` |
| `search_lang` | string |  | Language for the search results. one of: `ar`, `eu`, `bn`, `bg`, `ca`, `zh-hans`, `zh-hant`, `hr`, `cs`, `da`, `nl`, `en` …; default `"en"` |

## Details

Returns a list of places (points of interest) that match a search query in an area. You give a `q` such as `coffee` and either a `location` string or `latitude` and `longitude`. Each result has a name, address, coordinates, phone number, opening hours and rating.

### Use cases

- Build a store locator that lists nearby cafes with address and phone number.
- Show opening hours for each day so a user can see which places are open now.
- Compare ratings and review counts across places of one type in a city.
- Plot results on a map using the coordinates of each place.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/brave/local-place-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "coffee", "location": "seattle washington united states"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `count` | integer | No | Number of results to return. The maximum is 100. |
| `country` | string | No | Two-letter country code (ISO 3166-1 alpha-2) to scope the search. |
| `geoloc` | string | No | Optional geolocation of the user in the format <latitude>x<longitude> . Used to calculate distance values in results. |
| `latitude` | number | No | Latitude of the geographical coordinates. |
| `location` | string | No | Location string to search for points of interest in an area. This is alternative to the latitude and longitude parameters. For locations in US prefer the form <city> <state> <country name> , ie. san francisco ca united s |
| `longitude` | number | No | Longitude of the geographical coordinates. |
| `q` | string | No | Query string to search for points of interest in an area. If no q is provided, the endpoint will return general points of interest in the given area. |
| `radius` | number | No | Search radius bias around the given coordinates, in meters. NOTE : This is not strictly the radius of the search (nor the resulting radius of the results), but rather a bias towards results that are closer to the given c |
| `safesearch` | string | No | Safe search level for the query results. |
| `search_lang` | string | No | Language for the search results. |
| `spellcheck` | boolean | No | Whether to apply spellcheck before executing the search. |
| `ui_lang` | string | No | User interface language for the response. Usually <language>-<region> . |
| `units` | string | No | Units of measurement for distance values: metric is kilometres, imperial is miles. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "addresses": [],
  "cities": [],
  "countries": [],
  "location": {
    "coordinates": [
      47.60621
    ],
    "country": "US",
    "name": "Seattle"
  },
  "mixed": [
    {
      "all": false,
      "index": 0,
      "type": "results"
    }
  ],
  "neighborhoods": [],
  "regions": [],
  "results": [
    {
      "categories": [
        "bakery"
      ],
      "contact": {
        "telephone": "+12067805777"
      },
      "coordinates": [
        47.60895
      ],
      "description": "Coffee Shop",
      "family_friendly": true,
      "icon_category": "cafe",
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
      }
    }
  ],
  "streets": [],
  "type": "locations"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `results[].title` | Name of the place. |
| `results[].id` | Place ID, such as `loc4DFZ5OEXSZVDUAEEDV6PMTFK6YDFANIHQIRRVKLA=`. Use it to look up more details about the place. |
| `results[].postal_address.displayAddress` | Full street address as one text line. |
| `results[].coordinates` | Two numbers for the place. The first value matches latitude and the second matches longitude. |
| `results[].contact.telephone` | Phone number in international format. |
| `results[].rating.ratingValue / results[].rating.bestRating / results[].rating.reviewCount` | Average rating, the top possible rating, and the number of reviews behind the rating. |
| `results[].opening_hours.current_day[] / results[].opening_hours.days[][]` | Opening and closing times (`opens`, `closes`, as `HH:MM`) with the day name in `full_name` and `abbr_name`. `current_day` holds today's hours. |
| `results[].categories / results[].description` | Category tags and a short type label such as `Coffee Shop`. |
| `results[].url / results[].thumbnail.src / results[].pictures.results[].original` | The place's website, a thumbnail image URL, and full-size photo URLs. |
| `location.name / location.coordinates / location.country` | The area the search resolved to, with its center coordinates and country code. |

### Notes

- Send either `location` (for example `seattle washington united states`) or both `latitude` and `longitude` to set the search area.
- Use `count` to set how many places come back. The default is 20 and the maximum is 100.
- Pass the `id` values from `results[]` to [Brave POI Descriptions](/apis/brave/local-descriptions) or [Brave Local POIs](/apis/brave/local-pois) to get more detail on each place.
- Empty lists such as `addresses`, `cities` and `streets` appear in the response when the query matches only places.

### Pricing

$0.005 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/brave/local-place-search.json`](../../../catalog/models/brave/local-place-search.json) · Store page: https://www.sandbase.ai/model/brave/local-place-search
