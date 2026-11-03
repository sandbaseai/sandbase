# Shorts search (raw data, recommend V2) API: pricing, parameters and code examples

`youtube/web-v2/shorts-search` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

YouTube Shorts specialized search using native YouTube API.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/web-v2/shorts-search", "search_query": "Python编程"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/web-v2/shorts-search', {'search_query': 'Python编程'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/web-v2/shorts-search", {
  "search_query": "Python编程"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/web-v2/shorts-search", sandbase.Params{
	"search_query": "Python编程",
})
```

Same call via the path form: `POST /v1/api/youtube/web-v2/shorts-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sort_by` |  |  | Sort by for Shorts  |
| `time_zone` | string |  | Time zone (e.g., America/Los_Angeles, Asia/Shanghai) default `"America/Los_Angeles"` |
| `upload_time` |  |  | Upload time filter for Shorts  |
| `country_code` | string |  | Country code affecting regional relevance default `"US"` |
| `search_query` | string | yes | Search keyword  |
| `language_code` | string |  | Language code (zh-CN for Chinese, en-US for English) default `"en-US"` |
| `continuation_token` |  |  | Pagination token  |
| `filter_mixed_content` | boolean |  | Whether to filter long videos from mixed content (default true) default `true` |

## Details

Returns YouTube Shorts search results for a keyword, in YouTube's own response format. Each result is a Short with its video ID, a text summary that includes the title and view count, and player data. The only required input is `search_query`.

### Use cases

- Find recent Shorts about a topic such as NASA to track what creators are posting.
- Sort Shorts by `view_count` to find the most watched clips for a keyword.
- Limit results with `upload_time` to monitor new Shorts from the last hour or day.
- Collect video IDs from a search and pass them to a video detail or comments API.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web-v2/shorts-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"search_query": "NASA"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `search_query` | string | Yes | Search keyword |
| `continuation_token` | string | No | Pagination token |
| `country_code` | string | No | Country code affecting regional relevance |
| `filter_mixed_content` | boolean | No | Whether to filter long videos from mixed content (default true) |
| `language_code` | string | No | Language code (zh-CN for Chinese, en-US for English) |
| `sort_by` | string | No | Sort by for Shorts |
| `time_zone` | string | No | Time zone (e.g., America/Los_Angeles, Asia/Shanghai) |
| `upload_time` | string | No | Upload time filter for Shorts |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "contents": {
    "twoColumnSearchResultsRenderer": {
      "primaryContents": {
        "sectionListRenderer": {
          "contents": [
            {
              "itemSectionRenderer": {
                "contents": [
                  {
                    "gridShelfViewModel": {
                      "contentAspectRatio": "GRID_SHELF_CONTENT_ASPECT_RATIO_TWO_BY_THREE",
                      "contents": [
                        {
                          "shortsLockupViewModel": {
                            "accessibilityText": "NASA's simulated Mars mission crew emerges after 378 days, 18 thousand views - p…",
                            "badge": {
                              "badgeViewModel": {
                                "accessibilityLabel": "New",
                                "badgeStyle": "BADGE_OVERLAY_WHITE",
                                "badgeText": "New",
                                "loggingDirectives": {
                                  "gestures": {
                                    "types": "2"
                                  },
                                  "trackingParams": "CJkDEJTOCyITCIzrs-in65cDFaqP0QQdHDI2MA==",
                                  "visibility": {
                                    "types": "12"
                                  }
                                },
                                "trackingParams": "CJkDEJTOCyITCIzrs-in65cDFaqP0QQdHDI2MA=="
                              }
                            },
                            "entityId": "shorts-shelf-item-1KtjAcwK1bU",
                            "indexInCollection": 0,
                            "inlinePlayerData": {
                              "enableAudioControl": true,
                              "maxPlaybackLengthSec": 0,
                              "onVisible": {
                                "innertubeCommand": {
                                  "clickTrackingParams": "CJcDEIf2BBgAIhMIjOuz6KfrlwMVqo_RBB0cMjYwMgZzZWFyY2hSBE5BU0GaAQUIMhD0JMoBBJHNdqA=",
                                  "commandMetadata": {
                                    "webCommandMetadata": {
                                      "rootVe": 3832,
                                      "url": "/watch?v=1KtjAcwK1bU&pp=YAHIAQHwAQG6AwIYAqIGFQGodqkzJtG3cTVNPwiReP8b7uTVyJAHAg%3…",
                                      "webPageType": "WEB_PAGE_TYPE_WATCH"
                                    }
                                  },
                                  "watchEndpoint": {
                                    "playerExtraUrlParams": [
                                      {
                                        "key": "inline",
                                        "value": "1"
                                      }
                                    ],
                                    "playerParams": "YAHIAQHwAQG6AwIYAqIGFQGodqkzJtG3cTVNPwiReP8b7uTVyJAHAg%3D%3D",
                                    "videoId": "1KtjAcwK1bU",
                                    "watchEndpointSupportedOnesieConfig": {
                                      "html5PlaybackOnesieConfig": {
                                        "commonConfig": {
                                          "url": "https://rr5---sn-bvvbaxivnuxqjvhj5nu-hp5e.googlevideo.com/initplayback?source=yo…"
                                        }
                                      }
                                    }
                                  }
                                }
                              }
                            },
                            "inlinePopStateEntityKey": "Eh1zaG9ydHMtc2hlbGYtaXRlbS0xS3RqQWN3SzFiVSDMAygB0.570618",
                            "loggingDirectives": {
                              "gestures": {
                                "types": "2"
                              },
                              "trackingParams": "CJcDEIf2BBgAIhMIjOuz6KfrlwMVqo_RBB0cMjYw",
                              "useGreenPath": true,
                              "visibility": {
                                "types": "12"
                              }
                            },
                            "menuOnTap": {
                              "innertubeCommand": {
                                "clickTrackingParams": "CJcDEIf2BBgAIhMIjOuz6KfrlwMVqo_RBB0cMjYwygEEkc12oA==",
                                "showSheetCommand": {
                                  "panelLoadingStrategy": {
                                    "inlineContent": {
                                      "sheetViewModel": {
                                        "content": {
                                          "listViewModel": {
                                            "listItems": [
                                              {
                                                "listItemViewModel": {
                                                  "leadingImage": {
                                                    "sources": [
                                                      {
                                                        "clientResource": {
                                                          "imageName": "ADD_TO_QUEUE_TAIL"
                                                        }
                                                      }
                                                    ]
                                                  },
                                                  "rendererContext": {
                                                    "commandContext": {
                                                      "onTap": {
                                                        "innertubeCommand": {
                                                          "clickTrackingParams": "CJgDEP6YBBgCIhMIjOuz6KfrlwMVqo_RBB0cMjYwygEEkc12oA==",
                                                          "commandMetadata": {
                                                            "webCommandMetadata": {
                                                              "sendPost": true
                                                            }
                                                          },
                                                          "signalServiceEndpoint": {
                                                            "actions": [
                                                              {
                                                                "addToPlaylistCommand": {
                                                                  "listType": "PLAYLIST_EDIT_LIST_TYPE_QUEUE",
                                                                  "onCreateListCommand": {
                                                                    "clickTrackingParams": "CJgDEP6YBBgCIhMIjOuz6KfrlwMVqo_RBB0cMjYwygEEkc12oA==",
                                                                    "commandMetadata": {
                                                                      "webCommandMetadata": {
                                                                        "apiUrl": "/youtubei/v1/playlist/create",
                                                                        "sendPost": true
                                                                      }
                                                                    },
                                                                    "createPlaylistServiceEndpoint": {
                                                                      "params": "CAQ%3D",
                                                                      "videoIds": [
                                                                        "1KtjAcwK1bU"
                                                                      ]
                                                                    }
                                                                  },
                                                                  "openMiniplayer": true,
                                                                  "videoCommand": {
                                                                    "clickTrackingParams": "CJgDEP6YBBgCIhMIjOuz6KfrlwMVqo_RBB0cMjYwygEEkc12oA==",
                                                                    "commandMetadata": {
                                                                      "webCommandMetadata": {
                                                                        "rootVe": 3832,
                                                                        "url": "/watch?v=1KtjAcwK1bU",
                                                                        "webPageType": "WEB_PAGE_TYPE_WATCH"
                                                                      }
                                                                    },
                                                                    "watchEndpoint": {
                                                                      "videoId": "1KtjAcwK1bU",
                                                                      "watchEndpointSupportedOnesieConfig": {
                                                                        "html5PlaybackOnesieConfig": {
                                                                          "commonConfig": {
                                                                            "url": "https://rr5---sn-bvvbaxivnuxqjvhj5nu-hp5e.googlevideo.com/initplayback?source=yo…"
                                                                          }
                                                                        }
                                                                      }
                                                                    }
                                                                  },
                                                                  "videoId": "1KtjAcwK1bU",
                                                                  "videoIds": [
                                                                    "1KtjAcwK1bU"
                                                                  ]
                                                                },
                                                                "clickTrackingParams": "CJgDEP6YBBgCIhMIjOuz6KfrlwMVqo_RBB0cMjYwygEEkc12oA=="
                                                              }
                                                            ],
                                                            "signal": "CLIENT_SIGNAL"
                                                          }
                                                        }
                                                      }
                                                    },
                                                    "loggingContext": {
                                                      "loggingDirectives": {
                                                        "trackingParams": "CJgDEP6YBBgCIhMIjOuz6KfrlwMVqo_RBB0cMjYw",
                                                        "visibility": {
                                                          "types": "12"
                                                        }
                                                      }
                                                    }
                                                  },
                                                  "title": {
                                                    "content": "Add to queue"
                                                  }
                                                }
                                              }
                                            ]
                                          }
                                        }
                                      }
                                    }
                                  }
                                }
                              }
                            }
                          }
                        }
                      ],
                      "enableVerticalExpansion": true,
                      "header": {
                        "sectionHeaderViewModel": {
                          "headline": {
                            "content": "Shorts"
                          },
                          "leadingAccessory": {
                            "image": {
                              "sources": [
                                {
                                  "clientResource": {
                                    "imageName": "YOUTUBE_SHORTS_BRAND_24"
                                  }
                                }
                              ]
                            }
                          }
                        }
                      },
                      "loggingDirectives": {
                        "trackingParams": "CIcDEJSUChgAIhMIjOuz6KfrlwMVqo_RBB0cMjYw",
                        "visibility": {
                          "types": "12"
                        }
                      },
                      "minCollapsedItemCount": 10,
                      "showLessButton": {
                        "buttonViewModel": {
                          "buttonSize": "BUTTON_VIEW_MODEL_SIZE_DEFAULT",
                          "iconName": "COLLAPSE",
                          "iconPosition": "BUTTON_VIEW_MODEL_ICON_POSITION_TRAILING",
                          "state": "BUTTON_VIEW_MODEL_STATE_ACTIVE",
                          "style": "BUTTON_VIEW_MODEL_STYLE_MONO",
                          "title": "Show less",
                          "trackingParams": "CIgDEPBbIhMIjOuz6KfrlwMVqo_RBB0cMjYw",
                          "type": "BUTTON_VIEW_MODEL_TYPE_OUTLINE"
                        }
                      },
                      "showMoreButton": {
                        "buttonViewModel": {
                          "buttonSize": "BUTTON_VIEW_MODEL_SIZE_DEFAULT",
                          "iconName": "EXPAND",
                          "iconPosition": "BUTTON_VIEW_MODEL_ICON_POSITION_TRAILING",
                          "state": "BUTTON_VIEW_MODEL_STATE_ACTIVE",
                          "style": "BUTTON_VIEW_MODEL_STYLE_MONO",
                          "title": "Show more",
                          "trackingParams": "CIkDEPBbIhMIjOuz6KfrlwMVqo_RBB0cMjYw",
                          "type": "BUTTON_VIEW_MODEL_TYPE_OUTLINE"
                        }
                      }
                    }
                  }
                ],
                "trackingParams": "CDUQuy8YACITCIzrs-in65cDFaqP0QQdHDI2MA=="
              }
            }
          ],
          "hideBottomSeparator": true,
          "subMenu": {
            "searchSubMenuRenderer": {
              "trackingParams": "CDMQkXUiEwiM67Pop-uXAxWqj9EEHRwyNjA="
            }
          },
          "targetId": "search-feed",
          "trackingParams": "CDIQui8iEwiM67Pop-uXAxWqj9EEHRwyNjA="
        }
      }
    }
  },
  "estimatedResults": "31921895",
  "header": {
    "searchHeaderRenderer": {
      "searchFilterButton": {
        "buttonRenderer": {
          "accessibilityData": {
            "accessibilityData": {
              "label": "Search filters"
            }
          },
          "command": {
            "clickTrackingParams": "CBMQ8FsiEwiM67Pop-uXAxWqj9EEHRwyNjDKAQSRzXag",
            "openPopupAction": {
              "popup": {
                "searchFilterOptionsDialogRenderer": {
                  "groups": [
                    {
                      "searchFilterGroupRenderer": {
                        "filters": [
                          {
                            "searchFilterRenderer": {
                              "label": {
                                "simpleText": "Videos"
                              },
                              "navigationEndpoint": {
                                "clickTrackingParams": "CDEQk3UYACITCIzrs-in65cDFaqP0QQdHDI2MMoBBJHNdqA=",
                                "commandMetadata": {
                                  "webCommandMetadata": {
                                    "rootVe": 4724,
                                    "url": "/results?search_query=NASA&sp=EgIQAQ%253D%253D",
                                    "webPageType": "WEB_PAGE_TYPE_SEARCH"
                                  }
                                },
                                "searchEndpoint": {
                                  "params": "EgIQAQ%3D%3D",
                                  "query": "NASA"
                                }
                              },
                              "tooltip": "Search for Videos",
                              "trackingParams": "CDEQk3UYACITCIzrs-in65cDFaqP0QQdHDI2MA=="
                            }
                          }
                        ],
                        "title": {
                          "simpleText": "Type"
                        },
                        "trackingParams": "CCwQknUYACITCIzrs-in65cDFaqP0QQdHDI2MA=="
                      }
                    }
                  ],
                  "title": {
                    "runs": [
                      {
                        "text": "Search filters"
                      }
                    ]
                  }
                }
              },
              "popupType": "DIALOG"
            }
          },
          "icon": {
            "iconType": "TUNE"
          },
          "iconPosition": "BUTTON_ICON_POSITION_TYPE_RIGHT_OF_TEXT",
          "isDisabled": false,
          "size": "SIZE_DEFAULT",
          "style": "STYLE_TEXT",
          "text": {
            "runs": [
              {
                "text": "Filters"
              }
            ]
          }
        }
      },
      "trackingParams": "CBIQiOoKIhMIjOuz6KfrlwMVqo_RBB0cMjYw"
    }
  },
  "isShortsContext": true,
  "responseContext": {
    "mainAppWebResponseContext": {
      "loggedOut": true,
      "trackingParam": "k5_fmPxhoXZRKYJIlrN4VFNMRPiERtgENSAneud0aQg7huLn6ko4XoVjqzRMkuMESLBwOcCw59TLtslL…"
    },
    "responseId": "IhMIjOuz6KfrlwMVqo_RBB0cMjYw",
    "serviceTrackingParams": [
      {
        "params": [
          {
            "key": "context",
            "value": "yt_web_search"
          }
        ],
        "service": "GUIDED_HELP"
      }
    ],
    "visitorData": "CgtGSGpwU2swTWowcyjOo6bXBjIKCgJVUxIEGgAgPQ%3D%3D",
    "webResponseContextExtensionData": {
      "hasDecorated": true,
      "webResponseContextPreloadData": {
        "preloadMessageNames": [
          "twoColumnSearchResultsRenderer"
        ]
      }
    }
  },
  "targetId": "search-page",
  "topbar": {
    "desktopTopbarRenderer": {
      "a11ySkipNavigationButton": {
        "buttonRenderer": {
          "command": {
            "clickTrackingParams": "CAUQ8FsiEwiM67Pop-uXAxWqj9EEHRwyNjDKAQSRzXag",
            "commandMetadata": {
              "webCommandMetadata": {
                "sendPost": true
              }
            },
            "signalServiceEndpoint": {
              "actions": [
                {
                  "clickTrackingParams": "CAUQ8FsiEwiM67Pop-uXAxWqj9EEHRwyNjDKAQSRzXag",
                  "signalAction": {
                    "signal": "SKIP_NAVIGATION"
                  }
                }
              ],
              "signal": "CLIENT_SIGNAL"
            }
          },
          "isDisabled": false,
          "size": "SIZE_DEFAULT",
          "style": "STYLE_DEFAULT",
          "text": {
            "runs": [
              {
                "text": "Skip navigation"
              }
            ]
          },
          "trackingParams": "CAUQ8FsiEwiM67Pop-uXAxWqj9EEHRwyNjA="
        }
      },
      "backButton": {
        "buttonRenderer": {
          "command": {
            "clickTrackingParams": "CAcQvIYDIhMIjOuz6KfrlwMVqo_RBB0cMjYwygEEkc12oA==",
            "commandMetadata": {
              "webCommandMetadata": {
                "sendPost": true
              }
            },
            "signalServiceEndpoint": {
              "actions": [
                {
                  "clickTrackingParams": "CAcQvIYDIhMIjOuz6KfrlwMVqo_RBB0cMjYwygEEkc12oA==",
                  "signalAction": {
                    "signal": "HISTORY_BACK"
                  }
                }
              ],
              "signal": "CLIENT_SIGNAL"
            }
          },
          "trackingParams": "CAcQvIYDIhMIjOuz6KfrlwMVqo_RBB0cMjYw"
        }
      },
      "forwardButton": {
        "buttonRenderer": {
          "command": {
            "clickTrackingParams": "CAYQvYYDIhMIjOuz6KfrlwMVqo_RBB0cMjYwygEEkc12oA==",
            "commandMetadata": {
              "webCommandMetadata": {
                "sendPost": true
              }
            },
            "signalServiceEndpoint": {
              "actions": [
                {
                  "clickTrackingParams": "CAYQvYYDIhMIjOuz6KfrlwMVqo_RBB0cMjYwygEEkc12oA==",
                  "signalAction": {
                    "signal": "HISTORY_FORWARD"
                  }
                }
              ],
              "signal": "CLIENT_SIGNAL"
            }
          },
          "trackingParams": "CAYQvYYDIhMIjOuz6KfrlwMVqo_RBB0cMjYw"
        }
      },
      "hotkeyDialog": {
        "hotkeyDialogRenderer": {
          "dismissButton": {
            "buttonRenderer": {
              "isDisabled": false,
              "size": "SIZE_DEFAULT",
              "style": "STYLE_BLUE_TEXT",
              "text": {
                "runs": [
                  {
                    "text": "Dismiss"
                  }
                ]
              },
              "trackingParams": "CAkQ8FsiEwiM67Pop-uXAxWqj9EEHRwyNjA="
            }
          },
          "sections": [
            {
              "hotkeyDialogSectionRenderer": {
                "options": [
                  {
                    "hotkeyDialogSectionOptionRenderer": {
                      "hotkey": "k",
                      "label": {
                        "runs": [
                          {
                            "text": "Toggle play/pause"
                          }
                        ]
                      }
                    }
                  }
                ],
                "title": {
                  "runs": [
                    {
                      "text": "Playback"
                    }
                  ]
                }
              }
            }
          ],
          "title": {
            "runs": [
              {
                "text": "Keyboard shortcuts"
              }
            ]
          },
          "trackingParams": "CAgQteYDIhMIjOuz6KfrlwMVqo_RBB0cMjYw"
        }
      },
      "logo": {
        "topbarLogoRenderer": {
          "endpoint": {
            "browseEndpoint": {
              "browseId": "FEwhat_to_watch"
            },
            "clickTrackingParams": "CBEQsV4iEwiM67Pop-uXAxWqj9EEHRwyNjDKAQSRzXag",
            "commandMetadata": {
              "webCommandMetadata": {
                "apiUrl": "/youtubei/v1/browse",
                "rootVe": 3854,
                "url": "/",
                "webPageType": "WEB_PAGE_TYPE_BROWSE"
              }
            }
          },
          "iconImage": {
            "iconType": "YOUTUBE_LOGO"
          },
          "overrideEntityKey": "EgZ0b3BiYXIg9QEoAQ%3D%3D",
          "tooltipText": {
            "runs": [
              {
                "text": "YouTube Home"
              }
            ]
          },
          "trackingParams": "CBEQsV4iEwiM67Pop-uXAxWqj9EEHRwyNjA="
        }
      },
      "searchbox": {
        "fusionSearchboxRenderer": {
          "clearButton": {
            "buttonRenderer": {
              "accessibilityData": {
                "accessibilityData": {
                  "label": "Clear search query"
                }
              },
              "icon": {
                "iconType": "CLOSE"
              },
              "isDisabled": false,
              "size": "SIZE_DEFAULT",
              "style": "STYLE_DEFAULT",
              "trackingParams": "CBAQ8FsiEwiM67Pop-uXAxWqj9EEHRwyNjA="
            }
          },
          "config": {
            "webSearchboxConfig": {
              "focusSearchbox": true,
              "hasOnscreenKeyboard": false,
              "requestDomain": "us",
              "requestLanguage": "en"
            }
          },
          "disableAiAppearance": true,
          "icon": {
            "iconType": "SEARCH"
          },
          "placeholderText": {
            "runs": [
              {
                "text": "Search"
              }
            ]
          },
          "searchEndpoint": {
            "clickTrackingParams": "CA0Q7VAiEwiM67Pop-uXAxWqj9EEHRwyNjDKAQSRzXag",
            "commandMetadata": {
              "webCommandMetadata": {
                "rootVe": 4724,
                "url": "/results?search_query=",
                "webPageType": "WEB_PAGE_TYPE_SEARCH"
              }
            },
            "searchEndpoint": {
              "query": ""
            }
          },
          "showImageSourceDialog": {
            "clickTrackingParams": "CA0Q7VAiEwiM67Pop-uXAxWqj9EEHRwyNjDKAQSRzXag",
            "showDialogCommand": {
              "panelLoadingStrategy": {
                "inlineContent": {
                  "dialogViewModel": {
                    "content": {
                      "basicContentViewModel": {
                        "paragraphs": [
                          {
                            "text": {
                              "content": "Visit image source website?"
                            }
                          }
                        ]
                      }
                    },
                    "footer": {
                      "panelFooterViewModel": {
                        "primaryButton": {
                          "buttonViewModel": {
                            "isFullWidth": true,
                            "style": "BUTTON_VIEW_MODEL_STYLE_MONO",
                            "title": "Visit source",
                            "trackingParams": "CA8Q8FsiEwiM67Pop-uXAxWqj9EEHRwyNjA=",
                            "type": "BUTTON_VIEW_MODEL_TYPE_FILLED"
                          }
                        },
                        "secondaryButton": {
                          "buttonViewModel": {
                            "isFullWidth": true,
                            "style": "BUTTON_VIEW_MODEL_STYLE_MONO",
                            "title": "Cancel",
                            "trackingParams": "CA4Q8FsiEwiM67Pop-uXAxWqj9EEHRwyNjA=",
                            "type": "BUTTON_VIEW_MODEL_TYPE_TONAL"
                          }
                        },
                        "shouldHideDivider": true
                      }
                    },
                    "header": {
                      "dialogHeaderViewModel": {
                        "headline": {
                          "content": "Image source"
                        }
                      }
                    }
                  }
                }
              }
            }
          },
          "trackingParams": "CA0Q7VAiEwiM67Pop-uXAxWqj9EEHRwyNjA="
        }
      },
      "topbarButtons": [
        {
          "topbarMenuButtonRenderer": {
            "accessibility": {
              "accessibilityData": {
                "label": "Settings"
              }
            },
            "icon": {
              "iconType": "MORE_VERT"
            },
            "menuRequest": {
              "clickTrackingParams": "CAsQ_qsBGAAiEwiM67Pop-uXAxWqj9EEHRwyNjDKAQSRzXag",
              "commandMetadata": {
                "webCommandMetadata": {
                  "apiUrl": "/youtubei/v1/account/account_menu",
                  "sendPost": true
                }
              },
              "signalServiceEndpoint": {
                "actions": [
                  {
                    "clickTrackingParams": "CAsQ_qsBGAAiEwiM67Pop-uXAxWqj9EEHRwyNjDKAQSRzXag",
                    "openPopupAction": {
                      "beReused": true,
                      "popup": {
                        "multiPageMenuRenderer": {
                          "showLoadingSpinner": true,
                          "style": "MULTI_PAGE_MENU_STYLE_TYPE_SYSTEM",
                          "trackingParams": "CAwQ_6sBIhMIjOuz6KfrlwMVqo_RBB0cMjYw"
                        }
                      },
                      "popupType": "DROPDOWN"
                    }
                  }
                ],
                "signal": "GET_ACCOUNT_MENU"
              }
            },
            "style": "STYLE_DEFAULT",
            "tooltip": "Settings",
            "trackingParams": "CAsQ_qsBGAAiEwiM67Pop-uXAxWqj9EEHRwyNjA="
          }
        }
      ],
      "trackingParams": "CAEQq6wBIhMIjOuz6KfrlwMVqo_RBB0cMjYw",
      "voiceSearchButton": {
        "buttonRenderer": {
          "accessibilityData": {
            "accessibilityData": {
              "label": "Search with your voice"
            }
          },
          "icon": {
            "iconType": "MICROPHONE_ON"
          },
          "isDisabled": false,
          "serviceEndpoint": {
            "clickTrackingParams": "CAIQ7a8FIhMIjOuz6KfrlwMVqo_RBB0cMjYwygEEkc12oA==",
            "commandMetadata": {
              "webCommandMetadata": {
                "sendPost": true
              }
            },
            "signalServiceEndpoint": {
              "actions": [
                {
                  "clickTrackingParams": "CAIQ7a8FIhMIjOuz6KfrlwMVqo_RBB0cMjYwygEEkc12oA==",
                  "openPopupAction": {
                    "popup": {
                      "voiceSearchDialogRenderer": {
                        "connectionErrorHeader": {
                          "runs": [
                            {
                              "text": "No connection"
                            }
                          ]
                        },
                        "connectionErrorMicrophoneLabel": {
                          "runs": [
                            {
                              "text": "Check your connection and try again"
                            }
                          ]
                        },
                        "disabledHeader": {
                          "runs": [
                            {
                              "text": "Search with your voice"
                            }
                          ]
                        },
                        "disabledSubtext": {
                          "runs": [
                            {
                              "text": "To search by voice, go to your browser settings and allow access to microphone"
                            }
                          ]
                        },
                        "exampleQuery1": {
                          "runs": [
                            {
                              "text": "\"Play Dua Lipa\""
                            }
                          ]
                        },
                        "exampleQuery2": {
                          "runs": [
                            {
                              "text": "\"Show me my subscriptions\""
                            }
                          ]
                        },
                        "exitButton": {
                          "buttonRenderer": {
                            "accessibilityData": {
                              "accessibilityData": {
                                "label": "Cancel"
                              }
                            },
                            "icon": {
                              "iconType": "CLOSE"
                            },
                            "isDisabled": false,
                            "size": "SIZE_DEFAULT",
                            "style": "STYLE_DEFAULT",
                            "trackingParams": "CAQQ0LEFIhMIjOuz6KfrlwMVqo_RBB0cMjYw"
                          }
                        },
                        "loadingHeader": {
                          "runs": [
                            {
                              "text": "Working..."
                            }
                          ]
                        }
                      }
                    },
                    "popupType": "TOP_ALIGNED_DIALOG"
                  }
                }
              ],
              "signal": "CLIENT_SIGNAL"
            }
          },
          "size": "SIZE_DEFAULT",
          "style": "STYLE_DEFAULT",
          "tooltip": "Search with your voice",
          "trackingParams": "CAIQ7a8FIhMIjOuz6KfrlwMVqo_RBB0cMjYw"
        }
      }
    }
  },
  "trackingParams": "CAAQvGkiEwiM67Pop-uXAxWqj9EEHRwyNjDKAQSRzXag"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `contents.twoColumnSearchResultsRenderer.primaryContents.sectionListRenderer.contents[].itemSectionRenderer.contents[].gridShelfViewModel.contents[]` | The list of Shorts in one result shelf. Each item holds a `shortsLockupViewModel` object. |
| `...gridShelfViewModel.contents[].shortsLockupViewModel.accessibilityText` | A text label with the Short's title and its view count, for example `8.8 thousand views`. It ends with `play Short`. |
| `...shortsLockupViewModel.entityId` | An ID in the form `shorts-shelf-item-<videoId>`. The part after the prefix is the YouTube video ID. |
| `...shortsLockupViewModel.inlinePlayerData.onVisible.innertubeCommand.watchEndpoint.videoId` | The YouTube video ID of the Short. |
| `...shortsLockupViewModel.inlinePlayerData.onVisible.innertubeCommand.commandMetadata.webCommandMetadata.url` | The watch page path for the Short, as `/watch?v=<videoId>` plus extra player parameters. |
| `...shortsLockupViewModel.badge.badgeViewModel.badgeText` | A badge label shown on the Short, such as `New`. |
| `...shortsLockupViewModel.indexInCollection` | The position index of the item in its collection. |
| `...shortsLockupViewModel.menuOnTap.innertubeCommand.showSheetCommand.panelLoadingStrategy.inlineContent.sheetViewModel.content.listViewModel.listItems[].listItemViewModel.title.content` | The label of each menu action on the Short, such as `Add to queue` or `Send feedback`. |

### Notes

- Use `continuation_token` to request the next page of results.
- Set `sort_by` to `relevance`, `upload_date`, `view_count` or `rating`. Set `upload_time` to `hour`, `today`, `week`, `month` or `year`.
- The response is raw YouTube data with many tracking fields. The video ID is the most useful value to carry forward.
- For a cleaner response, use [YouTube Shorts Search (V2)](/apis/youtube/web-v2/shorts-search-v2).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/youtube/web-v2/shorts-search.json`](../../../../catalog/models/youtube/web-v2/shorts-search.json) · Store page: https://www.sandbase.ai/model/youtube/web-v2/shorts-search
