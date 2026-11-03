# Douyin Video Mix Detail API: pricing, parameters and code examples

`douyin/app-v3/video-mix-detail` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed information about a specific Douyin video compilation playlist based on the provided mix identifier.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/video-mix-detail", "mix_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/video-mix-detail', {'mix_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/video-mix-detail", {
  "mix_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/video-mix-detail", sandbase.Params{
	"mix_id": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/video-mix-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `mix_id` | string | yes | Mix id  |

## Details

Use this endpoint to look up metadata and author details for a Douyin video mix using its `mix_id`.

### Use cases

- Inspect metadata and author profile info for a Douyin video compilation series.
- Verify video mix attributes before organizing content archives.
- Extract compilation playlist details for video cataloging systems.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/video-mix-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"mix_id": "7384792941870450726"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `mix_id` | string | Yes | Mix id |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "mix_info": {
    "author": {
      "cover_url": [
        {}
      ]
    }
  }
}
```

### Notes

- Requires a valid `mix_id` to look up compilation details.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Brand Hot Search List](/apis/douyin/app-v3/brand-hot-search-list): Returns the current Douyin brand hot search list and category data.
- [Douyin Brand Hot Search List Detail](/apis/douyin/app-v3/brand-hot-search-list-detail): Returns detailed brand hot search list data from Douyin for a specific category.
- [Douyin Short Link Generator](/apis/douyin/app-v3/generate-short-url): Converts a standard Douyin web link into a shortened Douyin URL.

---
Machine-readable: [`catalog/models/douyin/app-v3/video-mix-detail.json`](../../../../catalog/models/douyin/app-v3/video-mix-detail.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/video-mix-detail
