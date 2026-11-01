# YouTube Search Suggestions

`youtube/web-v2/search-suggestions` · api · YouTube

Returns YouTube autocomplete search suggestions for a given keyword query. Supports optional geographic region and language filtering.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/web-v2/search-suggestions", "keyword": "OpenAI"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/web-v2/search-suggestions', {'keyword': 'OpenAI'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/web-v2/search-suggestions", {
  "keyword": "OpenAI"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/web-v2/search-suggestions", sandbase.Params{
	"keyword": "OpenAI",
})
```

Same call via the path form: `POST /v1/api/youtube/web-v2/search-suggestions` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `region` | string |  | Region code (optional, default US) default `"US"` |
| `keyword` | string | yes | Search keyword (required)  |
| `language` | string |  | Language code (optional, default en) default `"en"` |

## Details

Fetch search query autocomplete suggestions by providing a target `keyword`. You can optionally adjust localized results using `region` and `language`.

### Use cases

- Populate autocomplete recommendations in video search interfaces.
- Analyze trending query variations and user search intent.
- Optimize video tags and titles based on popular search prompts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web-v2/search-suggestions" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "OpenAI"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword (required) |
| `region` | string | No | Region code (optional, default US) |
| `language` | string | No | Language code (optional, default en) |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "keyword": "OpenAI",
  "total_count": 14
}
```

### Notes

- The `region` parameter defaults to US if omitted.
- The `language` parameter defaults to en if omitted.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [YouTube Channel Community Posts](/model/youtube/web-v2/channel-community-posts): Returns community posts from a specific YouTube channel, including text content, polls, votes, and comment counts.
- [YouTube Channel Description](/model/youtube/web-v2/channel-description): Returns YouTube channel details including subscriber counts, video totals, view counts, joined date, and social links.
- [YouTube Channel ID from URL](/model/youtube/web-v2/channel-id): Resolves a YouTube channel URL to its canonical channel ID.

---
Machine-readable: [`catalog/models/youtube/web-v2/search-suggestions.json`](../../../../catalog/models/youtube/web-v2/search-suggestions.json) · Store page: https://www.sandbase.ai/model/youtube/web-v2/search-suggestions
