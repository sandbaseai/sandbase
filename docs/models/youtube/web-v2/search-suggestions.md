# YouTube Search Suggestions API: pricing, parameters and code examples

`youtube/web-v2/search-suggestions` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns YouTube autocomplete search suggestions for a given keyword query. Supports optional geographic region and language filtering.

## Pricing

- **$0.001 per call** (USD)
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

Returns YouTube autocomplete suggestions for a search keyword. You send a `keyword` and can set `region` and `language` to localize the results.

### Use cases

- Fill a search box in your own app with the same suggestions YouTube shows for a partial or full query.
- Find phrases people type after a brand or topic name, such as `OpenAI`, to plan video titles.
- Compare suggestions for the same `keyword` across different `region` and `language` values to see how searches differ by market.
- Build a keyword list for content research by running a seed term and collecting the returned phrases.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web-v2/search-suggestions" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "OpenAI"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword (required) |
| `language` | string | No | Language code (optional, default en) |
| `region` | string | No | Region code (optional, default US) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "keyword": "OpenAI",
  "suggestions": [
    "openai"
  ],
  "total_count": 14
}
```

### Response fields

| Field | Meaning |
|---|---|
| `keyword` | The search term the suggestions were requested for. It matches the `keyword` you sent. |
| `suggestions[]` | List of autocomplete phrases, as plain strings. The first item in the example is the keyword itself in lowercase, followed by longer phrases that start with it. |
| `total_count` | Number of suggestions reported for the query. In the example it is `14`, while the list is trimmed to a few items. |

### Notes

- `keyword` is required and can be up to 200 characters. `region` defaults to `US` and `language` defaults to `en`.
- Suggestions are returned as plain text strings with no IDs or URLs. To get videos for a suggestion, pass it to [YouTube General Search (Web V2, V2)](/apis/youtube/web-v2/general-search-v2).
- To find channels for a suggestion, use [YouTube Channel Search](/apis/youtube/web-v2/search-channels).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [YouTube Channel Community Posts](/apis/youtube/web-v2/channel-community-posts): Returns community posts from a specific YouTube channel, including text content, polls, votes, and comment counts.
- [YouTube Channel Description](/apis/youtube/web-v2/channel-description): Returns YouTube channel details including subscriber counts, video totals, view counts, joined date, and social links.
- [YouTube Channel ID from URL](/apis/youtube/web-v2/channel-id): Resolves a YouTube channel URL to its canonical channel ID.

---
Machine-readable: [`catalog/models/youtube/web-v2/search-suggestions.json`](../../../../catalog/models/youtube/web-v2/search-suggestions.json) · Store page: https://www.sandbase.ai/model/youtube/web-v2/search-suggestions
