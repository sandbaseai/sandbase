# Google Local API: pricing, parameters and code examples

`google/local` · data API · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Search local businesses on Google by keyword and location, with name, rating, reviews, address, hours, phone and place ID.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/local", "q": "coffee"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/local', {'q': 'coffee'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/local", {
  "q": "coffee"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/local", sandbase.Params{
	"q": "coffee",
})
```

Same call via the path form: `POST /v1/api/google/local` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string | yes | Parameter defines the query you want to search. You can use anything that you would use in a regular Google Local search.  |
| `gl` | string |  | Parameter defines the country to use for the Google Local search. It's a two-letter country code. (e.g., `us` for the United States, `uk` for United Kingdom, or `fr` for France) Head to the Google countries for a full…  |
| `hl` | string |  | Parameter defines the language to use for the Google Local search. It's a two or three-letter language code. (e.g., `en` for English, `es` for Spanish, or `fr` for French), optionally followed by a two-letter or…  |
| `tbs` | string |  | (to be searched) parameter defines advanced search parameters that aren't possible in the regular query field.  |
| `uule` | string |  | Parameter is the Google encoded location you want to use for the search. `uule` and `location` parameters can't be used together. For consistent results with coordinates-based `uule` parameter, a matching `gl`…  |
| `start` | string |  | Parameter defines the result offset. It skips the given number of results. It's used for pagination. The value depends on the number of results returned which can either be `10` or `20`. For eg, on mobile `10` results…  |
| `device` | string |  | Parameter defines the device to use to get the results. It can be set to `desktop` (default) to use a regular browser, `tablet` to use a tablet browser (currently using iPads), or `mobile` to use a mobile browser.  |
| `ludocid` | string |  | Parameter defines the Google CID (customer identifier) of a place. This parameter can be found in Google Local API and Google Search API local results under the name of `place_id`, as well as in Google Maps API local…  |
| `location` | string |  | Parameter defines from where you want the search to originate. If several locations match the location requested, we'll pick the most popular one. Head to the /locations.json API if you need more precise control. The…  |
| `google_domain` | string |  | Parameter defines the Google domain to use. It defaults to `google.com`. Head to the Google domains for a full list of supported Google domains.  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |

## Details

Search local businesses on Google by keyword and location, with name, rating, reviews, address, hours, phone and place ID.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google/local" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "coffee", "location": "Austin, Texas, United States"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | Yes | Parameter defines the query you want to search. You can use anything that you would use in a regular Google Local search. |
| `location` | string | No | Parameter defines from where you want the search to originate. If several locations match the location requested, we'll pick the most popular one. Head to the /locations.json API if you need more precise control. The `location` and `uule` p |
| `uule` | string | No | Parameter is the Google encoded location you want to use for the search. `uule` and `location` parameters can't be used together. For consistent results with coordinates-based `uule` parameter, a matching `gl` parameter is required. Head to |
| `google_domain` | string | No | Parameter defines the Google domain to use. It defaults to `google.com`. Head to the Google domains for a full list of supported Google domains. |
| `gl` | string | No | Parameter defines the country to use for the Google Local search. It's a two-letter country code. (e.g., `us` for the United States, `uk` for United Kingdom, or `fr` for France) Head to the Google countries for a full list of supported Goog |
| `hl` | string | No | Parameter defines the language to use for the Google Local search. It's a two or three-letter language code. (e.g., `en` for English, `es` for Spanish, or `fr` for French), optionally followed by a two-letter or three-digit region code (e.g |
| `ludocid` | string | No | Parameter defines the Google CID (customer identifier) of a place. This parameter can be found in Google Local API and Google Search API local results under the name of `place_id`, as well as in Google Maps API local results under the name  |
| `tbs` | string | No | (to be searched) parameter defines advanced search parameters that aren't possible in the regular query field. |
| `start` | string | No | Parameter defines the result offset. It skips the given number of results. It's used for pagination. The value depends on the number of results returned which can either be `10` or `20`. For eg, on mobile `10` results are returned, so `star |
| `device` | string | No | Parameter defines the device to use to get the results. It can be set to `desktop` (default) to use a regular browser, `tablet` to use a tablet browser (currently using iPads), or `mobile` to use a mobile browser. |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/google/local.json`](../../../catalog/models/google/local.json) · Store page: https://www.sandbase.ai/model/google/local
