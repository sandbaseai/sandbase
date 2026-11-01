# TikTok Search Module Safety Configuration

`tiktok/ads/configure-safety` · api · TikTok

Returns the safety and availability configuration switches for TikTok Creative Center search modules. It indicates whether searches for top ads, keywords, hashtags, sounds, and creators are currently available.

## Pricing

- **$0.0015 per call** (USD)
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

Check the operating status of TikTok Creative Center search tools without passing any parameters. It returns configuration switches indicating whether individual search modules are accessible.

### Use cases

- Check the availability of TikTok Creative Center search modules before querying them.
- Verify whether keyword, hashtag, or sound search features are currently active.
- Inspect feature flags for creator and top ad discovery tools.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/ads/configure-safety" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Ad Interactive Analysis](/model/tiktok/ads/ad-interactive-analysis): Returns audience retention and interaction analytics across video timestamps for a specified ad creative.
- [TikTok Ad Keyframe Analysis](/model/tiktok/ads/ad-keyframe-analysis): Returns keyframe performance metrics across video ad timestamps for a specified material ID, including retention and conversion figures.
- [TikTok Ad Material Percentile Rankings](/model/tiktok/ads/ad-percentile): Returns ad performance percentile rankings within the industry for a specific ad material.

---
Machine-readable: [`catalog/models/tiktok/ads/configure-safety.json`](../../../../catalog/models/tiktok/ads/configure-safety.json) · Store page: https://www.sandbase.ai/model/tiktok/ads/configure-safety
