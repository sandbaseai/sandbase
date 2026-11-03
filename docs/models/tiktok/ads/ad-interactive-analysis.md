# TikTok Ad Interactive Analysis API: pricing, parameters and code examples

`tiktok/ads/ad-interactive-analysis` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns audience retention and interaction analytics across video timestamps for a specified ad creative. Supports filtering by analysis metric and time period.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/ads/ad-interactive-analysis", "material_id": "7164467399885864962"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/ads/ad-interactive-analysis', {'material_id': '7164467399885864962'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/ads/ad-interactive-analysis", {
  "material_id": "7164467399885864962"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/ads/ad-interactive-analysis", sandbase.Params{
	"material_id": "7164467399885864962",
})
```

Same call via the path form: `POST /v1/api/tiktok/ads/ad-interactive-analysis` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `material_id` | string | yes | Ad material ID, required parameter  |
| `metric_type` | string |  | Analysis type  |
| `period_type` | integer |  | Time range, default 180 days  |

## Details

Returns audience retention and interaction analytics across video timestamps for one TikTok ad creative. The response has a `keyframe` block and a `percentile` block. The call needs a `material_id`, and you can add `metric_type` and `period_type` to filter the result.

### Use cases

- Check how audience retention changes across the timeline of a video ad.
- Find the moments in an ad creative that draw the most interaction.
- Compare the keyframe and percentile results for one creative in a single call.
- Re-run the same creative with a different `period_type` to see how results change over time.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/ads/ad-interactive-analysis" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"material_id": "<material_id>"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `material_id` | string | Yes | Ad material ID, required parameter |
| `metric_type` | string | No | Analysis type |
| `period_type` | integer | No | Time range, default 180 days |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "keyframe": {
    "code": 40000,
    "msg": "strconv.ParseInt: parsing \"<material_id>\": invalid syntax"
  },
  "percentile": {
    "code": 40000,
    "msg": "strconv.ParseInt: parsing \"<material_id>\": invalid syntax"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `keyframe` | Result block for the keyframe part of the analysis. In the sample response it holds only `code` and `msg`, because the call failed. |
| `percentile` | Result block for the percentile part of the analysis. In the sample response it holds only `code` and `msg`, because the call failed. |
| `keyframe.code / percentile.code` | Status code for each block. The sample shows `40000`, which came back because the `material_id` was not a valid number. |
| `keyframe.msg / percentile.msg` | Error text for each block. In the sample it says the `material_id` value could not be parsed as an integer. |

### Notes

- Send `material_id` as a string of digits. The placeholder value in the sample request failed with a parse error in both blocks.
- Each block reports its own `code` and `msg`, so check both `keyframe` and `percentile` after every call.
- `period_type` is an integer for the time range and defaults to 180 days. `metric_type` is a string that selects the analysis type.
- For one part of the data on its own, see [TikTok Ad Keyframe Analysis](/apis/tiktok/ads/ad-keyframe-analysis) or [TikTok Ad Material Percentile Rankings](/apis/tiktok/ads/ad-percentile).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Ad Keyframe Analysis](/apis/tiktok/ads/ad-keyframe-analysis): Returns keyframe performance metrics across video ad timestamps for a specified material ID, including retention and conversion figures.
- [TikTok Ad Material Percentile Rankings](/apis/tiktok/ads/ad-percentile): Returns ad performance percentile rankings within the industry for a specific ad material.
- [TikTok Ad Detail](/apis/tiktok/ads/ads-detail): Returns detailed information about a single TikTok ad, including creative content, creator information, and engagement performance metrics using a specific ad …

---
Machine-readable: [`catalog/models/tiktok/ads/ad-interactive-analysis.json`](../../../../catalog/models/tiktok/ads/ad-interactive-analysis.json) · Store page: https://www.sandbase.ai/model/tiktok/ads/ad-interactive-analysis
