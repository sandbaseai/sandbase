# TikTok Real msToken API: pricing, parameters and code examples

`tiktok/web/generate-real-ms-token` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Produces a real msToken for TikTok web requests. Accepts optional configuration parameters including browser type and randomized string data.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/generate-real-ms-token"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/generate-real-ms-token', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/generate-real-ms-token", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/generate-real-ms-token", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok/web/generate-real-ms-token` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `browser_type` | string |  | Browser Type  |
| `random_strData` | boolean |  | Random Strdata  |

## Details

This API returns a real `msToken` string for TikTok web requests. It needs no input, but you can pass `browser_type` and `random_strData` to change how the token is made.

### Use cases

- Add a fresh `msToken` to TikTok web requests that need one as a query parameter or cookie.
- Request a token for a specific browser type by setting `browser_type`.
- Test how `random_strData` changes the token you get back.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/generate-real-ms-token" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `browser_type` | string | No |  |
| `random_strData` | boolean | No |  |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "browser_type": null,
  "msToken": "DFJLzkge…",
  "random_strData": false
}
```

### Response fields

| Field | Meaning |
|---|---|
| `msToken` | The generated token string. Pass this value as the `msToken` in your TikTok web requests. |
| `browser_type` | Echoes the `browser_type` you sent. It is `null` when you leave the parameter out. |
| `random_strData` | Echoes the `random_strData` flag you sent. It is `false` in the sample call, where the parameter was not set. |

### Notes

- Both parameters are optional. An empty `{}` body returns a token.
- `browser_type` is a string and `random_strData` is a boolean.
- The token contains letters, digits, `-` and `_`. Copy it as is without extra encoding changes.
- For signed requests, pair the token with [TikTok Web X-Bogus Signature](/apis/tiktok/web/generate-xbogus) or [TikTok Web TTWID Identifier](/apis/tiktok/web/generate-ttwid).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/apis/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/apis/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/generate-real-ms-token.json`](../../../../catalog/models/tiktok/web/generate-real-ms-token.json) · Store page: https://www.sandbase.ai/model/tiktok/web/generate-real-ms-token
