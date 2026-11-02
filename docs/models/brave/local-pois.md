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

Local POIs from Brave. Returns the official Brave API response unchanged.

The response is the official Brave API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/brave/local-pois" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"ids": ["loc4DFZ5OEXSZVDUAEEDV6PMTFK6YDFANIHQIRRVKLA="]}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `ids` | array | Yes | A list of unique identifiers for the location. The ids are valid only for 8 hours. |
| `search_lang` | string | No | The search language preference. The 2 or more character language code for which the search results are provided. |
| `ui_lang` | string | No | User interface language preferred in response. Usually of the format <language_code>-<country_code>. For more, see RFC 9110 . |
| `units` | string | No | The measurement units. The following values are supported: metric - The standardized measurement system (km, celcius…) imperial - The British Imperial system of |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/brave/local-pois.json`](../../../catalog/models/brave/local-pois.json) · Store page: https://www.sandbase.ai/model/brave/local-pois
