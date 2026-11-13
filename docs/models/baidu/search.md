# Baidu Search API: pricing, parameters and code examples

`baidu/search` · data API · Baidu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Get Baidu web results for a query with organic results, answer boxes, related searches and pagination.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "baidu/search", "q": "人工智能"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('baidu/search', {'q': '人工智能'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("baidu/search", {
  "q": "人工智能"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "baidu/search", sandbase.Params{
	"q": "人工智能",
})
```

Same call via the path form: `POST /v1/api/baidu/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `f` | string |  | Defines the originating search type. (e.g., `8` is a normal search, `3` is from the suggestion list, and `1` is a related search.  |
| `q` | string | yes | Parameter defines the search query, including all Baidu search operators. (e.g., `inurl:`, `site:`, `intitle:`, etc.).  |
| `bs` | string |  | Defines the previous search query.  |
| `ct` | string |  | Parameter defines which language to restrict results. Available options: `1` - All languages `2` - Simplified Chinese `3` - Traditional Chinese  |
| `oq` | string |  | Defines the original search query when navigated from a related search.  |
| `pn` | string |  | Parameter defines the result offset. It skips the given number of results. It's used for pagination. (e.g., `0` (default) is the first page of results, `10` is the 2nd page of results, `20` is the 3rd page of results,…  |
| `q5` | string |  | Similar to using `inurl:` or `intitle:`. (e.g., `1` to search by page title, `2` to search by web address.).  |
| `q6` | string |  | Similar to using `site:`. (e.g., `q6=the API.com` to search for results only from the domain `the API.com`).  |
| `rn` | string |  | Parameter defines the maximum number of results to return, limited to 50. (e.g., `10` (default) returns 10 results, `30` returns 30 results, and `50` returns 50 results). This parameter is only available for **desktop…  |
| `gpc` | string |  | Parameter defines the time period for results. (e.g., `stf=1793918685,1794523485\|stftype=1` only returns results from the past 7 days. First integer within the parameter,`1793918685` is Unix Timestamp for 7 days ago.…  |
| `device` | string |  | Parameter defines the device to use to get the results. It can be set to `desktop` (default) to use a regular browser, `tablet` to use a tablet browser (currently using iPads), or `mobile` to use a mobile browser.  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |

## Details

Get Baidu web results for a query with organic results, answer boxes, related searches and pagination.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/baidu/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "人工智能"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | Yes | Parameter defines the search query, including all Baidu search operators. (e.g., `inurl:`, `site:`, `intitle:`, etc.). |
| `ct` | string | No | Parameter defines which language to restrict results. Available options: `1` - All languages `2` - Simplified Chinese `3` - Traditional Chinese |
| `pn` | string | No | Parameter defines the result offset. It skips the given number of results. It's used for pagination. (e.g., `0` (default) is the first page of results, `10` is the 2nd page of results, `20` is the 3rd page of results, etc.). |
| `rn` | string | No | Parameter defines the maximum number of results to return, limited to 50. (e.g., `10` (default) returns 10 results, `30` returns 30 results, and `50` returns 50 results). This parameter is only available for **desktop and tablet** searches. |
| `gpc` | string | No | Parameter defines the time period for results. (e.g., `stf=1793918685,1794523485/stftype=1` only returns results from the past 7 days. First integer within the parameter,`1793918685` is Unix Timestamp for 7 days ago. Second integer,`1794523 |
| `q5` | string | No | Similar to using `inurl:` or `intitle:`. (e.g., `1` to search by page title, `2` to search by web address.). |
| `q6` | string | No | Similar to using `site:`. (e.g., `q6=the API.com` to search for results only from the domain `the API.com`). |
| `bs` | string | No | Defines the previous search query. |
| `oq` | string | No | Defines the original search query when navigated from a related search. |
| `f` | string | No | Defines the originating search type. (e.g., `8` is a normal search, `3` is from the suggestion list, and `1` is a related search. |
| `device` | string | No | Parameter defines the device to use to get the results. It can be set to `desktop` (default) to use a regular browser, `tablet` to use a tablet browser (currently using iPads), or `mobile` to use a mobile browser. |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/baidu/search.json`](../../../catalog/models/baidu/search.json) · Store page: https://www.sandbase.ai/model/baidu/search
