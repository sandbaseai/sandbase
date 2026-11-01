# Instagram Music Posts (V1)

`instagram/v1/music-posts` · api · Instagram

Returns Reels and posts associated with a specific audio track using either an audio ID or URL. Supports cursor pagination to browse results.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v1/music-posts"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v1/music-posts', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v1/music-posts", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v1/music-posts", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/instagram/v1/music-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `max_id` | string |  | Pagination cursor, omit for first request  |
| `music_id` | string |  | Music ID (alternative to music_url)  |
| `music_url` | string |  | Music URL, ID will be extracted automatically (alternative to music_id)  |

## Details

Retrieve posts and Reels featuring a chosen audio track by providing either `music_id` or `music_url`. You can paginate through subsequent pages using `max_id`.

### Use cases

- Discover trending Reels that incorporate a specific audio clip.
- Monitor content engagement driven by a targeted music track.
- Analyze how creators use a particular sound in their posts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v1/music-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `max_id` | string | No | Pagination cursor, omit for first request |
| `music_id` | string | No | Music ID (alternative to music_url) |
| `music_url` | string | No | Music URL, ID will be extracted automatically (alternative to music_id) |

### Notes

- Provide either `music_id` or `music_url` to identify the audio track.
- Pass `max_id` as the cursor to paginate through subsequent results.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Cities by Country](/model/instagram/v1/cities): Returns a list of Instagram cities and regions for a specified country code.
- [Instagram Hashtag Posts (V1)](/model/instagram/v1/hashtag-posts): Returns public Instagram posts associated with a specific hashtag.
- [Instagram Location Details (V1)](/model/instagram/v1/location-info): Returns detailed metadata and profile information for a specified Instagram location using its unique identifier.

---
Machine-readable: [`catalog/models/instagram/v1/music-posts.json`](../../../../catalog/models/instagram/v1/music-posts.json) · Store page: https://www.sandbase.ai/model/instagram/v1/music-posts
