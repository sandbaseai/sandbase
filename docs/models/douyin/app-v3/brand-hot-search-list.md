# Douyin Brand Hot Search List API: pricing, parameters and code examples

`douyin/app-v3/brand-hot-search-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the current Douyin brand hot search list and category data. Use it to track trending brand searches and popular brand rankings across the platform.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/brand-hot-search-list"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/brand-hot-search-list', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/brand-hot-search-list", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/brand-hot-search-list", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/brand-hot-search-list` with the body above minus `model`.

## Details

Retrieves the latest brand hot search list and ranking data directly from Douyin without requiring additional query parameters.

### Use cases

- Track trending brand topics and keyword rankings on Douyin.
- Monitor consumer interest patterns across brand categories.
- Support competitive intelligence and market research workflows.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/brand-hot-search-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Brand Hot Search List Detail](/apis/douyin/app-v3/brand-hot-search-list-detail): Returns detailed brand hot search list data from Douyin for a specific category.
- [Douyin Short Link Generator](/apis/douyin/app-v3/generate-short-url): Converts a standard Douyin web link into a shortened Douyin URL.
- [Douyin Video Share QR Code](/apis/douyin/app-v3/generate-video-share-qrcode): Returns a Douyin share QR code for a designated target.

---
Machine-readable: [`catalog/models/douyin/app-v3/brand-hot-search-list.json`](../../../../catalog/models/douyin/app-v3/brand-hot-search-list.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/brand-hot-search-list
