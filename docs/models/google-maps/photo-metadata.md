# Google Maps Photo Metadata API: pricing, parameters and code examples

`google-maps/photo-metadata` · data API · Google Maps · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00015 per call (free daily quota) · **Modes:** sync

Contributor, place, coordinates, type and date of one Google Maps photo by its data ID.

## Pricing

- **$0.00015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google-maps/photo-metadata", "data_id": "CIABIhAAQr6KrxiC_knILBjf2RxL"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google-maps/photo-metadata', {'data_id': 'CIABIhAAQr6KrxiC_knILBjf2RxL'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google-maps/photo-metadata", {
  "data_id": "CIABIhAAQr6KrxiC_knILBjf2RxL"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google-maps/photo-metadata", sandbase.Params{
	"data_id": "CIABIhAAQr6KrxiC_knILBjf2RxL",
})
```

Same call via the path form: `POST /v1/api/google-maps/photo-metadata` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `gl` | string |  | Two-letter country code used to localize results.  |
| `hl` | string |  | Language code such as en, en-GB, or de. default `"en"` |
| `data_id` | string | yes | Required Google Maps photo ID. Follow a photo_meta_link from a Google Maps place response or copy the nested photo data_id.  |
| `timeout` | number |  | Optional budget for the entire request in seconds, measured from gateway receipt until the response is ready to send. Includes admission, queueing and settlement. Must be greater than 0 and at most 90. On expiry, the…  |
| `google_domain` | string |  | Google domain used for the request. default `"google.com"` |

## Details

Contributor, place, coordinates, type and date of one Google Maps photo by its data ID.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google-maps/photo-metadata" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"data_id": "CIABIhAAQr6KrxiC_knILBjf2RxL"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `data_id` | string | Yes | Required Google Maps photo ID. Follow a photo_meta_link from a Google Maps place response or copy the nested photo data_id. |
| `gl` | string | No | Two-letter country code used to localize results. |
| `google_domain` | string | No | Google domain used for the request. |
| `hl` | string | No | Language code such as en, en-GB, or de. |
| `timeout` | number | No | Optional budget for the entire request in seconds, measured from gateway receipt until the response is ready to send. Includes admission, queueing and settlement. Must be greater t |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/google-maps/photo-metadata.json`](../../../catalog/models/google-maps/photo-metadata.json) · Store page: https://www.sandbase.ai/model/google-maps/photo-metadata
