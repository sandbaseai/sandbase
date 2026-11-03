# TikTok Music Search API: pricing, parameters and code examples

`tiktok/app-v3/music-search-result` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns TikTok music search results matching specified keywords, with options to filter by title or author and sort by usage or duration.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/music-search-result", "keyword": "openai"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/music-search-result', {'keyword': 'openai'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/music-search-result", {
  "keyword": "openai"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/music-search-result", sandbase.Params{
	"keyword": "openai",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/music-search-result` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number, do not exceed 20 default `20` |
| `offset` | integer |  | Offset, starting from 0, the second page gets the cursor value from the response as the offset to continue the request. default `0` |
| `region` | string |  | Region, default is US-America, for optional values please refer to TikTok region codes or ISO 3166-1 alpha-2 country codes. default `"US"` |
| `keyword` | string | yes | Keyword  |
| `filter_by` | integer |  | Filter type, 0-All, 1-Title, 2-Author, default is 0-All default `0` |
| `sort_type` | integer |  | Sort type, 0-Relatedness, 1-Most used, 2-Latest, 3-Shortest duration, 4-Longest duration, default is 0-Relatedness default `0` |

## Details

Returns a list of TikTok music tracks that match a search `keyword`. Each track includes its title-level details, author, album, duration, cover images and licensing flags. You can filter by title or author, sort the results, and set the region.

### Use cases

- Find sounds that match a brand or topic name, such as `openai`, to see which tracks exist on TikTok.
- Sort by `sort_type` `1` to list the most used tracks for a keyword.
- Check `commercial_right_type` and `has_commerce_right` to screen tracks before a campaign picks one.
- Collect track IDs and pass them to a music detail or music video call.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/music-search-result" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "openai"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Keyword |
| `count` | integer | No | Number, do not exceed 20 |
| `filter_by` | integer | No | Filter type, 0-All, 1-Title, 2-Author, default is 0-All |
| `offset` | integer | No | Offset, starting from 0, the second page gets the cursor value from the response as the offset to continue the request. |
| `region` | string | No | Region, default is US-America, for optional values please refer to TikTok region codes or ISO 3166-1 alpha-2 country codes. |
| `sort_type` | integer | No | Sort type, 0-Relatedness, 1-Most used, 2-Latest, 3-Shortest duration, 4-Longest duration, default is 0-Relatedness |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "ad_info": {},
  "cursor": 20,
  "extra": {
    "api_debug_info": null,
    "fatal_item_ids": [],
    "logid": "202611030743562837450654C169018201",
    "now": 1793691837000,
    "search_request_id": "",
    "server_stream_time": 1000
  },
  "feedback_type": "music",
  "global_doodle_config": {
    "display_filter_bar": 1,
    "enable_music_mix_rank": 1,
    "feedback_survey": [
      {
        "feedback_type": "music",
        "long_stress_info": null,
        "multiple_choices": [
          {
            "key": "Dislike",
            "value": "Dislike"
          }
        ],
        "send_us_multiple_choices": null
      }
    ],
    "feel_good": {
      "extra": "has_logged=true&query_flag1=0&query_flag2=0&query_usability=0&search_display_sur…",
      "token": "eyJhbGci…",
      "token_type": "Bearer"
    },
    "hide_results": false,
    "hit_dolphin": false,
    "hit_shark": false,
    "keyword": "openai",
    "new_source": "normal_search",
    "search_channel": "musically_music",
    "tns_search_result": "Pass"
  },
  "has_more": 1,
  "log_pb": {
    "impr_id": "202611030743562837450654C169018201"
  },
  "music": [
    {
      "album": "Traffic Alert",
      "allow_offline_music_to_detail_page": false,
      "artists": [],
      "audition_duration": 60,
      "author": "OpenAI",
      "author_deleted": false,
      "author_position": null,
      "avatar_medium": {
        "height": 720,
        "uri": "musically-maliva-obj/1594805258216454",
        "url_list": [
          "https://p19-common-sign.tiktokcdn-us.com/musically-maliva-obj/1594805258216454~t…"
        ],
        "url_prefix": null,
        "width": 720
      },
      "avatar_thumb": {
        "height": 720,
        "uri": "musically-maliva-obj/1594805258216454",
        "url_list": [
          "https://p19-common-sign.tiktokcdn-us.com/musically-maliva-obj/1594805258216454~t…"
        ],
        "url_prefix": null,
        "width": 720
      },
      "binded_challenge_id": 0,
      "can_be_stitched": true,
      "can_not_reuse": false
    }
  ],
  "music_info_list": [
    {
      "aweme_list": null,
      "card_type": 1,
      "music": {
        "album": "Traffic Alert",
        "allow_offline_music_to_detail_page": false,
        "artists": [],
        "audition_duration": 60,
        "author": "OpenAI",
        "author_deleted": false,
        "author_position": null,
        "avatar_medium": {
          "height": 720,
          "uri": "musically-maliva-obj/1594805258216454",
          "url_list": [
            "https://p19-common-sign.tiktokcdn-us.com/musically-maliva-obj/1594805258216454~t…"
          ],
          "url_prefix": null,
          "width": 720
        }
      },
      "musics": null
    }
  ],
  "qc": "",
  "status_code": 0,
  "total": 352
}
```

### Response fields

| Field | Meaning |
|---|---|
| `music[].id / music[].id_str` | Track ID as a number and as a string. Use the string form to avoid number precision loss in your code. |
| `music[].author` | Name of the track's author or uploader. |
| `music[].album` | Album name shown for the track. |
| `music[].duration / music[].audition_duration` | Track length and preview length, both `60` in the sample. |
| `music[].create_time` | Creation time of the track as a Unix timestamp in seconds. |
| `music[].cover_large.url_list[] / music[].cover_medium.url_list[] / music[].cover_thumb.url_list[]` | Cover image URLs in three sizes. |
| `music[].commercial_right_type / music[].has_commerce_right / music[].is_commerce_music` | Flags that describe commercial licensing for the track. |
| `music[].is_original / music[].is_original_sound / music[].is_pgc` | Flags that show whether the track is an original sound or professionally produced content. |
| `music[].language` | Language tag of the track, for example `non_vocal`. |
| `cursor / has_more` | `cursor` is the offset value for the next page. `has_more` is `1` when more results remain. |

### Notes

- For the next page, send the `cursor` value from the response as `offset`. In the sample, `cursor` is `20`.
- `count` must not exceed 20.
- `filter_by` takes `0` (All), `1` (Title) or `2` (Author). `sort_type` takes `0` (Relatedness), `1` (Most used), `2` (Latest), `3` (Shortest duration) or `4` (Longest duration).
- Pass a track `id` to [TikTok Music Details](/apis/tiktok/app-v3/music-detail) or [TikTok Music Video List](/apis/tiktok/app-v3/music-video-list) to see more about a track.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok LIVE Status](/apis/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/apis/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/apis/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/music-search-result.json`](../../../../catalog/models/tiktok/app-v3/music-search-result.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/music-search-result
