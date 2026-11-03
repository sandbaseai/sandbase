# Douyin Hot Search List API: pricing, parameters and code examples

`douyin/app-v3/hot-search-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get the Douyin hot search list and other boards (seeding, entertainment, social and challenge lists): trending words with heat values and video counts.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/hot-search-list", "board_sub_type": "", "board_type": "0"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/hot-search-list', {'board_sub_type': '', 'board_type': '0'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/hot-search-list", {
  "board_sub_type": "",
  "board_type": "0"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/hot-search-list", sandbase.Params{
	"board_sub_type": "",
	"board_type": "0",
})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/hot-search-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `board_type` | string |  | - 0: Hot search list (default) default `"0"` |
| `board_sub_type` | string |  | - Empty string: Hot search list (default) default `""` |

## Details

This API returns the current Douyin hot search board as a ranked list of trending words, each with a heat value, video count and view count. It needs no input for the default hot search list. Set `board_type` and `board_sub_type` to request other boards.

### Use cases

- Track which words climb the Douyin hot search list and record their `hot_value` over time.
- Check whether a brand, person or event name appears in `word_list` and alert when it does.
- Build a daily snapshot of the top topics with their `video_count` to plan short video content.
- Read the rising topics in `trending_list` to spot stories before they reach the main board.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/hot-search-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `board_sub_type` | string | No | - Empty string: Hot search list (default) |
| `board_type` | string | No | - 0: Hot search list (default) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "banner_dark": {
    "uri": "33a57000197f34889bc27",
    "url_list": [
      "https://p26-sign.douyinpic.com/obj/33a57000197f34889bc27?lk3s=03ea9982&x-expires…"
    ]
  },
  "banner_light": {
    "uri": "33a580000cefdf44e9f76",
    "url_list": [
      "https://p11-sign.douyinpic.com/obj/33a580000cefdf44e9f76?lk3s=03ea9982&x-expires…"
    ]
  },
  "data": {
    "active_time": "2026-11-03 15:27:26",
    "banner_display": {},
    "display_style": 0,
    "share_info": {
      "share_link_desc": "我在看抖音热榜，发现最火的内容，赶快来看！戳这里>>",
      "share_title": "我在看抖音热榜，发现最火的内容，赶快来看！",
      "share_url": "https://www.iesdouyin.com/share/billboard/?id=0"
    },
    "trending_desc": "实时上升热点",
    "trending_list": [
      {
        "article_detail_count": 0,
        "discuss_video_count": 1,
        "display_style": 0,
        "event_time": 1793667178,
        "group_id": "6967627156244927781",
        "hot_value": 0,
        "hotlist_param": "{\"board_type\":3,\"rank\":0,\"time\":1793691095}",
        "label": 0,
        "sentence_id": "2726464",
        "sentence_tag": 7000,
        "video_count": 5,
        "word": "央行将上调外汇存款准备金率"
      }
    ],
    "word_list": [
      {
        "can_extend_detail": false,
        "discuss_video_count": 1,
        "hot_value": 0,
        "hotlist_param": "{\"board_type\":0,\"time\":1793691095}",
        "is_n1": true,
        "label": 0,
        "sentence_id": "2727285",
        "topic_info": {},
        "view_count": 0,
        "word": "让互联网更好造福人民造福世界",
        "word_type": 14
      }
    ]
  },
  "extra": {
    "logid": "202611031531351724301AEE0DFF43838A",
    "now": 1793691095000,
    "time_cost": {
      "stream_inner": 440
    }
  },
  "log_pb": {
    "impr_id": "202611031531351724301AEE0DFF43838A"
  },
  "status_code": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.word_list[].word` | The trending phrase as shown on the board. |
| `data.word_list[].position` | Current rank of the word on the board. The first item in the sample has `position` 1. |
| `data.word_list[].hot_value` | Heat value of the word. Higher values rank higher. |
| `data.word_list[].video_count / data.word_list[].discuss_video_count` | Number of videos tied to the word. `discuss_video_count` counts discussion videos. |
| `data.word_list[].view_count` | View count for the word. |
| `data.word_list[].sentence_id / data.word_list[].group_id` | IDs for the hot word and its related content group. Both are strings. |
| `data.word_list[].event_time` | Unix timestamp in seconds for the event behind the word. |
| `data.word_list[].label / data.word_list[].label_url` | Label code for the word. `label_url` is an icon image URL when a label is set. |
| `data.trending_list[].word` | A rising topic from the separate real-time trending list. Its `hot_value` is 0 in the sample, so rely on `video_count` to compare items. |
| `data.active_time` | Time of the board in the format `YYYY-MM-DD HH:MM:SS`. |

### Notes

- Send `board_type` as a string. The default `"0"` with an empty `board_sub_type` returns the main hot search list.
- `data.word_list[].hotlist_param` is a JSON string that holds the board type, rank and a Unix timestamp.
- Some entries in `data.word_list`, such as the one with `is_n1` set to `true`, have `hot_value` 0 and no `position`. Check for these before ranking.
- For brand boards, call [Douyin Brand Hot Search List](/apis/douyin/app-v3/brand-hot-search-list). For music boards, call [Douyin Music Hot Search List](/apis/douyin/app-v3/music-hot-search-list).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Video Statistics (Batch)](/apis/douyin/app-v3/multi-video-statistics): Get play, like, share and download counts for up to 50 Douyin videos in one request by passing comma-separated video IDs.
- [Douyin User Videos](/apis/douyin/app-v3/user-post-videos): Get the videos on a Douyin user's profile with descriptions, publish time and play, like, comment and share counts.
- [Get Douyin brand hot search list data](/apis/douyin/app-v3/brand-hot-search-list): Get Douyin brand hot search category data.

---
Machine-readable: [`catalog/models/douyin/app-v3/hot-search-list.json`](../../../../catalog/models/douyin/app-v3/hot-search-list.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/hot-search-list
