# Douyin Batch Video Information (Web) API: pricing, parameters and code examples

`douyin/web/multi-video` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.05 per call · **Modes:** sync

Retrieves details for multiple Douyin videos in a single batch request via the web interface. Accepts an array of video identifiers in the request payload.

## Pricing

- **$0.05 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/multi-video", "body": ["7372484719365098803", "7519111924212780338"]}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/multi-video', {'body': ['7372484719365098803', '7519111924212780338']})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/multi-video", {
  "body": [
    "7372484719365098803",
    "7519111924212780338"
  ]
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/multi-video", sandbase.Params{
	"body": []any{"7372484719365098803", "7519111924212780338"},
})
```

Same call via the path form: `POST /v1/api/douyin/web/multi-video` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `body` | array | yes | Aweme Ids  |

## Details

Call this endpoint to retrieve information for multiple Douyin videos at once. Provide an array of target video identifiers in the `body` parameter.

### Use cases

- Retrieve video metadata for a list of Douyin posts.
- Gather details for multiple video items in bulk.
- Inspect Douyin video attributes without making individual requests.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/multi-video" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"body": "<body>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `body` | array | Yes | — |

### Notes

- If this web interface fails, consider using the APP interface instead.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Batch Video ID Extraction](/model/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/model/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/model/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/multi-video.json`](../../../../catalog/models/douyin/web/multi-video.json) · Store page: https://www.sandbase.ai/model/douyin/web/multi-video
