# Google Maps Search API: pricing, parameters and code examples

`google-maps/search` · data API · Google Maps · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Search places on Google Maps by keyword around a location, with name, rating, reviews, address, hours, phone, website, GPS coordinates and place IDs.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google-maps/search", "type": "search"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google-maps/search', {'type': 'search'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google-maps/search", {
  "type": "search"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google-maps/search", sandbase.Params{
	"type": "search",
})
```

Same call via the path form: `POST /v1/api/google-maps/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `m` | string |  | Parameter defines a map height in meters. The minimum value is `1`. The maximum value is `15028132`, which roughly equals `3z` on the equator. At the end, it is encoded as part of the `ll` parameter. Either `m` or `z`…  |
| `q` | string |  | Parameter defines the query you want to search. You can use anything that you would use in a regular Google Maps search. The parameter is only required if `type` is set to `search`.  |
| `z` | string |  | Parameter defines a map zoom level. The minimum value is `3` (the map is completely zoomed out). The maximum effective value depends on the location, ranging from `18` to `23`. Some locations may support even higher…  |
| `gl` | string |  | Parameter defines the country to use for the Google Maps search. It's a two-letter country code. (e.g., `us` for the United States, `uk` for United Kingdom, or `fr` for France). Head to the Google countries page for a…  |
| `hl` | string |  | Parameter defines the language to use for the Google Maps search. It's a two or three-letter language code. (e.g., `en` for English, `es` for Spanish, or `fr` for French), optionally followed by a two-letter or…  |
| `ll` | string |  | Parameter defines the GPS coordinates for the search origin. Its value must match the following format: `@` + `latitude` + `,` + `longitude` + `,` + `zoom/map_height` This will form a string that looks like:…  |
| `lat` | string |  | Parameter defines a GPS latitude for the search origin. At the end, it is encoded as part of the `ll` parameter. Parameter is required when using `lon` parameter. Parameter should be used with `z` or `m` parameter.…  |
| `lon` | string |  | Parameter defines a GPS longitude for the search origin. At the end, it is encoded as part of the `ll` parameter. Parameter is required when using `lat` parameter. Parameter should be used with `z` or `m` parameter.…  |
| `data` | string |  | This parameter is deprecated, please use `place_id` or `data_cid` instead. Parameter can be used to filter the search results. You can visit Google Maps website, set filters you want and simply copy the `data` value…  |
| `type` | string | yes | Parameter defines the type of search you want to make. It can be set to: `search` - returns a list of results for the set `q` parameter, `place` - returns results for a specific place when `data` parameter is set…  |
| `start` | string |  | Parameter defines the result offset. It skips the given number of results. It's used for pagination. (e.g., `0` (default) is the first page of results, `20` is the 2nd page of results, `40` is the 3rd page of results,…  |
| `nearby` | string |  | Parameter forces to return search results closer to the specified location. Parameter is highly recommended when `q` parameter includes `near me` keywords. Parameter is not recommended when `q` parameter includes…  |
| `data_cid` | string |  | Parameter defines the Google CID (customer identifier) of a place. This parameter can be found in Google Maps API local results, as well as in Google Search API and Google Local API local results under the name of…  |
| `location` | string |  | Parameter defines the location, whose GPS coordinates are used for the search origin. At the end, coordinates are encoded as part of the `ll` parameter. Parameter should be used with `z` or `m` parameter. Parameter…  |
| `place_id` | string |  | Parameter defines the unique reference to a place in Google Maps. Place IDs are available for most locations, including businesses, landmarks, parks, and intersections. You can find the `place_id` using our Google Maps…  |
| `max_price` | string |  | Parameter defines the upper bound of the place price range. The places with the price range overlapping with the specified one will be returned. Parameter is applicable to searches expected to return places with…  |
| `min_price` | string |  | Parameter defines the lower bound of the place price range. The places with the price range overlapping with the specified one will be returned. Parameter is applicable to searches expected to return places with…  |
| `min_rating` | string |  | Parameter defines the preferred minimum rating of the place. Places without a rating or with a rating below the specified value can still be returned, but with reduced relevance. Options: `2.0` - 2.0 `2.5` - 2.5 `3.0`… one of: `2.0`, `2.5`, `3.0`, `3.5`, `4.0`, `4.5` |
| `open_state` | string |  | Parameter defines the open state of the place. Options: `now` - Open now `24h` - Open 24 hours Parameter can't be used with `open_on_day` or `open_at_hour` parameters. one of: `now`, `24h` |
| `open_on_day` | string |  | Parameter defines the day on which the place is open. Options: `mon` - Monday `tue` - Tuesday `wed` - Wednesday `thu` - Thursday `fri` - Friday `sat` - Saturday `sun` - Sunday Parameter can't be used with `open_state`… one of: `mon`, `tue`, `wed`, `thu`, `fri`, `sat`, `sun` |
| `open_at_hour` | string |  | Parameter defines the hour at which the place is open. Options: `0` - Midnight `1` - 1:00 AM `2` - 2:00 AM `3` - 3:00 AM `4` - 4:00 AM `5` - 5:00 AM `6` - 6:00 AM `7` - 7:00 AM `8` - 8:00 AM `9` - 9:00 AM `10` - 10:00… one of: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11` … |
| `google_domain` | string |  | Parameter defines the Google domain to use. It defaults to `google.com`. Head to the Google domains page for a full list of supported Google domains.  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |

## Details

Search places on Google Maps by keyword around a location, with name, rating, reviews, address, hours, phone, website, GPS coordinates and place IDs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google-maps/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "coffee", "type": "search", "ll": "@30.2672,-97.7431,14z"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `type` | string | Yes | Parameter defines the type of search you want to make. It can be set to: `search` - returns a list of results for the set `q` parameter, `place` - returns results for a specific place when `data` parameter is set Parameter is not required w |
| `q` | string | No | Parameter defines the query you want to search. You can use anything that you would use in a regular Google Maps search. The parameter is only required if `type` is set to `search`. |
| `ll` | string | No | Parameter defines the GPS coordinates for the search origin. Its value must match the following format: `@` + `latitude` + `,` + `longitude` + `,` + `zoom/map_height` This will form a string that looks like: `@40.7455096,-74.0083012,14z` or |
| `location` | string | No | Parameter defines the location, whose GPS coordinates are used for the search origin. At the end, coordinates are encoded as part of the `ll` parameter. Parameter should be used with `z` or `m` parameter. Parameter can't be used with `ll`,  |
| `lat` | string | No | Parameter defines a GPS latitude for the search origin. At the end, it is encoded as part of the `ll` parameter. Parameter is required when using `lon` parameter. Parameter should be used with `z` or `m` parameter. Parameter can't be used w |
| `lon` | string | No | Parameter defines a GPS longitude for the search origin. At the end, it is encoded as part of the `ll` parameter. Parameter is required when using `lat` parameter. Parameter should be used with `z` or `m` parameter. Parameter can't be used  |
| `z` | string | No | Parameter defines a map zoom level. The minimum value is `3` (the map is completely zoomed out). The maximum effective value depends on the location, ranging from `18` to `23`. Some locations may support even higher values, so we allow valu |
| `m` | string | No | Parameter defines a map height in meters. The minimum value is `1`. The maximum value is `15028132`, which roughly equals `3z` on the equator. At the end, it is encoded as part of the `ll` parameter. Either `m` or `z` is required when using |
| `nearby` | string | No | Parameter forces to return search results closer to the specified location. Parameter is highly recommended when `q` parameter includes `near me` keywords. Parameter is not recommended when `q` parameter includes location. Parameter should  |
| `google_domain` | string | No | Parameter defines the Google domain to use. It defaults to `google.com`. Head to the Google domains page for a full list of supported Google domains. |
| `hl` | string | No | Parameter defines the language to use for the Google Maps search. It's a two or three-letter language code. (e.g., `en` for English, `es` for Spanish, or `fr` for French), optionally followed by a two-letter or three-digit region code (e.g. |
| `gl` | string | No | Parameter defines the country to use for the Google Maps search. It's a two-letter country code. (e.g., `us` for the United States, `uk` for United Kingdom, or `fr` for France). Head to the Google countries page for a full list of supported |
| `data` | string | No | This parameter is deprecated, please use `place_id` or `data_cid` instead. Parameter can be used to filter the search results. You can visit Google Maps website, set filters you want and simply copy the `data` value from their URL to the AP |
| `place_id` | string | No | Parameter defines the unique reference to a place in Google Maps. Place IDs are available for most locations, including businesses, landmarks, parks, and intersections. You can find the `place_id` using our Google Maps API. You can read mor |
| `data_cid` | string | No | Parameter defines the Google CID (customer identifier) of a place. This parameter can be found in Google Maps API local results, as well as in Google Search API and Google Local API local results under the name of `place_id`. You can also a |
| `min_price` | string | No | Parameter defines the lower bound of the place price range. The places with the price range overlapping with the specified one will be returned. Parameter is applicable to searches expected to return places with numerical `price` data (e.g. |
| `max_price` | string | No | Parameter defines the upper bound of the place price range. The places with the price range overlapping with the specified one will be returned. Parameter is applicable to searches expected to return places with numerical `price` data (e.g. |
| `min_rating` | string | No | Parameter defines the preferred minimum rating of the place. Places without a rating or with a rating below the specified value can still be returned, but with reduced relevance. Options: `2.0` - 2.0 `2.5` - 2.5 `3.0` - 3.0 `3.5` - 3.5 `4.0 |
| `open_state` | string | No | Parameter defines the open state of the place. Options: `now` - Open now `24h` - Open 24 hours Parameter can't be used with `open_on_day` or `open_at_hour` parameters. |
| `open_on_day` | string | No | Parameter defines the day on which the place is open. Options: `mon` - Monday `tue` - Tuesday `wed` - Wednesday `thu` - Thursday `fri` - Friday `sat` - Saturday `sun` - Sunday Parameter can't be used with `open_state` parameter. |
| `open_at_hour` | string | No | Parameter defines the hour at which the place is open. Options: `0` - Midnight `1` - 1:00 AM `2` - 2:00 AM `3` - 3:00 AM `4` - 4:00 AM `5` - 5:00 AM `6` - 6:00 AM `7` - 7:00 AM `8` - 8:00 AM `9` - 9:00 AM `10` - 10:00 AM `11` - 11:00 AM `12 |
| `start` | string | No | Parameter defines the result offset. It skips the given number of results. It's used for pagination. (e.g., `0` (default) is the first page of results, `20` is the 2nd page of results, `40` is the 3rd page of results, etc.). We recommend st |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/google-maps/search.json`](../../../catalog/models/google-maps/search.json) · Store page: https://www.sandbase.ai/model/google-maps/search
