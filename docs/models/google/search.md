# Google Search API: pricing, parameters and code examples

`google/search` · data API · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Get Google web results for a query with organic results, knowledge graph, local pack, top stories, related questions and pagination, localized by country, language and location.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/search", "q": "best coffee grinder"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/search', {'q': 'best coffee grinder'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/search", {
  "q": "best coffee grinder"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/search", sandbase.Params{
	"q": "best coffee grinder",
})
```

Same call via the path form: `POST /v1/api/google/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string | yes | Parameter defines the query you want to search. You can use anything that you would use in a regular Google search. e.g. `inurl:`, `site:`, `intitle:`. We also support advanced search query parameters such as `as_dt`…  |
| `cr` | string |  | Parameter defines one or multiple countries to limit the search to. It uses `country{two-letter upper-case country code}` to specify countries and `\|` as a delimiter. (e.g., `countryFR\|countryDE` will only search…  |
| `gl` | string |  | Parameter defines the country to use for the Google search. It's a two-letter country code. (e.g., `us` for the United States, `uk` for United Kingdom, or `fr` for France). Head to the Google countries page for a full…  |
| `hl` | string |  | Parameter defines the language to use for the Google search. It's a two or three-letter language code. (e.g., `en` for English, `es` for Spanish, or `fr` for French), optionally followed by a two-letter or three-digit…  |
| `lr` | string |  | Parameter defines one or multiple languages to limit the search to. It uses `lang_{two-letter language code}` to specify languages and `\|` as a delimiter. (e.g., `lang_fr\|lang_de` will only search French and German…  |
| `si` | string |  | Parameter defines the cached search parameters of the Google Search you want to scrape. Searches with `si` parameter will return results for the originally encrypted search parameters. For some searches, `si` may…  |
| `ibp` | string |  | Parameter is responsible for rendering layouts and expansions for some elements (e.g., `gwp;0,7` to expand searches with `ludocid` for expanded knowledge graph).  |
| `lat` | string |  | Parameter defines a GPS latitude for the search origin. Parameter is required when using `lon` parameter. For consistent results, a matching `gl` parameter is required. Parameter can't be used together with `location`…  |
| `lon` | string |  | Parameter defines a GPS longitude for the search origin. Parameter is required when using `lat` parameter. For consistent results, a matching `gl` parameter is required. Parameter can't be used together with `location`…  |
| `tbm` | string |  | (To Be Matched) This parameter defines the type of search you want to do. Options: `(no selection)` - regular Google Search `isch` - Google Images API `lcl` - Google Local API `vid` - Google Videos API `nws` - Google… one of: `(no selection)`, `isch`, `lcl`, `vid`, `nws`, `shop`, `pts`, `bks` |
| `tbs` | string |  | (to be searched) parameter defines advanced search parameters that aren't possible in the regular query field. (e.g., advanced search for patents, dates, news, videos, images, apps, or text contents).  |
| `udm` | string |  | This parameter defines the type of Google Search display mode you want to use. Options: `(no selection)` - regular Google Search `web` or `14` - Web results `50` - Google AI Mode API `39` - Google Short Videos API `18`… one of: `(no selection)`, `14`, `50`, `39`, `18` |
| `uds` | string |  | Parameter enables to filter search. It's a string provided by Google as a filter. `uds` values are provided under the section: `filters` with `uds`, `q` and `the API_link` values provided for each filter.  |
| `lsig` | string |  | Parameter that you might have to use to force the knowledge graph map view to show up. You can find the `lsig` ID by using our Local Pack API or Google Local API. `lsig` ID is also available via a redirect Google uses…  |
| `nfpr` | string |  | Parameter defines the exclusion of results from an auto-corrected query when the original query is spelled wrong. It can be set to `1` to exclude these results, or `0` to include them (default). Note that this…  |
| `safe` | string |  | Parameter defines the level of filtering for adult content. It can be set to `active` or `off`, by default Google will blur explicit content.  |
| `uule` | string |  | Parameter is the Google encoded location you want to use for the search. `uule` and `location` parameters can't be used together. For consistent results with coordinates-based `uule` parameter, a matching `gl`…  |
| `kgmid` | string |  | Parameter defines the id (`KGMID`) of the Google Knowledge Graph listing you want to scrape. Also known as Google Knowledge Graph ID. Searches with `kgmid` parameter will return results for the originally encrypted…  |
| `start` | string |  | Parameter defines the result offset. It skips the given number of results. It's used for pagination. (e.g., `0` (default) is the first page of results, `10` is the 2nd page of results, `20` is the 3rd page of results,…  |
| `device` | string |  | Parameter defines the device to use to get the results. It can be set to `desktop` (default) to use a regular browser, `tablet` to use a tablet browser (currently using iPads), or `mobile` to use a mobile browser.  |
| `filter` | string |  | Parameter defines if the filters for 'Similar Results' and 'Omitted Results' are on or off. It can be set to `1` (default) to enable these filters, or `0` to disable these filters.  |
| `radius` | string |  | Parameter defines the distance (in meters) within which to bias the search results. Results inside of this region will be ranked higher than results outside of it. However, prominent results from outside of the search…  |
| `ludocid` | string |  | Parameter defines the Google CID (customer identifier) of a place. This parameter can be found in Google Search API and Google Local API local results under the name of `place_id`, as well as in Google Maps API local…  |
| `location` | string |  | Parameter defines from where you want the search to originate. If several locations match the location requested, we'll pick the most popular one. Head to the /locations.json API if you need more precise control. It is…  |
| `color_scheme` | string |  | Parameter forces the selected color scheme to be used on the results page. If the parameter is not set, a random color scheme will be returned. Options: `light` - Light `dark` - Dark one of: `light`, `dark` |
| `google_domain` | string |  | Parameter defines the Google domain to use. It defaults to `google.com`. Head to the Google domains page for a full list of supported Google domains.  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |

## Details

Get Google web results for a query with organic results, knowledge graph, local pack, top stories, related questions and pagination, localized by country, language and location.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "best coffee grinder"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | Yes | Parameter defines the query you want to search. You can use anything that you would use in a regular Google search. e.g. `inurl:`, `site:`, `intitle:`. We also support advanced search query parameters such as `as_dt` and `as_eq`. See the fu |
| `location` | string | No | Parameter defines from where you want the search to originate. If several locations match the location requested, we'll pick the most popular one. Head to the /locations.json API if you need more precise control. It is recommended to specif |
| `uule` | string | No | Parameter is the Google encoded location you want to use for the search. `uule` and `location` parameters can't be used together. For consistent results with coordinates-based `uule` parameter, a matching `gl` parameter is required. Head to |
| `lat` | string | No | Parameter defines a GPS latitude for the search origin. Parameter is required when using `lon` parameter. For consistent results, a matching `gl` parameter is required. Parameter can't be used together with `location` and `uule` parameters. |
| `lon` | string | No | Parameter defines a GPS longitude for the search origin. Parameter is required when using `lat` parameter. For consistent results, a matching `gl` parameter is required. Parameter can't be used together with `location` and `uule` parameters |
| `radius` | string | No | Parameter defines the distance (in meters) within which to bias the search results. Results inside of this region will be ranked higher than results outside of it. However, prominent results from outside of the search radius may still be in |
| `ludocid` | string | No | Parameter defines the Google CID (customer identifier) of a place. This parameter can be found in Google Search API and Google Local API local results under the name of `place_id`, as well as in Google Maps API local results under the name  |
| `lsig` | string | No | Parameter that you might have to use to force the knowledge graph map view to show up. You can find the `lsig` ID by using our Local Pack API or Google Local API. `lsig` ID is also available via a redirect Google uses within Google My Busin |
| `kgmid` | string | No | Parameter defines the id (`KGMID`) of the Google Knowledge Graph listing you want to scrape. Also known as Google Knowledge Graph ID. Searches with `kgmid` parameter will return results for the originally encrypted search parameters. For so |
| `si` | string | No | Parameter defines the cached search parameters of the Google Search you want to scrape. Searches with `si` parameter will return results for the originally encrypted search parameters. For some searches, `si` may override all other paramete |
| `ibp` | string | No | Parameter is responsible for rendering layouts and expansions for some elements (e.g., `gwp;0,7` to expand searches with `ludocid` for expanded knowledge graph). |
| `uds` | string | No | Parameter enables to filter search. It's a string provided by Google as a filter. `uds` values are provided under the section: `filters` with `uds`, `q` and `the API_link` values provided for each filter. |
| `color_scheme` | string | No | Parameter forces the selected color scheme to be used on the results page. If the parameter is not set, a random color scheme will be returned. Options: `light` - Light `dark` - Dark |
| `google_domain` | string | No | Parameter defines the Google domain to use. It defaults to `google.com`. Head to the Google domains page for a full list of supported Google domains. |
| `gl` | string | No | Parameter defines the country to use for the Google search. It's a two-letter country code. (e.g., `us` for the United States, `uk` for United Kingdom, or `fr` for France). Head to the Google countries page for a full list of supported Goog |
| `hl` | string | No | Parameter defines the language to use for the Google search. It's a two or three-letter language code. (e.g., `en` for English, `es` for Spanish, or `fr` for French), optionally followed by a two-letter or three-digit region code (e.g., `en |
| `cr` | string | No | Parameter defines one or multiple countries to limit the search to. It uses `country{two-letter upper-case country code}` to specify countries and `/` as a delimiter. (e.g., `countryFR/countryDE` will only search French and German pages). H |
| `lr` | string | No | Parameter defines one or multiple languages to limit the search to. It uses `lang_{two-letter language code}` to specify languages and `/` as a delimiter. (e.g., `lang_fr/lang_de` will only search French and German pages). Head to the Googl |
| `tbs` | string | No | (to be searched) parameter defines advanced search parameters that aren't possible in the regular query field. (e.g., advanced search for patents, dates, news, videos, images, apps, or text contents). |
| `safe` | string | No | Parameter defines the level of filtering for adult content. It can be set to `active` or `off`, by default Google will blur explicit content. |
| `nfpr` | string | No | Parameter defines the exclusion of results from an auto-corrected query when the original query is spelled wrong. It can be set to `1` to exclude these results, or `0` to include them (default). Note that this parameter may not prevent Goog |
| `filter` | string | No | Parameter defines if the filters for 'Similar Results' and 'Omitted Results' are on or off. It can be set to `1` (default) to enable these filters, or `0` to disable these filters. |
| `tbm` | string | No | (To Be Matched) This parameter defines the type of search you want to do. Options: `(no selection)` - regular Google Search `isch` - Google Images API `lcl` - Google Local API `vid` - Google Videos API `nws` - Google News API `shop` - Googl |
| `udm` | string | No | This parameter defines the type of Google Search display mode you want to use. Options: `(no selection)` - regular Google Search `web` or `14` - Web results `50` - Google AI Mode API `39` - Google Short Videos API `18` - Google Forums API ` |
| `start` | string | No | Parameter defines the result offset. It skips the given number of results. It's used for pagination. (e.g., `0` (default) is the first page of results, `10` is the 2nd page of results, `20` is the 3rd page of results, etc.). |
| `device` | string | No | Parameter defines the device to use to get the results. It can be set to `desktop` (default) to use a regular browser, `tablet` to use a tablet browser (currently using iPads), or `mobile` to use a mobile browser. |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/google/search.json`](../../../catalog/models/google/search.json) · Store page: https://www.sandbase.ai/model/google/search
