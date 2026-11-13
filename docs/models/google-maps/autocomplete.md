# Google Maps Autocomplete API: pricing, parameters and code examples

`google-maps/autocomplete` · data API · Google Maps · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Get Google Maps search box suggestions for a partial query near a location, with place names, addresses and place IDs.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google-maps/autocomplete", "q": "coffee", "ll": "@30.2672,-97.7431,14z"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google-maps/autocomplete', {'q': 'coffee', 'll': '@30.2672,-97.7431,14z'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google-maps/autocomplete", {
  "q": "coffee",
  "ll": "@30.2672,-97.7431,14z"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google-maps/autocomplete", sandbase.Params{
	"q": "coffee",
	"ll": "@30.2672,-97.7431,14z",
})
```

Same call via the path form: `POST /v1/api/google-maps/autocomplete` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string | yes | Parameter defines the search query. A query that would be used to provide completion options.  |
| `cp` | string |  | Cursor pointer defines the position of cursor for the query provided, position starts from 0 which is a case where cursor is placed before the query `\|query`. If not provided acts as cursor is placed in the end of…  |
| `gl` | string |  | Parameter defines the country to use for the Google Maps Autocomplete search. It's a two-letter country code. (e.g., `us` for the United States, `uk` for United Kingdom, or `fr` for France) Head to the Google countries…  |
| `hl` | string |  | Parameter defines the language to use for the Google Maps Autocomplete search. It's a two or three-letter language code. (e.g., `en` for English, `es` for Spanish, or `fr` for French), optionally followed by a…  |
| `ll` | string | yes | Parameter defines the GPS coordinates of the location where you want the search to originate from. Its value must match the following format: `@` + `latitude` + `,` + `longitude` + `,` + `zoom/map_height` This will…  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |

## Details

Get Google Maps search box suggestions for a partial query near a location, with place names, addresses and place IDs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google-maps/autocomplete" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "coffee", "ll": "@30.2672,-97.7431,14z"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | Yes | Parameter defines the search query. A query that would be used to provide completion options. |
| `ll` | string | Yes | Parameter defines the GPS coordinates of the location where you want the search to originate from. Its value must match the following format: `@` + `latitude` + `,` + `longitude` + `,` + `zoom/map_height` This will form a string that looks  |
| `gl` | string | No | Parameter defines the country to use for the Google Maps Autocomplete search. It's a two-letter country code. (e.g., `us` for the United States, `uk` for United Kingdom, or `fr` for France) Head to the Google countries page for a full list  |
| `hl` | string | No | Parameter defines the language to use for the Google Maps Autocomplete search. It's a two or three-letter language code. (e.g., `en` for English, `es` for Spanish, or `fr` for French), optionally followed by a two-letter or three-digit regi |
| `cp` | string | No | Cursor pointer defines the position of cursor for the query provided, position starts from 0 which is a case where cursor is placed before the query `/query`. If not provided acts as cursor is placed in the end of query `query/`. |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/google-maps/autocomplete.json`](../../../catalog/models/google-maps/autocomplete.json) · Store page: https://www.sandbase.ai/model/google-maps/autocomplete
