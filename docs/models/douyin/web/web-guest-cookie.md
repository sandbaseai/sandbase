# Douyin Web Guest Cookie API: pricing, parameters and code examples

`douyin/web/web-guest-cookie` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a guest cookie for Douyin Web based on a specified browser user agent string. This cookie helps establish identity for browsing web endpoints.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/web-guest-cookie", "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/web-guest-cookie', {'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/web-guest-cookie", {
  "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/web-guest-cookie", sandbase.Params{
	"user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
})
```

Same call via the path form: `POST /v1/api/douyin/web/web-guest-cookie` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_agent` | string | yes | User browser agent  |

## Details

Returns a guest cookie string for Douyin Web, built for the browser user agent you send. The only input is `user_agent`, and the response echoes that user agent back with the cookie.

### Use cases

- Get a guest `Cookie` header to attach to other Douyin Web requests that need a browser identity.
- Pair a cookie and a user agent so repeated web requests use the same browser profile.
- Refresh the guest cookie for a given user agent before running a batch of Douyin Web lookups.
- Test how different browser user agent strings change the cookie you receive.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/web-guest-cookie" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_agent` | string | Yes | User browser agent |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "Cookie": "__ac_non…",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)…"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `Cookie` | A single cookie header string made of `name=value` pairs separated by semicolons. The sample contains pairs named `__ac_nonce`, `__ac_signature`, `__ac_referer` and `web_sign_token`. Send the whole string as the `Cookie` header in Douyin Web requests. |
| `User-Agent` | The user agent string the cookie was issued for. It matches the `user_agent` you sent. Use the same value as the `User-Agent` header in later requests. |

### Notes

- Send a real browser user agent string in `user_agent`, such as a current Chrome string. Reuse the same string in later requests that use this cookie.
- The `Cookie` value is long and the sample here is cut short. Store the full string as returned.
- To get a signed identity token for other Douyin Web calls, see [Douyin Web TTWID Generator](/apis/douyin/web/generate-ttwid).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Batch Video ID Extraction](/apis/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/apis/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/apis/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/web-guest-cookie.json`](../../../../catalog/models/douyin/web/web-guest-cookie.json) · Store page: https://www.sandbase.ai/model/douyin/web/web-guest-cookie
