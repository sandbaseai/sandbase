# Douyin High Quality Video Play URL (App V3) API: pricing, parameters and code examples

`douyin/app-v3/video-high-quality-play-url` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.005 per call (free daily quota) · **Modes:** sync

Returns the highest quality playback URL for a Douyin video using a video identifier or share link, with optional region filtering.

## Pricing

- **$0.005 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/video-high-quality-play-url", "aweme_id": "7662510757757603122", "region": "CN", "share_url": "https://static.sandbase.ai/examples/83222b01-babd-47a9-a612-3a92a4e7c4bb/input/19f248e9-c747-4994-8b9f-285f2826271f.bin"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/video-high-quality-play-url', {'aweme_id': '7662510757757603122', 'region': 'CN', 'share_url': 'https://static.sandbase.ai/examples/83222b01-babd-47a9-a612-3a92a4e7c4bb/input/19f248e9-c747-4994-8b9f-285f2826271f.bin'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/video-high-quality-play-url", {
  "aweme_id": "7662510757757603122",
  "region": "CN",
  "share_url": "https://static.sandbase.ai/examples/83222b01-babd-47a9-a612-3a92a4e7c4bb/input/19f248e9-c747-4994-8b9f-285f2826271f.bin"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/video-high-quality-play-url", sandbase.Params{
	"aweme_id": "7662510757757603122",
	"region": "CN",
	"share_url": "https://static.sandbase.ai/examples/83222b01-babd-47a9-a612-3a92a4e7c4bb/input/19f248e9-c747-4994-8b9f-285f2826271f.bin",
})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/video-high-quality-play-url` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `region` | string |  | Optional, ISO country code (e.g. "CN" / "US" / "HK") used as the request exit region.  |
| `aweme_id` | string |  | Video id, prefer to use aweme_id, if not available, use share_url.  |
| `share_url` | string |  | Optional, share link, if the video id is provided, this parameter can be omitted.  |

## Details

Fetch high-quality video playback addresses by supplying an `aweme_id` or a `share_url`. You can also configure an optional `region` exit code.

### Use cases

- Retrieve the best available resolution video stream for media playback.
- Resolve Douyin share URLs into direct video stream addresses.
- Route playback link requests through a specified geographic exit region.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/video-high-quality-play-url" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `region` | string | No | Optional, ISO country code (e.g. "CN" / "US" / "HK") used as the request exit region. |
| `aweme_id` | string | No | Video id, prefer to use aweme_id, if not available, use share_url. |
| `share_url` | string | No | Optional, share link, if the video id is provided, this parameter can be omitted. |

### Notes

- Provide either `aweme_id` or `share_url`; `aweme_id` is preferred.
- The `region` parameter accepts an ISO country code such as CN, US, or HK.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Brand Hot Search List](/model/douyin/app-v3/brand-hot-search-list): Returns the current Douyin brand hot search list and category data.
- [Douyin Brand Hot Search List Detail](/model/douyin/app-v3/brand-hot-search-list-detail): Returns detailed brand hot search list data from Douyin for a specific category.
- [Douyin Short Link Generator](/model/douyin/app-v3/generate-short-url): Converts a standard Douyin web link into a shortened Douyin URL.

---
Machine-readable: [`catalog/models/douyin/app-v3/video-high-quality-play-url.json`](../../../../catalog/models/douyin/app-v3/video-high-quality-play-url.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/video-high-quality-play-url
