# TikTok Web X-Gnarly Signature

`tiktok/web/generate-xgnarly` · api · TikTok

Returns generated X-Gnarly signature values for TikTok web requests based on a target endpoint URL and optional request body data.

## Pricing

- **$0.003 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/generate-xgnarly", "url": "https://www.tiktok.com/tag/cat?_r=1&name=cat&u_code=f02lm2f78d1elh&_d=f02ll161mcjihj&share_challenge_id=7551&sharer_language=en&source=h5_m"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/generate-xgnarly', {'url': 'https://www.tiktok.com/tag/cat?_r=1&name=cat&u_code=f02lm2f78d1elh&_d=f02ll161mcjihj&share_challenge_id=7551&sharer_language=en&source=h5_m'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/generate-xgnarly", {
  "url": "https://www.tiktok.com/tag/cat?_r=1&name=cat&u_code=f02lm2f78d1elh&_d=f02ll161mcjihj&share_challenge_id=7551&sharer_language=en&source=h5_m"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/generate-xgnarly", sandbase.Params{
	"url": "https://www.tiktok.com/tag/cat?_r=1&name=cat&u_code=f02lm2f78d1elh&_d=f02ll161mcjihj&share_challenge_id=7551&sharer_language=en&source=h5_m",
})
```

Same call via the path form: `POST /v1/api/tiktok/web/generate-xgnarly` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | The requested API URL, no need to URL encode  |
| `body` |  |  | The API parameters of the request, applicable for POST requests  |

## Details

Call this endpoint with a target `url` and optional `body` payload to generate X-Gnarly signature values for TikTok web requests.

### Use cases

- Sign web requests directed at TikTok endpoints.
- Automate security signature generation for TikTok web calls.
- Prepare valid request parameters for operations with payload data.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/generate-xgnarly" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.tiktok.com/tag/cat?_r=1&name=cat&u_code=f02lm2f78d1elh&_d=f02ll161mcjihj&share_challenge_id=7551&sharer_language=en&source=h5_m"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | The requested API URL, no need to URL encode |
| `body` | string | No | The API parameters of the request, applicable for POST requests |

### Notes

- Provide the target `url` without URL encoding.
- The `body` parameter is applicable when signing POST requests.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/model/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/model/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/model/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/generate-xgnarly.json`](../../../../catalog/models/tiktok/web/generate-xgnarly.json) · Store page: https://www.sandbase.ai/model/tiktok/web/generate-xgnarly
