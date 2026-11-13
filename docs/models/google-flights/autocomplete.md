# Google Flights Autocomplete API: pricing, parameters and code examples

`google-flights/autocomplete` · data API · Google Flights · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Get Google Flights airport and city suggestions for a partial place name, with IATA codes and location IDs.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google-flights/autocomplete", "q": "austin"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google-flights/autocomplete', {'q': 'austin'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google-flights/autocomplete", {
  "q": "austin"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google-flights/autocomplete", sandbase.Params{
	"q": "austin",
})
```

Same call via the path form: `POST /v1/api/google-flights/autocomplete` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string | yes | Parameter defines the search query. A query that would be used to provide completion options.  |
| `gl` | string |  | Parameter defines the country to use for the Google Flights Autocomplete search. It's a two-letter country code. (e.g., `us` for the United States, `uk` for United Kingdom, or `fr` for France) Head to the Google…  |
| `hl` | string |  | Parameter defines the language to use for the Google Flights Autocomplete search. It's a two or three-letter language code. (e.g., `en` for English, `es` for Spanish, or `fr` for French), optionally followed by a…  |
| `exclude_regions` | string |  | Set to `true` to exclude region-level locations from suggestions. Regions include countries, sub-national regions, and multi-country areas (e.g. South Korea, South East England, South East Asia). Default to `false`.  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |

## Details

Get Google Flights airport and city suggestions for a partial place name, with IATA codes and location IDs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google-flights/autocomplete" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "austin"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | Yes | Parameter defines the search query. A query that would be used to provide completion options. |
| `gl` | string | No | Parameter defines the country to use for the Google Flights Autocomplete search. It's a two-letter country code. (e.g., `us` for the United States, `uk` for United Kingdom, or `fr` for France) Head to the Google countries page for a full li |
| `hl` | string | No | Parameter defines the language to use for the Google Flights Autocomplete search. It's a two or three-letter language code. (e.g., `en` for English, `es` for Spanish, or `fr` for French), optionally followed by a two-letter or three-digit r |
| `exclude_regions` | string | No | Set to `true` to exclude region-level locations from suggestions. Regions include countries, sub-national regions, and multi-country areas (e.g. South Korea, South East England, South East Asia). Default to `false`. |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/google-flights/autocomplete.json`](../../../catalog/models/google-flights/autocomplete.json) · Store page: https://www.sandbase.ai/model/google-flights/autocomplete
