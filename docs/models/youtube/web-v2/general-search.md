# General search (raw data, recommend V2) API: pricing, parameters and code examples

`youtube/web-v2/general-search` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

YouTube comprehensive search with multiple filter options for precise result filtering.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/web-v2/general-search", "search_query": "NASA"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/web-v2/general-search', {'search_query': 'NASA'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/web-v2/general-search", {
  "search_query": "NASA"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/web-v2/general-search", sandbase.Params{
	"search_query": "NASA",
})
```

Same call via the path form: `POST /v1/api/youtube/web-v2/general-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `feature` |  |  | Feature filter  |
| `sort_by` |  |  | Sort by  |
| `duration` |  |  | Duration filter  |
| `time_zone` | string |  | Time zone setting default `"America/Los_Angeles"` |
| `upload_time` |  |  | Upload time filter  |
| `content_type` |  |  | Content type filter  |
| `country_code` | string |  | Country code affecting regional relevance default `"US"` |
| `search_query` | string | yes | Search keyword  |
| `language_code` | string |  | Language code (zh-CN for Chinese, en-US for English) default `"zh-CN"` |
| `continuation_token` |  |  | Pagination token  |

## Details

This API runs a YouTube search and returns the raw YouTube result page as JSON. It needs a `search_query` and accepts optional filters for content type, duration, upload time, sort order and features.

### Use cases

- Find the official channel for a brand or organization by searching its name and reading the channel result.
- Collect recent videos on a topic by filtering with `upload_time` and sorting with `sort_by`.
- Build a list of video IDs for a keyword, then pass them to a video detail or comments API.
- Check which channels rank first for a keyword in a given `country_code` and `language_code`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web-v2/general-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"search_query": "NASA"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `search_query` | string | Yes | Search keyword |
| `content_type` | string | No | Content type filter |
| `continuation_token` | string | No | Pagination token |
| `country_code` | string | No | Country code affecting regional relevance |
| `duration` | string | No | Duration filter |
| `feature` | string | No | Feature filter |
| `language_code` | string | No | Language code (zh-CN for Chinese, en-US for English) |
| `sort_by` | string | No | Sort by |
| `time_zone` | string | No | Time zone setting |
| `upload_time` | string | No | Upload time filter |

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
                    "channelRenderer": {
                      "channelId": "UCLA_DiR1FfKNvjuUpBHmylQ",
                      "descriptionSnippet": {
                        "runs": [
                          {
                            "bold": true,
                            "text": "NASA's"
                          }
                        ]
                      },
                      "longBylineText": {
                        "runs": [
                          {
                            "navigationEndpoint": {
                              "browseEndpoint": {
                                "browseId": "UCLA_DiR1FfKNvjuUpBHmylQ",
                                "canonicalBaseUrl": "/@NASA"
                              },
                              "clickTrackingParams": "CNcCENowGAAiEwj32L_mp-uXAxV_yM4AHf5qOAHKAQTetXCi",
                              "commandMetadata": {
                                "webCommandMetadata": {
                                  "apiUrl": "/youtubei/v1/browse",
                                  "rootVe": 3611,
                                  "url": "/@NASA",
                                  "webPageType": "WEB_PAGE_TYPE_CHANNEL"
                                }
                              }
                            },
                            "text": "NASA"
                          }
                        ]
                      },
                      "navigationEndpoint": {
                        "browseEndpoint": {
                          "browseId": "UCLA_DiR1FfKNvjuUpBHmylQ",
                          "canonicalBaseUrl": "/@NASA"
                        },
                        "clickTrackingParams": "CNcCENowGAAiEwj32L_mp-uXAxV_yM4AHf5qOAHKAQTetXCi",
                        "commandMetadata": {
                          "webCommandMetadata": {
                            "apiUrl": "/youtubei/v1/browse",
                            "rootVe": 3611,
                            "url": "/@NASA",
                            "webPageType": "WEB_PAGE_TYPE_CHANNEL"
                          }
                        }
                      },
                      "ownerBadges": [
                        {
                          "metadataBadgeRenderer": {
                            "accessibilityData": {
                              "label": "已验证"
                            },
                            "icon": {
                              "iconType": "CHECK_CIRCLE_THICK"
                            },
                            "style": "BADGE_STYLE_TYPE_VERIFIED",
                            "tooltip": "已验证",
                            "trackingParams": "CNcCENowGAAiEwj32L_mp-uXAxV_yM4AHf5qOAE="
                          }
                        }
                      ],
                      "shortBylineText": {
                        "runs": [
                          {
                            "navigationEndpoint": {
                              "browseEndpoint": {
                                "browseId": "UCLA_DiR1FfKNvjuUpBHmylQ",
                                "canonicalBaseUrl": "/@NASA"
                              },
                              "clickTrackingParams": "CNcCENowGAAiEwj32L_mp-uXAxV_yM4AHf5qOAHKAQTetXCi",
                              "commandMetadata": {
                                "webCommandMetadata": {
                                  "apiUrl": "/youtubei/v1/browse",
                                  "rootVe": 3611,
                                  "url": "/@NASA",
                                  "webPageType": "WEB_PAGE_TYPE_CHANNEL"
                                }
                              }
                            },
                            "text": "NASA"
                          }
                        ]
                      },
                      "subscribeButton": {
                        "buttonRenderer": {
                          "isDisabled": false,
                          "navigationEndpoint": {
                            "clickTrackingParams": "CNgCEPBbIhMI99i_5qfrlwMVf8jOAB3-ajgBygEE3rVwog==",
                            "commandMetadata": {
                              "webCommandMetadata": {
                                "rootVe": 83769,
                                "url": "https://accounts.google.com/ServiceLogin?service=youtube&uilel=3&passive=true&co…",
                                "webPageType": "WEB_PAGE_TYPE_UNKNOWN"
                              }
                            },
                            "signInEndpoint": {
                              "continueAction": "QUlxb01IWUVaSGQ5amRoWmhHVEhMbHpvQVBuWXxBSTVJdTV1UWFCQW5MMTlmWGNJSnZUZzlmbTd2bVND…",
                              "nextEndpoint": {
                                "clickTrackingParams": "CNgCEPBbIhMI99i_5qfrlwMVf8jOAB3-ajgBygEE3rVwog==",
                                "commandMetadata": {
                                  "webCommandMetadata": {
                                    "rootVe": 4724,
                                    "url": "/results?search_query=NASA",
                                    "webPageType": "WEB_PAGE_TYPE_SEARCH"
                                  }
                                },
                                "searchEndpoint": {
                                  "query": "NASA"
                                }
                              }
                            }
                          },
                          "size": "SIZE_DEFAULT",
                          "style": "STYLE_DESTRUCTIVE",
                          "text": {
                            "runs": [
                              {
                                "text": "订阅"
                              }
                            ]
                          },
                          "trackingParams": "CNgCEPBbIhMI99i_5qfrlwMVf8jOAB3-ajgB"
                        }
                      },
                      "subscriberCountText": {
                        "simpleText": "@NASA"
                      }
                    }
                  }
                ],
                "trackingParams": "CDUQuy8YACITCPfYv-an65cDFX_IzgAd_mo4AQ=="
              }
            }
          ],
          "hideBottomSeparator": true,
          "subMenu": {
            "searchSubMenuRenderer": {
              "trackingParams": "CDMQkXUiEwj32L_mp-uXAxV_yM4AHf5qOAE="
            }
          },
          "targetId": "search-feed",
          "trackingParams": "CDIQui8iEwj32L_mp-uXAxV_yM4AHf5qOAE="
        }
      }
    }
  },
  "estimatedResults": "30529781",
  "header": {
    "searchHeaderRenderer": {
      "searchFilterButton": {
        "buttonRenderer": {
          "accessibilityData": {
            "accessibilityData": {
              "label": "搜索过滤条件"
            }
          },
          "command": {
            "clickTrackingParams": "CBMQ8FsiEwj32L_mp-uXAxV_yM4AHf5qOAHKAQTetXCi",
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
                                "simpleText": "长视频"
                              },
                              "navigationEndpoint": {
                                "clickTrackingParams": "CDEQk3UYACITCPfYv-an65cDFX_IzgAd_mo4AcoBBN61cKI=",
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
                              "tooltip": "搜索“长视频”",
                              "trackingParams": "CDEQk3UYACITCPfYv-an65cDFX_IzgAd_mo4AQ=="
                            }
                          }
                        ],
                        "title": {
                          "simpleText": "类型"
                        },
                        "trackingParams": "CCwQknUYACITCPfYv-an65cDFX_IzgAd_mo4AQ=="
                      }
                    }
                  ],
                  "title": {
                    "runs": [
                      {
                        "text": "搜索过滤条件"
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
                "text": "过滤"
              }
            ]
          }
        }
      },
      "trackingParams": "CBIQiOoKIhMI99i_5qfrlwMVf8jOAB3-ajgB"
    }
  },
  "responseContext": {
    "mainAppWebResponseContext": {
      "loggedOut": true,
      "trackingParam": "k5_fmPxhoXZRr-2IsuQ3MDHXRVUYiwrHgY47EzqQIuKnk0H_hkmAzGBfRzRMkuMESLBwOcCw59TLtslL…"
    },
    "responseId": "IhMI99i_5qfrlwMVf8jOAB3-ajgB",
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
    "visitorData": "CgtkMDNMaTgybHVCbyjKo6bXBjIKCgJVUxIEGgAgFA%3D%3D",
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
            "clickTrackingParams": "CAUQ8FsiEwj32L_mp-uXAxV_yM4AHf5qOAHKAQTetXCi",
            "commandMetadata": {
              "webCommandMetadata": {
                "sendPost": true
              }
            },
            "signalServiceEndpoint": {
              "actions": [
                {
                  "clickTrackingParams": "CAUQ8FsiEwj32L_mp-uXAxV_yM4AHf5qOAHKAQTetXCi",
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
                "text": "跳过导航"
              }
            ]
          },
          "trackingParams": "CAUQ8FsiEwj32L_mp-uXAxV_yM4AHf5qOAE="
        }
      },
      "backButton": {
        "buttonRenderer": {
          "command": {
            "clickTrackingParams": "CAcQvIYDIhMI99i_5qfrlwMVf8jOAB3-ajgBygEE3rVwog==",
            "commandMetadata": {
              "webCommandMetadata": {
                "sendPost": true
              }
            },
            "signalServiceEndpoint": {
              "actions": [
                {
                  "clickTrackingParams": "CAcQvIYDIhMI99i_5qfrlwMVf8jOAB3-ajgBygEE3rVwog==",
                  "signalAction": {
                    "signal": "HISTORY_BACK"
                  }
                }
              ],
              "signal": "CLIENT_SIGNAL"
            }
          },
          "trackingParams": "CAcQvIYDIhMI99i_5qfrlwMVf8jOAB3-ajgB"
        }
      },
      "forwardButton": {
        "buttonRenderer": {
          "command": {
            "clickTrackingParams": "CAYQvYYDIhMI99i_5qfrlwMVf8jOAB3-ajgBygEE3rVwog==",
            "commandMetadata": {
              "webCommandMetadata": {
                "sendPost": true
              }
            },
            "signalServiceEndpoint": {
              "actions": [
                {
                  "clickTrackingParams": "CAYQvYYDIhMI99i_5qfrlwMVf8jOAB3-ajgBygEE3rVwog==",
                  "signalAction": {
                    "signal": "HISTORY_FORWARD"
                  }
                }
              ],
              "signal": "CLIENT_SIGNAL"
            }
          },
          "trackingParams": "CAYQvYYDIhMI99i_5qfrlwMVf8jOAB3-ajgB"
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
                    "text": "关闭"
                  }
                ]
              },
              "trackingParams": "CAkQ8FsiEwj32L_mp-uXAxV_yM4AHf5qOAE="
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
                            "text": "在播放和暂停之间切换"
                          }
                        ]
                      }
                    }
                  }
                ],
                "title": {
                  "runs": [
                    {
                      "text": "播放"
                    }
                  ]
                }
              }
            }
          ],
          "title": {
            "runs": [
              {
                "text": "键盘快捷键"
              }
            ]
          },
          "trackingParams": "CAgQteYDIhMI99i_5qfrlwMVf8jOAB3-ajgB"
        }
      },
      "logo": {
        "topbarLogoRenderer": {
          "endpoint": {
            "browseEndpoint": {
              "browseId": "FEwhat_to_watch"
            },
            "clickTrackingParams": "CBEQsV4iEwj32L_mp-uXAxV_yM4AHf5qOAHKAQTetXCi",
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
                "text": "YouTube 首页"
              }
            ]
          },
          "trackingParams": "CBEQsV4iEwj32L_mp-uXAxV_yM4AHf5qOAE="
        }
      },
      "searchbox": {
        "fusionSearchboxRenderer": {
          "clearButton": {
            "buttonRenderer": {
              "accessibilityData": {
                "accessibilityData": {
                  "label": "清空搜索查询"
                }
              },
              "icon": {
                "iconType": "CLOSE"
              },
              "isDisabled": false,
              "size": "SIZE_DEFAULT",
              "style": "STYLE_DEFAULT",
              "trackingParams": "CBAQ8FsiEwj32L_mp-uXAxV_yM4AHf5qOAE="
            }
          },
          "config": {
            "webSearchboxConfig": {
              "focusSearchbox": true,
              "hasOnscreenKeyboard": false,
              "requestDomain": "us",
              "requestLanguage": "zh-CN"
            }
          },
          "disableAiAppearance": true,
          "icon": {
            "iconType": "SEARCH"
          },
          "placeholderText": {
            "runs": [
              {
                "text": "搜索"
              }
            ]
          },
          "searchEndpoint": {
            "clickTrackingParams": "CA0Q7VAiEwj32L_mp-uXAxV_yM4AHf5qOAHKAQTetXCi",
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
            "clickTrackingParams": "CA0Q7VAiEwj32L_mp-uXAxV_yM4AHf5qOAHKAQTetXCi",
            "showDialogCommand": {
              "panelLoadingStrategy": {
                "inlineContent": {
                  "dialogViewModel": {
                    "content": {
                      "basicContentViewModel": {
                        "paragraphs": [
                          {
                            "text": {
                              "content": "访问图片来源网站？"
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
                            "title": "查看来源",
                            "trackingParams": "CA8Q8FsiEwj32L_mp-uXAxV_yM4AHf5qOAE=",
                            "type": "BUTTON_VIEW_MODEL_TYPE_FILLED"
                          }
                        },
                        "secondaryButton": {
                          "buttonViewModel": {
                            "isFullWidth": true,
                            "style": "BUTTON_VIEW_MODEL_STYLE_MONO",
                            "title": "取消",
                            "trackingParams": "CA4Q8FsiEwj32L_mp-uXAxV_yM4AHf5qOAE=",
                            "type": "BUTTON_VIEW_MODEL_TYPE_TONAL"
                          }
                        },
                        "shouldHideDivider": true
                      }
                    },
                    "header": {
                      "dialogHeaderViewModel": {
                        "headline": {
                          "content": "图片来源"
                        }
                      }
                    }
                  }
                }
              }
            }
          },
          "trackingParams": "CA0Q7VAiEwj32L_mp-uXAxV_yM4AHf5qOAE="
        }
      },
      "topbarButtons": [
        {
          "topbarMenuButtonRenderer": {
            "accessibility": {
              "accessibilityData": {
                "label": "设置"
              }
            },
            "icon": {
              "iconType": "MORE_VERT"
            },
            "menuRequest": {
              "clickTrackingParams": "CAsQ_qsBGAAiEwj32L_mp-uXAxV_yM4AHf5qOAHKAQTetXCi",
              "commandMetadata": {
                "webCommandMetadata": {
                  "apiUrl": "/youtubei/v1/account/account_menu",
                  "sendPost": true
                }
              },
              "signalServiceEndpoint": {
                "actions": [
                  {
                    "clickTrackingParams": "CAsQ_qsBGAAiEwj32L_mp-uXAxV_yM4AHf5qOAHKAQTetXCi",
                    "openPopupAction": {
                      "beReused": true,
                      "popup": {
                        "multiPageMenuRenderer": {
                          "showLoadingSpinner": true,
                          "style": "MULTI_PAGE_MENU_STYLE_TYPE_SYSTEM",
                          "trackingParams": "CAwQ_6sBIhMI99i_5qfrlwMVf8jOAB3-ajgB"
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
            "tooltip": "设置",
            "trackingParams": "CAsQ_qsBGAAiEwj32L_mp-uXAxV_yM4AHf5qOAE="
          }
        }
      ],
      "trackingParams": "CAEQq6wBIhMI99i_5qfrlwMVf8jOAB3-ajgB",
      "voiceSearchButton": {
        "buttonRenderer": {
          "accessibilityData": {
            "accessibilityData": {
              "label": "通过语音搜索内容"
            }
          },
          "icon": {
            "iconType": "MICROPHONE_ON"
          },
          "isDisabled": false,
          "serviceEndpoint": {
            "clickTrackingParams": "CAIQ7a8FIhMI99i_5qfrlwMVf8jOAB3-ajgBygEE3rVwog==",
            "commandMetadata": {
              "webCommandMetadata": {
                "sendPost": true
              }
            },
            "signalServiceEndpoint": {
              "actions": [
                {
                  "clickTrackingParams": "CAIQ7a8FIhMI99i_5qfrlwMVf8jOAB3-ajgBygEE3rVwog==",
                  "openPopupAction": {
                    "popup": {
                      "voiceSearchDialogRenderer": {
                        "connectionErrorHeader": {
                          "runs": [
                            {
                              "text": "无网络连接"
                            }
                          ]
                        },
                        "connectionErrorMicrophoneLabel": {
                          "runs": [
                            {
                              "text": "请检查你的网络连接，然后重试"
                            }
                          ]
                        },
                        "disabledHeader": {
                          "runs": [
                            {
                              "text": "通过语音搜索内容"
                            }
                          ]
                        },
                        "disabledSubtext": {
                          "runs": [
                            {
                              "text": "要执行语音搜索，请转至浏览器的设置部分，然后授予麦克风使用权限"
                            }
                          ]
                        },
                        "exampleQuery1": {
                          "runs": [
                            {
                              "text": "“播放 Dua Lipa 的音乐”"
                            }
                          ]
                        },
                        "exampleQuery2": {
                          "runs": [
                            {
                              "text": "“显示我订阅的频道的视频”"
                            }
                          ]
                        },
                        "exitButton": {
                          "buttonRenderer": {
                            "accessibilityData": {
                              "accessibilityData": {
                                "label": "取消"
                              }
                            },
                            "icon": {
                              "iconType": "CLOSE"
                            },
                            "isDisabled": false,
                            "size": "SIZE_DEFAULT",
                            "style": "STYLE_DEFAULT",
                            "trackingParams": "CAQQ0LEFIhMI99i_5qfrlwMVf8jOAB3-ajgB"
                          }
                        },
                        "loadingHeader": {
                          "runs": [
                            {
                              "text": "正在处理…"
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
          "tooltip": "通过语音搜索内容",
          "trackingParams": "CAIQ7a8FIhMI99i_5qfrlwMVf8jOAB3-ajgB"
        }
      }
    }
  },
  "trackingParams": "CAAQvGkiEwj32L_mp-uXAxV_yM4AHf5qOAHKAQTetXCi"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `contents.twoColumnSearchResultsRenderer.primaryContents.sectionListRenderer.contents[].itemSectionRenderer.contents[]` | The list of search results. Each item holds one result type, such as `channelRenderer`, `shelfRenderer` or `videoRenderer`. |
| `...itemSectionRenderer.contents[].channelRenderer.channelId` | The ID of a matched channel. It starts with `UC`. |
| `...channelRenderer.longBylineText.runs[].text / ...channelRenderer.shortBylineText.runs[].text` | The channel display name, such as `NASA`. |
| `...channelRenderer.navigationEndpoint.browseEndpoint.canonicalBaseUrl` | The channel handle path, such as `/@NASA`. |
| `...channelRenderer.descriptionSnippet.runs[].text` | A short piece of the channel description. Runs with `bold` set to `true` mark the words that matched the query. |
| `...channelRenderer.ownerBadges[].metadataBadgeRenderer.style` | The badge type on the channel. `BADGE_STYLE_TYPE_VERIFIED` marks a verified channel. |
| `...shelfRenderer.content.verticalListRenderer.items[].videoRenderer` | A video result grouped inside a shelf. It has the channel avatar, badges, a description snippet and menu data. |
| `...videoRenderer.detailedMetadataSnippets[].snippetText.runs[].text` | A text snippet from the video description that relates to the query. |
| `...videoRenderer.longBylineText.runs[].text` | The name of the channel that published the video. |

### Notes

- The response keeps YouTube's own nested structure, so read results by walking `itemSectionRenderer.contents[]` and checking which renderer key each item has.
- Some labels come back in Chinese because `language_code` defaults to `zh-CN`. Set `language_code` to `en-US` for English labels.
- Pass the `continuation_token` parameter to get the next page of results.
- For a cleaner response, use [YouTube General Search (Web V2, V2)](/apis/youtube/web-v2/general-search-v2). To get details for a video found here, call [YouTube Video Information](/apis/youtube/web-v2/video-info).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/youtube/web-v2/general-search.json`](../../../../catalog/models/youtube/web-v2/general-search.json) · Store page: https://www.sandbase.ai/model/youtube/web-v2/general-search
