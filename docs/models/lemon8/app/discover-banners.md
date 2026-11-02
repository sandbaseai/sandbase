# Lemon8 Discover Page Banners API: pricing, parameters and code examples

`lemon8/app/discover-banners` · data API · Lemon8 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the current promotional and featured banners displayed on the Lemon8 discover page. Applications can use this data to inspect active platform campaigns and highlighted topics.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "lemon8/app/discover-banners"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('lemon8/app/discover-banners', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("lemon8/app/discover-banners", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "lemon8/app/discover-banners", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/lemon8/app/discover-banners` with the body above minus `model`.

## Details

Call this endpoint without additional parameters to inspect the latest promotional banners featured on the Lemon8 discover page.

### Use cases

- Display current Lemon8 campaign banners inside external dashboards.
- Monitor featured marketing events showcased on the discover page.
- Track active promotional highlights across the Lemon8 platform.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/lemon8/app/discover-banners" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Lemon8 Discover Page Content](/model/lemon8/app/discover-tab): Returns the main content featured on the Lemon8 discover tab.
- [Lemon8 Discover Editor Picks](/model/lemon8/app/discover-tab-information-tabs): Returns the Editor's Picks and discover tab information from the Lemon8 mobile app.
- [Lemon8 Hot Search Keywords](/model/lemon8/app/hot-search-keywords): Returns trending search keywords and topics currently popular on Lemon8.

---
Machine-readable: [`catalog/models/lemon8/app/discover-banners.json`](../../../../catalog/models/lemon8/app/discover-banners.json) · Store page: https://www.sandbase.ai/model/lemon8/app/discover-banners
