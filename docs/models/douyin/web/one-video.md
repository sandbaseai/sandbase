# Douyin Single Video Details (V1) API: pricing, parameters and code examples

`douyin/web/one-video` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns detailed metadata for a single Douyin video using its video ID. Supports optional inclusion of anchor details such as location and merchant data.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/one-video", "aweme_id": "7372484719365098803", "need_anchor_info": false}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/one-video', {'aweme_id': '7372484719365098803', 'need_anchor_info': False})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/one-video", {
  "aweme_id": "7372484719365098803",
  "need_anchor_info": false
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/one-video", sandbase.Params{
	"aweme_id": "7372484719365098803",
	"need_anchor_info": false,
})
```

Same call via the path form: `POST /v1/api/douyin/web/one-video` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `aweme_id` | string | yes | Video id  |
| `need_anchor_info` | boolean |  | Whether anchor information is needed, default is False, enabling it will show some anchor information about the video, such as location, merchant information, product showcase, etc., which may increase the interface… default `false` |

## Details

Retrieve detailed metadata for a specific Douyin video by supplying `aweme_id`. You can also configure `need_anchor_info` to include associated location, merchant, or product showcase data.

### Use cases

- Retrieve video quality specifications and bitrate options for a specific post.
- Inspect Douyin video metadata alongside associated merchant or showcase links.
- Display video details and location context within analytics dashboards.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/one-video" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"aweme_id": "7372484719365098803"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `aweme_id` | string | Yes | Video id |
| `need_anchor_info` | boolean | No | Whether anchor information is needed, default is False, enabling it will show some anchor information about the video, such as location, merchant information, … |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "aweme_detail": {
    "video": {
      "bit_rate": [
        {
          "bit_rate": 1603814,
          "gear_name": "normal_1080_0",
          "quality_type": 1
        }
      ]
    }
  }
}
```

### Notes

- Setting `need_anchor_info` to true returns extra anchor metadata such as location, merchant, or product showcases, which may increase response time.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Batch Video ID Extraction](/model/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/model/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/model/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/one-video.json`](../../../../catalog/models/douyin/web/one-video.json) · Store page: https://www.sandbase.ai/model/douyin/web/one-video
