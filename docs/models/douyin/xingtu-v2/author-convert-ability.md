# Douyin Xingtu Author Conversion Ability API: pricing, parameters and code examples

`douyin/xingtu-v2/author-convert-ability` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.003 per call (free daily quota) · **Modes:** sync

Returns creator conversion ability metrics including GMV, clicks, and conversion rate ranges filtered by creator, time range, and industry.

## Pricing

- **$0.003 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/author-convert-ability", "o_author_id": "7029342444797820939"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/author-convert-ability', {'o_author_id': '7029342444797820939'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/author-convert-ability", {
  "o_author_id": "7029342444797820939"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/author-convert-ability", sandbase.Params{
	"o_author_id": "7029342444797820939",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/author-convert-ability` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `time_range` | integer |  | Time range tier, default 2  |
| `industry_id` | integer |  | Industry ID, 0=unlimited, default 0  |
| `o_author_id` | string | yes | Creator ID  |
| `platform_source` | integer |  | Platform source, default 1  |
| `platform_channel` | integer |  | Platform channel, default 1  |

## Details

Fetch creator conversion performance metrics by supplying the creator ID in `o_author_id`. Optional filters allow narrowing data by industry, time period, and platform source.

### Use cases

- Evaluate Douyin creator sales conversion metrics for influencer marketing selection.
- Compare creator conversion rates across specific industry categories.
- Track creator click and GMV tier performance over defined time periods.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/author-convert-ability" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"o_author_id": "<o_author_id>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `o_author_id` | string | Yes | Creator ID |
| `time_range` | integer | No | Time range tier, default 2 |
| `industry_id` | integer | No | Industry ID, 0=unlimited, default 0 |
| `platform_source` | integer | No | Platform source, default 1 |
| `platform_channel` | integer | No | Platform channel, default 1 |

### Notes

- `o_author_id` is required to identify the target creator.
- `industry_id` defaults to 0 for unlimited industry coverage.
- `time_range` defaults to 2.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/model/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/model/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/model/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/author-convert-ability.json`](../../../../catalog/models/douyin/xingtu-v2/author-convert-ability.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/author-convert-ability
