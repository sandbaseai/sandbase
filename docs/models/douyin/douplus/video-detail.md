# Douyin Douplus Video Detail API: pricing, parameters and code examples

`douyin/douplus/video-detail` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns Douyin video details using a direct video ID or a shared link. Input video identifiers or share text containing short links to inspect video metadata.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/douplus/video-detail", "video": "7651708301280906538"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/douplus/video-detail', {'video': '7651708301280906538'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/douplus/video-detail", {
  "video": "7651708301280906538"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/douplus/video-detail", sandbase.Params{
	"video": "7651708301280906538",
})
```

Same call via the path form: `POST /v1/api/douyin/douplus/video-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `video` | string | yes | Video ID, or share link/text (required). e.g. `7651708301280906538`, or a share caption containing a v.douyin.com link  |

## Details

Retrieve detailed information for a Douyin video by providing the `video` parameter.

### Use cases

- Look up video details directly from a Douyin video ID.
- Resolve metadata from shared Douyin links or share text.
- Inspect Douyin video information for content tracking.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/douplus/video-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"video": "<video>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `video` | string | Yes | Video ID, or share link/text (required). e.g. |

### Notes

- The `video` parameter accepts a numeric video ID or a share caption containing a v.douyin.com URL.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin DOU+ Promotable Items](/model/douyin/douplus/promotable-item-list): Returns the promotable video item list for a Douyin account on the DOU+ promotion page.
- [Douyin DOU+ User Search](/model/douyin/douplus/search-user): Searches for Douyin users in the DOU+ delivery context using a Douyin ID or nickname.
- [Douyin DOU+ Talent Categories](/model/douyin/douplus/talent-categories): Returns the Douyin DOU+ talent category directory.

---
Machine-readable: [`catalog/models/douyin/douplus/video-detail.json`](../../../../catalog/models/douyin/douplus/video-detail.json) · Store page: https://www.sandbase.ai/model/douyin/douplus/video-detail
