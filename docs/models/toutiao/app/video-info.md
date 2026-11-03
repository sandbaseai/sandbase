# Toutiao Video Information API: pricing, parameters and code examples

`toutiao/app/video-info` · data API · Toutiao · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed information for a specified Toutiao video using its post identifier. Useful for retrieving metadata and content status from Toutiao posts.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "toutiao/app/video-info", "group_id": "7431543350882206242"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('toutiao/app/video-info', {'group_id': '7431543350882206242'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("toutiao/app/video-info", {
  "group_id": "7431543350882206242"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "toutiao/app/video-info", sandbase.Params{
	"group_id": "7431543350882206242",
})
```

Same call via the path form: `POST /v1/api/toutiao/app/video-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `group_id` | string | yes | Post ID, can be obtained from the link  |

## Details

Retrieve detailed information for a specific video post on Toutiao. Provide the video post identifier via `group_id` to query its metadata.

### Use cases

- Retrieve metadata for a specific Toutiao video post.
- Verify the availability and details of linked Toutiao video content.
- Display Toutiao video attributes within external dashboards.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/toutiao/app/video-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"group_id": "7431543350882206242"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `group_id` | string | Yes | Post ID, can be obtained from the link |

### Notes

- The `group_id` parameter represents the post ID and can be obtained from the video URL link.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Toutiao Article Details (App)](/apis/toutiao/app/article-info): Returns details and interface settings for a specified Toutiao post.
- [Toutiao Post Comments](/apis/toutiao/app/comments): Returns user comments and interaction metrics for a specific Toutiao post.
- [Toutiao Profile User ID](/apis/toutiao/app/user-id): Resolves a Toutiao user profile URL into numeric and secure user identifiers.

---
Machine-readable: [`catalog/models/toutiao/app/video-info.json`](../../../../catalog/models/toutiao/app/video-info.json) · Store page: https://www.sandbase.ai/model/toutiao/app/video-info
