# Douyin sec_user_ids from URLs (Batch) API: pricing, parameters and code examples

`douyin/web/all-sec-user-id` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs. Accepts an array of profile links to return the corresponding platform identifiers.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/all-sec-user-id", "body": ["https://static.sandbase.ai/examples/f66ded91-c75d-40dd-8377-5675eceeeb3d/input/25f4436b-5642-4e06-93ec-dc108424d26e.bin"]}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/all-sec-user-id', {'body': ['https://static.sandbase.ai/examples/f66ded91-c75d-40dd-8377-5675eceeeb3d/input/25f4436b-5642-4e06-93ec-dc108424d26e.bin']})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/all-sec-user-id", {
  "body": [
    "https://static.sandbase.ai/examples/f66ded91-c75d-40dd-8377-5675eceeeb3d/input/25f4436b-5642-4e06-93ec-dc108424d26e.bin"
  ]
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/all-sec-user-id", sandbase.Params{
	"body": []any{"https://static.sandbase.ai/examples/f66ded91-c75d-40dd-8377-5675eceeeb3d/input/25f4436b-5642-4e06-93ec-dc108424d26e.bin"},
})
```

Same call via the path form: `POST /v1/api/douyin/web/all-sec-user-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `body` | array | yes | User homepage link list  |

## Details

Retrieve Douyin user security IDs in bulk by passing an array of profile homepage links in the `body` parameter. This endpoint returns the platform identifiers for downstream profile lookups.

### Use cases

- Convert multiple Douyin profile URLs into sec_user_id identifiers in a single request.
- Prepare user identifiers for subsequent profile and video metadata queries.
- Resolve batch lists of creator homepage links into platform security IDs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/all-sec-user-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"body": "<body>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `body` | array | Yes | User homepage link list |

### Notes

- Supply Douyin user homepage links as an array in the `body` parameter.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Batch Video ID Extraction](/model/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin Webcast ID Extraction](/model/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.
- [Douyin Video ID Extractor](/model/douyin/web/aweme-id): Extracts the internal video ID from a given Douyin video web URL.

---
Machine-readable: [`catalog/models/douyin/web/all-sec-user-id.json`](../../../../catalog/models/douyin/web/all-sec-user-id.json) · Store page: https://www.sandbase.ai/model/douyin/web/all-sec-user-id
