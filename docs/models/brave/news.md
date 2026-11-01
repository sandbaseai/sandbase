# Brave News Search

`brave/news` · api · Brave

News Search from Brave. Returns the official Brave API response unchanged.

## Pricing

- **$0.005 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "brave/news", "q": "best coffee in seattle"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('brave/news', {'q': 'best coffee in seattle'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("brave/news", {
  "q": "best coffee in seattle"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "brave/news", sandbase.Params{
	"q": "best coffee in seattle",
})
```

Same call via the path form: `POST /v1/api/brave/news` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string | yes | The user’s search query term. Query can not be empty. Maximum of 400 characters and 50 words in the query.  |
| `count` | integer |  | The number of search results returned in response. The maximum is 50. The actual number delivered may be less than requested. Combine this parameter with offset to paginate search results. default `20`; range 1–50 |
| `offset` | integer |  | The zero based offset that indicates number of search results per page (count) to skip before returning the result. The maximum is 9. The actual number delivered may be less than requested based on the query. In order… default `0`; range 0–9 |
| `country` | string |  | The search query country, where the results come from. The country string is limited to 2 character country codes of supported countries or ALL for worldwide. one of: `AR`, `AU`, `AT`, `BE`, `BR`, `CA`, `CL`, `DK`, `FI`, `FR`, `DE`, `GR` …; default `"US"` |
| `goggles` | string |  | Goggles act as a custom re-ranking on top of Brave’s search index. The parameter supports both a url where the Goggle is hosted or the definition of the Goggle. For more details, see the Goggles documentation . The…  |
| `ui_lang` | string |  | User interface language preferred in response. Usually of the format <language_code>-<country_code> . For more, see RFC 9110 . one of: `es-AR`, `en-AU`, `de-AT`, `nl-BE`, `fr-BE`, `pt-BR`, `en-CA`, `fr-CA`, `es-CL`, `da-DK`, `fi-FI`, `fr-FR` …; default `"en-US"` |
| `freshness` | string |  | Filters search results by page age. The age of a page is determined by the most relevant date reported by the content, such as its published or last modified date. The following values are supported: pd - Pages aged 24… default `""` |
| `operators` | boolean |  | Whether to apply search operators. default `true` |
| `safesearch` | string |  | Filters search results for adult content. The following values are supported: off - No filtering is done. moderate - Filter out explicit content. strict - Filter out explicit and suggestive content. one of: `off`, `moderate`, `strict`; default `"strict"` |
| `spellcheck` | boolean |  | Whether to spell check the provided query. If the spellchecker is enabled, the modified query is always used for search. The modified query can be found in altered key from the query response model. default `true` |
| `search_lang` | string |  | The search language preference. The 2 or more character language code for which the search results are provided. one of: `ar`, `eu`, `bn`, `bg`, `ca`, `zh-hans`, `zh-hant`, `hr`, `cs`, `da`, `nl`, `en` …; default `"en"` |
| `extra_snippets` | boolean |  | A snippet is an excerpt from a page you get as a result of the query, and extra_snippets allow you to get up to 5 additional, alternative excerpts.  |
| `include_fetch_metadata` | boolean |  | Include fetch metadata. default `false` |

## Details

News Search from Brave. Returns the official Brave API response unchanged.

The response is the official Brave API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/brave/news" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "best coffee in seattle"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `count` | integer | No | The number of search results returned in response. The maximum is 50. The actual number delivered may be less than requested. Combine this parameter with offset |
| `country` | string | No | The search query country, where the results come from. The country string is limited to 2 character country codes of supported countries or ALL for worldwide. |
| `extra_snippets` | boolean | No | A snippet is an excerpt from a page you get as a result of the query, and extra_snippets allow you to get up to 5 additional, alternative excerpts. |
| `freshness` | string | No | Filters search results by page age. The age of a page is determined by the most relevant date reported by the content, such as its published or last modified da |
| `goggles` | string | No | Goggles act as a custom re-ranking on top of Brave’s search index. The parameter supports both a url where the Goggle is hosted or the definition of the Goggle. |
| `include_fetch_metadata` | boolean | No | Include fetch metadata. |
| `offset` | integer | No | The zero based offset that indicates number of search results per page (count) to skip before returning the result. The maximum is 9. The actual number delivere |
| `operators` | boolean | No | Whether to apply search operators. |
| `q` | string | Yes | The user’s search query term. Query can not be empty. Maximum of 400 characters and 50 words in the query. |
| `safesearch` | string | No | Filters search results for adult content. The following values are supported: off - No filtering is done. moderate - Filter out explicit content. strict - Filte |
| `search_lang` | string | No | The search language preference. The 2 or more character language code for which the search results are provided. |
| `spellcheck` | boolean | No | Whether to spell check the provided query. If the spellchecker is enabled, the modified query is always used for search. The modified query can be found in alte |
| `ui_lang` | string | No | User interface language preferred in response. Usually of the format <language_code>-<country_code> . For more, see RFC 9110 . |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/brave/news.json`](../../../catalog/models/brave/news.json) · Store page: https://www.sandbase.ai/model/brave/news
