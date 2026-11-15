# Steam Featured API: pricing, parameters and code examples

`steam/featured` · data API · Steam · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Get featured, special, trending, and top-selling products from the Steam store. Returns products grouped by category (specials, top_sellers, new_releases, coming_soon) with pricing and discount information. When category is specified, only that section is returned.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "steam/featured"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('steam/featured', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("steam/featured", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "steam/featured", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/steam/featured` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `country` | string |  | Country code for pricing (e.g. US, GB, DE) default `"US"` |
| `category` | string |  | Category filter to return only one section  |

## Details

Get featured, special, trending, and top-selling products from the Steam store. Returns products grouped by category (specials, top_sellers, new_releases, coming_soon) with pricing and discount information. When category is specified, only that section is returned.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "steam/featured", "country": "US", "category": "specials"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `category` | string | No | Category filter to return only one section |
| `country` | string | No | Country code for pricing (e.g. US, GB, DE) |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/steam/featured.json`](../../../catalog/models/steam/featured.json) · Store page: https://www.sandbase.ai/model/steam/featured
