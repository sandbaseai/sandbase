# Brave Video Search API: pricing, parameters and code examples

`brave/videos` · data API · Brave · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.005 per call (free daily quota) · **Modes:** sync

Video Search from Brave. Returns the official Brave API response unchanged.

## Pricing

- **$0.005 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "brave/videos", "q": "how to brew pour over coffee"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('brave/videos', {'q': 'how to brew pour over coffee'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("brave/videos", {
  "q": "how to brew pour over coffee"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "brave/videos", sandbase.Params{
	"q": "how to brew pour over coffee",
})
```

Same call via the path form: `POST /v1/api/brave/videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string | yes | The user’s search query term. Query can not be empty. Maximum of 400 characters and 50 words in the query.  |
| `count` | integer |  | The number of search results returned in response. The maximum is 50. The actual number delivered may be less than requested. Combine this parameter with offset to paginate search results. default `20`; range 1–50 |
| `offset` | integer |  | The zero based offset that indicates number of search results per page (count) to skip before returning the result. The maximum is 9. The actual number delivered may be less than requested based on the query. In order… default `0`; range 0–9 |
| `country` | string |  | The search query country, where the results come from. The country string is limited to 2 character country codes of supported countries or ALL for worldwide. one of: `AR`, `AU`, `AT`, `BE`, `BR`, `CA`, `CL`, `DK`, `FI`, `FR`, `DE`, `GR` …; default `"US"` |
| `ui_lang` | string |  | User interface language preferred in response. Usually of the format <language_code>-<country_code> . For more, see RFC 9110 . one of: `es-AR`, `en-AU`, `de-AT`, `nl-BE`, `fr-BE`, `pt-BR`, `en-CA`, `fr-CA`, `es-CL`, `da-DK`, `fi-FI`, `fr-FR` …; default `"en-US"` |
| `freshness` | string |  | Filters search results by page age. The age of a page is determined by the most relevant date reported by the content, such as its published or last modified date. The following values are supported: pd - Pages aged 24… default `""` |
| `operators` | boolean |  | Whether to apply search operators. default `true` |
| `safesearch` | string |  | Filters search results for adult content. The following values are supported: off - No filtering is done. moderate - Filters explicit content, like images and videos, but allows adult domains in the search results.… one of: `off`, `moderate`, `strict`; default `"moderate"` |
| `spellcheck` | boolean |  | Whether to spell check the provided query. If the spellchecker is enabled, the modified query is always used for search. The modified query can be found in altered key from the query response model. default `true` |
| `search_lang` | string |  | The search language preference. The 2 or more character language code for which the search results are provided. one of: `ar`, `eu`, `bn`, `bg`, `ca`, `zh-hans`, `zh-hant`, `hr`, `cs`, `da`, `nl`, `en` …; default `"en"` |
| `include_fetch_metadata` | boolean |  | Include fetch metadata. default `false` |

## Details

Returns video search results for a text query, in the same shape as the Brave video search response. Each result has a title, page URL, description, thumbnail and video details such as creator and duration. The only required input is `q`.

### Use cases

- Find tutorial videos on a topic and list them with title, thumbnail and duration.
- Build a video feed for a niche by running searches and keeping results from chosen channels.
- Check which creators and sites appear for a keyword by reading `video.author.name` and `meta_url.hostname`.
- Narrow results to recent videos with the `freshness` parameter and sort them by `page_age`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/brave/videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "how to brew pour over coffee"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | Yes | The user’s search query term. Query can not be empty. Maximum of 400 characters and 50 words in the query. |
| `count` | integer | No | The number of search results returned in response. The maximum is 50. The actual number delivered may be less than requested. Combine this parameter with offset to paginate search results. |
| `country` | string | No | The search query country, where the results come from. The country string is limited to 2 character country codes of supported countries or ALL for worldwide. |
| `freshness` | string | No | Filters search results by page age. The age of a page is determined by the most relevant date reported by the content, such as its published or last modified date. The following values are supported: pd - Pages aged 24 h |
| `include_fetch_metadata` | boolean | No | Include fetch metadata. |
| `offset` | integer | No | The zero based offset that indicates number of search results per page (count) to skip before returning the result. The maximum is 9. The actual number delivered may be less than requested based on the query. In order to |
| `operators` | boolean | No | Whether to apply search operators. |
| `safesearch` | string | No | Filters search results for adult content. The following values are supported: off - No filtering is done. moderate - Filters explicit content, like images and videos, but allows adult domains in the search results. stric |
| `search_lang` | string | No | The search language preference. The 2 or more character language code for which the search results are provided. |
| `spellcheck` | boolean | No | Whether to spell check the provided query. If the spellchecker is enabled, the modified query is always used for search. The modified query can be found in altered key from the query response model. |
| `ui_lang` | string | No | User interface language preferred in response. Usually of the format <language_code>-<country_code> . For more, see RFC 9110 . |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "extra": {
    "might_be_offensive": false
  },
  "query": {
    "original": "how to brew pour over coffee",
    "show_strict_warning": false,
    "spellcheck_off": false
  },
  "results": [
    {
      "age": "December 9, 2023",
      "description": "Our friend Alex Kaplan (once the youngest certified Q Coffee Grader...ever, and …",
      "meta_url": {
        "favicon": "https://imgs.search.brave.com/Wg4wjE5SHAargkzePU3eSLmWgVz84BEZk1SjSglJK_U/rs:fit…",
        "hostname": "www.youtube.com",
        "netloc": "youtube.com",
        "path": "› watch",
        "scheme": "https"
      },
      "page_age": "2023-12-09T03:17:01",
      "thumbnail": {
        "original": "https://i.ytimg.com/vi/FQWhY5mPGRg/maxresdefault.jpg",
        "src": "https://imgs.search.brave.com/Fv39Vqg-ITsz3QmtENVl0tXCnnXCezNKJCE-GPB_fLc/rs:fit…"
      },
      "title": "A beginner's guide to POUR-OVER COFFEE - YouTube",
      "type": "video_result",
      "url": "https://www.youtube.com/watch?v=FQWhY5mPGRg",
      "video": {
        "author": {
          "name": "Majordomo",
          "url": "http://www.youtube.com/@majordomomedia"
        },
        "creator": "Majordomo",
        "duration": "06:07",
        "publisher": "YouTube",
        "requires_subscription": false,
        "tags": [
          "los angeles food"
        ],
        "views": 8906
      }
    }
  ],
  "type": "videos"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `results[].title` | Title of the video page. |
| `results[].url` | Link to the page that hosts the video. |
| `results[].description` | Short text from the video page. It can be cut off. |
| `results[].age / results[].page_age` | Publish date of the page. `age` is a readable date such as `December 9, 2023`. `page_age` is an ISO style timestamp such as `2023-12-09T03:17:01`. |
| `results[].video.author.name / results[].video.author.url` | Name and channel link of the video author. |
| `results[].video.creator / results[].video.publisher` | Creator name and the platform that publishes the video, such as `YouTube`. |
| `results[].video.duration` | Length of the video as a text value such as `06:07`. |
| `results[].video.views` | View count. This key is missing on some results. |
| `results[].thumbnail.src / results[].thumbnail.original` | Thumbnail URLs. `src` is a resized copy and `original` points to the image on the source site. |
| `results[].meta_url.hostname` | Host name of the result page. It shows which site the video comes from. |

### Notes

- Some keys, such as `video.views`, `video.tags` and `video.requires_subscription`, appear only on some results. Check that they exist before you read them.
- To page through results, send `count` (up to 50) with `offset` (0 to 9). `offset` counts pages of `count` results.
- The `query.original` field echoes your query. With `spellcheck` on, the search may use a changed query.
- For other result types, see [Brave Web Search](/apis/brave/web), [Brave News Search](/apis/brave/news) or [Brave Image Search](/apis/brave/images).

### Pricing

$0.005 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/brave/videos.json`](../../../catalog/models/brave/videos.json) · Store page: https://www.sandbase.ai/model/brave/videos
