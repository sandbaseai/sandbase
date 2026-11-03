# Douyin Webcast ID Extraction API: pricing, parameters and code examples

`douyin/web/all-webcast-id` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Extracts webcast IDs from a submitted list of Douyin live room links. Useful for resolving live stream identifiers across multiple URLs in bulk.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/all-webcast-id", "body": ["<body>"]}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/all-webcast-id', {'body': ['<body>']})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/all-webcast-id", {
  "body": [
    "<body>"
  ]
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/all-webcast-id", sandbase.Params{
	"body": []any{"<body>"},
})
```

Same call via the path form: `POST /v1/api/douyin/web/all-webcast-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `body` | array | yes | Room link list  |

## Details

Retrieve webcast identifiers from a list of Douyin live room URLs by providing the URLs in the `body` array.

### Use cases

- Extract webcast IDs from Douyin live stream room URLs.
- Process multiple room links in a single batch request.
- Resolve raw room URLs into standard identifiers for downstream queries.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/all-webcast-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"body": "<body>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `body` | array | Yes | Room link list |

### Notes

- Accepts an array of Douyin room links in the request `body`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Batch Video ID Extraction](/apis/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/apis/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Video ID Extractor](/apis/douyin/web/aweme-id): Extracts the internal video ID from a given Douyin video web URL.

---
Machine-readable: [`catalog/models/douyin/web/all-webcast-id.json`](../../../../catalog/models/douyin/web/all-webcast-id.json) · Store page: https://www.sandbase.ai/model/douyin/web/all-webcast-id
