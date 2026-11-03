# Brave LLM Context API: pricing, parameters and code examples

`brave/llm-context` · data API · Brave · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.005 per call (free daily quota) · **Modes:** sync

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

Returns page content snippets from web search results, shaped for use as context in an LLM prompt. It needs one search query in `q`. The response lists source pages with their text chunks and a metadata map keyed by URL.

### Use cases

- Feed fresh web snippets about a topic into a chatbot prompt so it can answer a question with cited pages.
- Build a research assistant that collects text chunks and source URLs for a query like `best coffee in seattle`.
- Check the age of each source page and drop old pages before you pass text to a model.
- Cap context size with `maximum_number_of_tokens` and `maximum_number_of_urls` to fit a model's prompt limit.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/brave/llm-context" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "best coffee in seattle"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | Yes | The user’s search query term. Query can not be empty. Maximum of 600 characters and 75 words in the query. |
| `context_threshold_mode` | string | No | The mode to use to determine the threshold for including content in context. |
| `count` | integer | No | The maximum number of search results considered to select the LLM context data. The default is 20 and the maximum is 50. |
| `country` | string | No | The search query country, where the results come from. The country string is limited to 2 character country codes of supported countries. |
| `enable_local` | boolean | No | Whether to enable local recall. Not setting this value means auto-detect: local recall is used if a location is provided ( X-Loc-Lat with X-Loc-Long , or X-Loc-City ). |
| `enable_source_metadata` | boolean | No | Enable source metadata enrichment (site_name, favicon, thumbnail, description, fetched_content_timestamp) in the sources attribute of the response. |
| `freshness` | string | No | Filters search results by page age. The age of a page is determined by the most relevant date reported by the content, such as its published or last modified date. The following values are supported: pd - Pages aged 24 h |
| `goggles` | string | No | Goggles act as a custom re-ranking on top of Brave’s search index. The parameter supports both a url where the Goggle is hosted or the definition of the Goggle. For more details, see the Goggles documentation . The param |
| `maximum_number_of_snippets` | integer | No | Maximum number of different snippets (or chunks of text) to include in LLM context. The default is 50 and maximum is 256 . |
| `maximum_number_of_snippets_per_url` | integer | No | Maximum number of snippets to include per URL. The default is 50 and maximum is 100 . |
| `maximum_number_of_tokens` | integer | No | Approximate maximum number of tokens to include in context. The default is 8192 and maximum is 32768 . |
| `maximum_number_of_tokens_per_url` | integer | No | Maximum number of tokens to include per URL. The default is 4096 and maximum is 8192 . |
| `maximum_number_of_urls` | integer | No | Maximum number of different URLs to include in LLM context. |
| `safesearch` | string | No | Filters results for adult content. The following values are supported: off - No filtering is done. moderate - Drops adult content from the results used for context. strict - Drops all adult content from the results used  |
| `search_lang` | string | No | The search language preference. The 2 or more character language code for which the search results are provided. |
| `spellcheck` | boolean | No | Whether to enable spellcheck on the query. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "grounding": {
    "generic": [
      {
        "snippets": [
          "# The Best Seattle Coffee Shops\n## Cardoon\nAs for coffee you can’t go wrong with…"
        ],
        "title": "The Best Coffee Shops in the Seattle Area",
        "url": "https://seattle.eater.com/maps/seattles-best-coffee-shops"
      }
    ],
    "map": []
  },
  "sources": {
    "https://alyeatsfood.com/2022/07/31/must-try-seattle-coffee-shops/": {
      "age": [
        "Sunday, July 31, 2022"
      ],
      "hostname": "alyeatsfood.com",
      "snippet": "Seattle has some of the best coffee out there and chances are you may have tried…",
      "title": "Must Try Seattle Coffee Shops"
    },
    "https://anchorheadcoffee.com/": {
      "age": [
        "Friday, November 14, 2025"
      ],
      "hostname": "anchorheadcoffee.com",
      "snippet": "Anchorhead Coffee is a Seattle-based specialty coffee roaster with cafes in Down…",
      "title": "Anchorhead Coffee"
    },
    "https://explorewashingtonstate.com/10-cafes-to-grab-a-coffee-in-seattle/": {
      "age": [
        "Sunday, November 01, 2026"
      ],
      "hostname": "explorewashingtonstate.com",
      "snippet": "Seattle is stereotypically associated with its rainy weather, tech companies suc…",
      "title": "Best Coffee in Seattle (2026)"
    },
    "https://feastio.com/coffee-shops-seattle/": {
      "age": [
        "Friday, August 14, 2026"
      ],
      "hostname": "feastio.com",
      "snippet": "Explore the best Seattle coffee shops from iconic venues to hidden gems.",
      "title": "Exploring Seattle's Best Third-Wave Coffee Shops"
    },
    "https://seattle.eater.com/maps/seattles-best-coffee-shops": {
      "age": [
        "Wednesday, March 11, 2026"
      ],
      "hostname": "seattle.eater.com",
      "snippet": "Vietnamese brews topped with salted cream, old-school espresso, and innovative i…",
      "title": "The Best Coffee Shops in the Seattle Area"
    },
    "https://seattleunexplored.com/the-2018-best-seattle-coffee-shop-awards-part-1/": {
      "age": [
        "Saturday, December 12, 2020"
      ],
      "hostname": "seattleunexplored.com",
      "snippet": "With two young’uns, we’ve had to trade in our frequency of night life in Seattle…",
      "title": "The Seattle Coffee Shop Awards - Part 1 - Seattle Unexplored"
    },
    "https://seattleunexplored.com/the-seattle-coffee-shop-awards-part-4/": {
      "age": [
        "Saturday, December 12, 2020"
      ],
      "hostname": "seattleunexplored.com",
      "snippet": "See our other installments of Seattle Coffee Shop Awards: Everything You Always …",
      "title": "The Seattle Coffee Shop Awards - Part 4 - Seattle Unexplored"
    },
    "https://sevencoffeeroasters.com/pages/seven-market-cafe": {
      "age": [],
      "hostname": "sevencoffeeroasters.com",
      "snippet": "One of the best-reviewed coffee shops in Seattle on Google Maps.",
      "title": "Seven Market"
    },
    "https://wheatlesswanderlust.com/best-coffee-shops-in-seattle/": {
      "age": [
        "Tuesday, September 15, 2026"
      ],
      "hostname": "wheatlesswanderlust.com",
      "snippet": "Three coffee snobs go on a quest to uncover the best coffee in Seattle. Read to …",
      "title": "The Best Coffee In Seattle: A Guide For Coffee Lovers"
    },
    "https://www.cntraveler.com/gallery/best-coffee-shops-in-seattle-united-states": {
      "age": [
        "Friday, September 04, 2026"
      ],
      "hostname": "www.cntraveler.com",
      "snippet": "Our top recommendations for the best coffee in Seattle with pictures, reviews, a…",
      "title": "10 Best Coffee Shops in Seattle"
    },
    "https://www.doubleskinnymacchiato.com/2020/03/seattle-specialty-coffee-shops-guide-map.html": {
      "age": [
        "Monday, March 02, 2020"
      ],
      "hostname": "www.doubleskinnymacchiato.com",
      "snippet": "The first Starbucks opened in Pike Place Market in 1971, and whatever you feel a…",
      "title": "Double Skinny Macchiato"
    },
    "https://www.emeraldpalate.com/best-coffee-shops-in-seattle/": {
      "age": [
        "Thursday, July 30, 2026"
      ],
      "hostname": "www.emeraldpalate.com",
      "snippet": "A local shares the best coffee shops in Seattle, WA. Find creative coffee drinks…",
      "title": "26 Best Coffee Shops in Seattle, WA for a Caffeine Fix"
    }
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `grounding.generic[].title` | Title of a page whose text was selected as context. |
| `grounding.generic[].url` | URL of the page. It matches a key in the `sources` object. |
| `grounding.generic[].snippets[]` | Text chunks taken from the page. Pass these to your LLM as context. |
| `grounding.map` | List of map-style results. It is empty in this response. |
| `sources.<url>.title` | Page title for the source, keyed by the full page URL. |
| `sources.<url>.hostname` | Domain name of the source page. |
| `sources.<url>.snippet` | Short description of the page. |
| `sources.<url>.age` | List of three items: a readable date, an ISO date such as `2026-11-01`, and a relative age such as `2 days ago`. The list is empty when no date is known. |

### Notes

- Only `q` is required. Use `count`, `maximum_number_of_urls`, `maximum_number_of_snippets` and `maximum_number_of_tokens` to control how much context comes back.
- Match `grounding.generic[].url` to the keys of `sources` to get the hostname and age of each page.
- `sources` can hold more pages than `grounding.generic`, so not every source has snippets.
- Set `enable_source_metadata` to `true` to add fields such as `site_name`, `favicon` and `thumbnail` to `sources`. For plain result lists, try [Brave Web Search](/apis/brave/web).

### Pricing

$0.005 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/brave/llm-context.json`](../../../catalog/models/brave/llm-context.json) · Store page: https://www.sandbase.ai/model/brave/llm-context
