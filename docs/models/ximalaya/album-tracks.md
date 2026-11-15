# Ximalaya Album Tracks API: pricing, parameters and code examples

`ximalaya/album-tracks` · data API · Ximalaya · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

List tracks within an album with pagination. Returns track title, duration (seconds), play count, likes, comments count, pricing info, and order number. Paginates via page number.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "ximalaya/album-tracks", "album_id": "81519744"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('ximalaya/album-tracks', {'album_id': '81519744'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("ximalaya/album-tracks", {
  "album_id": "81519744"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "ximalaya/album-tracks", sandbase.Params{
	"album_id": "81519744",
})
```

Same call via the path form: `POST /v1/api/ximalaya/album-tracks` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number for pagination. default `1` |
| `album_id` | string | yes | Numeric album ID (e.g. 77855794). Obtainable from get_category_albums or search_albums results.  |
| `sort_asc` | string |  | Sort order. Accepted values: true (ascending by track order), false (descending). default `"true"` |
| `page_size` | integer |  | Number of tracks per page. default `30` |

## Details

List tracks within an album with pagination. Returns track title, duration (seconds), play count, likes, comments count, pricing info, and order number. Paginates via page number.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "ximalaya/album-tracks", "album_id": "81519744"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `album_id` | string | Yes | Numeric album ID (e.g. 77855794). Obtainable from get_category_albums or search_albums results. |
| `page` | integer | No | Page number for pagination. |
| `page_size` | integer | No | Number of tracks per page. |
| `sort_asc` | string | No | Sort order. Accepted values: true (ascending by track order), false (descending). |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/ximalaya/album-tracks.json`](../../../catalog/models/ximalaya/album-tracks.json) · Store page: https://www.sandbase.ai/model/ximalaya/album-tracks
