# Reddit App Search Typeahead API: pricing, parameters and code examples

`reddit/app/search-typeahead` · data API · Reddit · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns autocomplete suggestions for the Reddit search box based on typed input. Includes options to toggle adult content, apply safe search settings, and format response data.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/app/search-typeahead", "query": "OpenAI"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/app/search-typeahead', {'query': 'OpenAI'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/app/search-typeahead", {
  "query": "OpenAI"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/app/search-typeahead", sandbase.Params{
	"query": "OpenAI",
})
```

Same call via the path form: `POST /v1/api/reddit/app/search-typeahead` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Search keyword, the search text being typed  |
| `allow_nsfw` | string |  | Whether to allow NSFW (adult) content display, "0" means disallow, "1" means allow default `"0"` |
| `need_format` | boolean |  | Whether to clean and format the data default `false` |
| `safe_search` | string |  | Safe search setting, options are "unset" or "strict" default `"unset"` |

## Details

Query autocomplete suggestions for search terms using the `query` parameter. You can also configure adult content visibility and safe search behavior.

### Use cases

- Display real-time search suggestions in custom Reddit clients.
- Help users discover relevant subreddits and search terms as they type.
- Filter autocomplete suggestions according to safe search requirements.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/app/search-typeahead" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "OpenAI"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search keyword, the search text being typed |
| `allow_nsfw` | string | No | Whether to allow NSFW (adult) content display, "0" means disallow, "1" means allow |
| `need_format` | boolean | No | Whether to clean and format the data |
| `safe_search` | string | No | Safe search setting, options are "unset" or "strict" |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "search": {
    "dynamic": {
      "components": {
        "main": [
          {
            "children": [
              {
                "__typename": "QueryAutocomplete",
                "presentation": {
                  "__typename": "QueryAutocompleteDefaultPresentation",
                  "query": "openai"
                },
                "telemetry": {
                  "__typename": "SearchElementTelemetry"
                }
              }
            ]
          }
        ]
      }
    }
  }
}
```

### Notes

- Set `allow_nsfw` to "1" to include adult content or "0" to exclude it.
- The `safe_search` parameter accepts "unset" or "strict".

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Reddit Subreddit Mute Status](/model/reddit/app/check-subreddit-muted): Checks whether a specified Reddit subreddit is muted by the current account using its ID.
- [Reddit App Comment Replies](/model/reddit/app/comment-replies): Returns replies and nested sub-comments under a Reddit post comment using a continuation cursor.
- [Reddit Community Highlights](/model/reddit/app/community-highlights): Returns featured highlight content for a designated Reddit community, such as popular posts and announcements, by subreddit ID.

---
Machine-readable: [`catalog/models/reddit/app/search-typeahead.json`](../../../../catalog/models/reddit/app/search-typeahead.json) · Store page: https://www.sandbase.ai/model/reddit/app/search-typeahead
