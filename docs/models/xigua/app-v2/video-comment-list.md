# Xigua Video Comment List

`xigua/app-v2/video-comment-list` · api · Xigua

Returns comments for a specified Xigua video. Supports paginating through discussion threads using offset and result count parameters.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xigua/app-v2/video-comment-list", "item_id": "7354954305222377999"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xigua/app-v2/video-comment-list', {'item_id': '7354954305222377999'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xigua/app-v2/video-comment-list", {
  "item_id": "7354954305222377999"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xigua/app-v2/video-comment-list", sandbase.Params{
	"item_id": "7354954305222377999",
})
```

Same call via the path form: `POST /v1/api/xigua/app-v2/video-comment-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Quantity, default 20, it is recommended to keep the default.  |
| `offset` | integer |  | Offset, pass 0 for the first request, pass the offset returned by the previous request for subsequent requests  |
| `item_id` | string | yes | Video id  |

## Details

Fetch comments for a Xigua video by specifying its `item_id`. Supports sequential pagination via `offset` and `count`.

### Use cases

- Retrieve user comments on a specific Xigua video.
- Track audience discussion and viewer feedback over time.
- Paginate through full comment threads for sentiment analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xigua/app-v2/video-comment-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"item_id": "<item_id>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `item_id` | string | Yes | Video id |
| `count` | integer | No | Quantity, default 20, it is recommended to keep the default. |
| `offset` | integer | No | Offset, pass 0 for the first request, pass the offset returned by the previous request for subsequent requests |

### Notes

- Requires the video identifier in `item_id`.
- Use `offset` for pagination, passing 0 on the first call and the returned offset for subsequent requests.
- The `count` parameter defaults to 20.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Xigua Single Video Information](/model/xigua/app-v2/one-video): Returns lightweight single video data and associated related video information from Xigua for a specific post by its unique item ID.
- [Xigua Video Play URL](/model/xigua/app-v2/one-video-play-url): Returns the direct playback URL for a specific Xigua video using its unique item identifier.
- [Xigua Video Search](/model/xigua/app-v2/search-video): Search Xigua Video (ByteDance long-form video) by keyword: titles, creators, duration, publish time and comment counts, with sort and duration filters.

---
Machine-readable: [`catalog/models/xigua/app-v2/video-comment-list.json`](../../../../catalog/models/xigua/app-v2/video-comment-list.json) · Store page: https://www.sandbase.ai/model/xigua/app-v2/video-comment-list
