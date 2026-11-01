# Douyin Batch Video ID Extraction

`douyin/web/all-aweme-id` · api · Douyin

Extracts video IDs from a list of Douyin video URLs. Accepts an array of links and returns the corresponding item identifiers.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/all-aweme-id", "body": ["https://static.sandbase.ai/examples/065a6f00-759d-4a47-b76e-ee86608434dd/input/37b54c15-fdda-4fbc-9918-f5aeae5c4218.bin"]}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/all-aweme-id', {'body': ['https://static.sandbase.ai/examples/065a6f00-759d-4a47-b76e-ee86608434dd/input/37b54c15-fdda-4fbc-9918-f5aeae5c4218.bin']})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/all-aweme-id", {
  "body": [
    "https://static.sandbase.ai/examples/065a6f00-759d-4a47-b76e-ee86608434dd/input/37b54c15-fdda-4fbc-9918-f5aeae5c4218.bin"
  ]
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/all-aweme-id", sandbase.Params{
	"body": []any{"https://static.sandbase.ai/examples/065a6f00-759d-4a47-b76e-ee86608434dd/input/37b54c15-fdda-4fbc-9918-f5aeae5c4218.bin"},
})
```

Same call via the path form: `POST /v1/api/douyin/web/all-aweme-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `body` | array | yes | Video link list  |

## Details

Retrieve Douyin video IDs from provided URLs by passing an array of links in `body`.

### Use cases

- Parse Douyin video IDs from public web links in bulk.
- Normalize video URLs into clean identifiers for downstream queries.
- Resolve up to 20 video links in a single request.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/all-aweme-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"body": ["https://www.douyin.com/video/7512756548356492544"]}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `body` | array | Yes | Video link list |

### Notes

- Supports up to 20 video links in the request `body`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin sec_user_ids from URLs (Batch)](/model/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/model/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.
- [Douyin Video ID Extractor](/model/douyin/web/aweme-id): Extracts the internal video ID from a given Douyin video web URL.

---
Machine-readable: [`catalog/models/douyin/web/all-aweme-id.json`](../../../../catalog/models/douyin/web/all-aweme-id.json) · Store page: https://www.sandbase.ai/model/douyin/web/all-aweme-id
