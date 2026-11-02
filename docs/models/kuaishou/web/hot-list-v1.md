# Kuaishou Web Hot List API: pricing, parameters and code examples

`kuaishou/web/hot-list-v1` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the current trending hot list from Kuaishou Web. It delivers trending topics and popular content rankings directly from the platform.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/web/hot-list-v1"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/web/hot-list-v1', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/web/hot-list-v1", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/web/hot-list-v1", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/kuaishou/web/hot-list-v1` with the body above minus `model`.

## Details

Access real-time trending topics and popular rankings from Kuaishou Web without requiring query parameters.

### Use cases

- Track trending topics and viral discussions across Kuaishou in real time.
- Monitor shifts in audience interest and public sentiment on the platform.
- Identify popular themes to guide video content strategy and research.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/web/hot-list-v1" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Kuaishou Web Share Short URL](/model/kuaishou/web/generate-share-short-url): Returns a shareable short URL for a specified Kuaishou video or photo post.
- [Kuaishou User ID Lookup](/model/kuaishou/web/get-user-id): Resolves a Kuaishou user ID from a provided user share link.
- [Kuaishou Web Hot List (V2)](/model/kuaishou/web/hot-list-v2): Returns current trending search rankings and hot topics on Kuaishou web.

---
Machine-readable: [`catalog/models/kuaishou/web/hot-list-v1.json`](../../../../catalog/models/kuaishou/web/hot-list-v1.json) · Store page: https://www.sandbase.ai/model/kuaishou/web/hot-list-v1
