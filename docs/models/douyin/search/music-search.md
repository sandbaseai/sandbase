# Douyin Music Search API: pricing, parameters and code examples

`douyin/search/music-search` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns music search results from Douyin based on keywords and filters such as sort type, content type, and duration.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/search/music-search", "backtrace": "", "content_type": "0", "cursor": 0, "filter_duration": "0", "keyword": "猫咪", "publish_time": "0", "search_id": "", "sort_type": "0"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/search/music-search', {'backtrace': '', 'content_type': '0', 'cursor': 0, 'filter_duration': '0', 'keyword': '猫咪', 'publish_time': '0', 'search_id': '', 'sort_type': '0'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/search/music-search", {
  "backtrace": "",
  "content_type": "0",
  "cursor": 0,
  "filter_duration": "0",
  "keyword": "猫咪",
  "publish_time": "0",
  "search_id": "",
  "sort_type": "0"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/search/music-search", sandbase.Params{
	"backtrace": "",
	"content_type": "0",
	"cursor": 0,
	"filter_duration": "0",
	"keyword": "猫咪",
	"publish_time": "0",
	"search_id": "",
	"sort_type": "0",
})
```

Same call via the path form: `POST /v1/api/douyin/search/music-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | integer |  | Pagination cursor (0 for first request) default `0` |
| `keyword` | string |  | Search keyword, e.g., "game background music" default `"猫咪"` |
| `backtrace` | string |  | Backtrace for pagination, obtained from the last response default `""` |
| `search_id` | string |  | Search ID for pagination default `""` |
| `sort_type` | string |  | Sorting method default `"0"` |
| `content_type` | string |  | Content type filter default `"0"` |
| `publish_time` | string |  | Publish time filter default `"0"` |
| `filter_duration` | string |  | Video duration filter default `"0"` |

## Details

Returns a page of Douyin music search results for a search `keyword`. Each result is a music track with its author, duration, cover images and lyric URL. You can narrow results with `sort_type`, `content_type`, `publish_time` and `filter_duration`.

### Use cases

- Find Douyin tracks that match a theme such as a pet or a mood, then collect their IDs.
- Build a list of track authors and durations for a given keyword.
- Download cover images and lyric files for the tracks a search returns.
- Page through deeper results to build a larger set of tracks for one keyword.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/search/music-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `backtrace` | string | No | Backtrace for pagination, obtained from the last response |
| `content_type` | string | No | Content type filter |
| `cursor` | integer | No | Pagination cursor (0 for first request) |
| `filter_duration` | string | No | Video duration filter |
| `keyword` | string | No | Search keyword, e.g., "game background music" |
| `publish_time` | string | No | Publish time filter |
| `search_id` | string | No | Search ID for pagination |
| `sort_type` | string | No | Sorting method |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "ad_info": {},
  "cursor": 10,
  "extra": {
    "fatal_item_ids": [],
    "logid": "20261103153219CE98A368E9F20E36B9C7",
    "now": 1793691139000,
    "scenes": null,
    "search_request_id": ""
  },
  "global_doodle_config": {
    "keyword": "猫咪"
  },
  "has_more": 1,
  "log_pb": {
    "impr_id": "20261103153219CE98A368E9F20E36B9C7",
    "stab_extra": {
      "traffic_identification": "normal"
    }
  },
  "music": [
    {
      "album": "",
      "artist_user_infos": null,
      "artists": [],
      "audition_duration": 18,
      "author": "念能先生",
      "author_deleted": false,
      "author_position": null,
      "binded_challenge_id": 0,
      "can_background_play": true,
      "collect_stat": 0,
      "cover_color_hsv": {
        "h": 53,
        "s": 15,
        "v": 96
      },
      "cover_hd": {
        "height": 720,
        "uri": "tos-cn-v-2774c002/ogCeF4XyiLHA6aOAIVIGYBeSIAQ4AAHeBaIVPz",
        "url_list": [
          "https://p3.douyinpic.com/aweme/1080x1080/tos-cn-v-2774c002/ogCeF4XyiLHA6aOAIVIGY…"
        ],
        "width": 720
      }
    }
  ],
  "music_header_info_list": [],
  "music_info_list": [
    {
      "card_type": 999,
      "dynamic_patch": {
        "card_type_name": "music_channel",
        "height": 84,
        "origin_type": 3,
        "raw_data": "{\"music\":{\"id\":7702401322850748456,\"id_str\":\"7702401322850748456\",\"title\":\"小猫咪（剪…",
        "schema": "aweme://lynxview/?channel=fe_lynx_main_v2_normal&bundle=music-card-vertical%2Fte…"
      },
      "music": {
        "album": "",
        "artist_user_infos": null,
        "artists": [],
        "audition_duration": 18,
        "author": "念能先生",
        "author_deleted": false,
        "author_position": null,
        "binded_challenge_id": 0
      },
      "musics": null
    }
  ],
  "qc": "",
  "render_type": 0,
  "search_channel": "aweme_music"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `music[].id / music[].id_str` | Track ID as a number and as a string. Use the string form to avoid number precision problems. |
| `music[].author` | Name of the track's author or artist. |
| `music[].duration / music[].audition_duration` | Length values for the track, as whole numbers. They match each other in the sample items. |
| `music[].cover_hd / cover_large / cover_medium / cover_thumb` | Cover image in four sizes. Each has `url_list` with image URLs, plus `uri`, `width` and `height`. |
| `music[].lyric_url` | Link to the lyric file for the track. |
| `music[].is_original / is_original_sound / is_pgc / is_commerce_music` | Flags that describe the track type, such as original audio, PGC or commercial music. |
| `music_info_list[].dynamic_patch.raw_data` | JSON string of a music card. It holds the track title (the `title` key), which the main `music[]` items in this trimmed response do not show. |
| `has_more` | Value `1` means more results are available for the next page. |
| `cursor` | Cursor value returned for the next page request. This response returned `10`. |
| `log_pb.impr_id` | Search request ID for this response. It matches `extra.logid` in this sample. |

### Notes

- Send `cursor` as `0` for the first page. For the next page, pass the `cursor` value from the response.
- For deeper pages, also send `backtrace` and `search_id` from the previous response.
- Check `has_more` to see whether another page exists.
- To work with a track after a search, pass its ID to [Douyin Music Details](/apis/douyin/app-v3/music-detail) or [Douyin Music Video List](/apis/douyin/app-v3/music-video-list).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Challenge Search](/apis/douyin/search/challenge-search-v1): Returns Douyin challenge and hashtag search results matching a query.
- [Douyin Hashtag Challenge Search (V2)](/apis/douyin/search/challenge-search-v2): Returns Douyin hashtag and challenge search results matching a query keyword.
- [Douyin Hashtag Suggestions](/apis/douyin/search/challenge-suggest): Returns a list of suggested Douyin hashtags and challenges matching a query keyword, including challenge IDs and view counts.

---
Machine-readable: [`catalog/models/douyin/search/music-search.json`](../../../../catalog/models/douyin/search/music-search.json) · Store page: https://www.sandbase.ai/model/douyin/search/music-search
