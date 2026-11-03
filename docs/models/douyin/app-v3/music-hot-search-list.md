# Douyin Music Hot Search List API: pricing, parameters and code examples

`douyin/app-v3/music-hot-search-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Retrieves Douyin hot search music rankings, audio details, and artist metadata based on the selected chart category and pagination cursor.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/music-hot-search-list", "chart_type": "hot", "cursor": "0"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/music-hot-search-list', {'chart_type': 'hot', 'cursor': '0'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/music-hot-search-list", {
  "chart_type": "hot",
  "cursor": "0"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/music-hot-search-list", sandbase.Params{
	"chart_type": "hot",
	"cursor": "0",
})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/music-hot-search-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Cursor, default value is '0', used for paginating data retrieval. After each request, the next cursor value will be returned, and the `has_more` field indicates whether there is more data available. default `"0"` |
| `chart_type` | string |  | Chart type, default value is 'hot', supports the following values: 'hot': Hot chart; 'trending': Trending chart; 'original': Original chart default `"hot"` |

## Details

Returns a ranked list of music tracks from a Douyin music chart. You can pick the chart with `chart_type` (`hot`, `trending` or `original`) and page through results with `cursor`. Both inputs are optional.

### Use cases

- Pull the current `hot` chart to see which songs are gaining heat on Douyin.
- Compare the `hot`, `trending` and `original` charts to find tracks that appear on more than one.
- Store the `heat` value of each track over time to chart how a song rises or falls.
- Build a list of track and album names to check for sounds to use in new videos.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/music-hot-search-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `chart_type` | string | No | Chart type, default value is 'hot', supports the following values: 'hot': Hot chart; 'trending': Trending chart; 'original': Original chart |
| `cursor` | string | No | Cursor, default value is '0', used for paginating data retrieval. After each request, the next cursor value will be returned, and the `has_more` field indicates whether there is more data available. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "aweme_list": [],
  "chart_content_type": 1,
  "cursor": 0,
  "extra": {
    "fatal_item_ids": [],
    "logid": "20261103153136FB69BAA40A084911D413",
    "now": 1793691096000
  },
  "has_more": 0,
  "log_pb": {
    "impr_id": "20261103153136FB69BAA40A084911D413"
  },
  "material_list": [],
  "music_list": [
    {
      "can_background_play": true,
      "has_copyright": true,
      "heat": 19951092,
      "music_info": {
        "album": "你的不经意",
        "artist_user_infos": null,
        "artists": [],
        "audition_duration": 30,
        "author": "Fozik佛子克",
        "author_deleted": false,
        "author_position": null,
        "binded_challenge_id": 0
      }
    }
  ],
  "release_date": "2026-10-30",
  "show_author": false,
  "show_heat": true,
  "status_code": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `music_list[]` | One ranked track on the chart. Items come in chart order. |
| `music_list[].heat` | Heat score of the track on this chart. A higher number means a higher position. |
| `music_list[].music_info.author` | Name of the artist or account that published the track. |
| `music_list[].music_info.album` | Album or song title shown for the track. It can be an empty string. |
| `music_list[].music_info.audition_duration` | Length of the preview clip, as a number. Compare it with the other duration fields in the item before you assume units. |
| `music_list[].has_copyright / music_list[].can_background_play` | Boolean flags. `has_copyright` marks whether the track carries copyright info. `can_background_play` marks whether it can play in the background. |
| `music_list[].music_info.binded_challenge_id` | ID of a challenge linked to the track. The value is `0` when none is linked. |
| `release_date` | Date of the chart, in `YYYY-MM-DD` format. |
| `has_more / cursor` | Pagination state. `has_more` is `0` when there are no more pages. `cursor` is the cursor value returned for this page. |
| `show_heat / show_author` | Boolean display flags for the chart. `show_heat` is `true` when the chart shows heat values. |

### Notes

- Send `chart_type` as `hot`, `trending` or `original`. The default is `hot`.
- For the next page, send the returned `cursor` as the new `cursor` value while `has_more` is not `0`.
- `aweme_list` and `material_list` were empty in this response. The track data is in `music_list`.
- To get full details for one track, call [Douyin Music Details](/apis/douyin/app-v3/music-detail). To list videos that use a track, call [Douyin Music Video List](/apis/douyin/app-v3/music-video-list).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Brand Hot Search List](/apis/douyin/app-v3/brand-hot-search-list): Returns the current Douyin brand hot search list and category data.
- [Douyin Brand Hot Search List Detail](/apis/douyin/app-v3/brand-hot-search-list-detail): Returns detailed brand hot search list data from Douyin for a specific category.
- [Douyin Short Link Generator](/apis/douyin/app-v3/generate-short-url): Converts a standard Douyin web link into a shortened Douyin URL.

---
Machine-readable: [`catalog/models/douyin/app-v3/music-hot-search-list.json`](../../../../catalog/models/douyin/app-v3/music-hot-search-list.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/music-hot-search-list
