# Open-Meteo Geocoding API: pricing, parameters and code examples

`open-meteo/geocoding` · data API · Open-Meteo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0001 per call (free daily quota) · **Modes:** sync

Look up places by name and get coordinates, country, timezone, population and elevation for use with the weather APIs.

## Pricing

- **$0.0001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "open-meteo/geocoding", "name": "Berlin"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('open-meteo/geocoding', {'name': 'Berlin'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("open-meteo/geocoding", {
  "name": "Berlin"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "open-meteo/geocoding", sandbase.Params{
	"name": "Berlin",
})
```

Same call via the path form: `POST /v1/api/open-meteo/geocoding` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `name` | string | yes | Location name or postal code. Append `, ` or `, ` to narrow results.  |
| `count` | integer |  | Maximum number of results (1-100). Default 10. default `10` |
| `format` | string |  | Response format. Default `json`. one of: `json`, `protobuf`; default `"json"` |
| `language` | string |  | Two-letter language code for translated names. Default `en`. default `"en"` |
| `countryCode` | string |  | ISO-3166-1 alpha-2 country code to filter results.  |

## Details

Look up places by name and get coordinates, country, timezone, population and elevation for use with the weather APIs.

The result is returned in `outputs[0].data` as the official Open-Meteo API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/open-meteo/geocoding" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"name": "Berlin"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `count` | integer | No | Maximum number of results (1-100). Default 10. |
| `countryCode` | string | No | ISO-3166-1 alpha-2 country code to filter results. |
| `format` | string | No | Response format. Default `json`. |
| `language` | string | No | Two-letter language code for translated names. Default `en`. |
| `name` | string | Yes | Location name or postal code. Append `, ` or `, ` to narrow results. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/open-meteo/geocoding.json`](../../../catalog/models/open-meteo/geocoding.json) · Store page: https://www.sandbase.ai/model/open-meteo/geocoding
