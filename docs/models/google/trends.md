# Google Trends API: pricing, parameters and code examples

`google/trends` · data API · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Get Google Trends data for up to five keywords: interest over time, interest by region, related topics and related queries, by country, time range and category.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/trends", "q": "coffee,tea"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/trends', {'q': 'coffee,tea'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/trends", {
  "q": "coffee,tea"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/trends", sandbase.Params{
	"q": "coffee,tea",
})
```

Same call via the path form: `POST /v1/api/google/trends` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string | yes | Parameter defines the query or queries you want to search. You can use anything that you would use in a regular Google Trends search. The maximum number of queries per search is `5` (this only applies to "Interest over…  |
| `hl` | string |  | Parameter defines the language to use for the Google Trends search. It's a two or three-letter language code. (e.g., `en` for English, `es` for Spanish, or `fr` for French), optionally followed by a two-letter or…  |
| `tz` | string |  | Parameter is used to define a time zone offset. The default value is set to `420` (Pacific Day Time(PDT): -07:00). Value is shown in minutes and can span from `-1439` to `1439`. `tz` can be calculated using the time…  |
| `cat` | string |  | Parameter is used to define a search category. The default value is 0 (All categories). You can find or download all supported values in the Google Trends Categories list. Note that these are different from the…  |
| `csv` | string |  | Parameter is used for retrieving the CSV results. Set the parameter to `true` to retrieve CSV results as an array.  |
| `geo` | string |  | Parameter defines the location from where you want the search to originate. It defaults to `Worldwide` (activated when the value of `geo` parameter is not set or empty). Head to the Google Trends Locations for a full…  |
| `date` | string |  | Parameter is used to define a date. Available options: `now 1-H` - Past hour `now 4-H` - Past 4 hours `now 1-d` - Past day `now 7-d` - Past 7 days `today 1-m` - Past 30 days `today 3-m` - Past 90 days `today 12-m` -…  |
| `gprop` | string |  | Parameter is used for sorting results by property. The default property is set to `Web Search` (activated when the value of `gprop` parameter is not set or empty). Other available options: `images` - Image Search…  |
| `region` | string |  | Parameter is used for getting more specific results when using "Compared breakdown by region" and "Interest by region" `data_type` charts. Other `data_type` charts do not accept `region` parameter. The default value…  |
| `data_type` | string |  | Parameter defines the type of search you want to do. Available options: `TIMESERIES` - Interest over time (default) - Accepts both single and multiple queries per search. `GEO_MAP` - Compared breakdown by region -…  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |
| `include_low_search_volume` | string |  | Parameter is used for including low search volume regions in the results. Set the parameter to `true` to include low search volume regions in the results. This parameter is ignored if `data_type` is not set to…  |

## Details

Get Google Trends data for up to five keywords: interest over time, interest by region, related topics and related queries, by country, time range and category.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google/trends" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "coffee,tea", "data_type": "TIMESERIES"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | Yes | Parameter defines the query or queries you want to search. You can use anything that you would use in a regular Google Trends search. The maximum number of queries per search is `5` (this only applies to "Interest over time" and "Compared b |
| `data_type` | string | No | Parameter defines the type of search you want to do. Available options: `TIMESERIES` - Interest over time (default) - Accepts both single and multiple queries per search. `GEO_MAP` - Compared breakdown by region - Accepts only multiple quer |
| `hl` | string | No | Parameter defines the language to use for the Google Trends search. It's a two or three-letter language code. (e.g., `en` for English, `es` for Spanish, or `fr` for French), optionally followed by a two-letter or three-digit region code (e. |
| `geo` | string | No | Parameter defines the location from where you want the search to originate. It defaults to `Worldwide` (activated when the value of `geo` parameter is not set or empty). Head to the Google Trends Locations for a full list of supported Googl |
| `region` | string | No | Parameter is used for getting more specific results when using "Compared breakdown by region" and "Interest by region" `data_type` charts. Other `data_type` charts do not accept `region` parameter. The default value depends on the `geo` loc |
| `tz` | string | No | Parameter is used to define a time zone offset. The default value is set to `420` (Pacific Day Time(PDT): -07:00). Value is shown in minutes and can span from `-1439` to `1439`. `tz` can be calculated using the time difference between UTC + |
| `cat` | string | No | Parameter is used to define a search category. The default value is 0 (All categories). You can find or download all supported values in the Google Trends Categories list. Note that these are different from the categories supported for Goog |
| `gprop` | string | No | Parameter is used for sorting results by property. The default property is set to `Web Search` (activated when the value of `gprop` parameter is not set or empty). Other available options: `images` - Image Search `news` - News Search `froog |
| `date` | string | No | Parameter is used to define a date. Available options: `now 1-H` - Past hour `now 4-H` - Past 4 hours `now 1-d` - Past day `now 7-d` - Past 7 days `today 1-m` - Past 30 days `today 3-m` - Past 90 days `today 12-m` - Past 12 months `today 5- |
| `csv` | string | No | Parameter is used for retrieving the CSV results. Set the parameter to `true` to retrieve CSV results as an array. |
| `include_low_search_volume` | string | No | Parameter is used for including low search volume regions in the results. Set the parameter to `true` to include low search volume regions in the results. This parameter is ignored if `data_type` is not set to `GEO_MAP` or `GEO_MAP_0`. |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/google/trends.json`](../../../catalog/models/google/trends.json) · Store page: https://www.sandbase.ai/model/google/trends
