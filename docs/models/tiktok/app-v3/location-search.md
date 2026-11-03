# TikTok Location Search API: pricing, parameters and code examples

`tiktok/app-v3/location-search` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Searches for locations on TikTok using a text query. Returns matching place results with pagination support via offset and count parameters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/location-search", "keyword": "OpenAI"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/location-search', {'keyword': 'OpenAI'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/location-search", {
  "keyword": "OpenAI"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/location-search", sandbase.Params{
	"keyword": "OpenAI",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/location-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number default `20` |
| `offset` | integer |  | Offset default `0` |
| `keyword` | string | yes | Keyword  |

## Details

Searches TikTok places by a text query and returns matching points of interest. Each result has a name, address, coordinates, place type and video count. The only required input is `keyword`.

### Use cases

- Find the TikTok place ID for a venue, landmark or town by searching its name.
- Compare how many videos are tagged at different places with similar names.
- Map search results by `lat` and `lng` to see where matching places are located.
- Filter results by `poi_type` or `country_code` to narrow a broad name search.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/location-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "OpenAI"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Keyword |
| `count` | integer | No | Number |
| `offset` | integer | No | Offset |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "cursor": 20,
  "extra": {
    "api_debug_info": [
      "1269"
    ],
    "fatal_item_ids": [],
    "logid": "20261103074355B12B42E16EC2A4CB89F7",
    "now": 1793691837158,
    "search_request_id": "",
    "server_stream_time": 1333
  },
  "feedback_type": "poi",
  "global_doodle_config": {
    "display_filter_bar": 1,
    "feedback_survey": [
      {
        "feedback_type": "poi",
        "long_stress_info": null,
        "multiple_choices": [
          {
            "key": "Unrelated location",
            "value": "Unrelated location"
          }
        ],
        "send_us_multiple_choices": null
      }
    ],
    "hide_results": false,
    "hit_dolphin": false,
    "hit_shark": false,
    "keyword": "OpenAI",
    "new_source": "switch_tab",
    "search_channel": "tiktok_places",
    "tns_search_result": "Pass"
  },
  "has_more": 1,
  "log_pb": {
    "impr_id": "20261103074355B12B42E16EC2A4CB89F7"
  },
  "poi_info": {
    "dynamic_patch": {
      "aweme_list": null,
      "aweme_multi_tab_list": null,
      "related_word_list": null,
      "tab_map": null
    },
    "local_service_info": {
      "anchor_poi_index": "",
      "ttd_poi_id": "0",
      "vertical_filter_pass_through": ""
    },
    "nearby_auth": {
      "aweme_list": null,
      "aweme_multi_tab_list": null,
      "nearby_auth": {},
      "related_word_list": null,
      "tab_map": null
    },
    "poi_info": [
      {
        "collect_info": "{\"tt_type_code\":\"08a1b4\",\"is_tt_key_category\":1,\"tt_poi_type_name_level0\":\"Trave…",
        "country_code": "FR",
        "extra": "",
        "is_collected": 0,
        "is_fallback_header_icon": 0,
        "lat": "43.711900",
        "lng": "4.982780",
        "local_service_key_category": "Travel",
        "local_service_key_category_enum": 5,
        "local_service_todo_model": "Other",
        "opening_time": "",
        "parent_poi": "Bouches-du-Rhone"
      }
    ]
  },
  "status_code": 0,
  "version": "v2"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `poi_info.poi_info[].poi_id_str` | The place ID as a string. Use this string form to avoid rounding of the long number in `poi_id`. |
| `poi_info.poi_info[].poi_name` | The name of the place. |
| `poi_info.poi_info[].poi_location` | The full address of the place as a single line of text. |
| `poi_info.poi_info[].poi_type` | The place type, such as `Mountain`, `Golf Course` or `District`. |
| `poi_info.poi_info[].lat / poi_info.poi_info[].lng` | Latitude and longitude of the place. Both are strings. |
| `poi_info.poi_info[].country_code` | Two-letter country code of the place, such as `FR`. |
| `poi_info.poi_info[].parent_poi` | The larger area that contains the place, such as a department or region. |
| `poi_info.poi_info[].video_count` | Number of TikTok videos linked to the place. |
| `poi_info.poi_info[].total_count_of_reviews` | Number of reviews recorded for the place. |
| `has_more / cursor` | `has_more` is `1` when more results are available. `cursor` holds the next position value, `20` in this response. |

### Notes

- Page through results with `count` (default `20`) and `offset` (default `0`). The response had `cursor` set to `20` and `has_more` set to `1`.
- Use `poi_id_str` rather than `poi_id` when you store or pass IDs on.
- Some places include `operating_hours`, with a `day` number and an `opening_show_time` text. Many fields, such as `poi_rating` and `opening_time`, can be empty strings.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok LIVE Status](/apis/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/apis/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/apis/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/location-search.json`](../../../../catalog/models/tiktok/app-v3/location-search.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/location-search
