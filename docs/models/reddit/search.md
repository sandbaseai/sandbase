# Reddit Keyword Search API: pricing, parameters and code examples

`reddit/search` · data API · Reddit · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Search Reddit posts by keyword with an optional continuation token. Use it to discover topic-related discussions or continue through additional search-result pages.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/search", "keyword": "iphone"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/search', {'keyword': 'iphone'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/search", {
  "keyword": "iphone"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/search", sandbase.Params{
	"keyword": "iphone",
})
```

Same call via the path form: `POST /v1/api/reddit/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `after` | string |  | Pagination token to retrieve the next set of results.  |
| `keyword` | string | yes | Search query keywords.  |

## Details

Returns Reddit posts that match a keyword search. The only required input is `keyword`, and an optional `after` token fetches the next page of results.

### Use cases

- Find recent discussions about a product name such as `iphone` across all of Reddit.
- Collect the subreddits where a topic comes up most often.
- Build a list of post titles and authors to review for brand or topic monitoring.
- Page through search results with `after` to build a larger sample of posts on one topic.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "iphone"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search query keywords. |
| `after` | string | No | Pagination token to retrieve the next set of results. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "search": {
    "dynamic": {
      "components": {
        "__typename": "SearchResultsMainLayout",
        "appliedState": {
          "__typename": "SearchAppliedState",
          "filters": [
            {
              "key": "component",
              "value": "SearchAppliedState"
            }
          ],
          "pane": "posts"
        },
        "main": {
          "edges": [
            {
              "cursor": "",
              "node": {
                "__typename": "SearchListComponent",
                "behaviors": {
                  "header": null
                },
                "children": [
                  {
                    "__typename": "SearchPost",
                    "behaviors": {
                      "community": {
                        "__typename": "SearchCommunityNavigationBehavior",
                        "id": "t5_2qh2b",
                        "name": "iphone",
                        "telemetry": {
                          "__typename": "SearchElementTelemetry",
                          "events": [
                            {
                              "action": "click",
                              "noun": "post",
                              "source": "search",
                              "trigger": "CLICK",
                              "triggerConfiguration": null
                            }
                          ],
                          "trackingContext": {
                            "__typename": "SearchTelemetryTrackingContext",
                            "actionInfo": {
                              "paneName": "posts",
                              "position": 0,
                              "reason": null,
                              "relativePosition": 0,
                              "type": "community"
                            },
                            "answers": null,
                            "metaSearch": null,
                            "post": {
                              "id": "t3_1xlp71j",
                              "isNsfw": false,
                              "isSpoiler": false,
                              "title": "iPhone tricks that still surprise people who’ve used an iPhone for years",
                              "type": "TEXT"
                            },
                            "profile": {
                              "id": "t2_2pornx1d3s",
                              "name": "sweet-bae7"
                            },
                            "search": {
                              "isNsfw": false,
                              "query": "iphone",
                              "queryID": "c030a721-88ba-4f19-99a9-613f1547cdd9",
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
                            "subreddit": {
                              "id": "t5_2qh2b",
                              "isNsfw": false,
                              "isQuarantined": false,
                              "name": "iphone"
                            }
                          }
                        }
                      },
                      "default": {
                        "__typename": "SearchPDPNavigationBehavior",
                        "id": "t3_1xlp71j",
                        "telemetry": {
                          "__typename": "SearchElementTelemetry",
                          "events": [
                            {
                              "action": "click",
                              "noun": "post",
                              "source": "search",
                              "trigger": "CLICK",
                              "triggerConfiguration": null
                            }
                          ],
                          "trackingContext": {
                            "__typename": "SearchTelemetryTrackingContext",
                            "actionInfo": {
                              "paneName": "posts",
                              "position": 0,
                              "reason": null,
                              "relativePosition": 0,
                              "type": "post"
                            },
                            "answers": null,
                            "metaSearch": null,
                            "post": {
                              "id": "t3_1xlp71j",
                              "isNsfw": false,
                              "isSpoiler": false,
                              "title": "iPhone tricks that still surprise people who’ve used an iPhone for years",
                              "type": "TEXT"
                            },
                            "profile": {
                              "id": "t2_2pornx1d3s",
                              "name": "sweet-bae7"
                            },
                            "search": {
                              "isNsfw": false,
                              "query": "iphone",
                              "queryID": "c030a721-88ba-4f19-99a9-613f1547cdd9",
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
                            "subreddit": {
                              "id": "t5_2qh2b",
                              "isNsfw": false,
                              "isQuarantined": false,
                              "name": "iphone"
                            }
                          }
                        }
                      },
                      "profile": {
                        "__typename": "SearchProfileNavigationBehavior",
                        "id": "t5_km4y14",
                        "name": "u_sweet-bae7",
                        "telemetry": {
                          "__typename": "SearchElementTelemetry",
                          "events": [
                            {
                              "action": "click",
                              "noun": "post",
                              "source": "search",
                              "trigger": "CLICK",
                              "triggerConfiguration": null
                            }
                          ],
                          "trackingContext": {
                            "__typename": "SearchTelemetryTrackingContext",
                            "actionInfo": {
                              "paneName": "posts",
                              "position": 0,
                              "reason": null,
                              "relativePosition": 0,
                              "type": "profile"
                            },
                            "answers": null,
                            "metaSearch": null,
                            "post": {
                              "id": "t3_1xlp71j",
                              "isNsfw": false,
                              "isSpoiler": false,
                              "title": "iPhone tricks that still surprise people who’ve used an iPhone for years",
                              "type": "TEXT"
                            },
                            "profile": {
                              "id": "t2_2pornx1d3s",
                              "name": "sweet-bae7"
                            },
                            "search": {
                              "isNsfw": false,
                              "query": "iphone",
                              "queryID": "c030a721-88ba-4f19-99a9-613f1547cdd9",
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
                            "subreddit": {
                              "id": "t5_2qh2b",
                              "isNsfw": false,
                              "isQuarantined": false,
                              "name": "iphone"
                            }
                          }
                        }
                      },
                      "thumbnail": {
                        "__typename": "SearchPDPNavigationBehavior",
                        "id": "t3_1xlp71j",
                        "telemetry": {
                          "__typename": "SearchElementTelemetry",
                          "events": [
                            {
                              "action": "click",
                              "noun": "post",
                              "source": "search",
                              "trigger": "CLICK",
                              "triggerConfiguration": null
                            }
                          ],
                          "trackingContext": {
                            "__typename": "SearchTelemetryTrackingContext",
                            "actionInfo": {
                              "paneName": "posts",
                              "position": 0,
                              "reason": null,
                              "relativePosition": 0,
                              "type": "thumbnail"
                            },
                            "answers": null,
                            "metaSearch": null,
                            "post": {
                              "id": "t3_1xlp71j",
                              "isNsfw": false,
                              "isSpoiler": false,
                              "title": "iPhone tricks that still surprise people who’ve used an iPhone for years",
                              "type": "TEXT"
                            },
                            "profile": {
                              "id": "t2_2pornx1d3s",
                              "name": "sweet-bae7"
                            },
                            "search": {
                              "isNsfw": false,
                              "query": "iphone",
                              "queryID": "c030a721-88ba-4f19-99a9-613f1547cdd9",
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
                            "subreddit": {
                              "id": "t5_2qh2b",
                              "isNsfw": false,
                              "isQuarantined": false,
                              "name": "iphone"
                            }
                          }
                        }
                      }
                    },
                    "post": {
                      "__typename": "SubredditPost",
                      "attributionInfo": null,
                      "authorFlair": {
                        "__typename": "AuthorFlair",
                        "richtext": null,
                        "template": {
                          "backgroundColor": null,
                          "id": null
                        },
                        "text": "Human Detected",
                        "textColor": "DARK"
                      },
                      "authorInfo": {
                        "__typename": "Redditor",
                        "accountType": "USER",
                        "iconSmall": {
                          "__typename": "MediaSource",
                          "dimensions": {
                            "height": 256,
                            "width": 256
                          },
                          "url": "https://www.redditstatic.com/avatars/defaults/v2/avatar_default_0.png"
                        },
                        "id": "t2_2pornx1d3s",
                        "isBlocked": false,
                        "isCakeDayNow": false,
                        "name": "sweet-bae7",
                        "newIcon": {
                          "__typename": "MediaSource",
                          "dimensions": {
                            "height": 256,
                            "width": 256
                          },
                          "url": "https://www.redditstatic.com/avatars/defaults/v2/avatar_default_0.png"
                        }
                      },
                      "awardings": [
                        {
                          "__typename": "AwardingTotal",
                          "award": {
                            "__typename": "Award",
                            "id": "award_helpful_3",
                            "name": "Helpful",
                            "static_icon_16": {
                              "__typename": "MediaSource",
                              "dimensions": {
                                "height": 16,
                                "width": 16
                              },
                              "url": "https://i.redd.it/snoovatar/snoo_assets/marketing/Helpful_16.png"
                            },
                            "static_icon_24": {
                              "__typename": "MediaSource",
                              "dimensions": {
                                "height": 24,
                                "width": 24
                              },
                              "url": "https://i.redd.it/snoovatar/snoo_assets/marketing/Helpful_24.png"
                            },
                            "static_icon_32": {
                              "__typename": "MediaSource",
                              "dimensions": {
                                "height": 32,
                                "width": 32
                              },
                              "url": "https://i.redd.it/snoovatar/snoo_assets/marketing/Helpful_32.png"
                            },
                            "static_icon_48": {
                              "__typename": "MediaSource",
                              "dimensions": {
                                "height": 48,
                                "width": 48
                              },
                              "url": "https://i.redd.it/snoovatar/snoo_assets/marketing/Helpful_48.png"
                            },
                            "static_icon_64": {
                              "__typename": "MediaSource",
                              "dimensions": {
                                "height": 64,
                                "width": 64
                              },
                              "url": "https://i.redd.it/snoovatar/snoo_assets/marketing/Helpful_64.png"
                            }
                          },
                          "awardingByCurrentUser": [],
                          "total": 1
                        }
                      ],
                      "commentCount": 458,
                      "content": {
                        "html": "Numbers without switching keyboards: Press and hold the “123” key, slide your fi…",
                        "markdown": "Numbers without switching keyboards: Press and hold the “123” key, slide your fi…",
                        "preview": "Numbers without switching keyboards: Press and hold the “123” key, slide your fi…",
                        "richtext": "{\"document\":[{\"c\":[{\"e\":\"text\",\"t\":\"Numbers without switching keyboards: Press a…",
                        "richtextMedia": []
                      },
                      "createdAt": "2026-11-02T05:45:58.931000+0000"
                    },
                    "telemetry": {
                      "__typename": "SearchElementTelemetry",
                      "events": [
                        {
                          "action": "view",
                          "noun": "post",
                          "source": "search",
                          "trigger": "VIEW",
                          "triggerConfiguration": null
                        }
                      ],
                      "trackingContext": {
                        "__typename": "SearchTelemetryTrackingContext",
                        "actionInfo": {
                          "paneName": "posts",
                          "position": 0,
                          "reason": null,
                          "relativePosition": 0,
                          "type": null
                        },
                        "answers": null,
                        "metaSearch": null,
                        "post": {
                          "id": "t3_1xlp71j",
                          "isNsfw": false,
                          "isSpoiler": false,
                          "title": "iPhone tricks that still surprise people who’ve used an iPhone for years",
                          "type": "TEXT"
                        },
                        "profile": {
                          "id": "t2_2pornx1d3s",
                          "name": "sweet-bae7"
                        },
                        "search": {
                          "isNsfw": false,
                          "query": "iphone",
                          "queryID": "c030a721-88ba-4f19-99a9-613f1547cdd9",
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
                        "subreddit": {
                          "id": "t5_2qh2b",
                          "isNsfw": false,
                          "isQuarantined": false,
                          "name": "iphone"
                        }
                      }
                    }
                  }
                ],
                "presentation": {
                  "__typename": "SearchListComponentDefaultPresentation",
                  "isDefaultPresentation": false
                }
              }
            }
          ],
          "pageInfo": {
            "endCursor": "eyJjYW5kaWRhdGVzX3JldHVybmVkIjoie1wic2VjdGlvbl8xX3BpcGVsaW5lXzBfZ2xvYmFsX21vZGlm…",
            "hasNextPage": true,
            "hasPreviousPage": false,
            "startCursor": ""
          }
        },
        "telemetry": {
          "__typename": "SearchElementTelemetry",
          "events": [
            {
              "action": "load",
              "noun": "feed",
              "source": "search",
              "trigger": "LOAD",
              "triggerConfiguration": null
            }
          ],
          "trackingContext": {
            "__typename": "SearchTelemetryTrackingContext",
            "actionInfo": {
              "paneName": "posts",
              "position": null,
              "reason": null,
              "relativePosition": null,
              "type": null
            },
            "answers": null,
            "metaSearch": null,
            "post": null,
            "profile": null,
            "search": {
              "isNsfw": false,
              "query": "iphone",
              "queryID": "c030a721-88ba-4f19-99a9-613f1547cdd9",
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
        },
        "top": {
          "filterBar": [
            {
              "__typename": "SearchDropdown",
              "behaviors": [
                {
                  "__typename": "SearchFilterBehavior",
                  "filters": [
                    {
                      "key": "sort",
                      "value": "RELEVANCE"
                    }
                  ],
                  "id": "relevance",
                  "isAppliedFiltersRemoved": false,
                  "isAppliedOptionsRemoved": false,
                  "options": [],
                  "pane": "posts",
                  "query": "iphone"
                }
              ],
              "presentation": {
                "__typename": "SearchFilterOptionListPresentation",
                "buttonText": "Relevance",
                "id": "post_sort",
                "options": [
                  {
                    "isSelected": true,
                    "secondaryText": null,
                    "text": "Relevance"
                  }
                ],
                "title": "Sort by"
              }
            }
          ],
          "filterModal": null,
          "navigation": {
            "__typename": "SearchNavigationList",
            "behaviors": [
              {
                "__typename": "SearchFilterBehavior",
                "filters": [
                  {
                    "key": "safe_search",
                    "value": "unset"
                  }
                ],
                "id": "all",
                "isAppliedFiltersRemoved": true,
                "isAppliedOptionsRemoved": false,
                "options": [
                  {
                    "key": "mode",
                    "value": "search"
                  }
                ],
                "pane": "all",
                "query": "iphone"
              }
            ],
            "listPresentation": {
              "items": [
                {
                  "id": "all",
                  "isSelected": false,
                  "text": "All"
                }
              ]
            }
          }
        }
      }
    }
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `search.dynamic.components.main.edges[].node.children[]` | One search result. In the sample, `__typename` is `SearchPost`, which marks a post result. |
| `search.dynamic.components.main.edges[].node.children[].behaviors.default.id` | ID of the post, for example `t3_1xlp71j`. |
| `search.dynamic.components.main.edges[].node.children[].behaviors.default.telemetry.trackingContext.post.title` | Title of the post. |
| `search.dynamic.components.main.edges[].node.children[].behaviors.default.telemetry.trackingContext.post.type / isNsfw / isSpoiler` | Post type (for example `TEXT`) and whether the post is flagged NSFW or as a spoiler. |
| `search.dynamic.components.main.edges[].node.children[].behaviors.community.name / id` | Name and ID of the subreddit that holds the post, for example `iphone` and `t5_2qh2b`. |
| `search.dynamic.components.main.edges[].node.children[].post.authorInfo.name / id` | Username and user ID of the post author. |
| `search.dynamic.components.main.edges[].node.children[].post.authorFlair.text` | Flair text shown next to the author, when one is set. |
| `search.dynamic.components.main.edges[].node.children[].post.awardings[].award.name / total` | Name of each award the post received and how many times it was given. |
| `search.dynamic.components.main.edges[].node.children[].behaviors.default.telemetry.trackingContext.search.query / queryID` | The keyword that was searched and the ID of this search request. |
| `search.dynamic.components.appliedState.filters[]` | Filters applied to the search as `key` and `value` pairs, such as `safe_search` and `experience_selection`. |

### Notes

- Send the first request with only `keyword`. To get more results, send the same `keyword` with the `after` pagination token.
- IDs carry a type prefix: `t3_` for posts, `t2_` for users and `t5_` for subreddits.
- To read the discussion under a post, call [Reddit Post Comments](/apis/reddit/post-comments). For the post itself, call [Reddit Post](/apis/reddit/post).
- To search for communities instead of posts, use [Reddit Subreddit Search](/apis/reddit/subreddit-search).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/reddit/search.json`](../../../catalog/models/reddit/search.json) · Store page: https://www.sandbase.ai/model/reddit/search
