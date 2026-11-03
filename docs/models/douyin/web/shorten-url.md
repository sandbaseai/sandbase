# Douyin URL Shortener API: pricing, parameters and code examples

`douyin/web/shorten-url` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Shortens a target web address for Douyin web workflows. Accepts a full destination link and returns a compact shortened URL.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/shorten-url", "target_url": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/shorten-url', {'target_url': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/shorten-url", {
  "target_url": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/shorten-url", sandbase.Params{
	"target_url": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/web/shorten-url` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `target_url` | string | yes | Target URL to be converted  |

## Details

Convert standard web links into shortened Douyin links using the required `target_url` parameter.

### Use cases

- Generating compact URLs for sharing Douyin links across external channels.
- Formatting long web addresses into clean, shareable Douyin links.
- Preparing concise links for display in space-constrained user interfaces.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/shorten-url" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"target_url": "https://www.douyin.com/video/7575136499386720761"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `target_url` | string | Yes | Target URL to be converted |

### Notes

- The `target_url` parameter requires the full destination address to convert.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Batch Video ID Extraction](/apis/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/apis/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/apis/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/shorten-url.json`](../../../../catalog/models/douyin/web/shorten-url.json) · Store page: https://www.sandbase.ai/model/douyin/web/shorten-url
