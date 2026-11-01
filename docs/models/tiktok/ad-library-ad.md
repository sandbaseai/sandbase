# TikTok Ad Library Ad

`tiktok/ad-library-ad` · api · TikTok

Fetch full details for a single TikTok ad (brand, title, spend, CTR, objectives, landing page, and video info).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/ad-library-ad", "adId": "7648493525660270600"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/ad-library-ad', {'adId': '7648493525660270600'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/ad-library-ad", {
  "adId": "7648493525660270600"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/ad-library-ad", sandbase.Params{
	"adId": "7648493525660270600",
})
```

Same call via the path form: `POST /v1/api/tiktok/ad-library-ad` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `adId` | string | yes | TikTok Top Ads material/ad ID, or a Top Ads detail URL (e.g. 7648493525660270600).  |

## Details

Fetch full details for a single TikTok ad (brand, title, spend, CTR, objectives, landing page, and video info).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/ad-library-ad" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"adId": "7648493525660270600"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `adId` | string | Yes | TikTok Top Ads material/ad ID, or a Top Ads detail URL (e.g. 7648493525660270600). |

### Pricing

Billed at the actual cost of each call, usually $0.0012 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/tiktok/ad-library-ad.json`](../../../catalog/models/tiktok/ad-library-ad.json) · Store page: https://www.sandbase.ai/model/tiktok/ad-library-ad
