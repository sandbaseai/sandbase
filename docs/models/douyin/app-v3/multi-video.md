# Douyin Batch Video Information (App V3) API: pricing, parameters and code examples

`douyin/app-v3/multi-video` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Retrieves details for multiple Douyin videos in a single call. Accepts an array of video identifiers in the request body to return batch post metadata.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/multi-video", "body": ["7372484719365098803", "7519111924212780338"]}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/multi-video', {'body': ['7372484719365098803', '7519111924212780338']})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/multi-video", {
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
run, err := c.Run(ctx, "douyin/app-v3/multi-video", sandbase.Params{
	"body": []any{"7372484719365098803", "7519111924212780338"},
})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/multi-video` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `body` | array | yes | Aweme Ids  |

## Details

Retrieve information for multiple Douyin videos in batch by submitting an array of items via `body`.

### Use cases

- Retrieve metadata for multiple Douyin videos simultaneously.
- Inspect batch video metrics and details across multiple posts.
- Gather bulk video data for reporting and content analytics.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/multi-video" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"body": "<body>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `body` | array | Yes | — |

### Notes

- Requires an array passed to the `body` parameter.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Brand Hot Search List](/model/douyin/app-v3/brand-hot-search-list): Returns the current Douyin brand hot search list and category data.
- [Douyin Brand Hot Search List Detail](/model/douyin/app-v3/brand-hot-search-list-detail): Returns detailed brand hot search list data from Douyin for a specific category.
- [Douyin Short Link Generator](/model/douyin/app-v3/generate-short-url): Converts a standard Douyin web link into a shortened Douyin URL.

---
Machine-readable: [`catalog/models/douyin/app-v3/multi-video.json`](../../../../catalog/models/douyin/app-v3/multi-video.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/multi-video
