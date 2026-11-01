# Bilibili App Cinema Tab

`bilibili/app/cinema-tab` · api · Bilibili

Returns cinema tab content from the Bilibili app, featuring curated movies, TV shows, and entertainment recommendations without requiring additional query parameters.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/app/cinema-tab"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/app/cinema-tab', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/app/cinema-tab", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/app/cinema-tab", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/bilibili/app/cinema-tab` with the body above minus `model`.

## Details

Retrieve movie and TV show recommendation feeds from the Bilibili app cinema tab without passing any input parameters.

### Use cases

- Display trending film and television recommendations from Bilibili
- Monitor cinema section highlights for media research
- Integrate entertainment discovery feeds into external dashboards

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/app/cinema-tab" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Bilibili App Bangumi Tab](/model/bilibili/app/bangumi-tab): Returns Bilibili app bangumi tab data, providing curated anime recommendations, feed items, and category listings for mobile clients.
- [Bilibili App Home Feed](/model/bilibili/app/home-feed): Returns recommended video items from the Bilibili app home feed.
- [Bilibili App Single Video Details](/model/bilibili/app/one-video): Returns detailed video metadata for a specific Bilibili video.

---
Machine-readable: [`catalog/models/bilibili/app/cinema-tab.json`](../../../../catalog/models/bilibili/app/cinema-tab.json) · Store page: https://www.sandbase.ai/model/bilibili/app/cinema-tab
