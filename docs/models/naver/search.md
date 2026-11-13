# Naver Search API: pricing, parameters and code examples

`naver/search` · data API · Naver · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Get Naver web results for a query with organic results, news, blogs, knowledge panels and other Naver sections.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "naver/search", "query": "커피"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('naver/search', {'query': '커피'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("naver/search", {
  "query": "커피"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "naver/search", sandbase.Params{
	"query": "커피",
})
```

Same call via the path form: `POST /v1/api/naver/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `num` | string |  | Parameter defines the maximum number of results to return. `50` (default) returns 50 results. Maximum number of results to return is `100`. Parameter can only be used with Naver Images API.  |
| `page` | string |  | The page parameter does the `start` parameter math for you! Just define the page number you want. Pagination starts from 1.  |
| `query` | string | yes | Parameter defines the search query. You can use anything that you would use in a regular Naver search. (e.g., `'query'`, `NOT`, `OR`, `site:`, `filetype:`, `near:`, `ip:`, `loc:`, `feed:` etc.).  |
| `start` | string |  | Parameter controls the offset of the organic results. This parameter defaults to 1 (except for the `web`). (e.g. The formula for all searches except the web is `start = (page number * 10) - 9` e.g. Page number 3 ` (3 *…  |
| `where` | string |  | Parameter defines the Search type. This parameter defaults to `nexearch`. Available options: `nexearch`: regular Naver Search, `web`: Naver Web Organic Results, `video`: Naver Video Results, `news`: Naver News Results,…  |
| `device` | string |  | Parameter defines the device to use to get the results. It can be set to `desktop` (default) to use a regular browser, `tablet` to use a tablet browser (currently using iPads), or `mobile` to use a mobile browser.  |
| `period` | string |  | Parameter defines the time period for search results. This parameter defaults to `all`. Available options: `all`: search without time restrictions (default), `1h`: 1 hour, `1d`: 1 day, `1w`: 1 week, `1m`: 1 month,…  |
| `sort_by` | string |  | Parameter defines how the search results are sorted. This parameter defaults to `0` for Naver News Results, and `r` for other search types. For Naver News Results: `0`: Relevance (default), `1`: Latest, `2`: Oldest…  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |

## Details

Get Naver web results for a query with organic results, news, blogs, knowledge panels and other Naver sections.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/naver/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "커피"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Parameter defines the search query. You can use anything that you would use in a regular Naver search. (e.g., `'query'`, `NOT`, `OR`, `site:`, `filetype:`, `near:`, `ip:`, `loc:`, `feed:` etc.). |
| `start` | string | No | Parameter controls the offset of the organic results. This parameter defaults to 1 (except for the `web`). (e.g. The formula for all searches except the web is `start = (page number * 10) - 9` e.g. Page number 3 ` (3 * 10) - 9 = 21`) The fo |
| `page` | string | No | The page parameter does the `start` parameter math for you! Just define the page number you want. Pagination starts from 1. |
| `num` | string | No | Parameter defines the maximum number of results to return. `50` (default) returns 50 results. Maximum number of results to return is `100`. Parameter can only be used with Naver Images API. |
| `where` | string | No | Parameter defines the Search type. This parameter defaults to `nexearch`. Available options: `nexearch`: regular Naver Search, `web`: Naver Web Organic Results, `video`: Naver Video Results, `news`: Naver News Results, `image`: Naver Images |
| `sort_by` | string | No | Parameter defines how the search results are sorted. This parameter defaults to `0` for Naver News Results, and `r` for other search types. For Naver News Results: `0`: Relevance (default), `1`: Latest, `2`: Oldest (only supported for news) |
| `period` | string | No | Parameter defines the time period for search results. This parameter defaults to `all`. Available options: `all`: search without time restrictions (default), `1h`: 1 hour, `1d`: 1 day, `1w`: 1 week, `1m`: 1 month, `3m`: 3 months, `6m`: 6 mo |
| `device` | string | No | Parameter defines the device to use to get the results. It can be set to `desktop` (default) to use a regular browser, `tablet` to use a tablet browser (currently using iPads), or `mobile` to use a mobile browser. |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/naver/search.json`](../../../catalog/models/naver/search.json) · Store page: https://www.sandbase.ai/model/naver/search
