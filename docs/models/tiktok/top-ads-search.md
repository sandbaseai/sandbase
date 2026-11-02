# TikTok Top Ads Search API: pricing, parameters and code examples

`tiktok/top-ads-search` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

Search TikTok Creative Center top video ads by keyword, with campaign objective, performance percentile, and time-window filters.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/top-ads-search", "query": "glasses"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/top-ads-search', {'query': 'glasses'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/top-ads-search", {
  "query": "glasses"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/top-ads-search", sandbase.Params{
	"query": "glasses",
})
```

Same call via the path form: `POST /v1/api/tiktok/top-ads-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | One-based provider page number (default 1). default `1`; range 1– |
| `limit` | integer |  | Maximum number of ads requested for this page, from 1 through 20 (default 20). default `20`; range 1–20 |
| `query` | string | yes | Keyword to search in TikTok Creative Center top video ads.  |
| `period` | integer |  | Lookback period in days (default 180). one of: `7`, `30`, `180`; default `180` |
| `objective` | string |  | Campaign objective filter. Omit it to search every objective. one of: `traffic`, `app_installs`, `conversions`, `video_views`, `reach`, `lead_generation`, `product_sales` |
| `performanceRank` | string |  | Ad performance percentile bucket, where top_1_20 is the highest-performing 20 percent. Omit it to search every bucket. one of: `top_1_20`, `top_21_40`, `top_41_60`, `top_61_80` |

## Details

Search TikTok Creative Center top video ads by keyword, with campaign objective, performance percentile, and time-window filters.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/top-ads-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "glasses"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Keyword to search in TikTok Creative Center top video ads. |
| `limit` | integer | No | Maximum number of ads requested for this page, from 1 through 20 (default 20). |
| `objective` | string | No | Campaign objective filter. Omit it to search every objective. One of: `traffic`, `app_installs`, `conversions`, `video_views`, `reach`, `lead_generation`, `product_sales`. |
| `page` | integer | No | One-based provider page number (default 1). |
| `performanceRank` | string | No | Ad performance percentile bucket, where top_1_20 is the highest-performing 20 percent. Omit it to search every bucket. One of: `top_1_20`, `top_21_40`, `top_41_60`, `top_61_80`. |
| `period` | integer | No | Lookback period in days (default 180). One of: `7`, `30`, `180`. |

### Pricing

Billed at the actual cost of each call, usually $0.0012 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/tiktok/top-ads-search.json`](../../../catalog/models/tiktok/top-ads-search.json) · Store page: https://www.sandbase.ai/model/tiktok/top-ads-search
