# Yellow Pages Explore Cities API: pricing, parameters and code examples

`yellowpages/explore-cities` · data API · Yellow Pages · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Return a list of all US states from the YellowPages sitemap for browsing businesses by location. Each state entry includes the state name and its browse URL.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "yellowpages/explore-cities"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('yellowpages/explore-cities', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("yellowpages/explore-cities", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "yellowpages/explore-cities", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/yellowpages/explore-cities` with the body above minus `model`.

## Details

Return a list of all US states from the YellowPages sitemap for browsing businesses by location. Each state entry includes the state name and its browse URL.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "yellowpages/explore-cities"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/yellowpages/explore-cities.json`](../../../catalog/models/yellowpages/explore-cities.json) · Store page: https://www.sandbase.ai/model/yellowpages/explore-cities
