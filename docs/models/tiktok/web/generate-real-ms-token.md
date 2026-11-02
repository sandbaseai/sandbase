# TikTok Real msToken API: pricing, parameters and code examples

`tiktok/web/generate-real-ms-token` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Produces a real msToken for TikTok web requests. Accepts optional configuration parameters including browser type and randomized string data.

## Pricing

- **$0.0015 per call** (USD)
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

This endpoint produces a real msToken for TikTok web interactions. It accepts optional parameters including `browser_type` and `random_strData`.

### Use cases

- Authenticating downstream TikTok web requests with a valid token
- Simulating specific browser environments using browser type settings
- Producing randomized token payloads for web sessions

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/generate-real-ms-token" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `browser_type` | string | No | — |
| `random_strData` | boolean | No | — |

### Notes

- Set `browser_type` to specify the target browser environment.
- Toggle `random_strData` to enable or disable randomized string data.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/model/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/model/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/model/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/generate-real-ms-token.json`](../../../../catalog/models/tiktok/web/generate-real-ms-token.json) · Store page: https://www.sandbase.ai/model/tiktok/web/generate-real-ms-token
