# TikTok Web TTWID Identifier API: pricing, parameters and code examples

`tiktok/web/generate-ttwid` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a valid TikTok ttwid cookie value for web session handling. Accepts an optional user_agent string to match specific browser environments.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/generate-ttwid"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/generate-ttwid', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/generate-ttwid", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/generate-ttwid", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok/web/generate-ttwid` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_agent` | string |  | User Agent  |

## Details

Returns a TikTok `ttwid` cookie value as a single string. The only input is an optional `user_agent` string, so you can call it with an empty body.

### Use cases

- Set the `ttwid` cookie on a web client before it sends requests to TikTok web endpoints.
- Pair the cookie with a specific browser `user_agent` so your request headers stay consistent.
- Fetch a new cookie value when a scraper needs a fresh web session identity.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/generate-ttwid" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_agent` | string | No |  |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "ttwid": "1%7C0K27…"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `ttwid` | The full cookie value as a URL-encoded string. Send it as `ttwid=<value>` in a `Cookie` header. |
| `ttwid` | The value has four segments separated by `%7C`, which decodes to `/`. The segments are `1`, a short token, a 10-digit number, and a 64-character hex string. |
| `ttwid` | The 10-digit third segment looks like a Unix timestamp in seconds. The response does not say if it marks creation or expiry. |

### Notes

- Send `{}` to get a cookie with no `user_agent`. Add `user_agent` to match a specific browser string.
- The value is already URL-encoded. Use it as is, without encoding it again.
- Related tokens for TikTok web requests: [TikTok Web ID](/apis/tiktok/web/generate-webid), [TikTok Real msToken](/apis/tiktok/web/generate-real-ms-token) and [TikTok Web X-Bogus Signature](/apis/tiktok/web/generate-xbogus).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/apis/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/apis/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/generate-ttwid.json`](../../../../catalog/models/tiktok/web/generate-ttwid.json) · Store page: https://www.sandbase.ai/model/tiktok/web/generate-ttwid
