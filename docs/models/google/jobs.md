# Google Jobs API: pricing, parameters and code examples

`google/jobs` · data API · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Search job listings aggregated by Google Jobs with title, company, location, posting date, salary and apply links, filtered by location and language.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/jobs", "q": "data engineer"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/jobs', {'q': 'data engineer'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/jobs", {
  "q": "data engineer"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/jobs", sandbase.Params{
	"q": "data engineer",
})
```

Same call via the path form: `POST /v1/api/google/jobs` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string | yes | Parameter defines the query you want to search.  |
| `gl` | string |  | Parameter defines the country to use for the Google Jobs search. It's a two-letter country code. (e.g., `us` for the United States, `uk` for United Kingdom, or `fr` for France) Head to the Google Jobs countries page…  |
| `hl` | string |  | Parameter defines the language to use for the Google Jobs search. It's a two or three-letter language code. (e.g., `en` for English, `es` for Spanish, or `fr` for French), optionally followed by a two-letter or…  |
| `uds` | string |  | Parameter enables to filter search. It's a string provided by Google as a filter. `uds` values are provided under the section: `filters` with `uds`, `q` and `the API_link` values provided for each filter.  |
| `lrad` | string |  | Defines search radius in kilometers. Does not strictly limit the radius.  |
| `uule` | string |  | Parameter is the Google encoded location you want to use for the search. `uule` and `location` parameters can't be used together. For consistent results with coordinates-based `uule` parameter, a matching `gl`…  |
| `chips` | string |  | Parameter defines additional query conditions. Top of a job search page contains elements called chips, its values are extracted in order to be passed to chips parameter. E.g. `city:Owg_06VPwoli_nfhBo8LyA==` will…  |
| `ltype` | string |  | Parameter will filter the results by work from home. This parameter has been deprecated by Google.  |
| `location` | string |  | Parameter defines from where you want the search to originate. If several locations match the location requested, we'll pick the most popular one. Head to the /locations.json API if you need more precise control. The…  |
| `google_domain` | string |  | Parameter defines the Google domain to use. It defaults to `google.com`. Head to the Google domains page for a full list of supported Google domains.  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |
| `next_page_token` | string |  | Parameter defines the next page token. It is used for retrieving the next page of results. Up to `10` results are returned per page. The next page token can be found in the the API JSON response: `the API_pagination ->…  |

## Details

Search job listings aggregated by Google Jobs with title, company, location, posting date, salary and apply links, filtered by location and language.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google/jobs" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "data engineer", "location": "Austin, Texas, United States"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | Yes | Parameter defines the query you want to search. |
| `location` | string | No | Parameter defines from where you want the search to originate. If several locations match the location requested, we'll pick the most popular one. Head to the /locations.json API if you need more precise control. The `location` and `uule` p |
| `uule` | string | No | Parameter is the Google encoded location you want to use for the search. `uule` and `location` parameters can't be used together. For consistent results with coordinates-based `uule` parameter, a matching `gl` parameter is required. Head to |
| `google_domain` | string | No | Parameter defines the Google domain to use. It defaults to `google.com`. Head to the Google domains page for a full list of supported Google domains. |
| `gl` | string | No | Parameter defines the country to use for the Google Jobs search. It's a two-letter country code. (e.g., `us` for the United States, `uk` for United Kingdom, or `fr` for France) Head to the Google Jobs countries page for a full list of suppo |
| `hl` | string | No | Parameter defines the language to use for the Google Jobs search. It's a two or three-letter language code. (e.g., `en` for English, `es` for Spanish, or `fr` for French), optionally followed by a two-letter or three-digit region code (e.g. |
| `next_page_token` | string | No | Parameter defines the next page token. It is used for retrieving the next page of results. Up to `10` results are returned per page. The next page token can be found in the the API JSON response: `the API_pagination -> next_page_token` Usag |
| `chips` | string | No | Parameter defines additional query conditions. Top of a job search page contains elements called chips, its values are extracted in order to be passed to chips parameter. E.g. `city:Owg_06VPwoli_nfhBo8LyA==` will return results for New York |
| `lrad` | string | No | Defines search radius in kilometers. Does not strictly limit the radius. |
| `ltype` | string | No | Parameter will filter the results by work from home. This parameter has been deprecated by Google. |
| `uds` | string | No | Parameter enables to filter search. It's a string provided by Google as a filter. `uds` values are provided under the section: `filters` with `uds`, `q` and `the API_link` values provided for each filter. |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/google/jobs.json`](../../../catalog/models/google/jobs.json) · Store page: https://www.sandbase.ai/model/google/jobs
