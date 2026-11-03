# IMDb Critics Review Summary API: pricing, parameters and code examples

`imdb/title-critics-review-summary-query` · data API · IMDb · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.007143 per call (free daily quota) · **Modes:** sync

Get the IMDb critics-review summary for a title ID using selected language and country preferences. Use it to review critical reception or compare titles during research.

## Pricing

- **$0.007143 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "imdb/title-critics-review-summary-query", "id": "tt0111161"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('imdb/title-critics-review-summary-query', {'id': 'tt0111161'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("imdb/title-critics-review-summary-query", {
  "id": "tt0111161"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "imdb/title-critics-review-summary-query", sandbase.Params{
	"id": "tt0111161",
})
```

Same call via the path form: `POST /v1/api/imdb/title-critics-review-summary-query` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string | yes | The IMDb title identifier in tt<digits> format.  |
| `languageCountry` | string |  | Language and country preferences. one of: `en_US`, `fr_CA`, `fr_FR`, `de_DE`, `hi_IN`, `it_IT`, `pt_BR`, `es_ES`, `es_US`, `es_MX`; default `"en_US"` |

## Details

Returns the critics-review summary for one IMDb title. It includes the Metacritic score, a list of individual critic reviews, and external review links. The input is an IMDb title ID in `tt<digits>` format.

### Use cases

- Show the Metacritic score and review count next to a movie in a catalog page.
- Collect critic names, outlets and scores to compare how reviewers rated a film.
- Gather external review URLs for a title to build a reading list.
- Compare critical reception across several titles by calling the API once per ID.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/imdb/title-critics-review-summary-query" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"id": "tt0111161"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string | Yes | The IMDb title identifier in tt<digits> format. |
| `languageCountry` | string | No | Language and country preferences. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "title": {
    "externalLinks": {
      "__typename": "ExternalLinkConnection",
      "edges": [
        {
          "node": {
            "externalLinkLanguages": null,
            "label": "Rogerebert.com - Dec 2012 [Gerardo Valero]",
            "url": "https://www.rogerebert.com/far-flung-correspondents/the-shawshank-greatness"
          }
        }
      ],
      "pageInfo": {
        "__typename": "PageInfo",
        "endCursor": "YW16bjEuaW1kYi5pdGVtLjI2MDk2NDEy",
        "hasNextPage": true,
        "hasPreviousPage": false,
        "startCursor": "YW16bjEuaW1kYi5pdGVtLjI2MDk2NDA3"
      },
      "total": 152
    },
    "id": "tt0111161",
    "metacritic": {
      "__typename": "Metacritic",
      "metascore": {
        "reviewCount": 22,
        "score": 82
      },
      "reviews": {
        "edges": [
          {
            "node": {
              "quote": {
                "language": "en"
              },
              "reviewer": "Peter Travers",
              "score": 90,
              "site": "Rolling Stone",
              "url": "https://www.rollingstone.com/tv-movies/tv-movie-reviews/"
            }
          }
        ]
      },
      "url": "https://www.metacritic.com/movie/the-shawshank-redemption?ftag=MCD-06-10aaa1c"
    }
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `title.id` | The IMDb title ID that the summary belongs to. |
| `title.metacritic.metascore.score` | The Metacritic score for the title. The example shows `82`. |
| `title.metacritic.metascore.reviewCount` | The number of critic reviews behind the Metacritic score. |
| `title.metacritic.reviews.edges[].node.reviewer / title.metacritic.reviews.edges[].node.site` | The critic's name and the outlet that published the review. `reviewer` can be `null`. |
| `title.metacritic.reviews.edges[].node.score` | The score this critic gave the title. |
| `title.metacritic.reviews.edges[].node.quote.value` | A short quote from the review. This key can be missing when no quote is available. |
| `title.metacritic.reviews.edges[].node.url` | Link to the individual review. It can be `null`. |
| `title.metacritic.url` | Link to the title's page on Metacritic. |
| `title.externalLinks.edges[].node.label / title.externalLinks.edges[].node.url` | The label and URL of an external review link. The label includes the outlet, the date and the author. |
| `title.externalLinks.total` | The total number of external links for the title. |

### Notes

- Take the `id` from an IMDb title URL or from another IMDb API. It always starts with `tt`.
- `title.externalLinks.pageInfo` returns `hasNextPage`, `startCursor` and `endCursor`. This request has no cursor parameter, so the response shows only the first few links out of `total`.
- `languageCountry` accepts `en_US`, `fr_CA`, `fr_FR`, `de_DE`, `hi_IN`, `it_IT`, `pt_BR`, `es_ES`, `es_US` and `es_MX`. The default is `en_US`.
- For audience opinions, call [IMDb User Reviews Summary](/apis/imdb/title-user-reviews-summary-query).

### Pricing

$0.007143 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/imdb/title-critics-review-summary-query.json`](../../../catalog/models/imdb/title-critics-review-summary-query.json) · Store page: https://www.sandbase.ai/model/imdb/title-critics-review-summary-query
