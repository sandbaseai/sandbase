# Xigua Single Video Information API: pricing, parameters and code examples

`xigua/app-v2/one-video` · data API · Xigua · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns lightweight single video data and associated related video information from Xigua for a specific post by its unique item ID.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xigua/app-v2/one-video", "item_id": "<item_id>"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xigua/app-v2/one-video', {'item_id': '<item_id>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xigua/app-v2/one-video", {
  "item_id": "<item_id>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xigua/app-v2/one-video", sandbase.Params{
	"item_id": "<item_id>",
})
```

Same call via the path form: `POST /v1/api/xigua/app-v2/one-video` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `item_id` | string | yes | Video id  |

## Details

Retrieve basic metadata and related video recommendations for a Xigua video by providing `item_id`.

### Use cases

- Discover related video recommendations for a specific post.
- Inspect baseline item data without full title metadata.
- Trace content recommendation graphs across Xigua videos.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xigua/app-v2/one-video" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"item_id": "<item_id>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `item_id` | string | Yes | Video id |

### Notes

- Requires a valid `item_id` representing the target Xigua video.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Xigua Video Play URL](/model/xigua/app-v2/one-video-play-url): Returns the direct playback URL for a specific Xigua video using its unique item identifier.
- [Xigua Video Search](/model/xigua/app-v2/search-video): Search Xigua Video (ByteDance long-form video) by keyword: titles, creators, duration, publish time and comment counts, with sort and duration filters.
- [Xigua User Profile Details](/model/xigua/app-v2/user-info): Returns profile and personal information for a specified Xigua account.

---
Machine-readable: [`catalog/models/xigua/app-v2/one-video.json`](../../../../catalog/models/xigua/app-v2/one-video.json) · Store page: https://www.sandbase.ai/model/xigua/app-v2/one-video
