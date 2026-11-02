# TikTok Single Video Details (V2) API: pricing, parameters and code examples

`tiktok/app-v3/one-video-v2` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns detailed post information and comment configuration for a specific TikTok video using its unique post identifier. Provide the video ID to retrieve item metadata.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/one-video-v2", "aweme_id": "7350810998023949599"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/one-video-v2', {'aweme_id': '7350810998023949599'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/one-video-v2", {
  "aweme_id": "7350810998023949599"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/one-video-v2", sandbase.Params{
	"aweme_id": "7350810998023949599",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/one-video-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `aweme_id` | string | yes | Video id  |

## Details

Look up metadata and configuration settings for an individual TikTok post by passing the `aweme_id` parameter.

### Use cases

- Retrieve configuration settings and details for a specific TikTok video.
- Inspect comment and emoji recommendation configurations on a video post.
- Access individual post metadata using a TikTok item identifier.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/one-video-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"aweme_id": "7350810998023949599"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `aweme_id` | string | Yes | Video id |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "aweme_detail": {
    "comment_config": {
      "emoji_recommend_list": [
        {
          "emoji_id": "smiley01_lol",
          "emoji_id_score": 11,
          "score": 11
        }
      ]
    }
  }
}
```

### Notes

- Provide the targeted video identifier in `aweme_id`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok LIVE Status](/model/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/model/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/model/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/one-video-v2.json`](../../../../catalog/models/tiktok/app-v3/one-video-v2.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/one-video-v2
