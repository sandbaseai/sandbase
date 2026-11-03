# Brave Web Search API: pricing, parameters and code examples

`brave/web` · data API · Brave · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.005 per call (free daily quota) · **Modes:** sync

Web Search from Brave. Returns the official Brave API response unchanged.

## Pricing

- **$0.005 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "brave/web", "q": "weather seattle"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('brave/web', {'q': 'weather seattle'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("brave/web", {
  "q": "weather seattle"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "brave/web", sandbase.Params{
	"q": "weather seattle",
})
```

Same call via the path form: `POST /v1/api/brave/web` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string | yes | The user’s search query term. Query can not be empty. Maximum of 600 characters and 75 words in the query.  |
| `count` | integer |  | The number of search results returned in response. The maximum is 20. The actual number delivered may be less than requested. Combine this parameter with offset to paginate search results. NOTE: Count only applies to… default `20`; range 1–20 |
| `units` | string |  | The measurement units. The following values are supported: metric - The standardized measurement system (km, celcius…) imperial - The British Imperial system of units (mile, fahrenheit…) one of: `imperial`, `metric` |
| `offset` | integer |  | The zero based offset that indicates number of search result pages (count) to skip before returning the result. The default is 0 and the maximum is 9. The actual number delivered may be less than requested. Use this… default `0`; range 0–9 |
| `country` | string |  | The 2 character country code where the search results come from. one of: `AR`, `AU`, `AT`, `BE`, `BR`, `CA`, `CL`, `DK`, `FI`, `FR`, `DE`, `GR` …; default `"US"` |
| `goggles` | string |  | Goggles act as a custom re-ranking on top of Brave’s search index. The parameter supports both a url where the Goggle is hosted or the definition of the Goggle. For more details, see the Goggles documentation . The…  |
| `summary` | boolean |  | This parameter enables summary key generation in web search results. This is required for summarizer to be enabled.  |
| `ui_lang` | string |  | User interface language preferred in response. Usually of the format <language_code>-<country_code>. For more, see RFC 9110 . one of: `es-AR`, `en-AU`, `de-AT`, `nl-BE`, `fr-BE`, `pt-BR`, `en-CA`, `fr-CA`, `es-CL`, `da-DK`, `fi-FI`, `fr-FR` …; default `"en-US"` |
| `freshness` | string |  | Filters search results by page age. The age of a page is determined by the most relevant date reported by the content, such as its published or last modified date. The following values are supported: pd - Pages aged 24… default `""` |
| `operators` | boolean |  | Whether to apply search operators default `true` |
| `goggles_id` | string |  | Goggles act as a custom re-ranking on top of Brave’s search index. For more details, refer to the Goggles repository. This parameter is deprecated. Please use the goggles parameter.  |
| `safesearch` | string |  | Filters search results for adult content. The following values are supported: off - No filtering is done. moderate - Filters explicit content, like images and videos, but allows adult domains in the search results.… one of: `off`, `moderate`, `strict`; default `"moderate"` |
| `spellcheck` | boolean |  | Whether to spell check provided query. If the spell checker is enabled, the modified query is always used for search. The modified query can be found in altered key from the query response model. default `true` |
| `search_lang` | string |  | The 2 or more character language code for which the search results are provided. one of: `ar`, `eu`, `bn`, `bg`, `ca`, `zh-hans`, `zh-hant`, `hr`, `cs`, `da`, `nl`, `en` …; default `"en"` |
| `result_filter` | array |  | A comma delimited string of result types to include in the search response. Not specifying this parameter will return back all result types in search response where data is available and the plan has the corresponding…  |
| `extra_snippets` | boolean |  | A snippet is an excerpt from a page you get as a result of the query, and extra_snippets allow you to get up to 5 additional, alternative excerpts.  |
| `text_decorations` | boolean |  | Whether display strings (e.g. result snippets) should include decoration markers (e.g. highlighting characters). default `true` |
| `enable_rich_callback` | boolean |  | Enable rich callback. Allows you to get real time rich results via a callback URL when they are relevant to your query. NOTE : Requires Search plan. default `false` |
| `include_fetch_metadata` | boolean |  | Include fetch metadata. default `false` |

## Details

Returns Brave web search results for a text query. The only required input is `q`. The response holds web results, news, FAQ entries, query details and a rich result hint, all in the original Brave format.

### Use cases

- Pull the top web pages for a query to build a search feature or a research tool.
- Collect recent news articles about a topic using the `news.results` list.
- Read `query.related_queries` to find related searches for keyword research.
- Use the `rich` callback hint to fetch live data such as weather for a location query.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/brave/web" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "weather seattle", "enable_rich_callback": true}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | Yes | The user’s search query term. Query can not be empty. Maximum of 600 characters and 75 words in the query. |
| `count` | integer | No | The number of search results returned in response. The maximum is 20. The actual number delivered may be less than requested. Combine this parameter with offset to paginate search results. NOTE: Count only applies to web |
| `country` | string | No | The 2 character country code where the search results come from. |
| `enable_rich_callback` | boolean | No | Enable rich callback. Allows you to get real time rich results via a callback URL when they are relevant to your query. NOTE : Requires Search plan. |
| `extra_snippets` | boolean | No | A snippet is an excerpt from a page you get as a result of the query, and extra_snippets allow you to get up to 5 additional, alternative excerpts. |
| `freshness` | string | No | Filters search results by page age. The age of a page is determined by the most relevant date reported by the content, such as its published or last modified date. The following values are supported: pd - Pages aged 24 h |
| `goggles` | string | No | Goggles act as a custom re-ranking on top of Brave’s search index. The parameter supports both a url where the Goggle is hosted or the definition of the Goggle. For more details, see the Goggles documentation . The param |
| `goggles_id` | string | No | Goggles act as a custom re-ranking on top of Brave’s search index. For more details, refer to the Goggles repository. This parameter is deprecated. Please use the goggles parameter. |
| `include_fetch_metadata` | boolean | No | Include fetch metadata. |
| `offset` | integer | No | The zero based offset that indicates number of search result pages (count) to skip before returning the result. The default is 0 and the maximum is 9. The actual number delivered may be less than requested. Use this para |
| `operators` | boolean | No | Whether to apply search operators |
| `result_filter` | array | No | A comma delimited string of result types to include in the search response. Not specifying this parameter will return back all result types in search response where data is available and the plan has the corresponding op |
| `safesearch` | string | No | Filters search results for adult content. The following values are supported: off - No filtering is done. moderate - Filters explicit content, like images and videos, but allows adult domains in the search results. stric |
| `search_lang` | string | No | The 2 or more character language code for which the search results are provided. |
| `spellcheck` | boolean | No | Whether to spell check provided query. If the spell checker is enabled, the modified query is always used for search. The modified query can be found in altered key from the query response model. |
| `summary` | boolean | No | This parameter enables summary key generation in web search results. This is required for summarizer to be enabled. |
| `text_decorations` | boolean | No | Whether display strings (e.g. result snippets) should include decoration markers (e.g. highlighting characters). |
| `ui_lang` | string | No | User interface language preferred in response. Usually of the format <language_code>-<country_code>. For more, see RFC 9110 . |
| `units` | string | No | The measurement units. The following values are supported: metric - The standardized measurement system (km, celcius…) imperial - The British Imperial system of units (mile, fahrenheit…) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "faq": {
    "results": [
      {
        "answer": "No",
        "meta_url": {
          "favicon": "https://imgs.search.brave.com/PngeKo7zbzNt-2zCSn559wzst7VixpZEDNgaxIMzo-E/rs:fit…",
          "hostname": "www.theweathernetwork.com",
          "netloc": "theweathernetwork.com",
          "path": "› en  › city  › us  › washington  › seattle  › current",
          "scheme": "https"
        },
        "question": "Are there any active weather alerts in Seattle?",
        "title": "Seattle, WA Current Weather - The Weather Network",
        "url": "https://www.theweathernetwork.com/en/city/us/washington/seattle/current"
      }
    ],
    "type": "faq"
  },
  "mixed": {
    "main": [
      {
        "all": false,
        "index": 0,
        "type": "rich"
      }
    ],
    "side": [],
    "top": [],
    "type": "mixed"
  },
  "news": {
    "mutated_by_goggles": false,
    "results": [
      {
        "age": "17 hours ago",
        "breaking": false,
        "description": "<strong>Seattle</strong> residents can also expect frigid temperatures stretchin…",
        "family_friendly": true,
        "fetched_content_timestamp": 1738268522,
        "is_live": false,
        "is_source_both": false,
        "is_source_local": false,
        "meta_url": {
          "favicon": "https://imgs.search.brave.com/fPoxYqQRrihSomdk0s9DwKe7SuN5tuntzBVqJ943XF8/rs:fit…",
          "hostname": "www.seattletimes.com",
          "netloc": "seattletimes.com",
          "path": "› seattle-news  › weather  › seattle-weather-chilly-foggy-fall-days-followed-by-…",
          "scheme": "https"
        },
        "page_age": "2026-11-02T14:48:55",
        "thumbnail": {
          "original": "https://www.seattletimes.com/wp-content/themes/st_refresh/img/st-meta-facebook.p…",
          "src": "https://imgs.search.brave.com/l3g2QySD_YG1ARk7Q-7uP1PWuEQvfo2KD-1tphVl8hc/rs:fit…"
        },
        "title": "Rain and gusty winds bookend chilly fall weather this week"
      }
    ],
    "type": "news"
  },
  "query": {
    "bad_results": false,
    "city": "",
    "country": "us",
    "header_country": "",
    "is_geolocal": true,
    "is_navigational": false,
    "is_news_breaking": false,
    "local_decision": "mix",
    "more_results_available": true,
    "original": "weather seattle",
    "postal_code": "",
    "related_queries": [
      "seattle weather 14 day forecast"
    ]
  },
  "rich": {
    "hint": {
      "callback_key": "5a73af8c2c9b4eaba2424115d4459332",
      "vertical": "weather"
    },
    "type": "rich"
  },
  "type": "search",
  "web": {
    "family_friendly": true,
    "results": [
      {
        "age": "1 week ago",
        "description": "Seattle, WA Weather Forecast, with current conditions, wind, air quality, and wh…",
        "extra_snippets": [
          "For Business For Partners For Advertising AccuWeather APIs AccuWeather Connect P…"
        ],
        "family_friendly": true,
        "is_live": false,
        "is_source_both": false,
        "is_source_local": false,
        "language": "en",
        "meta_url": {
          "favicon": "https://imgs.search.brave.com/fs6uyhM5xA6gctiAKJTHhWtpR2YRWceKfG_9aqjmfRs/rs:fit…",
          "hostname": "www.accuweather.com",
          "netloc": "accuweather.com",
          "path": "› en  › us  › seattle  › 98104  › weather-forecast  › 351409",
          "scheme": "https"
        },
        "page_age": "2026-10-27T15:58:37",
        "profile": {
          "img": "https://imgs.search.brave.com/fs6uyhM5xA6gctiAKJTHhWtpR2YRWceKfG_9aqjmfRs/rs:fit…",
          "long_name": "accuweather.com",
          "name": "AccuWeather",
          "url": "https://www.accuweather.com/en/us/seattle/98104/weather-forecast/351409"
        },
        "subtype": "generic"
      }
    ],
    "type": "search"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `web.results[].title / web.results[].url` | Title and link of each web result. |
| `web.results[].description` | Short text excerpt for the result. It can contain HTML such as `<strong>` tags around matched words. |
| `web.results[].extra_snippets` | Additional excerpts from the same page. It appears on some results. |
| `web.results[].page_age / web.results[].age` | `page_age` is an ISO style date and time for the page. `age` is a readable version such as `1 week ago`. |
| `web.results[].meta_url.hostname` | Host name of the result page. `meta_url` also holds `favicon`, `netloc`, `path` and `scheme`. |
| `web.results[].location.coordinates` | Latitude and longitude pair for a result tied to a place. `location.postal_address` holds the city, region and postal code. |
| `news.results[].title / news.results[].url / news.results[].description` | Headline, link and excerpt for each news article. |
| `news.results[].fetched_content_timestamp` | Numeric timestamp for when the article content was fetched. |
| `faq.results[].question / faq.results[].answer` | A question and short answer taken from a page, with the source `title` and `url`. |
| `query.original / query.related_queries / query.more_results_available` | The query as sent, a list of suggested related searches, and a flag showing whether more results exist. |
| `rich.hint.callback_key / rich.hint.vertical` | Key and topic (here `weather`) for the rich result. Use the key to request the rich data. |

### Notes

- Set `q` to the search text. The `count` parameter sets the number of web results and `offset` skips pages of that size.
- Send `enable_rich_callback` as `true` to get the `rich.hint` object when the query has a rich result.
- `mixed.main` lists the suggested display order of result types, with an `index` that points into each list.
- To get the rich result itself, call [Brave Rich Search](/apis/brave/web-rich) with the `callback_key`. For news only, use [Brave News Search](/apis/brave/news).

### Pricing

$0.005 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/brave/web.json`](../../../catalog/models/brave/web.json) · Store page: https://www.sandbase.ai/model/brave/web
