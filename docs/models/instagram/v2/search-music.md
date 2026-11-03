# Instagram Music Search API: pricing, parameters and code examples

`instagram/v2/search-music` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Search available music tracks on Instagram using a keyword. Returns matching audio items with audio IDs, track titles, duration, and licensing details.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v2/search-music", "keyword": "openai"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v2/search-music', {'keyword': 'openai'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v2/search-music", {
  "keyword": "openai"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v2/search-music", sandbase.Params{
	"keyword": "openai",
})
```

Same call via the path form: `POST /v1/api/instagram/v2/search-music` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | Search keyword  |

## Details

Search Instagram's audio catalog by specifying a search term via `keyword`. It returns matching audio tracks alongside identifiers and duration metadata.

### Use cases

- Find background music options for media production workflows.
- Look up Instagram audio IDs and track titles matching specific terms.
- Inspect audio duration and licensing subtype details for cataloging.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v2/search-music" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "openai"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "items": [
      {
        "audio_id": "406894795669106",
        "duration_in_ms": 164679,
        "id": "327387070466441",
        "licensed_music_subtype": "DEFAULT",
        "title": "OpenAI ChatGPT"
      }
    ]
  }
}
```

### Notes

- The `keyword` parameter is required to perform the music search query.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Comment Replies (V2)](/apis/instagram/v2/comment-replies): Retrieves a paginated list of replies to an Instagram comment using the post URL or shortcode and the target comment ID.
- [Instagram General Search (V2)](/apis/instagram/v2/general-search): Returns Instagram search results matching a specified keyword, including media items, user profiles, and engagement statistics.
- [Instagram Hashtag Posts (V2)](/apis/instagram/v2/hashtag-posts): Returns posts associated with a specific hashtag.

---
Machine-readable: [`catalog/models/instagram/v2/search-music.json`](../../../../catalog/models/instagram/v2/search-music.json) · Store page: https://www.sandbase.ai/model/instagram/v2/search-music
