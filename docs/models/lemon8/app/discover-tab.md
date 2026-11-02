# Lemon8 Discover Page Content API: pricing, parameters and code examples

`lemon8/app/discover-tab` · data API · Lemon8 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the main content featured on the Lemon8 discover tab. Retrieve trending recommendations and highlighted posts directly from the app feed.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "lemon8/app/discover-tab"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('lemon8/app/discover-tab', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("lemon8/app/discover-tab", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "lemon8/app/discover-tab", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/lemon8/app/discover-tab` with the body above minus `model`.

## Details

Retrieves the primary feed content displayed on the Lemon8 discover tab without requiring any input parameters.

### Use cases

- Display trending posts from the Lemon8 discover feed.
- Analyze featured content topics and community trends.
- Monitor discover page recommendations over time.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/lemon8/app/discover-tab" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Lemon8 Discover Page Banners](/model/lemon8/app/discover-banners): Returns the current promotional and featured banners displayed on the Lemon8 discover page.
- [Lemon8 Discover Editor Picks](/model/lemon8/app/discover-tab-information-tabs): Returns the Editor's Picks and discover tab information from the Lemon8 mobile app.
- [Lemon8 Hot Search Keywords](/model/lemon8/app/hot-search-keywords): Returns trending search keywords and topics currently popular on Lemon8.

---
Machine-readable: [`catalog/models/lemon8/app/discover-tab.json`](../../../../catalog/models/lemon8/app/discover-tab.json) · Store page: https://www.sandbase.ai/model/lemon8/app/discover-tab
