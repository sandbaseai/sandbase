# Brave News Search API: pricing, parameters and code examples

`brave/news` · data API · Brave · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.005 per call (free daily quota) · **Modes:** sync

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

Returns news search results from Brave for a text query. Each result has a title, URL, short description, source name, and age. The only required input is `q`, the search query.

### Use cases

- Track news coverage of a brand, product, or topic by running a query on a schedule.
- Build a news feed for a city or subject using `country`, `search_lang`, and `freshness` filters.
- Collect article titles, URLs, and snippets to feed a summarizer or research tool.
- Check which publishers cover a topic by reading `results[].profile.name` and `results[].meta_url.hostname`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/brave/news" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "best coffee in seattle"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | Yes | The user’s search query term. Query can not be empty. Maximum of 400 characters and 50 words in the query. |
| `count` | integer | No | The number of search results returned in response. The maximum is 50. The actual number delivered may be less than requested. Combine this parameter with offset to paginate search results. |
| `country` | string | No | The search query country, where the results come from. The country string is limited to 2 character country codes of supported countries or ALL for worldwide. |
| `extra_snippets` | boolean | No | A snippet is an excerpt from a page you get as a result of the query, and extra_snippets allow you to get up to 5 additional, alternative excerpts. |
| `freshness` | string | No | Filters search results by page age. The age of a page is determined by the most relevant date reported by the content, such as its published or last modified date. The following values are supported: pd - Pages aged 24 h |
| `goggles` | string | No | Goggles act as a custom re-ranking on top of Brave’s search index. The parameter supports both a url where the Goggle is hosted or the definition of the Goggle. For more details, see the Goggles documentation . The param |
| `include_fetch_metadata` | boolean | No | Include fetch metadata. |
| `offset` | integer | No | The zero based offset that indicates number of search results per page (count) to skip before returning the result. The maximum is 9. The actual number delivered may be less than requested based on the query. In order to |
| `operators` | boolean | No | Whether to apply search operators. |
| `safesearch` | string | No | Filters search results for adult content. The following values are supported: off - No filtering is done. moderate - Filter out explicit content. strict - Filter out explicit and suggestive content. |
| `search_lang` | string | No | The search language preference. The 2 or more character language code for which the search results are provided. |
| `spellcheck` | boolean | No | Whether to spell check the provided query. If the spellchecker is enabled, the modified query is always used for search. The modified query can be found in altered key from the query response model. |
| `ui_lang` | string | No | User interface language preferred in response. Usually of the format <language_code>-<country_code> . For more, see RFC 9110 . |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "query": {
    "original": "best coffee in seattle",
    "show_strict_warning": false,
    "spellcheck_off": false
  },
  "results": [
    {
      "age": "9 hours ago",
      "description": "Our favorite coffee spots in Seattle for sitting down and getting some work done…",
      "extra_snippets": [
        "All City Coffee is our favorite coffee shop in Georgetown for getting work done—…"
      ],
      "meta_url": {
        "favicon": "https://imgs.search.brave.com/3VTx1ykYSLM6wIkkWjezI6aUbxLh9fb82D4Ml5qPou4/rs:fit…",
        "hostname": "theinfatuation.com",
        "netloc": "theinfatuation.com",
        "path": "› seattle  › reviews  › all-city-coffee",
        "scheme": "https"
      },
      "page_age": "2026-11-02T22:39:38",
      "profile": {
        "name": "The Infatuation",
        "url": "https://theinfatuation.com/seattle/reviews/all-city-coffee"
      },
      "thumbnail": {
        "src": "https://imgs.search.brave.com/HCR-1mTmgRUuXT7KMPHvCK0NlhgVM3PVh4bWyvLmxYY/rs:fit…"
      },
      "title": "All City Coffee is the best spot to get work done in Georgetown - Review - Seatt…",
      "type": "news_result",
      "url": "https://theinfatuation.com/seattle/reviews/all-city-coffee"
    }
  ],
  "type": "news"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `results[].title` | Headline or page title of the news result. |
| `results[].url` | Full URL of the article. |
| `results[].description` | Short excerpt that describes the article. |
| `results[].extra_snippets[]` | Additional excerpts from the same page. These appear in the response when the request sets `extra_snippets` to `true`. |
| `results[].age` | Human-readable age of the result, such as `9 hours ago` or `February 17, 2026`. |
| `results[].page_age` | Page date as an ISO 8601 style timestamp, such as `2026-02-17T16:30:00`. |
| `results[].profile.name / results[].profile.url` | Name of the source publication and the URL tied to that source profile. |
| `results[].meta_url.hostname / results[].meta_url.netloc` | Domain of the article. Use it to group or filter results by site. |
| `results[].thumbnail.src` | URL of a thumbnail image for the result. |
| `query.original` | The query string as you sent it. |

### Notes

- `q` is the only required parameter. It accepts up to 400 characters and 50 words.
- To paginate, combine `count` (1 to 50, default 20) with `offset` (0 to 9). `offset` counts pages of `count` results.
- Each item in `results` has `type` set to `news_result`. The top-level `type` is `news`.
- For non-news results, call [Brave Web Search](/apis/brave/web). For pictures, call [Brave Image Search](/apis/brave/images).

### Pricing

$0.005 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/brave/news.json`](../../../catalog/models/brave/news.json) · Store page: https://www.sandbase.ai/model/brave/news
