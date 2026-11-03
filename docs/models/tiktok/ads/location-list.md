# TikTok Ads Location List API: pricing, parameters and code examples

`tiktok/ads/location-list` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the list of supported locations available for advertising targeting on TikTok. Access standard geographical targets to configure ad campaigns.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/ads/location-list"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/ads/location-list', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/ads/location-list", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/ads/location-list", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok/ads/location-list` with the body above minus `model`.

## Details

Returns the list of countries that TikTok Ads supports as geographic targets. The request takes no input. Each entry gives a country code and a country name.

### Use cases

- Fill a country dropdown in a campaign planning tool with TikTok-supported targets.
- Check whether a country appears in the TikTok Ads targeting list before building a campaign.
- Map two-letter country codes to country names in a marketing database.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/ads/location-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "country": [
      {
        "id": "AR",
        "label": "AR",
        "value": "Argentina"
      }
    ]
  },
  "msg": "OK"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `code` | Status code of the response. `0` means the call succeeded. |
| `msg` | Status message. `OK` appears on success. |
| `data.country[]` | List of countries available as ad targeting locations. |
| `data.country[].id / data.country[].label` | Two-letter country code, such as `AR` or `AU`. Both fields hold the same code in the sample. |
| `data.country[].value` | Country name in English, such as `Argentina`. |

### Notes

- Send an empty JSON object `{}`. The API has no request parameters.
- Use `id` as the code to store or match against. Use `value` when you need a display name.
- To look up places by name on TikTok, call [TikTok Location Search](/apis/tiktok/app-v3/location-search).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Ad Interactive Analysis](/apis/tiktok/ads/ad-interactive-analysis): Returns audience retention and interaction analytics across video timestamps for a specified ad creative.
- [TikTok Ad Keyframe Analysis](/apis/tiktok/ads/ad-keyframe-analysis): Returns keyframe performance metrics across video ad timestamps for a specified material ID, including retention and conversion figures.
- [TikTok Ad Material Percentile Rankings](/apis/tiktok/ads/ad-percentile): Returns ad performance percentile rankings within the industry for a specific ad material.

---
Machine-readable: [`catalog/models/tiktok/ads/location-list.json`](../../../../catalog/models/tiktok/ads/location-list.json) · Store page: https://www.sandbase.ai/model/tiktok/ads/location-list
