# Kuaishou App Selection Feed

`kuaishou/app/selection-feed` · api · Kuaishou

Returns the recommended selection feed from the Kuaishou app home page. The endpoint requires no parameters and provides fresh recommended video items on each call.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/app/selection-feed"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/app/selection-feed', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/app/selection-feed", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/app/selection-feed", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/kuaishou/app/selection-feed` with the body above minus `model`.

## Details

Retrieves the recommended selection feed items directly from the Kuaishou app home page without requiring any input parameters.

### Use cases

- Monitor trending and recommended video content on the Kuaishou platform.
- Gather home page selection feed data for audience interest research.
- Track popular media items displayed to general Kuaishou app users.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/app/selection-feed" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Notes

- The feed does not use cursor pagination; call the endpoint again to retrieve additional content.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Kuaishou Brand Top List](/model/kuaishou/app/brand-top-list): Returns top brand rankings and related live stream links from Kuaishou.
- [Kuaishou App Share Link](/model/kuaishou/app/generate-share-link): Generates a shareable URL for Kuaishou application content using a specified object identifier.
- [Kuaishou Hot Board Categories](/model/kuaishou/app/hot-board-categories): Returns the active list of hot board categories available in the Kuaishou app.

---
Machine-readable: [`catalog/models/kuaishou/app/selection-feed.json`](../../../../catalog/models/kuaishou/app/selection-feed.json) · Store page: https://www.sandbase.ai/model/kuaishou/app/selection-feed
