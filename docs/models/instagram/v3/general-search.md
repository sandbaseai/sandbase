# Instagram General Search (V3) API: pricing, parameters and code examples

`instagram/v3/general-search` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.012 per call (free daily quota) · **Modes:** sync

Returns search results across media grids based on a keyword query. Supports pagination tokens and optional metadata flags.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v3/general-search", "query": "openai"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v3/general-search', {'query': 'openai'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v3/general-search", {
  "query": "openai"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v3/general-search", sandbase.Params{
	"query": "openai",
})
```

Same call via the path form: `POST /v1/api/instagram/v3/general-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Search keyword  |
| `rank_token` | string |  | Rank token, omit for first request, get from previous response `data.rank_token`  |
| `next_max_id` | string |  | Pagination ID, omit for first request, get from previous response `data.next_max_id`  |
| `enable_metadata` | boolean |  | Enable metadata default `true` |

## Details

Search Instagram content using a target keyword via `query`. Retrieve subsequent pages using `next_max_id` and `rank_token`.

### Use cases

- Discover Instagram posts and media matching specific topic keywords.
- Collect media grid feeds for topic-based content analysis.
- Track brand or keyword presence across indexed platform posts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/general-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "openai"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search keyword |
| `rank_token` | string | No | Rank token, omit for first request, get from previous response `data.rank_token` |
| `next_max_id` | string | No | Pagination ID, omit for first request, get from previous response `data.next_max_id` |
| `enable_metadata` | boolean | No | Enable metadata |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "media_grid": {
    "sections": [
      {
        "feed_type": "media",
        "layout_type": "media_grid"
      }
    ]
  }
}
```

### Notes

- For subsequent pages, pass `next_max_id` from the previous response.
- Provide `rank_token` from `data.rank_token` of earlier calls to maintain search ranking.
- Set `enable_metadata` to include additional search metadata.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Comment Bulk Translation](/model/instagram/v3/bulk-translate-comments): Returns bulk translations for multiple Instagram comments using a list of comment identifiers.
- [Instagram Comment Replies (V3)](/model/instagram/v3/comment-replies): Returns child comment replies for a specific Instagram comment using the post media ID and parent comment ID.
- [Instagram Explore Feed](/model/instagram/v3/explore): Returns curated sectional items from the Instagram explore feed, including layout formats and feed types.

---
Machine-readable: [`catalog/models/instagram/v3/general-search.json`](../../../../catalog/models/instagram/v3/general-search.json) · Store page: https://www.sandbase.ai/model/instagram/v3/general-search
