# TikTok Search Module Safety Configuration API: pricing, parameters and code examples

`tiktok/ads/configure-safety` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the safety and availability configuration switches for TikTok Creative Center search modules. It indicates whether searches for top ads, keywords, hashtags, sounds, and creators are currently available.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/ads/configure-safety"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/ads/configure-safety', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/ads/configure-safety", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/ads/configure-safety", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok/ads/configure-safety` with the body above minus `model`.

## Details

Returns a set of configuration switches for the TikTok Creative Center search modules. It needs no input. The response has one flag each for top ads, keyword, hashtag, sound, and creator search.

### Use cases

- Check the switches before you call a Creative Center search API, so your job can skip a module that is turned off.
- Poll the response to log when a search module changes state.
- Show a status panel for top ads, keyword, hashtag, sound, and creator search in an internal dashboard.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/ads/configure-safety" \
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
    "cc_banner_key": "",
    "creator_search": 0,
    "hashtag_search": 0,
    "keyword_search": 0,
    "sound_search": 0,
    "top_ads_search": 0
  },
  "msg": "OK"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `code` | Status code of the call. `0` appears together with `msg` set to `OK` in the sample response. |
| `data.top_ads_search` | Switch for the top ads search module. The sample value is `0`. |
| `data.keyword_search` | Switch for the keyword search module. The sample value is `0`. |
| `data.hashtag_search` | Switch for the hashtag search module. The sample value is `0`. |
| `data.sound_search` | Switch for the sound search module. The sample value is `0`. |
| `data.creator_search` | Switch for the creator search module. The sample value is `0`. |
| `data.cc_banner_key` | Banner key string for the Creative Center. It is an empty string in the sample response. |

### Notes

- Send an empty JSON body `{}`. The API has no request parameters.
- All five search switches are `0` in the sample response. The response does not state what `0` or `1` means, so compare values over time rather than assuming a meaning.
- To search ads after checking the switches, call [TikTok Creative Center Ad Search](/apis/tiktok/ads/search-ads).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Ad Interactive Analysis](/apis/tiktok/ads/ad-interactive-analysis): Returns audience retention and interaction analytics across video timestamps for a specified ad creative.
- [TikTok Ad Keyframe Analysis](/apis/tiktok/ads/ad-keyframe-analysis): Returns keyframe performance metrics across video ad timestamps for a specified material ID, including retention and conversion figures.
- [TikTok Ad Material Percentile Rankings](/apis/tiktok/ads/ad-percentile): Returns ad performance percentile rankings within the industry for a specific ad material.

---
Machine-readable: [`catalog/models/tiktok/ads/configure-safety.json`](../../../../catalog/models/tiktok/ads/configure-safety.json) · Store page: https://www.sandbase.ai/model/tiktok/ads/configure-safety
