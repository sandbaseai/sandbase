# TikTok Web ID API: pricing, parameters and code examples

`tiktok/web/generate-webid` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a TikTok web_id value for web session handling. Accepts optional parameters including url, app_id, referer, user_agent, and user_unique_id.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/generate-webid"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/generate-webid', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/generate-webid", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/generate-webid", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok/web/generate-webid` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string |  | Url  |
| `app_id` | integer |  | App Id  |
| `referer` | string |  | Referer  |
| `user_agent` | string |  | User Agent  |
| `user_unique_id` | string |  | User Unique Id  |

## Details

Returns a TikTok `web_id` string for use in web session handling, along with a `user_agent` string. All inputs are optional, and an empty request returns a value.

### Use cases

- Get a `web_id` to attach to TikTok web requests that need a session identifier.
- Pass your own `user_agent` or `referer` to build a web session that matches the browser you simulate.
- Pass a `user_unique_id` to tie the generated ID to one browser context in your own tooling.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/generate-webid" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `app_id` | integer | No |  |
| `referer` | string | No |  |
| `url` | string | No |  |
| `user_agent` | string | No |  |
| `user_unique_id` | string | No |  |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "e": 0,
  "ssid": "un_support",
  "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:145.0) Gecko/20100101 Firefox/1…",
  "web_id": "7703847884642567693"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `web_id` | The generated TikTok web ID, returned as a string of digits. |
| `user_agent` | The browser user agent string returned with the ID. Reuse it in later web requests so the session stays consistent. |
| `ssid` | A session value. The sample returns `un_support`, so do not rely on it. |
| `e` | A status code. The sample returns `0`. |

### Notes

- All parameters are optional: `url`, `app_id`, `referer`, `user_agent` and `user_unique_id`. The sample request sent none of them.
- Treat `web_id` as a string. It is a long number and can lose digits if you parse it as a number.
- Pair this with [TikTok Web TTWID Identifier](/apis/tiktok/web/generate-ttwid) or [TikTok Real msToken](/apis/tiktok/web/generate-real-ms-token) when you need other session values.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/apis/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/apis/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/generate-webid.json`](../../../../catalog/models/tiktok/web/generate-webid.json) · Store page: https://www.sandbase.ai/model/tiktok/web/generate-webid
