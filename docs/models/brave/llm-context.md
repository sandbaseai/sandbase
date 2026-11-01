# Brave LLM Context

`brave/llm-context` · api · Brave

LLM Context from Brave. Returns the official Brave API response unchanged.

## Pricing

- **$0.005 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "brave/llm-context", "q": "best coffee in seattle"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('brave/llm-context', {'q': 'best coffee in seattle'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("brave/llm-context", {
  "q": "best coffee in seattle"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "brave/llm-context", sandbase.Params{
	"q": "best coffee in seattle",
})
```

Same call via the path form: `POST /v1/api/brave/llm-context` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string | yes | The user’s search query term. Query can not be empty. Maximum of 600 characters and 75 words in the query.  |
| `count` | integer |  | The maximum number of search results considered to select the LLM context data. The default is 20 and the maximum is 50. default `20`; range 1–50 |
| `country` | string |  | The search query country, where the results come from. The country string is limited to 2 character country codes of supported countries. one of: `AR`, `AU`, `AT`, `BE`, `BR`, `CA`, `CL`, `DK`, `FI`, `FR`, `DE`, `GR` …; default `"US"` |
| `goggles` | string |  | Goggles act as a custom re-ranking on top of Brave’s search index. The parameter supports both a url where the Goggle is hosted or the definition of the Goggle. For more details, see the Goggles documentation . The…  |
| `freshness` | string |  | Filters search results by page age. The age of a page is determined by the most relevant date reported by the content, such as its published or last modified date. The following values are supported: pd - Pages aged 24… default `""` |
| `safesearch` | string |  | Filters results for adult content. The following values are supported: off - No filtering is done. moderate - Drops adult content from the results used for context. strict - Drops all adult content from the results… one of: `off`, `moderate`, `strict` |
| `spellcheck` | boolean |  | Whether to enable spellcheck on the query. default `true` |
| `search_lang` | string |  | The search language preference. The 2 or more character language code for which the search results are provided. one of: `ar`, `eu`, `bn`, `bg`, `ca`, `zh-hans`, `zh-hant`, `hr`, `cs`, `da`, `nl`, `en` …; default `"en"` |
| `enable_local` | boolean |  | Whether to enable local recall. Not setting this value means auto-detect: local recall is used if a location is provided ( X-Loc-Lat with X-Loc-Long , or X-Loc-City ).  |
| `context_threshold_mode` | string |  | The mode to use to determine the threshold for including content in context. one of: `disabled`, `strict`, `lenient`, `balanced` |
| `enable_source_metadata` | boolean |  | Enable source metadata enrichment (site_name, favicon, thumbnail, description, fetched_content_timestamp) in the sources attribute of the response. default `false` |
| `maximum_number_of_urls` | integer |  | Maximum number of different URLs to include in LLM context. default `20`; range 1–50 |
| `maximum_number_of_tokens` | integer |  | Approximate maximum number of tokens to include in context. The default is 8192 and maximum is 32768 . default `8192`; range 1024–32768 |
| `maximum_number_of_snippets` | integer |  | Maximum number of different snippets (or chunks of text) to include in LLM context. The default is 50 and maximum is 256 . default `50`; range 1–256 |
| `maximum_number_of_tokens_per_url` | integer |  | Maximum number of tokens to include per URL. The default is 4096 and maximum is 8192 . default `4096`; range 512–8192 |
| `maximum_number_of_snippets_per_url` | integer |  | Maximum number of snippets to include per URL. The default is 50 and maximum is 100 . default `50`; range 1–100 |

## Details

LLM Context from Brave. Returns the official Brave API response unchanged.

The response is the official Brave API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/brave/llm-context" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "best coffee in seattle"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `context_threshold_mode` | string | No | The mode to use to determine the threshold for including content in context. |
| `count` | integer | No | The maximum number of search results considered to select the LLM context data. The default is 20 and the maximum is 50. |
| `country` | string | No | The search query country, where the results come from. The country string is limited to 2 character country codes of supported countries. |
| `enable_local` | boolean | No | Whether to enable local recall. Not setting this value means auto-detect: local recall is used if a location is provided ( X-Loc-Lat with X-Loc-Long , or X-Loc- |
| `enable_source_metadata` | boolean | No | Enable source metadata enrichment (site_name, favicon, thumbnail, description, fetched_content_timestamp) in the sources attribute of the response. |
| `freshness` | string | No | Filters search results by page age. The age of a page is determined by the most relevant date reported by the content, such as its published or last modified da |
| `goggles` | string | No | Goggles act as a custom re-ranking on top of Brave’s search index. The parameter supports both a url where the Goggle is hosted or the definition of the Goggle. |
| `maximum_number_of_snippets` | integer | No | Maximum number of different snippets (or chunks of text) to include in LLM context. The default is 50 and maximum is 256 . |
| `maximum_number_of_snippets_per_url` | integer | No | Maximum number of snippets to include per URL. The default is 50 and maximum is 100 . |
| `maximum_number_of_tokens` | integer | No | Approximate maximum number of tokens to include in context. The default is 8192 and maximum is 32768 . |
| `maximum_number_of_tokens_per_url` | integer | No | Maximum number of tokens to include per URL. The default is 4096 and maximum is 8192 . |
| `maximum_number_of_urls` | integer | No | Maximum number of different URLs to include in LLM context. |
| `q` | string | Yes | The user’s search query term. Query can not be empty. Maximum of 600 characters and 75 words in the query. |
| `safesearch` | string | No | Filters results for adult content. The following values are supported: off - No filtering is done. moderate - Drops adult content from the results used for cont |
| `search_lang` | string | No | The search language preference. The 2 or more character language code for which the search results are provided. |
| `spellcheck` | boolean | No | Whether to enable spellcheck on the query. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/brave/llm-context.json`](../../../catalog/models/brave/llm-context.json) · Store page: https://www.sandbase.ai/model/brave/llm-context
