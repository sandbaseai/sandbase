# Google Play App Search API: pricing, parameters and code examples

`google-play/apps` · data API · Google Play · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00015 per call (free daily quota) · **Modes:** sync

Search Google Play apps by keyword or browse categories and top charts, with rating, price and developer.

## Pricing

- **$0.00015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google-play/apps"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google-play/apps', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google-play/apps", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google-play/apps", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/google-play/apps` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string |  | At most 2,048 UTF-8 bytes.  |
| `gl` | string |  | Two-letter country code. default `"us"` |
| `hl` | string |  | Storefront language, such as en, de, or zh-TW. Maximum 32 characters. default `"en"` |
| `age` | string |  | Children's age range. Requires apps_category=FAMILY. one of: `AGE_RANGE1`, `AGE_RANGE2`, `AGE_RANGE3` |
| `chart` | string |  | Chart identifier such as topselling_free, topselling_paid, or topgrossing. Excludes q and all pagination selectors. Apps and games charts require phone or an omitted store_device.  |
| `timeout` | number |  | Optional budget for the entire request in seconds, measured from gateway receipt until the response is ready to send. Includes admission, queueing and settlement. Must be greater than 0 and at most 90. On expiry, the…  |
| `store_device` | string |  | Omit for the default phone storefront. An explicit selection excludes q and category. one of: `phone`, `tablet`, `tv`, `chromebook`, `watch`, `car` |
| `apps_category` | string |  | Native app category identifier, such as MEDICAL. Excludes q and an explicit store_device.  |
| `see_more_token` | string |  | Open a result collection using its returned token and the same parameters. Excludes the other pagination selectors and chart.  |
| `next_page_token` | string |  | Use the returned next_page_token with the same parameters. Excludes chart, section_page_token, and see_more_token.  |
| `section_page_token` | string |  | Continue one result group using its returned token and the same parameters. Excludes the other pagination selectors and chart.  |

## Details

Search Google Play apps by keyword or browse categories and top charts, with rating, price and developer.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google-play/apps" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "Duolingo"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `age` | string | No | Children's age range. Requires apps_category=FAMILY. |
| `apps_category` | string | No | Native app category identifier, such as MEDICAL. Excludes q and an explicit store_device. |
| `chart` | string | No | Chart identifier such as topselling_free, topselling_paid, or topgrossing. Excludes q and all pagination selectors. Apps and games charts require phone or an omitted store_device. |
| `gl` | string | No | Two-letter country code. |
| `hl` | string | No | Storefront language, such as en, de, or zh-TW. Maximum 32 characters. |
| `next_page_token` | string | No | Use the returned next_page_token with the same parameters. Excludes chart, section_page_token, and see_more_token. |
| `q` | string | No | At most 2,048 UTF-8 bytes. |
| `section_page_token` | string | No | Continue one result group using its returned token and the same parameters. Excludes the other pagination selectors and chart. |
| `see_more_token` | string | No | Open a result collection using its returned token and the same parameters. Excludes the other pagination selectors and chart. |
| `store_device` | string | No | Omit for the default phone storefront. An explicit selection excludes q and category. |
| `timeout` | number | No | Optional budget for the entire request in seconds, measured from gateway receipt until the response is ready to send. Includes admission, queueing and settlement. Must be greater t |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/google-play/apps.json`](../../../catalog/models/google-play/apps.json) · Store page: https://www.sandbase.ai/model/google-play/apps
