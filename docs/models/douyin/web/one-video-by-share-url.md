# Douyin Video Details by Share URL API: pricing, parameters and code examples

`douyin/web/one-video-by-share-url` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed video information and available stream bitrate qualities for a single Douyin video using its web sharing link.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/one-video-by-share-url", "share_url": "https://static.sandbase.ai/examples/359eb7d4-4fa9-4d07-8f2c-1848998bd134/input/ff5ce252-e396-407c-b39c-b43cbd50b1d7.bin"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/one-video-by-share-url', {'share_url': 'https://static.sandbase.ai/examples/359eb7d4-4fa9-4d07-8f2c-1848998bd134/input/ff5ce252-e396-407c-b39c-b43cbd50b1d7.bin'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/one-video-by-share-url", {
  "share_url": "https://static.sandbase.ai/examples/359eb7d4-4fa9-4d07-8f2c-1848998bd134/input/ff5ce252-e396-407c-b39c-b43cbd50b1d7.bin"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/one-video-by-share-url", sandbase.Params{
	"share_url": "https://static.sandbase.ai/examples/359eb7d4-4fa9-4d07-8f2c-1848998bd134/input/ff5ce252-e396-407c-b39c-b43cbd50b1d7.bin",
})
```

Same call via the path form: `POST /v1/api/douyin/web/one-video-by-share-url` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `share_url` | string | yes | Share link  |

## Details

Access Douyin video details by providing a post link in the `share_url` parameter. The endpoint returns video specifications such as available bitrates and quality levels.

### Use cases

- Retrieve video bitrate and quality configurations from a Douyin post.
- Inspect single video information by resolving a public web share link.
- Extract Douyin media playback specifications for media workflows.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/one-video-by-share-url" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"share_url": "https://www.douyin.com/video/7512756548356492544"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `share_url` | string | Yes | Share link |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "aweme_detail": {
    "video": {
      "bit_rate": [
        {
          "bit_rate": 2158047,
          "gear_name": "adapt_lowest_4_1",
          "quality_type": 72
        }
      ]
    }
  }
}
```

### Notes

- Requires a valid Douyin video link passed to `share_url`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Batch Video ID Extraction](/model/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/model/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/model/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/one-video-by-share-url.json`](../../../../catalog/models/douyin/web/one-video-by-share-url.json) · Store page: https://www.sandbase.ai/model/douyin/web/one-video-by-share-url
