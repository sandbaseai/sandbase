# Tripadvisor Place API: pricing, parameters and code examples

`tripadvisor/place` · data API · Tripadvisor · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00015 per call · **Modes:** async

Get one Tripadvisor place with rating, ranking, contacts, amenities, and prices.

## Pricing

- **$0.00015 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tripadvisor/place", "place_id": "<place_id>"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tripadvisor/place', {'place_id': '<place_id>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tripadvisor/place", {
  "place_id": "<place_id>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tripadvisor/place", sandbase.Params{
	"place_id": "<place_id>",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/tripadvisor/place` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `geo_id` | string |  | Positive parent geography id.  |
| `locale` | string |  | Language or language-COUNTRY code, such as 'en-US'. Default 'en-US'.  |
| `currency` | string |  | Three-letter ISO currency for price fields. Default 'USD'.  |
| `place_id` | string | yes | Positive Tripadvisor place id from a search result.  |
| `tripadvisor_domain` | string |  | Localized Tripadvisor hostname. Default 'www.tripadvisor.com'.  |

## Details

Get one Tripadvisor place with rating, ranking, contacts, amenities, and prices.

---
Machine-readable: [`catalog/models/tripadvisor/place.json`](../../../catalog/models/tripadvisor/place.json) · Store page: https://www.sandbase.ai/model/tripadvisor/place
