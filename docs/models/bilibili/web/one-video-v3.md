# Bilibili Single Video Details API: pricing, parameters and code examples

`bilibili/web/one-video-v3` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed metadata for a single Bilibili video, including season information, episode titles, duration, and post timestamps via its URL.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/web/one-video-v3", "url": "https://www.bilibili.com/video/BV1S5uKzzE4r"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/web/one-video-v3', {'url': 'https://www.bilibili.com/video/BV1S5uKzzE4r'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/web/one-video-v3", {
  "url": "https://www.bilibili.com/video/BV1S5uKzzE4r"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/web/one-video-v3", sandbase.Params{
	"url": "https://www.bilibili.com/video/BV1S5uKzzE4r",
})
```

Same call via the path form: `POST /v1/api/bilibili/web/one-video-v3` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Video URL  |

## Details

Retrieve video metadata and episode details from Bilibili by supplying a valid video link in `url`.

### Use cases

- Look up episode structure and duration for multi-part Bilibili videos.
- Extract video titles and release timestamps from web links.
- Inspect season and collection metadata linked to a specific Bilibili post.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/one-video-v3" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.bilibili.com/video/BV1S5uKzzE4r"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Video URL |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "ugc_season": {
    "sections": [
      {
        "episodes": [
          {
            "id": 130519510,
            "season_id": 5667281,
            "section_id": 6287956,
            "title": "《入侵脑细胞》",
            "arc": {
              "ctime": 1693555200,
              "duration": 2244,
              "pubdate": 1693555200,
              "title": "《入侵脑细胞》",
              "type_id": 0,
              "type_id_v2": 0
            },
            "page": {
              "duration": 2244
            }
          }
        ]
      }
    ]
  }
}
```

### Notes

- Requires a complete Bilibili video address in `url`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Bilibili Streaming Areas](/model/bilibili/web/all-live-areas): Returns the complete list of streaming broadcast areas and categories on Bilibili.
- [Bilibili BV to AID Converter](/model/bilibili/web/bv-to-aid): Converts a Bilibili BV identifier to its corresponding numeric AID value.
- [Bilibili User Collection Folders](/model/bilibili/web/collect-folders): Returns the collection folders owned by a specific Bilibili user.

---
Machine-readable: [`catalog/models/bilibili/web/one-video-v3.json`](../../../../catalog/models/bilibili/web/one-video-v3.json) · Store page: https://www.sandbase.ai/model/bilibili/web/one-video-v3
