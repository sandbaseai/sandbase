# Bing News API: pricing, parameters and code examples

`bing/news` · data API · Bing · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Search Bing News by keyword and get headlines with source, date, snippet and thumbnail, filtered by freshness and market.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bing/news", "q": "artificial intelligence"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bing/news', {'q': 'artificial intelligence'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bing/news", {
  "q": "artificial intelligence"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bing/news", sandbase.Params{
	"q": "artificial intelligence",
})
```

Same call via the path form: `POST /v1/api/bing/news` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string | yes | Parameter defines the search query. You can use anything that you would use in a regular Bing search. (e.g., `'query'`, `NOT`, `OR`, `site:`, `filetype:`, `near:`, `ip:`, `loc:`, `feed:` etc.).  |
| `cc` | string |  | Parameter defines the country to search from. It follows the 2-character ISO_3166-1 format. (e.g., `us` for United States, `de` for Germany, `gb` for United Kingdom, etc.). This parameter and the `mkt` query parameter…  |
| `mkt` | string |  | The market where the results come from (e.g. `en-US`). Typically, `mkt` is the country where the user is making the request from. However, it could be a different country if the user is not located in a country where…  |
| `qft` | string |  | Parameter defines results sorted by date. If the parameter is not set, it will default to the "Best match" sorting, otherwise, if set to: e.g. `interval="4"`, it will show results from the past hour. Other options are:…  |
| `count` | string |  | Parameter controls the number of results per page. This parameter is only a suggestion and might not reflect actual results returned.  |
| `first` | string |  | Parameter controls the offset of the organic results. This parameter defaults to `1`. (e.g., `first=10` will move the 10th organic result to the first position).  |
| `device` | string |  | Parameter defines the device to use to get the results. It can be set to `desktop` (default) to use a regular browser, `tablet` to use a tablet browser (currently using iPads), or `mobile` to use a mobile browser.  |
| `safeSearch` | string |  | Parameter defines the level of filtering for adult content. It can be set to: `Off` to return webpages with adult text, images, or videos. `Moderate` to return webpages with adult text, but not adult images or videos.…  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |

## Details

Search Bing News by keyword and get headlines with source, date, snippet and thumbnail, filtered by freshness and market.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bing/news" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "artificial intelligence"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | Yes | Parameter defines the search query. You can use anything that you would use in a regular Bing search. (e.g., `'query'`, `NOT`, `OR`, `site:`, `filetype:`, `near:`, `ip:`, `loc:`, `feed:` etc.). |
| `mkt` | string | No | The market where the results come from (e.g. `en-US`). Typically, `mkt` is the country where the user is making the request from. However, it could be a different country if the user is not located in a country where Bing delivers results.  |
| `cc` | string | No | Parameter defines the country to search from. It follows the 2-character ISO_3166-1 format. (e.g., `us` for United States, `de` for Germany, `gb` for United Kingdom, etc.). This parameter and the `mkt` query parameter are mutually exclusive |
| `first` | string | No | Parameter controls the offset of the organic results. This parameter defaults to `1`. (e.g., `first=10` will move the 10th organic result to the first position). |
| `count` | string | No | Parameter controls the number of results per page. This parameter is only a suggestion and might not reflect actual results returned. |
| `qft` | string | No | Parameter defines results sorted by date. If the parameter is not set, it will default to the "Best match" sorting, otherwise, if set to: e.g. `interval="4"`, it will show results from the past hour. Other options are: `interval="7"`: Past  |
| `safeSearch` | string | No | Parameter defines the level of filtering for adult content. It can be set to: `Off` to return webpages with adult text, images, or videos. `Moderate` to return webpages with adult text, but not adult images or videos. `Strict` to not return |
| `device` | string | No | Parameter defines the device to use to get the results. It can be set to `desktop` (default) to use a regular browser, `tablet` to use a tablet browser (currently using iPads), or `mobile` to use a mobile browser. |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/bing/news.json`](../../../catalog/models/bing/news.json) · Store page: https://www.sandbase.ai/model/bing/news
