# TikTok Web X-Bogus Signature API: pricing, parameters and code examples

`tiktok/web/generate-xbogus` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a signed TikTok Web request URL containing the required X-Bogus token. The endpoint takes an unsigned target API URL and a browser User-Agent string.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/generate-xbogus", "url": "https://www.tiktok.com/tag/cat?_r=1&name=cat&u_code=f02lm2f78d1elh&_d=f02ll161mcjihj&share_challenge_id=7551&sharer_language=en&source=h5_m", "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:145.0) Gecko/20100101 Firefox/145.0"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/generate-xbogus', {'url': 'https://www.tiktok.com/tag/cat?_r=1&name=cat&u_code=f02lm2f78d1elh&_d=f02ll161mcjihj&share_challenge_id=7551&sharer_language=en&source=h5_m', 'user_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:145.0) Gecko/20100101 Firefox/145.0'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/generate-xbogus", {
  "url": "https://www.tiktok.com/tag/cat?_r=1&name=cat&u_code=f02lm2f78d1elh&_d=f02ll161mcjihj&share_challenge_id=7551&sharer_language=en&source=h5_m",
  "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:145.0) Gecko/20100101 Firefox/145.0"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/generate-xbogus", sandbase.Params{
	"url": "https://www.tiktok.com/tag/cat?_r=1&name=cat&u_code=f02lm2f78d1elh&_d=f02ll161mcjihj&share_challenge_id=7551&sharer_language=en&source=h5_m",
	"user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:145.0) Gecko/20100101 Firefox/145.0",
})
```

Same call via the path form: `POST /v1/api/tiktok/web/generate-xbogus` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Unsigned API URL  |
| `user_agent` | string | yes | User browser User-Agent  |

## Details

Generate the `X-Bogus` signature for a TikTok web request URL and user agent. TikTok's web endpoints reject unsigned requests; the signature is appended to the query string as `X-Bogus=<value>`.

### Use cases

- Sign requests when you call TikTok web endpoints from your own crawler.
- Debug why a captured TikTok web request fails after its parameters change.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/generate-xbogus" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.tiktok.com/tag/cat?_r=1&name=cat&u_code=f02lm2f78d1elh&_d=f02ll161mcjihj&share_challenge_id=7551&sharer_language=en&source=h5_m", "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:145.0) Gecko/20100101 Firefox/145.0"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Unsigned API URL |
| `user_agent` | string | Yes | User browser User-Agent |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "url": "https://www.tiktok.com/tag/cat?_r=1&name=cat&u_code=f02lm2f78d1elh&_d=f02ll161mc…",
  "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:145.0) Gecko/20100101 Firefox/1…",
  "x_bogus": "DFSzswVY8ZXANGnECXHeqM9WX7nO"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `x_bogus` | The signature to append as `&X-Bogus=<value>`. |
| `url / user_agent` | The inputs, echoed back. |

### Notes

- The signature is bound to the exact query string and user agent: send requests with the same user agent you signed with, and sign again after changing any parameter.
- Pair it with [TikTok Device Register](/apis/tiktok/web/device-register) to get a matching device ID and cookie.

### Pricing

$0.001 per successful call. Failed calls, including lookups whose target does not exist, are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/apis/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/apis/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/generate-xbogus.json`](../../../../catalog/models/tiktok/web/generate-xbogus.json) · Store page: https://www.sandbase.ai/model/tiktok/web/generate-xbogus
