# TikTok Ad Material Percentile Rankings

`tiktok/ads/ad-percentile` · api · TikTok

Returns ad performance percentile rankings within the industry for a specific ad material. Supports filtering by metrics like CTR or conversion rate and time period.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/ads/ad-percentile", "material_id": "<material_id>"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/ads/ad-percentile', {'material_id': '<material_id>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/ads/ad-percentile", {
  "material_id": "<material_id>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/ads/ad-percentile", sandbase.Params{
	"material_id": "<material_id>",
})
```

Same call via the path form: `POST /v1/api/tiktok/ads/ad-percentile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `metric` | string |  | Analysis metric (ctr_percentile, time_attr_conversion_rate_percentile, click_cnt_percentile, time_attr_convert_cnt_percentile, show_cnt_percentile)  |
| `material_id` | string | yes | Ad material ID, required parameter  |
| `period_type` | integer |  | Time period in days, default 180  |

## Details

Look up industry benchmark percentiles for ad performance using a required `material_id`. You can specify an individual `metric` and configure the evaluation window with `period_type`.

### Use cases

- Compare ad click-through rate rankings against industry benchmarks.
- Evaluate conversion rate percentiles to identify top-performing creatives.
- Analyze relative show count and click count data across custom time windows.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/ads/ad-percentile" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"material_id": "<material_id>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `material_id` | string | Yes | Ad material ID, required parameter |
| `metric` | string | No | Analysis metric (ctr_percentile, time_attr_conversion_rate_percentile, click_cnt_percentile, time_attr_convert_cnt_percentile, show_cnt_percentile) |
| `period_type` | integer | No | Time period in days, default 180 |

### Notes

- `material_id` is required to identify the ad creative.
- `metric` options include `ctr_percentile`, `time_attr_conversion_rate_percentile`, `click_cnt_percentile`, `time_attr_convert_cnt_percentile`, and `show_cnt_percentile`.
- `period_type` sets the time period in days and defaults to 180.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Ad Interactive Analysis](/model/tiktok/ads/ad-interactive-analysis): Returns audience retention and interaction analytics across video timestamps for a specified ad creative.
- [TikTok Ad Keyframe Analysis](/model/tiktok/ads/ad-keyframe-analysis): Returns keyframe performance metrics across video ad timestamps for a specified material ID, including retention and conversion figures.
- [TikTok Ad Detail](/model/tiktok/ads/ads-detail): Returns detailed information about a single TikTok ad, including creative content, creator information, and engagement performance metrics using a specific ad …

---
Machine-readable: [`catalog/models/tiktok/ads/ad-percentile.json`](../../../../catalog/models/tiktok/ads/ad-percentile.json) · Store page: https://www.sandbase.ai/model/tiktok/ads/ad-percentile
