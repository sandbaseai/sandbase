# TikTok Ads Library Supported Regions API: pricing, parameters and code examples

`tiktok-ads-library/supported-regions` · data API · TikTok Ads Library · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Get the list of supported regions/countries available for filtering in the TikTok Ad Library. Returns European region codes and names that can be passed to search_ads as the region parameter.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok-ads-library/supported-regions"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok-ads-library/supported-regions', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok-ads-library/supported-regions", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok-ads-library/supported-regions", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok-ads-library/supported-regions` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `lang` | string |  | Language code for region name localization (e.g. 'en-US', 'fr-FR', 'de-DE') one of: `en-US`, `fr-FR`, `de-DE`; default `"en-US"` |

## Details

Get the list of supported regions/countries available for filtering in the TikTok Ad Library. Returns European region codes and names that can be passed to search_ads as the region parameter.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "tiktok-ads-library/supported-regions", "lang": "en-US"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `lang` | string | No | Language code for region name localization (e.g. 'en-US', 'fr-FR', 'de-DE') One of: `en-US`, `fr-FR`, `de-DE`. |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/tiktok-ads-library/supported-regions.json`](../../../catalog/models/tiktok-ads-library/supported-regions.json) · Store page: https://www.sandbase.ai/model/tiktok-ads-library/supported-regions
