# IMDb News by Category API: pricing, parameters and code examples

`imdb/news-by-category-query` · data API · IMDb · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.007143 per call (free daily quota) · **Modes:** sync

Get IMDb news for a selected top, movie, TV, or celebrity category using language and country preferences. Use it to monitor entertainment news or research a specific category.

## Pricing

- **$0.007143 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "imdb/news-by-category-query", "category": "TOP"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('imdb/news-by-category-query', {'category': 'TOP'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("imdb/news-by-category-query", {
  "category": "TOP"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "imdb/news-by-category-query", sandbase.Params{
	"category": "TOP",
})
```

Same call via the path form: `POST /v1/api/imdb/news-by-category-query` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `category` | string | yes | News category to filter by. one of: `TOP`, `MOVIE`, `TV`, `CELEBRITY` |
| `languageCountry` | string |  | Language and country preferences. one of: `en_US`, `fr_CA`, `fr_FR`, `de_DE`, `hi_IN`, `it_IT`, `pt_BR`, `es_ES`, `es_US`, `es_MX`; default `"en_US"` |

## Details

Returns a list of IMDb news articles for one category: `TOP`, `MOVIE`, `TV` or `CELEBRITY`. Each article has a title, byline, date, link, image and source. The only required input is `category`, and `languageCountry` sets the language and country preference.

### Use cases

- Build a feed of the latest top entertainment headlines for a news app.
- Track TV news such as renewals and cancellations by calling the `TV` category.
- Collect celebrity news to follow coverage of specific people.
- Compare headlines across `languageCountry` values to see how coverage differs by locale.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/imdb/news-by-category-query" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"category": "TOP"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `category` | string | Yes | News category to filter by. |
| `languageCountry` | string | No | Language and country preferences. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "news": {
    "__typename": "NewsConnection",
    "edges": [
      {
        "node": {
          "__typename": "News",
          "articleTitle": {
            "plainText": "Box Office Report: ‘You Can See Everything’ #1 in Third Week While ‘Resident Evi…"
          },
          "byline": "James Gamble",
          "date": "2026-11-02T20:12:34Z",
          "externalUrl": "https://www.imdb.com/news/ni66092278/",
          "id": "ni66092278",
          "image": {
            "__typename": "Image",
            "height": 5760,
            "id": "rm3794127618",
            "url": "https://m.media-amazon.com/images/M/MV5BZGQ5NjE5OGItZGEwMC00ZjJkLTllOTktM2RlNDk4…",
            "width": 8640
          },
          "source": {
            "description": null,
            "homepage": {
              "label": "IMDb News",
              "url": "https://www.imdb.com/"
            }
          }
        }
      }
    ],
    "pageInfo": {
      "__typename": "NewsPageInfo",
      "endCursor": "NjYwOTE4Mjh8MjAyNi0xMS0wMiAxNjozNjoxOQ",
      "hasNextPage": true
    },
    "total": 800472
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `news.edges[].node.articleTitle.plainText` | Headline of the article as plain text. |
| `news.edges[].node.byline` | Name of the author of the article. |
| `news.edges[].node.date` | Publication time of the article in UTC, in ISO 8601 format. |
| `news.edges[].node.externalUrl` | Link to the article. It points to an IMDb news page or to the original publisher's site. |
| `news.edges[].node.id` | IMDb news ID, such as `ni66092278`. |
| `news.edges[].node.image.url` | URL of the article's image. |
| `news.edges[].node.image.width / news.edges[].node.image.height` | Image dimensions. The values are pixel sizes of the image file. |
| `news.edges[].node.source.homepage.label` | Name of the outlet that published the article, such as IMDb News or The Hollywood Reporter. |
| `news.pageInfo.hasNextPage` | Whether more articles are available after this page. |
| `news.total` | Total number of news items reported for the request. |

### Notes

- `category` accepts `TOP`, `MOVIE`, `TV` or `CELEBRITY`. `languageCountry` accepts values such as `en_US`, `fr_FR`, `de_DE` and `es_MX`, and defaults to `en_US`.
- `news.pageInfo.endCursor` is a cursor for the next page, but this API lists no pagination parameter in its request schema.
- Articles are ordered with the newest `date` first in this response.
- To look up a title mentioned in a headline, try [IMDb Base Info](/apis/imdb/title-base-query) or [IMDb Top Cast and Crew](/apis/imdb/title-top-cast-and-crew).

### Pricing

$0.007143 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/imdb/news-by-category-query.json`](../../../catalog/models/imdb/news-by-category-query.json) · Store page: https://www.sandbase.ai/model/imdb/news-by-category-query
