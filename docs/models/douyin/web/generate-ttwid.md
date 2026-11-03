# Douyin Web TTWID Generator API: pricing, parameters and code examples

`douyin/web/generate-ttwid` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a Douyin web ttwid cookie value required for web session authentication. Accepts an optional custom user agent string.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/generate-ttwid"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/generate-ttwid', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/generate-ttwid", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/generate-ttwid", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/web/generate-ttwid` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_agent` | string |  | User Agent  |

## Details

Returns a Douyin web `ttwid` cookie value as a single string. The only input is an optional `user_agent` string, so you can call it with an empty body.

### Use cases

- Build a `Cookie` header for Douyin web requests that need a `ttwid` value.
- Replace a `ttwid` cookie in your own client when you start a new session.
- Pair a generated `ttwid` with the same `user_agent` you send in later web requests.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/generate-ttwid" \
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
  "ttwid": "1%7CvTde…"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `ttwid` | The full Douyin web `ttwid` cookie value as a URL-encoded string. Use it as is in a cookie header. |
| `ttwid` | The value has four parts separated by `%7C`, which is an encoded `/`. Keep the separators when you copy the value. |
| `ttwid` | The parts are a short leading number, a token, a 10-digit number, and a long hex string. Treat the whole string as opaque and do not edit it. |

### Notes

- Send `{}` to use the default user agent, or set `user_agent` to match the client headers you use later.
- The response has one key, `ttwid`. Pass its value as the `ttwid` cookie in your next Douyin web request.
- For a different kind of cookie, see [Douyin Web Guest Cookie](/apis/douyin/web/web-guest-cookie).
- To prepare IDs for later calls, use [Douyin Video ID Extractor](/apis/douyin/web/aweme-id) or [Douyin sec_user_id from URL](/apis/douyin/web/sec-user-id).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Batch Video ID Extraction](/apis/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/apis/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/apis/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/generate-ttwid.json`](../../../../catalog/models/douyin/web/generate-ttwid.json) · Store page: https://www.sandbase.ai/model/douyin/web/generate-ttwid
