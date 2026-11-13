# Google Short Videos API: pricing, parameters and code examples

`google/short-videos` · data API · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Get Google's Short Videos results for a query: short-form clips from YouTube Shorts, TikTok, Instagram and others with title, source, duration and link.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/short-videos", "q": "latte art"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/short-videos', {'q': 'latte art'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/short-videos", {
  "q": "latte art"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/short-videos", sandbase.Params{
	"q": "latte art",
})
```

Same call via the path form: `POST /v1/api/google/short-videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string | yes | Parameter defines the query you want to search. You can use anything that you would use in a regular Google Short Videos search. e.g. `inurl:`, `site:`, `intitle:`. We also support advanced search query parameters such…  |
| `gl` | string |  | Parameter defines the country to use for the Google search. It's a two-letter country code. (e.g., `us` for the United States, `uk` for United Kingdom, or `fr` for France). Head to the Google countries page for a full…  |
| `hl` | string |  | Parameter defines the language to use for the Google search. It's a two or three-letter language code. (e.g., `en` for English, `es` for Spanish, or `fr` for French), optionally followed by a two-letter or three-digit…  |
| `lr` | string |  | Parameter defines one or multiple languages to limit the search to. It uses `lang_{two-letter language code}` to specify languages and `\|` as a delimiter. (e.g., `lang_fr\|lang_de` will only search French and German…  |
| `tbs` | string |  | (to be searched) parameter defines advanced search parameters that aren't possible in the regular query field. (e.g., advanced search for patents, dates, news, videos, images, apps, or text contents).  |
| `nfpr` | string |  | Parameter defines the exclusion of results from an auto-corrected query when the original query is spelled wrong. It can be set to `1` to exclude these results, or `0` to include them (default). Note that this…  |
| `safe` | string |  | Parameter defines the level of filtering for adult content. It can be set to `active` or `off`, by default Google will blur explicit content.  |
| `uule` | string |  | Parameter is the Google encoded location you want to use for the search. `uule` and `location` parameters can't be used together. For consistent results with coordinates-based `uule` parameter, a matching `gl`…  |
| `start` | string |  | Parameter defines the result offset. It skips the given number of results. It's used for pagination. (e.g., `0` (default) is the first page of results, `12` (desktop) or `8` (mobile) is the 2nd page of results, etc.).  |
| `device` | string |  | Parameter defines the device to use to get the results. It can be set to `desktop` (default) to use a regular browser, `tablet` to use a tablet browser (currently using iPads), or `mobile` to use a mobile browser.  |
| `filter` | string |  | Parameter defines if the filters for 'Similar Results' and 'Omitted Results' are on or off. It can be set to `1` (default) to enable these filters, or `0` to disable these filters.  |
| `location` | string |  | Parameter defines from where you want the search to originate. If several locations match the location requested, we'll pick the most popular one. Head to the /locations.json API if you need more precise control. The…  |
| `google_domain` | string |  | Parameter defines the Google domain to use. It defaults to `google.com`. Head to the Google domains page for a full list of supported Google domains.  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |

## Details

Get Google's Short Videos results for a query: short-form clips from YouTube Shorts, TikTok, Instagram and others with title, source, duration and link.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google/short-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "latte art"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | Yes | Parameter defines the query you want to search. You can use anything that you would use in a regular Google Short Videos search. e.g. `inurl:`, `site:`, `intitle:`. We also support advanced search query parameters such as `as_dt` and `as_eq |
| `location` | string | No | Parameter defines from where you want the search to originate. If several locations match the location requested, we'll pick the most popular one. Head to the /locations.json API if you need more precise control. The `location` and `uule` p |
| `uule` | string | No | Parameter is the Google encoded location you want to use for the search. `uule` and `location` parameters can't be used together. For consistent results with coordinates-based `uule` parameter, a matching `gl` parameter is required. Head to |
| `google_domain` | string | No | Parameter defines the Google domain to use. It defaults to `google.com`. Head to the Google domains page for a full list of supported Google domains. |
| `gl` | string | No | Parameter defines the country to use for the Google search. It's a two-letter country code. (e.g., `us` for the United States, `uk` for United Kingdom, or `fr` for France). Head to the Google countries page for a full list of supported Goog |
| `hl` | string | No | Parameter defines the language to use for the Google search. It's a two or three-letter language code. (e.g., `en` for English, `es` for Spanish, or `fr` for French), optionally followed by a two-letter or three-digit region code (e.g., `en |
| `lr` | string | No | Parameter defines one or multiple languages to limit the search to. It uses `lang_{two-letter language code}` to specify languages and `/` as a delimiter. (e.g., `lang_fr/lang_de` will only search French and German pages). Head to the Googl |
| `tbs` | string | No | (to be searched) parameter defines advanced search parameters that aren't possible in the regular query field. (e.g., advanced search for patents, dates, news, videos, images, apps, or text contents). |
| `safe` | string | No | Parameter defines the level of filtering for adult content. It can be set to `active` or `off`, by default Google will blur explicit content. |
| `nfpr` | string | No | Parameter defines the exclusion of results from an auto-corrected query when the original query is spelled wrong. It can be set to `1` to exclude these results, or `0` to include them (default). Note that this parameter may not prevent Goog |
| `filter` | string | No | Parameter defines if the filters for 'Similar Results' and 'Omitted Results' are on or off. It can be set to `1` (default) to enable these filters, or `0` to disable these filters. |
| `start` | string | No | Parameter defines the result offset. It skips the given number of results. It's used for pagination. (e.g., `0` (default) is the first page of results, `12` (desktop) or `8` (mobile) is the 2nd page of results, etc.). |
| `device` | string | No | Parameter defines the device to use to get the results. It can be set to `desktop` (default) to use a regular browser, `tablet` to use a tablet browser (currently using iPads), or `mobile` to use a mobile browser. |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/google/short-videos.json`](../../../catalog/models/google/short-videos.json) · Store page: https://www.sandbase.ai/model/google/short-videos
