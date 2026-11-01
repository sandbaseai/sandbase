# TikTok WSS X-Bogus Signature

`tiktok/web/generate-wss-xb-signature` · api · TikTok

Generates the X-Bogus signature required for TikTok WebSocket connections. Accepts an optional custom browser user-agent string.

## Pricing

- **$0.0015 per call** (USD)
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

Retrieve an X-Bogus signature needed for TikTok WSS connections. You can optionally supply `user_agent` to match a specific client environment.

### Use cases

- Establish real-time TikTok WebSocket connections requiring signature verification.
- Provide custom user agent strings to match client request headers.
- Authenticate automated listeners for TikTok web stream events.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/generate-wss-xb-signature" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_agent` | string | No | User browser agent (optional, uses default UA if not provided) |

### Notes

- Uses a default user agent string if `user_agent` is omitted.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/model/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/model/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/model/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/generate-wss-xb-signature.json`](../../../../catalog/models/tiktok/web/generate-wss-xb-signature.json) · Store page: https://www.sandbase.ai/model/tiktok/web/generate-wss-xb-signature
