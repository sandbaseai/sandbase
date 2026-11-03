# Douyin Batch Video ID Extraction API: pricing, parameters and code examples

`douyin/web/all-aweme-id` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Extracts video IDs from a list of Douyin video URLs. Accepts an array of links and returns the corresponding item identifiers.

## Pricing

- **$0.001 per call** (USD)
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

Extract `aweme_id` values (Douyin video IDs) from several Douyin video links in one call.

### Use cases

- Convert a batch of shared links into IDs for bulk video detail or comment collection.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/all-aweme-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"body": ["https://www.douyin.com/video/7512756548356492544"]}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `body` | array | Yes | Video link list |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
[
  "7512756548356492544"
]
```

### Response fields

| Field | Meaning |
|---|---|
| `(body)` | Array of `aweme_id` strings, in the order of the input links. |

### Notes

- Pass the links as a JSON array in `body`.
- For a single link use [Douyin Aweme ID](/apis/douyin/web/aweme-id).

### Pricing

$0.001 per successful call. Failed calls, including lookups whose target does not exist, are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin sec_user_ids from URLs (Batch)](/apis/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/apis/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.
- [Douyin Video ID Extractor](/apis/douyin/web/aweme-id): Extracts the internal video ID from a given Douyin video web URL.

---
Machine-readable: [`catalog/models/douyin/web/all-aweme-id.json`](../../../../catalog/models/douyin/web/all-aweme-id.json) · Store page: https://www.sandbase.ai/model/douyin/web/all-aweme-id
