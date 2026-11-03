# TikTok WSS X-Bogus Signature API: pricing, parameters and code examples

`tiktok/web/generate-wss-xb-signature` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Generates the X-Bogus signature required for TikTok WebSocket connections. Accepts an optional custom browser user-agent string.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/generate-wss-xb-signature"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/generate-wss-xb-signature', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/generate-wss-xb-signature", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/generate-wss-xb-signature", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok/web/generate-wss-xb-signature` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_agent` | string |  | User browser agent (optional, uses default UA if not provided)  |

## Details

Returns an X-Bogus signature string for TikTok WebSocket (WSS) connections. The only input is an optional `user_agent` string. If you leave it out, the API uses a default browser user agent.

### Use cases

- Sign a TikTok live room WebSocket URL before you open the connection.
- Generate a signature that matches the user agent your own client sends.
- Refresh the signature in a script that reconnects to a TikTok WebSocket listener.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/generate-wss-xb-signature" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_agent` | string | No | User browser agent (optional, uses default UA if not provided) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "x_bogus": "fd9W5SN3j9PxkwTy"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `x_bogus` | The X-Bogus signature string for a TikTok WSS connection. |
| `x_bogus` | In the example, the value is a 16-character string of letters and digits. Treat it as an opaque token and pass it on unchanged. |
| `x_bogus` | The response has no other keys. Read this single value from the top level of the JSON object. |

### Notes

- Send an empty JSON object `{}` to use the default user agent.
- If you pass `user_agent`, use the same string in the headers of your own WebSocket request so the two match.
- For regular web requests instead of WSS, use [TikTok Web X-Bogus Signature](/apis/tiktok/web/generate-xbogus).
- To get both signatures in one call, use [TikTok Web X-Gnarly and X-Bogus Signatures](/apis/tiktok/web/generate-xgnarly-and-xbogus).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/apis/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/apis/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/generate-wss-xb-signature.json`](../../../../catalog/models/tiktok/web/generate-wss-xb-signature.json) · Store page: https://www.sandbase.ai/model/tiktok/web/generate-wss-xb-signature
