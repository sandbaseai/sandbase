# Apple Maps Search API: pricing, parameters and code examples

`apple-maps/search` · data API · Apple Maps · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Search places on Apple Maps by keyword and location, with name, category, rating, address, phone, hours and coordinates.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "apple-maps/search", "query": "coffee"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('apple-maps/search', {'query': 'coffee'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("apple-maps/search", {
  "query": "coffee"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "apple-maps/search", sandbase.Params{
	"query": "coffee",
})
```

Same call via the path form: `POST /v1/api/apple-maps/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sort` | string |  | Parameter defines the sorting refinement for the search. Can be one of the following: `distance` - Sort by distance from the `center`/`location`. `ratings` - Sort by result ratings. `default` - Sort by best match for…  |
| `span` | string |  | Parameter defines width and height of the search region as `latitudeDelta,longitudeDelta`. Smaller delta values correspond to a higher zoom level. (defaults to `0.5,0.5`).  |
| `query` | string | yes | Parameter defines the query you want to search. You can use anything that you would use in a regular Apple Maps search.  |
| `center` | string |  | Parameter defines coordinates of the center point of the region you want to search within. You can pass the coordinates as `latitude,longitude`. (e.g. `30.324639,-97.7304611` for Austin, TX). Either a `center` or a…  |
| `locale` | string |  | Parameter defines the locale the results should be localized for. Locales for Apple Maps are represented as `<LANGUAGE>-<REGION>`. (defaults to `en-US`, the locale for U.S. English). Head to Apple Maps Locales for the…  |
| `open_at` | string |  | Parameter defines the time at which result locations should be open at. The value must be a Unix timestamp that is in the future, and no more than 24 hours from the current time. (e.g. `1794559756`).  |
| `toggles` | string |  | Parameter defines the toggle options for the search. A comma separated list of toggle `key` values can be passed to this parameter. See the `refinements.toggles` object of the response to see available toggles for a…  |
| `location` | string |  | Parameter defines the GPS coordinates used for the search origin. (e.g. `Austin, Texas, United States`). Either a `center` or a `location` parameter is required. These parameters can't be used together.  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |
| `multi_select_options` | string |  | Parameter defines the options you want to filter by for multi select refinements. A comma separated list of toggle `key` values can be passed to this parameter. See the `refinement.multi_select.<type>.options` object…  |

## Details

Search places on Apple Maps by keyword and location, with name, category, rating, address, phone, hours and coordinates.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/apple-maps/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "coffee", "location": "Austin, TX"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Parameter defines the query you want to search. You can use anything that you would use in a regular Apple Maps search. |
| `location` | string | No | Parameter defines the GPS coordinates used for the search origin. (e.g. `Austin, Texas, United States`). Either a `center` or a `location` parameter is required. These parameters can't be used together. |
| `center` | string | No | Parameter defines coordinates of the center point of the region you want to search within. You can pass the coordinates as `latitude,longitude`. (e.g. `30.324639,-97.7304611` for Austin, TX). Either a `center` or a `location` parameter is r |
| `span` | string | No | Parameter defines width and height of the search region as `latitudeDelta,longitudeDelta`. Smaller delta values correspond to a higher zoom level. (defaults to `0.5,0.5`). |
| `sort` | string | No | Parameter defines the sorting refinement for the search. Can be one of the following: `distance` - Sort by distance from the `center`/`location`. `ratings` - Sort by result ratings. `default` - Sort by best match for your query. This is the |
| `toggles` | string | No | Parameter defines the toggle options for the search. A comma separated list of toggle `key` values can be passed to this parameter. See the `refinements.toggles` object of the response to see available toggles for a search. |
| `multi_select_options` | string | No | Parameter defines the options you want to filter by for multi select refinements. A comma separated list of toggle `key` values can be passed to this parameter. See the `refinement.multi_select.<type>.options` object of the response to see  |
| `open_at` | string | No | Parameter defines the time at which result locations should be open at. The value must be a Unix timestamp that is in the future, and no more than 24 hours from the current time. (e.g. `1794559756`). |
| `locale` | string | No | Parameter defines the locale the results should be localized for. Locales for Apple Maps are represented as `<LANGUAGE>-<REGION>`. (defaults to `en-US`, the locale for U.S. English). Head to Apple Maps Locales for the list of available loca |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/apple-maps/search.json`](../../../catalog/models/apple-maps/search.json) · Store page: https://www.sandbase.ai/model/apple-maps/search
