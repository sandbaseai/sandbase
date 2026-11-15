# TikTok Ads Library Ad Details API: pricing, parameters and code examples

`tiktok-ads-library/ad-details` · data API · TikTok Ads Library · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Get detailed information about a specific ad including advertiser info, targeting (location, age, gender), and creative assets.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok-ads-library/ad-details", "ad_id": "1880398616261842"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok-ads-library/ad-details', {'ad_id': '1880398616261842'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok-ads-library/ad-details", {
  "ad_id": "1880398616261842"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok-ads-library/ad-details", sandbase.Params{
	"ad_id": "1880398616261842",
})
```

Same call via the path form: `POST /v1/api/tiktok-ads-library/ad-details` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `lang` | string |  | Language code for the response (e.g. 'en-US', 'fr-FR', 'de-DE') one of: `en-US`, `fr-FR`, `de-DE`; default `"en-US"` |
| `ad_id` | string | yes | The ad ID (from search_ads results, e.g. '1867460299162625')  |

## Details

Get detailed information about a specific ad including advertiser info, targeting (location, age, gender), and creative assets.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "tiktok-ads-library/ad-details", "ad_id": "1880398616261842"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `ad_id` | string | Yes | The ad ID (from search_ads results, e.g. '1867460299162625') |
| `lang` | string | No | Language code for the response (e.g. 'en-US', 'fr-FR', 'de-DE') One of: `en-US`, `fr-FR`, `de-DE`. |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/tiktok-ads-library/ad-details.json`](../../../catalog/models/tiktok-ads-library/ad-details.json) · Store page: https://www.sandbase.ai/model/tiktok-ads-library/ad-details
