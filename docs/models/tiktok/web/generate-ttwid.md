# TikTok Web TTWID Identifier

`tiktok/web/generate-ttwid` · api · TikTok

Returns a valid TikTok ttwid cookie value for web session handling. Accepts an optional user_agent string to match specific browser environments.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/generate-ttwid"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/generate-ttwid', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/generate-ttwid", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/generate-ttwid", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok/web/generate-ttwid` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_agent` | string |  | User Agent  |

## Details

Obtain a TikTok web session ttwid cookie. You can optionally supply a custom `user_agent` to match the client environment.

### Use cases

- Acquire a ttwid cookie for authenticating downstream TikTok web queries.
- Configure web scrapers with matching browser user agent identifiers.
- Simulate web client session headers for automated TikTok data collection.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/generate-ttwid" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_agent` | string | No | — |

### Notes

- Supply `user_agent` to align the cookie with your target browser header.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/model/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/model/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/model/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/generate-ttwid.json`](../../../../catalog/models/tiktok/web/generate-ttwid.json) · Store page: https://www.sandbase.ai/model/tiktok/web/generate-ttwid
