# Kuaishou Video Details by URL API: pricing, parameters and code examples

`kuaishou/app/one-video-by-url` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns video and photo information for a single Kuaishou post using its shared link. Input the full share URL to retrieve media metadata.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/app/one-video-by-url", "share_text": "https://v.kuaishou.com/cNYP0Z"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/app/one-video-by-url', {'share_text': 'https://v.kuaishou.com/cNYP0Z'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/app/one-video-by-url", {
  "share_text": "https://v.kuaishou.com/cNYP0Z"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/app/one-video-by-url", sandbase.Params{
	"share_text": "https://v.kuaishou.com/cNYP0Z",
})
```

Same call via the path form: `POST /v1/api/kuaishou/app/one-video-by-url` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `share_text` | string | yes | 作品链接/Photo URL  |

## Details

Retrieve post and media metadata from Kuaishou by providing a valid share link via `share_text`.

### Use cases

- Look up post details from a shared Kuaishou URL.
- Inspect metadata and comment bar settings for target video items.
- Extract media properties using mobile app share links.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/app/one-video-by-url" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"share_text": "https://v.kuaishou.com/cNYP0Z"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `share_text` | string | Yes | — |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "photos": [
    {
      "commentTopBarPriority": [
        {
          "bizType": "PLC",
          "subBizType": "51"
        }
      ]
    }
  ]
}
```

### Notes

- Accepts a Kuaishou share link such as a short URL passed to `share_text`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Kuaishou Brand Top List](/model/kuaishou/app/brand-top-list): Returns top brand rankings and related live stream links from Kuaishou.
- [Kuaishou App Share Link](/model/kuaishou/app/generate-share-link): Generates a shareable URL for Kuaishou application content using a specified object identifier.
- [Kuaishou Hot Board Categories](/model/kuaishou/app/hot-board-categories): Returns the active list of hot board categories available in the Kuaishou app.

---
Machine-readable: [`catalog/models/kuaishou/app/one-video-by-url.json`](../../../../catalog/models/kuaishou/app/one-video-by-url.json) · Store page: https://www.sandbase.ai/model/kuaishou/app/one-video-by-url
