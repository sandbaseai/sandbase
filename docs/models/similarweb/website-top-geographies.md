# Similarweb Website Top Geographies API: pricing, parameters and code examples

`similarweb/website-top-geographies` · data API · Similarweb · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.225 per call · **Modes:** sync

Get the countries a website's traffic comes from, with share and visits for each country.

## Pricing

- Depends on parameters ().

Formula: `0.225 * Math.max(1.0, Math.min(10.0, (output.data?.data?.countries != nil ? len(output.data.data.countries) : 10) * 1.0))`

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "similarweb/website-top-geographies", "domain": "cnn.com"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('similarweb/website-top-geographies', {'domain': 'cnn.com'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("similarweb/website-top-geographies", {
  "domain": "cnn.com"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "similarweb/website-top-geographies", sandbase.Params{
	"domain": "cnn.com",
})
```

Same call via the path form: `POST /v1/api/similarweb/website-top-geographies` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `month` | string |  | Complete month in YYYY-MM.  |
| `domain` | string | yes | Bare website hostname without scheme, path, port, or credentials.  |

## Details

Get the countries a website's traffic comes from, with share and visits for each country.

The response is the official Similarweb API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/similarweb/website-top-geographies" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"domain": "cnn.com", "month": "2026-09"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `domain` | string | Yes | Bare website hostname without scheme, path, port, or credentials. |
| `month` | string | No | Complete month in YYYY-MM. |

### Pricing

$0.225 per country returned (3 Similarweb credits), up to 10 countries. Failed calls are not charged.

---
Machine-readable: [`catalog/models/similarweb/website-top-geographies.json`](../../../catalog/models/similarweb/website-top-geographies.json) · Store page: https://www.sandbase.ai/model/similarweb/website-top-geographies
