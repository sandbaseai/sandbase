# Reddit Search API: pricing, parameters and code examples

`reddit/app/dynamic-search` · data API · Reddit · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Search Reddit posts, communities, comments, media and users with the Reddit app search. Sort by relevance, hot, top, new or comments and filter by time range, with NSFW and safe-search controls.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/app/dynamic-search", "after": "", "allow_nsfw": "0", "need_format": false, "query": "OpenAI", "safe_search": "unset", "search_type": "post"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/app/dynamic-search', {'after': '', 'allow_nsfw': '0', 'need_format': False, 'query': 'OpenAI', 'safe_search': 'unset', 'search_type': 'post'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/app/dynamic-search", {
  "after": "",
  "allow_nsfw": "0",
  "need_format": false,
  "query": "OpenAI",
  "safe_search": "unset",
  "search_type": "post"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/app/dynamic-search", sandbase.Params{
	"after": "",
	"allow_nsfw": "0",
	"need_format": false,
	"query": "OpenAI",
	"safe_search": "unset",
	"search_type": "post",
})
```

Same call via the path form: `POST /v1/api/reddit/app/dynamic-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sort` | string |  | Sort method (only for post/comment/media): RELEVANCE, HOT, TOP, NEW, COMMENTS  |
| `after` | string |  | Pagination parameter for fetching next page default `""` |
| `query` | string | yes | Search keyword  |
| `allow_nsfw` | string |  | Allow NSFW content, "0" or "1" default `"0"` |
| `time_range` | string |  | Time range (only for post/media): all, year, month, week, day, hour  |
| `need_format` | boolean |  | Whether to clean and format the data default `false` |
| `safe_search` | string |  | Safe search setting, "unset" or "strict" default `"unset"` |
| `search_type` | string |  | Search type: post, community, comment, media, people default `"post"` |

## Details

Searches Reddit for a keyword and returns a list of matching results in the Reddit app search layout. It needs one input, `query`, and can search posts, communities, comments, media or people through `search_type`.

### Use cases

- Track new posts that mention a brand or product, sorted by `NEW`.
- Find the subreddits where a topic is discussed most, using `search_type` set to `community`.
- Collect post titles and comment counts for a keyword to compare how much discussion it draws.
- Pull the top posts of the past week for a topic with `sort` set to `TOP` and `time_range` set to `week`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/app/dynamic-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "OpenAI"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search keyword |
| `after` | string | No | Pagination parameter for fetching next page |
| `allow_nsfw` | string | No | Allow NSFW content, "0" or "1" |
| `need_format` | boolean | No | Whether to clean and format the data |
| `safe_search` | string | No | Safe search setting, "unset" or "strict" |
| `search_type` | string | No | Search type: post, community, comment, media, people |
| `sort` | string | No | Sort method (only for post/comment/media): RELEVANCE, HOT, TOP, NEW, COMMENTS |
| `time_range` | string | No | Time range (only for post/media): all, year, month, week, day, hour |

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
                        "id": "t5_7hqomg",
                        "name": "ChatGPT",
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
                              "id": "t3_1xjohbq",
                              "isNsfw": false,
                              "isSpoiler": false,
                              "title": "WTF, OpenAI?!",
                              "type": "IMAGE"
                            },
                            "profile": {
                              "id": "t2_1i6r6u44cc",
                              "name": "_GOREHOUND_"
                            },
                            "search": {
                              "isNsfw": false,
                              "query": "OpenAI",
                              "queryID": "78e0a15d-2fb3-4ea0-ab83-00a3378ce066",
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
                              "id": "t5_7hqomg",
                              "isNsfw": false,
                              "isQuarantined": false,
                              "name": "ChatGPT"
                            }
                          }
                        }
                      },
                      "default": {
                        "__typename": "SearchPDPNavigationBehavior",
                        "id": "t3_1xjohbq",
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
                              "id": "t3_1xjohbq",
                              "isNsfw": false,
                              "isSpoiler": false,
                              "title": "WTF, OpenAI?!",
                              "type": "IMAGE"
                            },
                            "profile": {
                              "id": "t2_1i6r6u44cc",
                              "name": "_GOREHOUND_"
                            },
                            "search": {
                              "isNsfw": false,
                              "query": "OpenAI",
                              "queryID": "78e0a15d-2fb3-4ea0-ab83-00a3378ce066",
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
                              "id": "t5_7hqomg",
                              "isNsfw": false,
                              "isQuarantined": false,
                              "name": "ChatGPT"
                            }
                          }
                        }
                      },
                      "profile": {
                        "__typename": "SearchProfileNavigationBehavior",
                        "id": "t5_el59hc",
                        "name": "u__GOREHOUND_",
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
                              "id": "t3_1xjohbq",
                              "isNsfw": false,
                              "isSpoiler": false,
                              "title": "WTF, OpenAI?!",
                              "type": "IMAGE"
                            },
                            "profile": {
                              "id": "t2_1i6r6u44cc",
                              "name": "_GOREHOUND_"
                            },
                            "search": {
                              "isNsfw": false,
                              "query": "OpenAI",
                              "queryID": "78e0a15d-2fb3-4ea0-ab83-00a3378ce066",
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
                              "id": "t5_7hqomg",
                              "isNsfw": false,
                              "isQuarantined": false,
                              "name": "ChatGPT"
                            }
                          }
                        }
                      },
                      "thumbnail": {
                        "__typename": "SearchPDPNavigationBehavior",
                        "id": "t3_1xjohbq",
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
                              "id": "t3_1xjohbq",
                              "isNsfw": false,
                              "isSpoiler": false,
                              "title": "WTF, OpenAI?!",
                              "type": "IMAGE"
                            },
                            "profile": {
                              "id": "t2_1i6r6u44cc",
                              "name": "_GOREHOUND_"
                            },
                            "search": {
                              "isNsfw": false,
                              "query": "OpenAI",
                              "queryID": "78e0a15d-2fb3-4ea0-ab83-00a3378ce066",
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
                              "id": "t5_7hqomg",
                              "isNsfw": false,
                              "isQuarantined": false,
                              "name": "ChatGPT"
                            }
                          }
                        }
                      }
                    },
                    "post": {
                      "__typename": "SubredditPost",
                      "attributionInfo": null,
                      "authorFlair": null,
                      "authorInfo": {
                        "__typename": "Redditor",
                        "accountType": "USER",
                        "iconSmall": {
                          "__typename": "MediaSource",
                          "dimensions": {
                            "height": 256,
                            "width": 256
                          },
                          "url": "https://www.redditstatic.com/avatars/defaults/v2/avatar_default_4.png"
                        },
                        "id": "t2_1i6r6u44cc",
                        "isBlocked": false,
                        "isCakeDayNow": false,
                        "name": "_GOREHOUND_",
                        "newIcon": {
                          "__typename": "MediaSource",
                          "dimensions": {
                            "height": 256,
                            "width": 256
                          },
                          "url": "https://www.redditstatic.com/avatars/defaults/v2/avatar_default_4.png"
                        }
                      },
                      "awardings": [],
                      "commentCount": 121,
                      "content": null,
                      "createdAt": "2026-10-30T19:12:42.108000+0000"
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
                          "id": "t3_1xjohbq",
                          "isNsfw": false,
                          "isSpoiler": false,
                          "title": "WTF, OpenAI?!",
                          "type": "IMAGE"
                        },
                        "profile": {
                          "id": "t2_1i6r6u44cc",
                          "name": "_GOREHOUND_"
                        },
                        "search": {
                          "isNsfw": false,
                          "query": "OpenAI",
                          "queryID": "78e0a15d-2fb3-4ea0-ab83-00a3378ce066",
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
                          "id": "t5_7hqomg",
                          "isNsfw": false,
                          "isQuarantined": false,
                          "name": "ChatGPT"
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
              "query": "OpenAI",
              "queryID": "78e0a15d-2fb3-4ea0-ab83-00a3378ce066",
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
                  "query": "OpenAI"
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
                "query": "OpenAI"
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
| `search.dynamic.components.main.edges[].node.children[]` | Result items for the page. Each item has a `__typename` such as `SearchPost` that shows the result type. |
| `search.dynamic.components.main.edges[].node.children[].post.id` | Post ID in the form `t3_...`. |
| `search.dynamic.components.main.edges[].node.children[].post.createdAt` | Creation time of the post as an ISO 8601 timestamp with a UTC offset. |
| `search.dynamic.components.main.edges[].node.children[].post.commentCount` | Number of comments on the post. |
| `search.dynamic.components.main.edges[].node.children[].post.authorInfo.name` | Username of the post author. |
| `search.dynamic.components.main.edges[].node.children[].post.authorInfo.id` | Author account ID in the form `t2_...`. |
| `search.dynamic.components.main.edges[].node.children[].behaviors.community.name` | Name of the subreddit where the post appears. |
| `search.dynamic.components.main.edges[].node.children[].behaviors.community.id` | Subreddit ID in the form `t5_...`. |
| `search.dynamic.components.main.edges[].node.children[].telemetry.trackingContext.post.title` | Title of the post. |
| `search.dynamic.components.main.edges[].node.children[].telemetry.trackingContext.post.type / search.dynamic.components.main.edges[].node.children[].telemetry.trackingContext.post.isNsfw` | Post format, such as `IMAGE`, and whether the post is marked NSFW. |

### Notes

- The tracking context under each item repeats the post title, type and NSFW flag. The `post` object itself carries the author, comment count and creation time.
- `sort` works only for post, comment and media searches. `time_range` works only for post and media searches.
- Pass the cursor from the response as `after` to get the next page.
- Set `need_format` to `true` to get cleaned data. To read a full post, call [Reddit Post Details](/apis/reddit/app/post-details) with a post ID, or [Reddit App Post Comments](/apis/reddit/app/post-comments) for its comments.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Check if Subreddit is Muted](/apis/reddit/app/check-subreddit-muted): Check if a specified Reddit subreddit is muted by the current user.
- [Fetch Reddit APP Comment Replies (Sub-comments)](/apis/reddit/app/comment-replies): Fetch replies (sub-comments/second-level comments) under a specified Reddit APP comment Use this endpoint when a comment node has more.cursor field to get its …
- [Fetch Reddit APP Community Highlights](/apis/reddit/app/community-highlights): Fetch featured highlight content of a specified Reddit APP community, including popular posts and important announcements.

---
Machine-readable: [`catalog/models/reddit/app/dynamic-search.json`](../../../../catalog/models/reddit/app/dynamic-search.json) · Store page: https://www.sandbase.ai/model/reddit/app/dynamic-search
