# Apple Maps Place API: pricing, parameters and code examples

`apple-maps/place` · data API · Apple Maps · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Get an Apple Maps place by MUID with name, category, rating, address, phone, website, hours and coordinates.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "apple-maps/place", "muid": "<muid>"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('apple-maps/place', {'muid': '<muid>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("apple-maps/place", {
  "muid": "<muid>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "apple-maps/place", sandbase.Params{
	"muid": "<muid>",
})
```

Same call via the path form: `POST /v1/api/apple-maps/place` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `muid` | string | yes | Parameter defines the MUID of the place you want to search. You can use the MUID from the Apple Maps Places API response. (e.g. `18366846785603624515` for London). You can also pass multiple MUIDs separated by commas…  |
| `locale` | string |  | Parameter defines the locale the results should be localized for. Locales for Apple Maps are represented as `<LANGUAGE>-<REGION>`. (defaults to `en-US`, the locale for U.S. English). Head to Apple Maps Locales for the…  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |

## Details

Get an Apple Maps place by MUID with name, category, rating, address, phone, website, hours and coordinates.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/apple-maps/place" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"muid": "<muid from Apple Maps Search>"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `muid` | string | Yes | Parameter defines the MUID of the place you want to search. You can use the MUID from the Apple Maps Places API response. (e.g. `18366846785603624515` for London). You can also pass multiple MUIDs separated by commas (e.g., `183668467856036 |
| `locale` | string | No | Parameter defines the locale the results should be localized for. Locales for Apple Maps are represented as `<LANGUAGE>-<REGION>`. (defaults to `en-US`, the locale for U.S. English). Head to Apple Maps Locales for the list of available loca |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/apple-maps/place.json`](../../../catalog/models/apple-maps/place.json) · Store page: https://www.sandbase.ai/model/apple-maps/place
