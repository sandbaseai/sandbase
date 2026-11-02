# Douyin sec_user_id from URL API: pricing, parameters and code examples

`douyin/web/sec-user-id` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Extracts the Douyin sec_user_id identifier from a provided web link or profile URL. Input the target link in the query parameter to resolve the user identifier.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/sec-user-id", "url": "https://www.douyin.com/video/7691553968815623478"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/sec-user-id', {'url': 'https://www.douyin.com/video/7691553968815623478'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/sec-user-id", {
  "url": "https://www.douyin.com/video/7691553968815623478"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/sec-user-id", sandbase.Params{
	"url": "https://www.douyin.com/video/7691553968815623478",
})
```

Same call via the path form: `POST /v1/api/douyin/web/sec-user-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Url  |

## Details

Resolve a Douyin user security identifier by providing a web link via the `url` parameter. This endpoint parses the input link and returns the corresponding user identifier.

### Use cases

- Resolve a Douyin user sec_user_id from a shared profile link.
- Convert profile web URLs into stable user identifiers for downstream queries.
- Automate profile identity extraction from Douyin web links.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/sec-user-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.douyin.com/video/7691553968815623478"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | — |

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Batch Video ID Extraction](/model/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/model/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/model/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/sec-user-id.json`](../../../../catalog/models/douyin/web/sec-user-id.json) · Store page: https://www.sandbase.ai/model/douyin/web/sec-user-id
