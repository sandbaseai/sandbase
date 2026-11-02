# Toutiao Specified Video Details API: pricing, parameters and code examples

`toutiao/web/video-info` · data API · Toutiao · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed information for a specified Toutiao video post. Retrieve post metadata and related video attributes using a valid post identifier.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "toutiao/web/video-info", "aweme_id": "7431543350882206242"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('toutiao/web/video-info', {'aweme_id': '7431543350882206242'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("toutiao/web/video-info", {
  "aweme_id": "7431543350882206242"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "toutiao/web/video-info", sandbase.Params{
	"aweme_id": "7431543350882206242",
})
```

Same call via the path form: `POST /v1/api/toutiao/web/video-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `aweme_id` | string | yes | Post ID  |

## Details

Fetch detailed information for a Toutiao video by supplying the post ID in `aweme_id`.

### Use cases

- Retrieve metadata for a specific Toutiao video post.
- Monitor video engagement metrics and post attributes.
- Inspect Toutiao content details using a known post identifier.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/toutiao/web/video-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"aweme_id": "7431543350882206242"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `aweme_id` | string | Yes | Post ID |

### Notes

- Provide the target post ID via the required `aweme_id` parameter.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Toutiao Article Details (Web)](/model/toutiao/web/article-info): Returns detailed post information and interface action settings for a specified Toutiao article based on its unique post identifier.

---
Machine-readable: [`catalog/models/toutiao/web/video-info.json`](../../../../catalog/models/toutiao/web/video-info.json) · Store page: https://www.sandbase.ai/model/toutiao/web/video-info
