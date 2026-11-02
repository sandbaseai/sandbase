# Douyin High Quality Video Play URL (Web) API: pricing, parameters and code examples

`douyin/web/video-high-quality-play-url` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0075 per call (free daily quota) · **Modes:** sync

Returns the highest quality playback URL for a Douyin video using a video ID or share URL, with an optional exit region specification.

## Pricing

- **$0.0075 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/video-high-quality-play-url", "aweme_id": "7512756548356492544", "region": "CN", "share_url": "https://static.sandbase.ai/examples/2d775896-4018-4f17-b056-55b641a736b3/input/7e844029-329b-4b7a-a407-bd7e1f15f4ca.bin"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/video-high-quality-play-url', {'aweme_id': '7512756548356492544', 'region': 'CN', 'share_url': 'https://static.sandbase.ai/examples/2d775896-4018-4f17-b056-55b641a736b3/input/7e844029-329b-4b7a-a407-bd7e1f15f4ca.bin'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/video-high-quality-play-url", {
  "aweme_id": "7512756548356492544",
  "region": "CN",
  "share_url": "https://static.sandbase.ai/examples/2d775896-4018-4f17-b056-55b641a736b3/input/7e844029-329b-4b7a-a407-bd7e1f15f4ca.bin"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/video-high-quality-play-url", sandbase.Params{
	"aweme_id": "7512756548356492544",
	"region": "CN",
	"share_url": "https://static.sandbase.ai/examples/2d775896-4018-4f17-b056-55b641a736b3/input/7e844029-329b-4b7a-a407-bd7e1f15f4ca.bin",
})
```

Same call via the path form: `POST /v1/api/douyin/web/video-high-quality-play-url` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `region` | string |  | Optional, ISO country code (e.g. "CN" / "US" / "HK") used as the request exit region.  |
| `aweme_id` | string |  | Video id, prefer to use aweme_id, if not available, use share_url.  |
| `share_url` | string |  | Optional, share link, if the video id is provided, this parameter can be omitted.  |

## Details

Retrieve high-quality playback links for Douyin videos by providing an `aweme_id` or `share_url`. An optional `region` code can be specified to route the request through a designated exit region.

### Use cases

- Extract maximum resolution video streams for media analysis.
- Stream high-definition Douyin video content in external players.
- Archive high-quality Douyin media using video IDs or share links.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/video-high-quality-play-url" \
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

- Provide `aweme_id` as the preferred identifier, or supply `share_url` if the video ID is not available.
- Specify `region` as an ISO country code such as CN, US, or HK to set the request exit location.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Batch Video ID Extraction](/model/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/model/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/model/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/video-high-quality-play-url.json`](../../../../catalog/models/douyin/web/video-high-quality-play-url.json) · Store page: https://www.sandbase.ai/model/douyin/web/video-high-quality-play-url
