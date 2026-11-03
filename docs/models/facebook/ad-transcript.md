# Facebook Ad Transcript API: pricing, parameters and code examples

`facebook/ad-transcript` · data API · Facebook · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

Get the spoken-word transcript of a Meta Ad Library video ad by ad ID or URL.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "facebook/ad-transcript"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('facebook/ad-transcript', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("facebook/ad-transcript", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "facebook/ad-transcript", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/facebook/ad-transcript` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string |  | Meta Ad Library ad ID (e.g. "1020359190509080"). Provide either id or url.  |
| `url` | string |  | Meta Ad Library ad URL (e.g. "https://www.facebook.com/ads/library?id=1020359190509080"). Provide either id or url.  |

## Details

This API returns the spoken-word transcript of a video ad in the Meta Ad Library. It needs either an ad ID (`id`) or an Ad Library ad URL (`url`).

### Use cases

- Pull the script of a competitor's video ad to study its hook and offer.
- Index ad transcripts to search for repeated claims or phrases across campaigns.
- Check whether a video ad has a transcript before sending it to a review or translation step.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/facebook/ad-transcript" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"id": "2045879599391945"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string | No | Meta Ad Library ad ID (e.g. "1020359190509080"). Provide either id or url. |
| `url` | string | No | Meta Ad Library ad URL (e.g. "https://www.facebook.com/ads/library?id=1020359190509080"). Provide either id or url. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "adId": "2045879599391945",
    "transcript": "",
    "transcriptAvailable": false,
    "url": "https://www.facebook.com/ads/library?id=2045879599391945"
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.adId` | The ID of the ad that was looked up. |
| `data.transcript` | The spoken-word text of the ad. It is an empty string when no transcript exists. |
| `data.transcriptAvailable` | `true` when a transcript was found for the ad, `false` when not. Check this before you use `transcript`. |
| `data.url` | The Meta Ad Library URL for the ad. |
| `found` | `true` when the lookup returned a result for the ad. |

### Notes

- Send either `id` or `url`. The `id` is the number in the `id` query parameter of an Ad Library URL, for example `2045879599391945`.
- A response can have `found: true` and still return an empty `transcript` with `transcriptAvailable: false`. Treat this as an ad with no transcript.
- To find ad IDs, use [Facebook Ad Search](/apis/facebook/ads-search) or [Facebook Company Ads](/apis/facebook/company-ads). For ad creative data, call [Facebook Ad Creative Details](/apis/facebook/ad-details-full).

### Pricing

Billed at the actual cost of each call, about $0.0012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/facebook/ad-transcript.json`](../../../catalog/models/facebook/ad-transcript.json) · Store page: https://www.sandbase.ai/model/facebook/ad-transcript
