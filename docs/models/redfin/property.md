# Redfin Property API: pricing, parameters and code examples

`redfin/property` · data API · Redfin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0008 per call · **Modes:** sync

Fetch full details for a single Redfin home by its listing URL (price, beds, baths, square feet, address, listing agent, description and photos) as normalized JSON.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0008**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "redfin/property", "url": "https://www.redfin.com/TX/Austin/1819-Village-Oak-Ct-78704/home/30981993"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('redfin/property', {'url': 'https://www.redfin.com/TX/Austin/1819-Village-Oak-Ct-78704/home/30981993'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("redfin/property", {
  "url": "https://www.redfin.com/TX/Austin/1819-Village-Oak-Ct-78704/home/30981993"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "redfin/property", sandbase.Params{
	"url": "https://www.redfin.com/TX/Austin/1819-Village-Oak-Ct-78704/home/30981993",
})
```

Same call via the path form: `POST /v1/api/redfin/property` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Redfin home details URL (e.g. https://www.redfin.com/TX/Austin/1819-Village-Oak-Ct-78704/home/30981993).  |

## Details

Fetch full details for a single Redfin home by its listing URL (price, beds, baths, square feet, address, listing agent, description and photos) as normalized JSON.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "redfin/property", "url": "https://www.redfin.com/TX/Austin/1819-Village-Oak-Ct-78704/home/30981993"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Redfin home details URL (e.g. https://www.redfin.com/TX/Austin/1819-Village-Oak-Ct-78704/home/30981993). |

### Pricing

Billed at the actual cost of each call, about $0.0008 per request. A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/redfin/property.json`](../../../catalog/models/redfin/property.json) · Store page: https://www.sandbase.ai/model/redfin/property
