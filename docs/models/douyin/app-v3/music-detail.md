# Douyin Music Details API: pricing, parameters and code examples

`douyin/app-v3/music-detail` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns detailed information for a specified Douyin audio track using its unique identifier.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/music-detail", "music_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/music-detail', {'music_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/music-detail", {
  "music_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/music-detail", sandbase.Params{
	"music_id": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/music-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `music_id` | string | yes | Music id  |

## Details

Fetch comprehensive metadata for a specific Douyin audio track by providing its `music_id`.

### Use cases

- Retrieve metadata for a specific Douyin audio track
- Inspect sound details associated with platform videos
- Verify audio identifiers when tracking music trends

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/music-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"music_id": "7348905216869174025"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `music_id` | string | Yes | Music id |

### Notes

- Requires a valid `music_id` string to identify the audio track.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Brand Hot Search List](/model/douyin/app-v3/brand-hot-search-list): Returns the current Douyin brand hot search list and category data.
- [Douyin Brand Hot Search List Detail](/model/douyin/app-v3/brand-hot-search-list-detail): Returns detailed brand hot search list data from Douyin for a specific category.
- [Douyin Short Link Generator](/model/douyin/app-v3/generate-short-url): Converts a standard Douyin web link into a shortened Douyin URL.

---
Machine-readable: [`catalog/models/douyin/app-v3/music-detail.json`](../../../../catalog/models/douyin/app-v3/music-detail.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/music-detail
