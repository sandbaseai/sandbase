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

Fetch creator search trend metrics using `query_id_str` to analyze search popularity by region and time.

### Use cases

- Analyze search popularity trends across different regions over time.
- Inspect query performance to guide content topic planning.
- Retrieve query analysis insights from search trends.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/creator-search-insights-trend" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query_id_str": "<query_id_str>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query_id_str` | string | Yes | Query ID, obtained from fetch_creator_search_insights response |
| `from_tab_path` | string | No | From tab path, default "TRENDING,TOPICS" |
| `query_analysis_required` | boolean | No | Whether query analysis is required, default True |

### Notes

- Obtain `query_id_str` from the creator search insights endpoint response.
- `from_tab_path` defaults to "TRENDING,TOPICS".
- `query_analysis_required` defaults to True.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok LIVE Status](/model/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/model/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/model/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/creator-search-insights-trend.json`](../../../../catalog/models/tiktok/app-v3/creator-search-insights-trend.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/creator-search-insights-trend
