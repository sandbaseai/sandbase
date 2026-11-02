# Douyin Index Subscribed Keywords API: pricing, parameters and code examples

`douyin/index/get-user-sub-word` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the list of subscribed keywords configured by the current logged-in user on Douyin Index. Useful for retrieving tracked topics without manual lookup.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/get-user-sub-word"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/get-user-sub-word', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/get-user-sub-word", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/get-user-sub-word", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/index/get-user-sub-word` with the body above minus `model`.

## Details

This endpoint retrieves the active keyword subscription list for the current Douyin Index user account without requiring query parameters.

### Use cases

- Retrieve keywords tracked by the authenticated Douyin Index account.
- Inspect active topic monitoring subscriptions across marketing dashboards.
- Sync monitored keyword lists with external analytics systems.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/get-user-sub-word" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Index Area List](/model/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/model/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/model/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/get-user-sub-word.json`](../../../../catalog/models/douyin/index/get-user-sub-word.json) · Store page: https://www.sandbase.ai/model/douyin/index/get-user-sub-word
