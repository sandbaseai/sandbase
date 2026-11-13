# Google Forums API: pricing, parameters and code examples

`google/forums` · data API · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Get Google's Forums results for a query: discussion threads from Reddit, Quora and other forums with title, snippet, source and answer counts.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/forums", "q": "best budget mechanical keyboard"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/forums', {'q': 'best budget mechanical keyboard'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/forums", {
  "q": "best budget mechanical keyboard"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/forums", sandbase.Params{
	"q": "best budget mechanical keyboard",
})
```

Same call via the path form: `POST /v1/api/google/forums` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string | yes | Parameter defines the query you want to search. To search for events in a specific location, just include the location inside your search query (e.g. `Events in Austin, TX`).  |
| `gl` | string |  | Parameter defines the country to use for the Google Forums search. It's a two-letter country code. (e.g., `us` for the United States, `uk` for United Kingdom, or `fr` for France). Head to the Google countries page for…  |
| `hl` | string |  | Parameter defines the language to use for the Google Forums search. It's a two or three-letter language code. (e.g., `en` for English, `es` for Spanish, or `fr` for French), optionally followed by a two-letter or…  |
| `tbs` | string |  | (to be searched) parameter defines advanced search parameters that aren't possible in the regular query field. (e.g., advanced search for dates, time period, etc.).  |
| `nfpr` | string |  | Parameter defines the exclusion of results from an auto-corrected query when the original query is spelled wrong. It can be set to `1` to exclude these results, or `0` to include them (default). Note that this…  |
| `uule` | string |  | Parameter is the Google encoded location you want to use for the search. `uule` and `location` parameters can't be used together. For consistent results with coordinates-based `uule` parameter, a matching `gl`…  |
| `start` | string |  | Parameter defines the result offset. It skips the given number of results. It's used for pagination. (e.g., `0` (default) is the first page of results, `10` is the 2nd page of results, `20` is the 3rd page of results,…  |
| `device` | string |  | Parameter defines the device to use to get the results. It can be set to `desktop` (default) to use a regular browser, `tablet` to use a tablet browser (currently using iPads), or `mobile` to use a mobile browser.  |
| `filter` | string |  | Parameter defines if the filters for 'Similar Results' and 'Omitted Results' are on or off. It can be set to `1` (default) to enable these filters, or `0` to disable these filters.  |
| `end_date` | string |  | Parameter defines the end date of time period you want to limit the image search to. Format: `YYYYMMDD` Example: `20251231` This parameter can't be used with `period_unit`/`period_value` parameters. `end_date` with…  |
| `location` | string |  | Parameter defines from where you want the search to originate. If several locations match the location requested, we'll pick the most popular one. Head to the /locations.json API if you need more precise control. The…  |
| `start_date` | string |  | Parameter defines the start date of time period you want to limit the image search to. Format: `YYYYMMDD` Example: `20251201` This parameter can't be used with `period_unit`/`period_value` parameters. `start_date` with…  |
| `period_unit` | string |  | Parameter defines the time period unit to search for the recent images, e.g. from past minute, hour, day etc. Options: `s` - Second `n` - Minute `h` - Hour `d` - Day `w` - Week `m` - Month `y` - Year This parameter… one of: `s`, `n`, `h`, `d`, `w`, `m`, `y` |
| `period_value` | string |  | Parameter defines an optional time period value that can be used with `period_unit` to describe time periods like `15 seconds`, `42 hours`, `178 days` etc. Default value: `1` Value range: `1..2147483647`  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |

## Details

Get Google's Forums results for a query: discussion threads from Reddit, Quora and other forums with title, snippet, source and answer counts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google/forums" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "best budget mechanical keyboard"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | Yes | Parameter defines the query you want to search. To search for events in a specific location, just include the location inside your search query (e.g. `Events in Austin, TX`). |
| `location` | string | No | Parameter defines from where you want the search to originate. If several locations match the location requested, we'll pick the most popular one. Head to the /locations.json API if you need more precise control. The `location` and `uule` p |
| `uule` | string | No | Parameter is the Google encoded location you want to use for the search. `uule` and `location` parameters can't be used together. For consistent results with coordinates-based `uule` parameter, a matching `gl` parameter is required. Head to |
| `gl` | string | No | Parameter defines the country to use for the Google Forums search. It's a two-letter country code. (e.g., `us` for the United States, `uk` for United Kingdom, or `fr` for France). Head to the Google countries page for a full list of support |
| `hl` | string | No | Parameter defines the language to use for the Google Forums search. It's a two or three-letter language code. (e.g., `en` for English, `es` for Spanish, or `fr` for French), optionally followed by a two-letter or three-digit region code (e. |
| `period_unit` | string | No | Parameter defines the time period unit to search for the recent images, e.g. from past minute, hour, day etc. Options: `s` - Second `n` - Minute `h` - Hour `d` - Day `w` - Week `m` - Month `y` - Year This parameter can't be used with `start |
| `period_value` | string | No | Parameter defines an optional time period value that can be used with `period_unit` to describe time periods like `15 seconds`, `42 hours`, `178 days` etc. Default value: `1` Value range: `1..2147483647` |
| `start_date` | string | No | Parameter defines the start date of time period you want to limit the image search to. Format: `YYYYMMDD` Example: `20251201` This parameter can't be used with `period_unit`/`period_value` parameters. `start_date` with blank `end_date` prod |
| `end_date` | string | No | Parameter defines the end date of time period you want to limit the image search to. Format: `YYYYMMDD` Example: `20251231` This parameter can't be used with `period_unit`/`period_value` parameters. `end_date` with blank `start_date` produc |
| `start` | string | No | Parameter defines the result offset. It skips the given number of results. It's used for pagination. (e.g., `0` (default) is the first page of results, `10` is the 2nd page of results, `20` is the 3rd page of results, etc.). |
| `nfpr` | string | No | Parameter defines the exclusion of results from an auto-corrected query when the original query is spelled wrong. It can be set to `1` to exclude these results, or `0` to include them (default). Note that this parameter may not prevent Goog |
| `filter` | string | No | Parameter defines if the filters for 'Similar Results' and 'Omitted Results' are on or off. It can be set to `1` (default) to enable these filters, or `0` to disable these filters. |
| `tbs` | string | No | (to be searched) parameter defines advanced search parameters that aren't possible in the regular query field. (e.g., advanced search for dates, time period, etc.). |
| `device` | string | No | Parameter defines the device to use to get the results. It can be set to `desktop` (default) to use a regular browser, `tablet` to use a tablet browser (currently using iPads), or `mobile` to use a mobile browser. |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/google/forums.json`](../../../catalog/models/google/forums.json) · Store page: https://www.sandbase.ai/model/google/forums
