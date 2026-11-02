# Douyin Author Market Fields API: pricing, parameters and code examples

`douyin/xingtu-v2/author-market-fields` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns all filter field options available within the Douyin creator marketplace. Accepts an optional marketplace scene identifier to tailor field choices.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/author-market-fields"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/author-market-fields', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/author-market-fields", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/author-market-fields", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/author-market-fields` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `market_scene` | integer |  | Market scene, 1=default default `1` |

## Details

Look up available creator marketplace filter fields on Douyin, optionally filtered by `market_scene`.

### Use cases

- Retrieve available filtering options for author discovery.
- Populate creator marketplace filter options in search interfaces.
- Determine supported author criteria for a specific marketplace scene.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/author-market-fields" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `market_scene` | integer | No | Market scene, 1=default |

### Notes

- Set `market_scene` to specify the scene context, where `1` represents the default scene.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/model/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/model/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/model/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/author-market-fields.json`](../../../../catalog/models/douyin/xingtu-v2/author-market-fields.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/author-market-fields
