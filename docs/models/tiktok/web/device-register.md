# TikTok Web Device Registration API: pricing, parameters and code examples

`tiktok/web/device-register` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.003 per call (free daily quota) · **Modes:** sync

Registers a virtual client session to generate a device ID and guest cookie for TikTok Web requests. Returns device tokens and session parameters.

## Pricing

- **$0.003 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/device-register"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/device-register', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/device-register", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/device-register", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok/web/device-register` with the body above minus `model`.

## Details

Generates a fresh device identifier and guest session cookies for TikTok Web without requiring any input parameters.

### Use cases

- Initialize new web sessions for TikTok data scraping workflows.
- Obtain guest cookies needed to query TikTok Web endpoints.
- Acquire a registered device ID for subsequent web requests.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/device-register" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/model/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/model/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/model/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/device-register.json`](../../../../catalog/models/tiktok/web/device-register.json) · Store page: https://www.sandbase.ai/model/tiktok/web/device-register
