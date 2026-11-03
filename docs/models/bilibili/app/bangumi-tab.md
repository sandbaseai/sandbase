# Bilibili App Bangumi Tab API: pricing, parameters and code examples

`bilibili/app/bangumi-tab` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns Bilibili app bangumi tab data, providing curated anime recommendations, feed items, and category listings for mobile clients.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/app/bangumi-tab"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/app/bangumi-tab', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/app/bangumi-tab", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/app/bangumi-tab", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/bilibili/app/bangumi-tab` with the body above minus `model`.

## Details

Retrieve Bilibili app bangumi tab content, including anime recommendations and featured series listings without requiring input parameters.

### Use cases

- Display curated anime recommendations from the Bilibili app.
- Track featured bangumi titles and season promotions.
- Populate anime discovery feeds in client applications.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/app/bangumi-tab" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Bilibili App Cinema Tab](/apis/bilibili/app/cinema-tab): Returns cinema tab content from the Bilibili app, featuring curated movies, TV shows, and entertainment recommendations without requiring additional query para…
- [Bilibili App Home Feed](/apis/bilibili/app/home-feed): Returns recommended video items from the Bilibili app home feed.
- [Bilibili App Single Video Details](/apis/bilibili/app/one-video): Returns detailed video metadata for a specific Bilibili video.

---
Machine-readable: [`catalog/models/bilibili/app/bangumi-tab.json`](../../../../catalog/models/bilibili/app/bangumi-tab.json) · Store page: https://www.sandbase.ai/model/bilibili/app/bangumi-tab
