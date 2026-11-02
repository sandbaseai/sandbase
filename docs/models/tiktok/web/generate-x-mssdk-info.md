# TikTok Web X-Mssdk-Info Tokens API: pricing, parameters and code examples

`tiktok/web/generate-x-mssdk-info` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Generates X-Mssdk-Info and X-Mssdk-RC values for TikTok Web authentication scenarios, accepting an optional user agent string.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/generate-x-mssdk-info"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/generate-x-mssdk-info', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/generate-x-mssdk-info", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/generate-x-mssdk-info", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok/web/generate-x-mssdk-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_agent` |  |  | The User-Agent string used  |

## Details

Returns X-Mssdk-Info and X-Mssdk-RC security parameters for TikTok Web operations. You can optionally pass a custom `user_agent` string.

### Use cases

- Register TikTok Web devices securely.
- Handle TikTok Web login and authentication flows.
- Produce required security headers for TikTok Web requests.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/generate-x-mssdk-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_agent` | string | No | The User-Agent string used |

### Notes

- Accepts an optional `user_agent` parameter matching the target client environment.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/model/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/model/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/model/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/generate-x-mssdk-info.json`](../../../../catalog/models/tiktok/web/generate-x-mssdk-info.json) · Store page: https://www.sandbase.ai/model/tiktok/web/generate-x-mssdk-info
