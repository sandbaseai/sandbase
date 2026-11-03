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

Returns Reddit search box autocomplete suggestions for a typed text. It needs one input, `query`, and returns suggested search phrases plus matching subreddits.

### Use cases

- Build a search box for a custom Reddit client that shows suggestions as the user types.
- Find subreddits that match a brand or topic name, such as the communities that appear for `OpenAI`.
- Collect the phrases Reddit suggests for a keyword to find related search terms.
- Resolve a topic to a subreddit ID and URL path before calling a subreddit API.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/app/search-typeahead" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "OpenAI"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search keyword, the search text being typed |
| `allow_nsfw` | string | No | Whether to allow NSFW (adult) content display, "0" means disallow, "1" means allow |
| `need_format` | boolean | No | Whether to clean and format the data |
| `safe_search` | string | No | Safe search setting, options are "unset" or "strict" |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "search": {
    "dynamic": {
      "components": {
        "__typename": "TypeaheadLayout",
        "main": [
          {
            "__typename": "SearchTypeaheadList",
            "behaviors": {
              "collapse": null,
              "expand": null,
              "expandCta": null
            },
            "children": [
              {
                "__typename": "QueryAutocomplete",
                "behaviors": {
                  "default": {
                    "__typename": "SearchQueryReformulationBehavior",
                    "query": "openai",
                    "telemetry": {
                      "__typename": "SearchElementTelemetry",
                      "events": [
                        {
                          "action": "click",
                          "noun": "typeahead",
                          "source": "search",
                          "trigger": "CLICK",
                          "triggerConfiguration": null
                        }
                      ],
                      "trackingContext": {
                        "__typename": "SearchTelemetryTrackingContext",
                        "actionInfo": {
                          "paneName": null,
                          "position": 0,
                          "reason": null,
                          "relativePosition": 0,
                          "type": "query_suggestion"
                        },
                        "answers": null,
                        "metaSearch": {
                          "displayQuery": "openai",
                          "rawQuery": "openai"
                        },
                        "post": null,
                        "profile": null,
                        "search": {
                          "isNsfw": false,
                          "query": "OpenAI",
                          "queryID": "f2458504-7cda-400f-abc7-324fd62e4f9f",
                          "range": null,
                          "safeSearch": "UNAVAILABLE",
                          "scope": {
                            "id": null,
                            "name": null,
                            "path": "/",
                            "type": "GLOBAL"
                          },
                          "snippet": null,
                          "snippetId": null
                        },
                        "subreddit": null
                      }
                    }
                  }
                },
                "presentation": {
                  "__typename": "QueryAutocompleteDefaultPresentation",
                  "query": "openai",
                  "suggestion": "%query%"
                },
                "telemetry": {
                  "__typename": "SearchElementTelemetry",
                  "events": [
                    {
                      "action": "view",
                      "noun": "typeahead",
                      "source": "search",
                      "trigger": "VIEW",
                      "triggerConfiguration": null
                    }
                  ],
                  "trackingContext": {
                    "__typename": "SearchTelemetryTrackingContext",
                    "actionInfo": {
                      "paneName": null,
                      "position": 0,
                      "reason": null,
                      "relativePosition": 0,
                      "type": "query_suggestion"
                    },
                    "answers": null,
                    "metaSearch": {
                      "displayQuery": "openai",
                      "rawQuery": "openai"
                    },
                    "post": null,
                    "profile": null,
                    "search": {
                      "isNsfw": false,
                      "query": "OpenAI",
                      "queryID": "f2458504-7cda-400f-abc7-324fd62e4f9f",
                      "range": null,
                      "safeSearch": "UNAVAILABLE",
                      "scope": {
                        "id": null,
                        "name": null,
                        "path": "/",
                        "type": "GLOBAL"
                      },
                      "snippet": null,
                      "snippetId": null
                    },
                    "subreddit": null
                  }
                }
              }
            ],
            "id": "section_0_pipeline_1_query_autocomplete",
            "presentation": {
              "__typename": "SearchTypeaheadListDefaultPresentation",
              "title": ""
            }
          }
        ]
      }
    }
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `search.dynamic.components.main[]` | Sections of the typeahead list. One section holds query suggestions (`QueryAutocomplete`) and another holds subreddit suggestions (`TypeaheadSuggestion`). |
| `search.dynamic.components.main[].children[].__typename` | Type of each suggestion. `QueryAutocomplete` is a search phrase and `TypeaheadSuggestion` is a community result. |
| `search.dynamic.components.main[].children[].behaviors.default.query` | The full search phrase to run if the user picks this suggestion. Present on query suggestions. |
| `search.dynamic.components.main[].children[].presentation.suggestion` | Display template for a query suggestion. The `%query%` token stands for the typed text. |
| `search.dynamic.components.main[].children[].behaviors.default.id / search.dynamic.components.main[].children[].behaviors.default.name` | ID and name of the suggested subreddit, for example `t5_7hqomg` and `ChatGPT`. |
| `search.dynamic.components.main[].children[].behaviors.default.url` | Relative path of the suggested subreddit, for example `/r/ChatGPT/`. |
| `search.dynamic.components.main[].children[].presentation.name` | Display name of the suggested subreddit, for example `r/ChatGPT`. |
| `search.dynamic.components.main[].children[].presentation.description / search.dynamic.components.main[].children[].presentation.icon` | Short description text and icon image URL for a subreddit suggestion. |
| `search.dynamic.components.main[].children[].telemetry.trackingContext.actionInfo.position` | Zero-based position of the suggestion in its list. `type` in the same object shows the kind, such as `query_suggestion` or `subreddit`. |
| `search.dynamic.components.main[].children[].telemetry.trackingContext.search.queryID` | UUID that identifies this typeahead request. All suggestions in one response share it. |

### Notes

- Pass the text typed so far in `query`. The search `query` is echoed back inside the tracking context.
- `allow_nsfw` takes `"0"` or `"1"`, and `safe_search` takes `"unset"` or `"strict"`.
- Subreddit IDs use the `t5_` prefix. Use them with [Reddit App Subreddit Info](/apis/reddit/app/subreddit-info) or [Reddit Community Highlights](/apis/reddit/app/community-highlights).
- To run the full search for a chosen phrase, call [Reddit Search](/apis/reddit/app/dynamic-search).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Reddit Subreddit Mute Status](/apis/reddit/app/check-subreddit-muted): Checks whether a specified Reddit subreddit is muted by the current account using its ID.
- [Reddit App Comment Replies](/apis/reddit/app/comment-replies): Returns replies and nested sub-comments under a Reddit post comment using a continuation cursor.
- [Reddit Community Highlights](/apis/reddit/app/community-highlights): Returns featured highlight content for a designated Reddit community, such as popular posts and announcements, by subreddit ID.

---
Machine-readable: [`catalog/models/reddit/app/search-typeahead.json`](../../../../catalog/models/reddit/app/search-typeahead.json) · Store page: https://www.sandbase.ai/model/reddit/app/search-typeahead
