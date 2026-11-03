# TikTok Web X-Gnarly and X-Bogus Signatures API: pricing, parameters and code examples

`tiktok/web/generate-xgnarly-and-xbogus` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.005 per call (free daily quota) · **Modes:** sync

Generates X-Gnarly and X-Bogus signature tokens for TikTok web requests using a target endpoint URL and optional request body parameters.

## Pricing

- **$0.005 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/generate-xgnarly-and-xbogus", "url": "https://www.tiktok.com/tag/cat?_r=1&name=cat&u_code=f02lm2f78d1elh&_d=f02ll161mcjihj&share_challenge_id=7551&sharer_language=en&source=h5_m"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/generate-xgnarly-and-xbogus', {'url': 'https://www.tiktok.com/tag/cat?_r=1&name=cat&u_code=f02lm2f78d1elh&_d=f02ll161mcjihj&share_challenge_id=7551&sharer_language=en&source=h5_m'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/generate-xgnarly-and-xbogus", {
  "url": "https://www.tiktok.com/tag/cat?_r=1&name=cat&u_code=f02lm2f78d1elh&_d=f02ll161mcjihj&share_challenge_id=7551&sharer_language=en&source=h5_m"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/generate-xgnarly-and-xbogus", sandbase.Params{
	"url": "https://www.tiktok.com/tag/cat?_r=1&name=cat&u_code=f02lm2f78d1elh&_d=f02ll161mcjihj&share_challenge_id=7551&sharer_language=en&source=h5_m",
})
```

Same call via the path form: `POST /v1/api/tiktok/web/generate-xgnarly-and-xbogus` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | The requested API URL, no need to URL encode  |
| `body` |  |  | The API parameters of the request, applicable for POST requests  |

## Details

Returns signature tokens for a TikTok web request. You send the full target `url`, and optionally a `body` string for POST requests. The response contains `xGnarly`, `xBogus`, `xDynosaur`, and a `signedUrl`.

### Use cases

- Sign a TikTok tag page URL before you request it from your own HTTP client.
- Get an `xGnarly` value to attach to a TikTok web request that needs it.
- Build a signed POST request by passing the request parameters in `body`.
- Reuse the returned `user_agent` so your signed request uses the same browser string.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/generate-xgnarly-and-xbogus" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.tiktok.com/tag/cat?_r=1&name=cat&u_code=f02lm2f78d1elh&_d=f02ll161mcjihj&share_challenge_id=7551&sharer_language=en&source=h5_m"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | The requested API URL, no need to URL encode |
| `body` | string | No | The API parameters of the request, applicable for POST requests |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "body": "",
  "signature": {
    "signedUrl": "https://www.tiktok.com/tag/cat?_r=1&name=cat&u_code=f02lm2f78d1elh&_d=f02ll161mc…",
    "xBogus": "1",
    "xDynosaur": "MaFdT8S5zzDCNu2FdzJoSPebgrTnVCKYHQQuRjpE8iRm1-MxvNak5hedfIyt4/NiDVBNySaJIg6kfva0…",
    "xGnarly": "MaTjg74vTVfgmm0vW/dwPfk43OgEtyKRP28T6NjvhZPZhZ9JI-9WdjukhjSDmoIRoEMljTcYD8oyJ4gE…"
  },
  "status": "success",
  "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:146.0) Gecko/20100101 Firefox/1…",
  "version": "5.3.2"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `signature.signedUrl` | The input `url` with the signature parameters added, such as `X-Dynosaur`. You can use it as the request URL. |
| `signature.xGnarly` | The X-Gnarly token generated for the given `url`. |
| `signature.xBogus` | The X-Bogus value for the given `url`. In this sample it is `1`, so check it before you rely on it. |
| `signature.xDynosaur` | The X-Dynosaur token. The `signedUrl` carries this same value as a query parameter. |
| `body` | The body string used for signing. It is empty when you send no `body`. |
| `user_agent` | The browser user agent string used when the signatures were made. Send the same value in your request headers. |
| `version` | The version string of the signing logic, here `5.3.2`. |
| `status` | Result of the call. A successful call returns `success`. |

### Notes

- Pass `url` as a plain string. You do not need to URL encode it.
- Set `body` only for POST requests. Leave it out for GET requests.
- Send the returned `user_agent` with your signed request so the headers match the signature.
- For single-token needs, see [TikTok Web X-Gnarly Signature](/apis/tiktok/web/generate-xgnarly) or [TikTok Web X-Bogus Signature](/apis/tiktok/web/generate-xbogus).

### Pricing

$0.005 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/apis/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/apis/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/generate-xgnarly-and-xbogus.json`](../../../../catalog/models/tiktok/web/generate-xgnarly-and-xbogus.json) · Store page: https://www.sandbase.ai/model/tiktok/web/generate-xgnarly-and-xbogus
