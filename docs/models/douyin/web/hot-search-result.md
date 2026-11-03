# Douyin Web Hot Search Results API: pricing, parameters and code examples

`douyin/web/hot-search-result` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns current hot search rankings and trending query results from Douyin web. Access active search trends directly without required query parameters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/hot-search-result"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/hot-search-result', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/hot-search-result", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/hot-search-result", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/web/hot-search-result` with the body above minus `model`.

## Details

Returns the current Douyin web hot search board. It includes a ranked list of hot words and a list of rising trending topics. The request takes no input parameters, so send an empty JSON object `{}`.

### Use cases

- Pull the ranked hot words on Douyin and store them to see which topics lead the board over time.
- Compare `hot_value` and `view_count` across hot words to find the topics that draw the most attention.
- Collect the rising topics in `data.trending_list` to spot stories before they reach the main ranking.
- Save the cover images and `sentence_id` values to build a dashboard of current Douyin news topics.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/hot-search-result" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

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
    "active_time": "2026-11-03 15:31:55",
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
        "event_time": 1793628525,
        "group_id": "7702756444730922282",
        "hot_value": 0,
        "hotlist_param": "{\"board_type\":3,\"rank\":0,\"time\":1793691146}",
        "label": 0,
        "sentence_id": "2726328",
        "sentence_tag": 3002,
        "video_count": 3,
        "word": "比利时首相因预算谈判失败请辞"
      }
    ],
    "word_list": [
      {
        "can_extend_detail": false,
        "discuss_video_count": 1,
        "hot_value": 0,
        "hotlist_param": "{\"board_type\":0,\"time\":1793691146}",
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
    "logid": "202611031532264EE322D5C259B56DE447",
    "now": 1793691146000,
    "time_cost": {
      "stream_inner": 188
    }
  },
  "log_pb": {
    "impr_id": "202611031532264EE322D5C259B56DE447"
  },
  "status_code": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.word_list[].word` | The hot search phrase as shown on the Douyin board. |
| `data.word_list[].position / data.word_list[].max_rank` | `position` is the rank of the word in the list, starting at 1. `max_rank` is the best rank value returned for the word. |
| `data.word_list[].hot_value / data.word_list[].view_count` | Heat score and view count for the hot word. Some entries, such as pinned items without a rank, return no `hot_value`. |
| `data.word_list[].video_count / data.word_list[].discuss_video_count` | Number of videos tied to the hot word. `discuss_video_count` is a second video count that comes with it. |
| `data.word_list[].sentence_id / data.word_list[].group_id` | Identifiers for the hot word and its related content group. Both are returned as strings. |
| `data.word_list[].event_time` | Time of the event behind the word, as a Unix timestamp in seconds. |
| `data.word_list[].word_cover.url_list` | Signed image URLs for the cover picture of the word. The URLs carry an `x-expires` parameter. |
| `data.trending_list[].word / data.trending_list[].video_count` | The rising topic phrase and the number of videos linked to it. Entries in this list have a `hot_value` of 0 in this sample. |
| `data.trending_desc / data.active_time` | `trending_desc` is the label for the rising list. `active_time` is the date and time string for the board. |
| `extra.now` | Server time of the response as a Unix timestamp in milliseconds. |

### Notes

- No parameters are needed. Send `{}` as the request body.
- `data.word_list[].hotlist_param` is a JSON string with `board_type`, `rank` and `time`. Parse it if you need the board type and timestamp.
- `data.word_list[]` entries with `is_n1` set to `true` have no `position` or `hot_value` in the sample, so check for missing keys.
- To read the videos in a chosen topic or find the creators behind them, use [Douyin Video Channel Feed](/apis/douyin/web/video-channel-result) or [Douyin Web Home Feed](/apis/douyin/web/home-feed).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Batch Video ID Extraction](/apis/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/apis/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/apis/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/hot-search-result.json`](../../../../catalog/models/douyin/web/hot-search-result.json) · Store page: https://www.sandbase.ai/model/douyin/web/hot-search-result
