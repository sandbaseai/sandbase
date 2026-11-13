# Yahoo Search API: pricing, parameters and code examples

`yahoo/search` · data API · Yahoo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Get Yahoo web results for a query with organic results, related searches and pagination, localized by domain and language.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "yahoo/search", "p": "best coffee grinder"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('yahoo/search', {'p': 'best coffee grinder'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("yahoo/search", {
  "p": "best coffee grinder"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "yahoo/search", sandbase.Params{
	"p": "best coffee grinder",
})
```

Same call via the path form: `POST /v1/api/yahoo/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `b` | string |  | Parameter defines the result offset. It skips the given number of results. It's used for pagination. (e.g., `1` (default) is the first page of results, `11` is the 2nd page of results, `21` is the 3rd page of results,…  |
| `d` | string |  | Parameter specifies the destination for related topics. By including a unique identifier for the destination page, this parameter directs users to specific content related to their search query, providing them with…  |
| `p` | string | yes | Parameter defines the search query. You can use anything that you would use in a regular Yahoo! search.  |
| `vc` | string |  | Parameter defines the country to use for the Yahoo! search. It's a two-letter country code. (e.g., `us` for the United States, `uk` for United Kingdom, or `fr` for France) Head to the Yahoo! countries for a full list…  |
| `vf` | string |  | `all formats` or specific file format like `pdf` or `txt`. You can check a full list of supported Yahoo! file formats.  |
| `vl` | string |  | Parameter defines language to limit the search to. It uses `lang_{two-letter language code}` to specify languages. (e.g., `vl=lang_fr` will only search French). `fl` will be set to `1` if this parameter is used. You…  |
| `vm` | string |  | Parameter defines the level of filtering for adult content. Strict: `r`, Moderate: `i`, Off: `p`  |
| `vs` | string |  | Filter results by top-level domains separated by ','. (e.g., `.com,.org`)  |
| `fr2` | string |  | Parameter is responsible for rendering positions and expansions for some elements (e.g., `p:s,v:w,m:trendingdomain_center` to expand Related Trending Searches).  |
| `device` | string |  | Parameter defines the device to use to get the results. It can be set to `desktop` (default) to use a regular browser, `tablet` to use a tablet browser (currently using iPads), or `mobile` to use a mobile browser.  |
| `yahoo_domain` | string |  | Parameter defines the Yahoo! domain to use. It defaults to `search.yahoo.com`. If specified domain is allowed, it will be prepended to the domain (e.g., `fr.search.yahoo.com`). You can check a full list of supported…  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |

## Details

Get Yahoo web results for a query with organic results, related searches and pagination, localized by domain and language.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/yahoo/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"p": "best coffee grinder"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `p` | string | Yes | Parameter defines the search query. You can use anything that you would use in a regular Yahoo! search. |
| `yahoo_domain` | string | No | Parameter defines the Yahoo! domain to use. It defaults to `search.yahoo.com`. If specified domain is allowed, it will be prepended to the domain (e.g., `fr.search.yahoo.com`). You can check a full list of supported Yahoo! domains. |
| `vc` | string | No | Parameter defines the country to use for the Yahoo! search. It's a two-letter country code. (e.g., `us` for the United States, `uk` for United Kingdom, or `fr` for France) Head to the Yahoo! countries for a full list of supported Yahoo! cou |
| `vl` | string | No | Parameter defines language to limit the search to. It uses `lang_{two-letter language code}` to specify languages. (e.g., `vl=lang_fr` will only search French). `fl` will be set to `1` if this parameter is used. You can check a full list of |
| `b` | string | No | Parameter defines the result offset. It skips the given number of results. It's used for pagination. (e.g., `1` (default) is the first page of results, `11` is the 2nd page of results, `21` is the 3rd page of results, etc.). |
| `vm` | string | No | Parameter defines the level of filtering for adult content. Strict: `r`, Moderate: `i`, Off: `p` |
| `vs` | string | No | Filter results by top-level domains separated by ','. (e.g., `.com,.org`) |
| `vf` | string | No | `all formats` or specific file format like `pdf` or `txt`. You can check a full list of supported Yahoo! file formats. |
| `fr2` | string | No | Parameter is responsible for rendering positions and expansions for some elements (e.g., `p:s,v:w,m:trendingdomain_center` to expand Related Trending Searches). |
| `d` | string | No | Parameter specifies the destination for related topics. By including a unique identifier for the destination page, this parameter directs users to specific content related to their search query, providing them with more targeted results. (e |
| `device` | string | No | Parameter defines the device to use to get the results. It can be set to `desktop` (default) to use a regular browser, `tablet` to use a tablet browser (currently using iPads), or `mobile` to use a mobile browser. |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/yahoo/search.json`](../../../catalog/models/yahoo/search.json) · Store page: https://www.sandbase.ai/model/yahoo/search
