# Douyin Multi Video Information (V2) API: pricing, parameters and code examples

`douyin/app-v3/multi-video-v2` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.05 per call · **Modes:** sync

Returns metadata and details for multiple Douyin videos in a single batch request using an array provided in the request payload.

## Pricing

- **$0.05 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/multi-video-v2", "body": ["7687107502068026650", "7682040509572983400"]}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/multi-video-v2', {'body': ['7687107502068026650', '7682040509572983400']})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/multi-video-v2", {
  "body": [
    "7687107502068026650",
    "7682040509572983400"
  ]
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/multi-video-v2", sandbase.Params{
	"body": []any{"7687107502068026650", "7682040509572983400"},
})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/multi-video-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `body` | array | yes | Aweme Ids  |

## Details

Fetch detailed information for multiple Douyin videos at once by providing a list in the `body` parameter.

### Use cases

- Retrieve metadata for multiple Douyin videos simultaneously.
- Monitor video statistics and details across a batch of posts.
- Populate media libraries with bulk Douyin video information.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/multi-video-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"body": "<body>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `body` | array | Yes | — |

### Notes

- Requires an array of video identifiers passed in the `body` parameter.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Brand Hot Search List](/model/douyin/app-v3/brand-hot-search-list): Returns the current Douyin brand hot search list and category data.
- [Douyin Brand Hot Search List Detail](/model/douyin/app-v3/brand-hot-search-list-detail): Returns detailed brand hot search list data from Douyin for a specific category.
- [Douyin Short Link Generator](/model/douyin/app-v3/generate-short-url): Converts a standard Douyin web link into a shortened Douyin URL.

---
Machine-readable: [`catalog/models/douyin/app-v3/multi-video-v2.json`](../../../../catalog/models/douyin/app-v3/multi-video-v2.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/multi-video-v2
