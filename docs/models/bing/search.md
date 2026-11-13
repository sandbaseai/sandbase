# Bing Search API: pricing, parameters and code examples

`bing/search` · data API · Bing · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Get Bing web results for a query with organic results, answer boxes, related searches and pagination, localized by market and country.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bing/search", "q": "best coffee grinder"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bing/search', {'q': 'best coffee grinder'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bing/search", {
  "q": "best coffee grinder"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bing/search", sandbase.Params{
	"q": "best coffee grinder",
})
```

Same call via the path form: `POST /v1/api/bing/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string | yes | Parameter defines the search query. You can use anything that you would use in a regular Bing search. (e.g., `'query'`, `NOT`, `OR`, `site:`, `filetype:`, `near:`, `ip:`, `loc:`, `feed:` etc.).  |
| `cc` | string |  | Parameter defines the country to search from. It follows the 2-character ISO_3166-1 format. (e.g., `us` for United States, `de` for Germany, `gb` for United Kingdom, etc.). This parameter and the `mkt` query parameter…  |
| `lat` | string |  | Defines a GPS latitude for the search origin  |
| `lon` | string |  | Defines a GPS longitude for the search origin  |
| `mkt` | string |  | The market where the results come from (e.g. `en-US`). Typically, `mkt` is the country where the user is making the request from. However, it could be a different country if the user is not located in a country where…  |
| `first` | string |  | Parameter controls the offset of the organic results. This parameter defaults to `1`. (e.g., `first=10` will move the 10th organic result to the first position).  |
| `device` | string |  | Parameter defines the device to use to get the results. It can be set to `desktop` (default) to use a regular browser, `tablet` to use a tablet browser (currently using iPads), or `mobile` to use a mobile browser.  |
| `filters` | string |  | Parameter allows usage of a more complex filtering options such as filtering by date range `ex1:"ez5_18169_18230"` or using a specific display filters such as…  |
| `location` | string |  | Parameter defines from where you want the search to originate. If several locations match the location requested, we'll pick the most popular one. Head to the /locations.json API if you need more precise control. The…  |
| `safeSearch` | string |  | Parameter defines the level of filtering for adult content. It can be set to: `Off` to return webpages with adult text, images, or videos. `Moderate` to return webpages with adult text, but not adult images or videos.…  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |

## Details

Get Bing web results for a query with organic results, answer boxes, related searches and pagination, localized by market and country.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bing/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "best coffee grinder"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | Yes | Parameter defines the search query. You can use anything that you would use in a regular Bing search. (e.g., `'query'`, `NOT`, `OR`, `site:`, `filetype:`, `near:`, `ip:`, `loc:`, `feed:` etc.). |
| `location` | string | No | Parameter defines from where you want the search to originate. If several locations match the location requested, we'll pick the most popular one. Head to the /locations.json API if you need more precise control. The `location` and `uule` p |
| `lat` | string | No | Defines a GPS latitude for the search origin |
| `lon` | string | No | Defines a GPS longitude for the search origin |
| `mkt` | string | No | The market where the results come from (e.g. `en-US`). Typically, `mkt` is the country where the user is making the request from. However, it could be a different country if the user is not located in a country where Bing delivers results.  |
| `cc` | string | No | Parameter defines the country to search from. It follows the 2-character ISO_3166-1 format. (e.g., `us` for United States, `de` for Germany, `gb` for United Kingdom, etc.). This parameter and the `mkt` query parameter are mutually exclusive |
| `first` | string | No | Parameter controls the offset of the organic results. This parameter defaults to `1`. (e.g., `first=10` will move the 10th organic result to the first position). |
| `safeSearch` | string | No | Parameter defines the level of filtering for adult content. It can be set to: `Off` to return webpages with adult text, images, or videos. `Moderate` to return webpages with adult text, but not adult images or videos. `Strict` to not return |
| `filters` | string | No | Parameter allows usage of a more complex filtering options such as filtering by date range `ex1:"ez5_18169_18230"` or using a specific display filters such as `ufn:"Wunderman+Thompson"+sid:"5bede9a2-1bda-9887-e6eb-30b1b8b6b513"+catguid:"5be |
| `device` | string | No | Parameter defines the device to use to get the results. It can be set to `desktop` (default) to use a regular browser, `tablet` to use a tablet browser (currently using iPads), or `mobile` to use a mobile browser. |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/bing/search.json`](../../../catalog/models/bing/search.json) · Store page: https://www.sandbase.ai/model/bing/search
