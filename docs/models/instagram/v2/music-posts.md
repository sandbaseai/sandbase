# Instagram Music Posts (V2) API: pricing, parameters and code examples

`instagram/v2/music-posts` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Returns Instagram posts that use a specific audio track identified by its audio ID. Supports paginated results using a pagination token.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v2/music-posts", "audio_canonical_id": "564058920086577"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v2/music-posts', {'audio_canonical_id': '564058920086577'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v2/music-posts", {
  "audio_canonical_id": "564058920086577"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v2/music-posts", sandbase.Params{
	"audio_canonical_id": "564058920086577",
})
```

Same call via the path form: `POST /v1/api/instagram/v2/music-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `pagination_token` | string |  | Pagination token from previous response  |
| `audio_canonical_id` | string | yes | Audio ID  |

## Details

Retrieve Instagram posts associated with a specific audio track using `audio_canonical_id`. Paginate through subsequent pages with `pagination_token`.

### Use cases

- Analyze posts featuring a specific audio track or sound.
- Track content trends around a particular piece of music.
- Discover creator content using selected Instagram audio tracks.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v2/music-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"audio_canonical_id": "564058920086577"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `audio_canonical_id` | string | Yes | Audio ID |
| `pagination_token` | string | No | Pagination token from previous response |

### Notes

- Obtain the `audio_canonical_id` from post details.
- Pass `pagination_token` from a previous response to paginate through results.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Comment Replies (V2)](/model/instagram/v2/comment-replies): Retrieves a paginated list of replies to an Instagram comment using the post URL or shortcode and the target comment ID.
- [Instagram General Search (V2)](/model/instagram/v2/general-search): Returns Instagram search results matching a specified keyword, including media items, user profiles, and engagement statistics.
- [Instagram Hashtag Posts (V2)](/model/instagram/v2/hashtag-posts): Returns posts associated with a specific hashtag.

---
Machine-readable: [`catalog/models/instagram/v2/music-posts.json`](../../../../catalog/models/instagram/v2/music-posts.json) · Store page: https://www.sandbase.ai/model/instagram/v2/music-posts
