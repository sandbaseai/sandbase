# Ximalaya Album Info API: pricing, parameters and code examples

`ximalaya/album-info` · data API · Ximalaya · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Retrieve detailed metadata for a single album by its numeric ID. Returns title, cover, play count, subscription count, pricing, intro text, category, dates added and last changed, and anchor details. A single round-trip; no pagination.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "ximalaya/album-info", "album_id": "81519744"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('ximalaya/album-info', {'album_id': '81519744'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("ximalaya/album-info", {
  "album_id": "81519744"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "ximalaya/album-info", sandbase.Params{
	"album_id": "81519744",
})
```

Same call via the path form: `POST /v1/api/ximalaya/album-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `album_id` | string | yes | Numeric album ID (e.g. 77855794). Obtainable from get_category_albums or search_albums results.  |

## Details

Retrieve detailed metadata for a single album by its numeric ID. Returns title, cover, play count, subscription count, pricing, intro text, category, dates added and last changed, and anchor details. A single round-trip; no pagination.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "ximalaya/album-info", "album_id": "81519744"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `album_id` | string | Yes | Numeric album ID (e.g. 77855794). Obtainable from get_category_albums or search_albums results. |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/ximalaya/album-info.json`](../../../catalog/models/ximalaya/album-info.json) · Store page: https://www.sandbase.ai/model/ximalaya/album-info
