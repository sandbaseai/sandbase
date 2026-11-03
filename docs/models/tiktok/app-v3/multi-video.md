# TikTok Batch Video Info (App V3) API: pricing, parameters and code examples

`tiktok/app-v3/multi-video` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns metadata and post details for multiple TikTok videos simultaneously. Takes an array of video IDs in the request `body` to retrieve batch information.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/multi-video", "body": ["7683891628230315295", "7690632480868650253", "7689040091116850445"]}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/multi-video', {'body': ['7683891628230315295', '7690632480868650253', '7689040091116850445']})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/multi-video", {
  "body": [
    "7683891628230315295",
    "7690632480868650253",
    "7689040091116850445"
  ]
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/multi-video", sandbase.Params{
	"body": []any{"7683891628230315295", "7690632480868650253", "7689040091116850445"},
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/multi-video` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `body` | array | yes | Video id list  |

## Details

Look up details for multiple TikTok clips at once by submitting a list of video IDs in the `body` parameter.

### Use cases

- Retrieve details for multiple TikTok videos simultaneously.
- Monitor metrics across a curated list of TikTok post IDs.
- Inspect metadata for batches of TikTok clips.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/multi-video" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"body": "<body>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `body` | array | Yes | Video id list |

### Notes

- Accepts a list of video IDs in the `body` parameter.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok LIVE Status](/apis/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/apis/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/apis/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/multi-video.json`](../../../../catalog/models/tiktok/app-v3/multi-video.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/multi-video
