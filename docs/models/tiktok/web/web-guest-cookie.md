# TikTok Web Guest Cookie API: pricing, parameters and code examples

`tiktok/web/web-guest-cookie` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Returns guest session cookies for TikTok Web based on a specified browser user agent string. Helps maintain session identity when querying web-based TikTok data.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/web-guest-cookie", "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:145.0) Gecko/20100101 Firefox/145.0"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/web-guest-cookie', {'user_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:145.0) Gecko/20100101 Firefox/145.0'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/web-guest-cookie", {
  "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:145.0) Gecko/20100101 Firefox/145.0"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/web-guest-cookie", sandbase.Params{
	"user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:145.0) Gecko/20100101 Firefox/145.0",
})
```

Same call via the path form: `POST /v1/api/tiktok/web/web-guest-cookie` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_agent` | string | yes | User browser agent  |

## Details

Returns a set of guest session headers for TikTok Web: a `Cookie` string, a `Referer` URL and the `User-Agent` you sent. It needs one input, a browser `user_agent` string.

### Use cases

- Build a cookie header for guest requests to TikTok Web endpoints.
- Pair a cookie with a chosen browser `user_agent` so both headers match across requests.
- Fetch fresh guest cookies at the start of a scraping job that reads public TikTok data.
- Copy the returned `Referer` and `User-Agent` into your own HTTP client along with the cookie.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/web-guest-cookie" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:145.0) Gecko/20100101 Firefox/145.0"}'
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
  "Cookie": "tt_csrf_…",
  "Referer": "https://www.tiktok.com/explore",
  "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:145.0) Gecko/20100101 Firefox/1…"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `Cookie` | Full cookie string for a guest session, ready to use as a `Cookie` header. It holds several name=value pairs separated by semicolons, including `tt_csrf_token` and `ttwid`. |
| `Referer` | Referer URL to send with requests, here `https://www.tiktok.com/explore`. |
| `User-Agent` | The browser user agent string the cookie was issued for. It matches the `user_agent` you sent. |

### Notes

- Send the same `User-Agent` value in your later requests that you passed in `user_agent` here.
- The `Cookie` value is a single string. Use it as is in the `Cookie` header.
- For a standalone `ttwid` value, call [TikTok Web TTWID Identifier](/apis/tiktok/web/generate-ttwid).
- To sign web requests, see [TikTok Web X-Bogus Signature](/apis/tiktok/web/generate-xbogus).

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/apis/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/apis/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/web-guest-cookie.json`](../../../../catalog/models/tiktok/web/web-guest-cookie.json) · Store page: https://www.sandbase.ai/model/tiktok/web/web-guest-cookie
