# Xigua Video Play URL API: pricing, parameters and code examples

`xigua/app-v2/one-video-play-url` · data API · Xigua · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the direct playback URL for a specific Xigua video using its unique item identifier. Developers supply the target video ID to retrieve playable media links.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xigua/app-v2/one-video-play-url", "item_id": "7354954305222377999"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xigua/app-v2/one-video-play-url', {'item_id': '7354954305222377999'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xigua/app-v2/one-video-play-url", {
  "item_id": "7354954305222377999"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xigua/app-v2/one-video-play-url", sandbase.Params{
	"item_id": "7354954305222377999",
})
```

Same call via the path form: `POST /v1/api/xigua/app-v2/one-video-play-url` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `item_id` | string | yes | Video id  |

## Details

Retrieve direct video playback links for Xigua videos by providing the target `item_id`. This endpoint allows clients to obtain playable media stream URLs directly.

### Use cases

- Integrate playable Xigua media streams directly into external video players.
- Retrieve video playback links for content analysis and automated processing pipelines.
- Verify media availability and inspect streaming URLs for specific video IDs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xigua/app-v2/one-video-play-url" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"item_id": "7354954305222377999"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `item_id` | string | Yes | Video id |

### Notes

- `item_id` is required and specifies the unique identifier of the Xigua video.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Xigua Single Video Information](/apis/xigua/app-v2/one-video): Returns lightweight single video data and associated related video information from Xigua for a specific post by its unique item ID.
- [Xigua Video Search](/apis/xigua/app-v2/search-video): Search Xigua Video (ByteDance long-form video) by keyword: titles, creators, duration, publish time and comment counts, with sort and duration filters.
- [Xigua User Profile Details](/apis/xigua/app-v2/user-info): Returns profile and personal information for a specified Xigua account.

---
Machine-readable: [`catalog/models/xigua/app-v2/one-video-play-url.json`](../../../../catalog/models/xigua/app-v2/one-video-play-url.json) · Store page: https://www.sandbase.ai/model/xigua/app-v2/one-video-play-url
