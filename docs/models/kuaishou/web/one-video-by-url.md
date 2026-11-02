# Kuaishou Single Video by URL API: pricing, parameters and code examples

`kuaishou/web/one-video-by-url` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.003 per call (free daily quota) · **Modes:** sync

Retrieves video manifest data and streaming representation details for a specific Kuaishou post using its web link. Returns media properties such as resolution, frame rate, and direct video URLs.

## Pricing

- **$0.003 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/web/one-video-by-url", "url": "https://v.kuaishou.com/GKTpYm"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/web/one-video-by-url', {'url': 'https://v.kuaishou.com/GKTpYm'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/web/one-video-by-url", {
  "url": "https://v.kuaishou.com/GKTpYm"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/web/one-video-by-url", sandbase.Params{
	"url": "https://v.kuaishou.com/GKTpYm",
})
```

Same call via the path form: `POST /v1/api/kuaishou/web/one-video-by-url` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | 作品链接/Photo URL  |

## Details

Access video stream manifests and quality representations for Kuaishou content by supplying a post link in `url`.

### Use cases

- Retrieve direct stream URLs and video quality representations from a post link.
- Inspect video resolution, frame rates, and manifest data.
- Integrate Kuaishou video playback capabilities into external applications.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/web/one-video-by-url" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://v.kuaishou.com/GKTpYm"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | — |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "photo": {
    "manifest": {
      "adaptationSet": [
        {
          "representation": [
            {
              "frameRate": 29.97003,
              "hdrType": 0,
              "id": 1,
              "qualityLabel": "高清",
              "qualityType": "720p",
              "url": "https://v23-3.kwaicdn.com/upic/2024/06/19/21/BMjAyNDA2MTkyMTA5NDJfMTA5NjYzNzQwMV…",
              "kvqScore": {
                "nnvcScore": -1
              }
            }
          ]
        }
      ]
    }
  }
}
```

### Notes

- Provide a valid Kuaishou post link using the required `url` parameter.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Kuaishou Web Share Short URL](/model/kuaishou/web/generate-share-short-url): Returns a shareable short URL for a specified Kuaishou video or photo post.
- [Kuaishou User ID Lookup](/model/kuaishou/web/get-user-id): Resolves a Kuaishou user ID from a provided user share link.
- [Kuaishou Web Hot List](/model/kuaishou/web/hot-list-v1): Returns the current trending hot list from Kuaishou Web.

---
Machine-readable: [`catalog/models/kuaishou/web/one-video-by-url.json`](../../../../catalog/models/kuaishou/web/one-video-by-url.json) · Store page: https://www.sandbase.ai/model/kuaishou/web/one-video-by-url
