# Lemon8 Discover Editor Picks API: pricing, parameters and code examples

`lemon8/app/discover-tab-information-tabs` · data API · Lemon8 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns the Editor's Picks and discover tab information from the Lemon8 mobile app. Use this endpoint to inspect curated featured categories and discover sections.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "lemon8/app/discover-tab-information-tabs"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('lemon8/app/discover-tab-information-tabs', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("lemon8/app/discover-tab-information-tabs", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "lemon8/app/discover-tab-information-tabs", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/lemon8/app/discover-tab-information-tabs` with the body above minus `model`.

## Details

This endpoint returns Editor's Picks and discover tab sections from the Lemon8 app without requiring input parameters.

### Use cases

- Display curated Lemon8 discover categories in a mobile or web interface.
- Track featured Editor's Picks content sections across Lemon8 discover tabs.
- Analyze curated discovery topics promoted on the Lemon8 platform.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/lemon8/app/discover-tab-information-tabs" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Lemon8 Discover Page Banners](/model/lemon8/app/discover-banners): Returns the current promotional and featured banners displayed on the Lemon8 discover page.
- [Lemon8 Discover Page Content](/model/lemon8/app/discover-tab): Returns the main content featured on the Lemon8 discover tab.
- [Lemon8 Hot Search Keywords](/model/lemon8/app/hot-search-keywords): Returns trending search keywords and topics currently popular on Lemon8.

---
Machine-readable: [`catalog/models/lemon8/app/discover-tab-information-tabs.json`](../../../../catalog/models/lemon8/app/discover-tab-information-tabs.json) · Store page: https://www.sandbase.ai/model/lemon8/app/discover-tab-information-tabs
