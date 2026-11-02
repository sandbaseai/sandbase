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

Place Search from Brave. Returns the official Brave API response unchanged.

The response is the official Brave API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/brave/local-place-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "coffee", "location": "seattle washington united states"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `count` | integer | No | Number of results to return. The maximum is 100. |
| `country` | string | No | Two-letter country code (ISO 3166-1 alpha-2) to scope the search. |
| `geoloc` | string | No | Optional geolocation of the user in the format <latitude>x<longitude> . Used to calculate distance values in results. |
| `latitude` | number | No | Latitude of the geographical coordinates. |
| `location` | string | No | Location string to search for points of interest in an area. This is alternative to the latitude and longitude parameters. For locations in US prefer the form < |
| `longitude` | number | No | Longitude of the geographical coordinates. |
| `q` | string | No | Query string to search for points of interest in an area. If no q is provided, the endpoint will return general points of interest in the given area. |
| `radius` | number | No | Search radius bias around the given coordinates, in meters. NOTE : This is not strictly the radius of the search (nor the resulting radius of the results), but  |
| `safesearch` | string | No | Safe search level for the query results. |
| `search_lang` | string | No | Language for the search results. |
| `spellcheck` | boolean | No | Whether to apply spellcheck before executing the search. |
| `ui_lang` | string | No | User interface language for the response. Usually <language>-<region> . |
| `units` | string | No | Units of measurement for distance values: metric is kilometres, imperial is miles. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/brave/local-place-search.json`](../../../catalog/models/brave/local-place-search.json) · Store page: https://www.sandbase.ai/model/brave/local-place-search
