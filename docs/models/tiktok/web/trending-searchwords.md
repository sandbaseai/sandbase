# TikTok Daily Trending Search Words API: pricing, parameters and code examples

`tiktok/web/trending-searchwords` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns daily trending search terms and keywords from TikTok Web. Use this endpoint to monitor popular search queries and emerging platform topics.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/trending-searchwords"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/trending-searchwords', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/trending-searchwords", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/trending-searchwords", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok/web/trending-searchwords` with the body above minus `model`.

## Details

Returns current daily trending search words on TikTok Web without requiring any request parameters. Use this data to track popular search queries across the platform.

### Use cases

- Discover popular search terms and topics currently trending on TikTok.
- Analyze query popularity shifts to inform content strategy.
- Monitor emerging search patterns across TikTok Web.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/trending-searchwords" \
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
Machine-readable: [`catalog/models/tiktok/web/trending-searchwords.json`](../../../../catalog/models/tiktok/web/trending-searchwords.json) · Store page: https://www.sandbase.ai/model/tiktok/web/trending-searchwords
