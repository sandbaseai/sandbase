# Xigua Video Search API: pricing, parameters and code examples

`xigua/app-v2/search-video` · data API · Xigua · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Search Xigua Video (ByteDance long-form video) by keyword: titles, creators, duration, publish time and comment counts, with sort and duration filters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xigua/app-v2/search-video", "keyword": "美食"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xigua/app-v2/search-video', {'keyword': '美食'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xigua/app-v2/search-video", {
  "keyword": "美食"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xigua/app-v2/search-video", sandbase.Params{
	"keyword": "美食",
})
```

Same call via the path form: `POST /v1/api/xigua/app-v2/search-video` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `offset` | integer |  | Offset, pass 0 for the first request, pass the offset returned by the previous request for subsequent requests default `0` |
| `keyword` | string | yes | Keyword  |
| `order_type` | string |  | Order type, empty for default sorting, the following are optional sorting methods.  |
| `max_duration` | integer |  | Maximum duration, default empty, in seconds.  |
| `min_duration` | integer |  | Minimum duration, default empty, in seconds.  |

## Details

This API searches Xigua Video by keyword and returns a page of 10 matching videos. It needs a `keyword` and can also take duration filters, a sort type and an `offset` for paging.

### Use cases

- Collect Xigua videos that mention a brand or product, such as OpenAI, with their comment counts.
- Rank search hits by `comment_count` to see which videos draw the most discussion.
- Find the channels that publish on a topic, using the `emphasized.source` name on each result.
- Limit a search to short or long videos with `min_duration` and `max_duration` to study one format.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xigua/app-v2/search-video" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "OpenAI"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Keyword |
| `max_duration` | integer | No | Maximum duration, default empty, in seconds. |
| `min_duration` | integer | No | Minimum duration, default empty, in seconds. |
| `offset` | integer | No | Offset, pass 0 for the first request, pass the offset returned by the previous request for subsequent requests |
| `order_type` | string | No | Order type, empty for default sorting, the following are optional sorting methods. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "common_data": {
    "abFields": {},
    "client": {
      "height": 0,
      "isAndroid": true,
      "isPad": true,
      "pixelRatio": 2,
      "platform": "android_pad",
      "userAgent": "Dalvik/2.1.0 (Linux; U; Android 13; 23078PND5G Build/TP1A.220624.014) VideoArtic…",
      "width": 0
    },
    "isSsrFrame": true,
    "location": {
      "hash": "",
      "host": "security.snssdk.com",
      "hostname": "security.snssdk.com",
      "href": "https://security.snssdk.com/s/video_search/video/app/search/search_content/?devi…",
      "origin": "https://security.snssdk.com",
      "pathname": "/s/video_search/video/app/search/search_content/",
      "port": "",
      "protocol": "https:",
      "search": "?device_id=939401905983347&iid=1783851837819571&ac=wifi&channel=google_play&aid=…"
    },
    "query": {
      "ab_version": "668853,9274002,668856,9273984,668855,9273955,668859,9273981,668858,9273942,66885…",
      "ac": "wifi",
      "aid": "32",
      "app_name": "video_article",
      "channel": "google_play",
      "device_brand": "Xiaomi",
      "device_id": "939401905983347",
      "device_platform": "android",
      "device_type": "23078PND5G",
      "dpi": "480",
      "filter_info": "order_type=None&min_duration=None&max_duration=None",
      "forum": "1"
    },
    "runtimeVersion": 980,
    "targetChannel": "video_search",
    "userAgent": "Dalvik/2.1.0 (Linux; U; Android 13; 23078PND5G Build/TP1A.220624.014) VideoArtic…"
  },
  "count": 10,
  "custom_data": {
    "extraData": {
      "abFields": {},
      "baseHeight": 0,
      "baseWidth": 0,
      "cardTypeContext": [],
      "client": {
        "height": 0,
        "isAndroid": true,
        "isPad": true,
        "pixelRatio": 2,
        "platform": "android_pad",
        "userAgent": "Dalvik/2.1.0 (Linux; U; Android 13; 23078PND5G Build/TP1A.220624.014) VideoArtic…",
        "width": 0
      },
      "durationType": "default",
      "extraInfo": {
        "enable_tag_search_xigua_tab": true,
        "fe_ab_params": null,
        "fe_client_ab_params": null,
        "game_aladdin_show_cnt": 3,
        "is_hit_new_tag_ui": true,
        "is_hit_shark": false,
        "is_no_result": false,
        "is_req_skip_ten": false
      },
      "isAndroid": true,
      "isIOS": false,
      "isSsrFrame": true,
      "keyword": "OpenAI",
      "keywordType": "keyword_type"
    }
  },
  "err_code": 0,
  "extra_data": {
    "initCount": 10,
    "initHasMore": true,
    "initIsEmptyContent": false,
    "initOffset": 10,
    "initReqId": "20261103154724B82D0677FE75EF02CB5A",
    "initSearchId": "20261102122708FAB1AED852AD4265A36F"
  },
  "extra_data_element": {
    "attr": [
      [
        "type"
      ]
    ],
    "inner": "{\"initOffset\":10,\"initHasMore\":true,\"initReqId\":\"20261103154724B82D0677FE75EF02C…",
    "tag": "script"
  },
  "fb_results": [
    {
      "abaseKey": "[card_html]video_search:32:OpenAI:0:::android:Inner_FilterBar",
      "browserJs": "//lf3-material.searchpstatp.com/toutiao/feoffline/search-materials-source-video_…",
      "compileCss": ".s-filter-bar{z-index:800}@font-face{font-family:Condensed-Bold-Number;src:local…",
      "html": "",
      "id": "cff626c0",
      "itemDataStr": "{\"extraData\":{}}",
      "output": {
        "dom": [
          {
            "attr": [
              [
                "id"
              ]
            ],
            "inner": "",
            "tag": "div"
          }
        ],
        "script": [
          {
            "attr": [
              [
                "type"
              ]
            ],
            "inner": "{\"extraData\":{}}",
            "tag": "script"
          }
        ],
        "style": [
          {
            "attr": [],
            "inner": ".s-filter-bar{z-index:800}@font-face{font-family:Condensed-Bold-Number;src:local…",
            "tag": "style"
          }
        ]
      },
      "templateId": "Inner_FilterBar",
      "templateVersion": 72
    }
  ],
  "feed_down_tag": "",
  "feed_up_tag": "",
  "filtered_data": [],
  "has_more": true,
  "is_empty_content": false
}
```

### Response fields

| Field | Meaning |
|---|---|
| `results[].data.group_id / results[].data.id_str` | The ID of the video, as a string. Use it to look up the video in other Xigua APIs. |
| `results[].data.emphasized.title` | The video title. Matched search terms are wrapped in `<em>` tags. |
| `results[].data.emphasized.source` | The name of the source that posted the video. |
| `results[].data.emphasized.summary` | The description text of the video. |
| `results[].data.comment_count` | The number of comments on the video. |
| `results[].data.highlight.title[]` | Where the matched terms sit in the title. `start` is the position and `count` is the length of the match. |
| `has_more` | `true` when more results exist after this page. |
| `offset` | The offset to send as `offset` in the next request to get the next page. |
| `count / list_length` | The number of results on this page. |
| `search_id` | The ID of this search session. It stays the same for the same query. |

### Notes

- For the first page, pass `offset` as `0`. For the next page, pass the `offset` value from the previous response (10 in this example).
- Keep requesting while `has_more` is `true`.
- `min_duration` and `max_duration` are in seconds.
- To get more detail on a video, pass its `group_id` to [Xigua Single Video Information](/apis/xigua/app-v2/one-video) or read its comments with [Xigua Video Comment List](/apis/xigua/app-v2/video-comment-list).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Get single video data](/apis/xigua/app-v2/one-video): Get single video data (less information, does not include title and other information, but includes information about related videos).
- [Get single video play URL](/apis/xigua/app-v2/one-video-play-url): App V2 One Video Play Url provides a focused capability for applications, automation, and data workflows.
- [Personal information](/apis/xigua/app-v2/user-info): Personal information.

---
Machine-readable: [`catalog/models/xigua/app-v2/search-video.json`](../../../../catalog/models/xigua/app-v2/search-video.json) · Store page: https://www.sandbase.ai/model/xigua/app-v2/search-video
