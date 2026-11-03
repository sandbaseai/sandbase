# TikTok Web X-Gnarly Signature API: pricing, parameters and code examples

`tiktok/web/generate-xgnarly` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Returns generated X-Gnarly signature values for TikTok web requests based on a target endpoint URL and optional request body data.

## Pricing

- **$0.002 per call** (USD)
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

Returns signature values for a TikTok web request, including `xGnarly`, `xBogus` and `xDynosaur`, plus a signed copy of the URL. It needs the full request `url` and an optional `body` string for POST requests.

### Use cases

- Sign a TikTok web endpoint URL before you send the request yourself.
- Get the `xGnarly` value to attach to a request that needs it.
- Sign a POST request by passing its parameters in `body`.
- Reuse the returned `user_agent` so your request headers match the signature.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/generate-xgnarly" \
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
    "xDynosaur": "MwDqFZsDyJz0WUQqmwWXyw3eVqiiAocN4i8HrXlDijQD7wFNRr2Tz5/6YUbiz4AE3BgF2bNXJHozDynN…",
    "xGnarly": "MkD6M/0-wSOgEHM72xx9Pmya70CI67jZFmlC6-SUgWujQf0-x/rRdQxOIvXBvWjzh0hCieJoa1YfSSWb…"
  },
  "status": "success",
  "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:146.0) Gecko/20100101 Firefox/1…",
  "version": "5.3.2"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `signature.xGnarly` | The X-Gnarly signature value generated for the given `url`. |
| `signature.xBogus` | The X-Bogus value for the same request. It is `1` in this example. |
| `signature.xDynosaur` | The X-Dynosaur value generated for the request. |
| `signature.signedUrl` | The input `url` with the `X-Dynosaur` parameter appended as a query parameter. |
| `body` | The request body that was signed. It is an empty string when you send no `body`. |
| `user_agent` | The browser User-Agent string the signature was generated with. |
| `version` | The version string of the signing logic, for example `5.3.2`. |
| `status` | Whether the call worked. A good call returns `success`. |

### Notes

- Send `url` as plain text. You do not need to URL encode it.
- Set `body` only for POST requests. Leave it out for GET requests.
- To get both `xGnarly` and `xBogus` in one call, use [TikTok Web X-Gnarly and X-Bogus Signatures](/apis/tiktok/web/generate-xgnarly-and-xbogus).
- To get only the X-Bogus value, use [TikTok Web X-Bogus Signature](/apis/tiktok/web/generate-xbogus).

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/apis/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/apis/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/generate-xgnarly.json`](../../../../catalog/models/tiktok/web/generate-xgnarly.json) · Store page: https://www.sandbase.ai/model/tiktok/web/generate-xgnarly
