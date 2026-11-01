# Douyin Billboard City List

`douyin/billboard/city-list` · api · Douyin

Returns the list of Chinese cities supported by Douyin billboard rankings. Use this data to populate regional filters for location-specific trending lists.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/billboard/city-list"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/billboard/city-list', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/billboard/city-list", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/billboard/city-list", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/billboard/city-list` with the body above minus `model`.

## Details

This endpoint returns the list of supported Chinese cities for Douyin billboard queries. It requires no input parameters.

### Use cases

- Retrieve available city identifiers to query localized Douyin trending charts.
- Populate city selection dropdowns in analytics dashboards.
- Map regional billboard metrics across supported Chinese municipal markets.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/billboard/city-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Billboard Vertical Content Tags](/model/douyin/billboard/content-tag): Returns a list of vertical content tags available on the Douyin billboard platform.
- [Douyin Fan Interest Account List](/model/douyin/billboard/hot-account-fans-interest-account-list): Returns a list of 20 accounts that followers of a target creator are interested in on Douyin.
- [Douyin Account Fan Interest Search Terms](/model/douyin/billboard/hot-account-fans-interest-search-list): Returns the top ten search terms reflecting fan interest over the last three days for a specified Douyin creator account using their user sec_id.

---
Machine-readable: [`catalog/models/douyin/billboard/city-list.json`](../../../../catalog/models/douyin/billboard/city-list.json) · Store page: https://www.sandbase.ai/model/douyin/billboard/city-list
