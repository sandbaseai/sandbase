# TikTok Creator Search Insights Trend API: pricing, parameters and code examples

`tiktok/app-v3/creator-search-insights-trend` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns creator search insights trend data, covering search popularity across regions and time periods for a specified query ID.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/creator-search-insights-trend", "query_id_str": "7555720035176562699"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/creator-search-insights-trend', {'query_id_str': '7555720035176562699'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/creator-search-insights-trend", {
  "query_id_str": "7555720035176562699"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/creator-search-insights-trend", sandbase.Params{
	"query_id_str": "7555720035176562699",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/creator-search-insights-trend` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query_id_str` | string | yes | Query ID, obtained from fetch_creator_search_insights response  |
| `from_tab_path` | string |  | From tab path, default "TRENDING,TOPICS"  |
| `query_analysis_required` | boolean |  | Whether query analysis is required, default True  |

## Details

Returns search trend data for one TikTok Creator Search Insights query. It includes the query text, a popularity score, recent trend values, the top countries and a topic category. It needs a `query_id_str` value.

### Use cases

- Track how a search query's popularity has moved over its most recent data points.
- Find which countries search for a query most, to choose a target audience.
- Check a query's topic category and labels, such as `content_gap`, before planning videos.
- Compare the video count for a query against its popularity to judge how crowded the topic is.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/creator-search-insights-trend" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query_id_str": "7555720035176562699"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query_id_str` | string | Yes | Query ID, obtained from fetch_creator_search_insights response |
| `from_tab_path` | string | No | From tab path, default "TRENDING,TOPICS" |
| `query_analysis_required` | boolean | No | Whether query analysis is required, default True |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "extra": {
    "latency": 59,
    "logid": "20261103074352BD3FE2C596D3AF021A95",
    "now": 1793691832174,
    "vgeo": "VGeo-US"
  },
  "inspiration_related_product": [],
  "status_code": 0,
  "status_msg": "",
  "top_countries": [
    {
      "country_code": "US",
      "country_name": "United States of America"
    }
  ],
  "user_inspiration": {
    "business_types": [
      "basic"
    ],
    "cover_image": "",
    "dislike_option_enabled": false,
    "entity_id": 0,
    "favorited_updated_at": 0,
    "inspiration_types": [
      "search"
    ],
    "is_favorited": false,
    "order_popularity_seq": [],
    "popularity": 74,
    "popularity_updated_at": 1793687815,
    "popularity_v2": 285385,
    "query_id": 7555720035176562699
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `user_inspiration.query_text` | The search phrase this record describes. |
| `user_inspiration.popularity / user_inspiration.popularity_v2` | Two popularity scores for the query. `popularity` is a small number (74 in this sample) and `popularity_v2` is a larger number (285385 in this sample). |
| `user_inspiration.trending_seq / user_inspiration.trending_seq_v2` | Lists of recent popularity values for the query, matching the two popularity scores. Each list holds one value per data point. |
| `user_inspiration.popularity_updated_at` | Unix timestamp in seconds of the last popularity update. |
| `user_inspiration.video_num` | Number of videos tied to the query. |
| `user_inspiration.query_labels` | Labels for the query, such as `content_gap`. |
| `user_inspiration.textnet.layer1 / user_inspiration.textnet.layer2 / user_inspiration.textnet.layer3 / user_inspiration.textnet.layer4` | Topic category from broad to narrow, for example ACGN, Games, Game Works, Game Tutorials and Strategies. |
| `top_countries[].country_code / top_countries[].country_name` | Countries where the query is most popular, with the country code and its name. |

### Notes

- Get `query_id_str` from the [TikTok Creator Search Insights](/apis/tiktok/app-v3/creator-search-insights) response.
- The response repeats the ID as a number in `user_inspiration.query_id` and as a string in `user_inspiration.query_id_str`. Send the string form.
- For more on the same query, call [TikTok Creator Search Insights Detail](/apis/tiktok/app-v3/creator-search-insights-detail) or [TikTok Creator Search Insights Videos](/apis/tiktok/app-v3/creator-search-insights-videos).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok LIVE Status](/apis/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/apis/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/apis/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/creator-search-insights-trend.json`](../../../../catalog/models/tiktok/app-v3/creator-search-insights-trend.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/creator-search-insights-trend
