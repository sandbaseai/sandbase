# Douyin Billboard Vertical Content Tags

`douyin/billboard/content-tag` · api · Douyin

Returns a list of vertical content tags available on the Douyin billboard platform. Useful for categorizing trending topics and discovering niche content segments.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/billboard/content-tag"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/billboard/content-tag', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/billboard/content-tag", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/billboard/content-tag", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/billboard/content-tag` with the body above minus `model`.

## Details

Access the current vertical content tags used across Douyin billboard rankings. This endpoint requires no query parameters to retrieve the tag list.

### Use cases

- Explore available vertical topic categories on Douyin.
- Map platform content tags to internal classification systems.
- Monitor active industry verticals tracked on the Douyin billboard.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/billboard/content-tag" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Billboard City List](/model/douyin/billboard/city-list): Returns the list of Chinese cities supported by Douyin billboard rankings.
- [Douyin Fan Interest Account List](/model/douyin/billboard/hot-account-fans-interest-account-list): Returns a list of 20 accounts that followers of a target creator are interested in on Douyin.
- [Douyin Account Fan Interest Search Terms](/model/douyin/billboard/hot-account-fans-interest-search-list): Returns the top ten search terms reflecting fan interest over the last three days for a specified Douyin creator account using their user sec_id.

---
Machine-readable: [`catalog/models/douyin/billboard/content-tag.json`](../../../../catalog/models/douyin/billboard/content-tag.json) · Store page: https://www.sandbase.ai/model/douyin/billboard/content-tag
