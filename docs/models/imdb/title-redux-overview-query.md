# IMDb Redux Overview API: pricing, parameters and code examples

`imdb/title-redux-overview-query` · data API · IMDb · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.007143 per call (free daily quota) · **Modes:** sync

Get the IMDb Redux overview for a title ID using selected language and country preferences. Use it to obtain a consolidated title overview for catalog review or content research.

## Pricing

- **$0.007143 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "imdb/title-redux-overview-query", "id": "tt0111161"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('imdb/title-redux-overview-query', {'id': 'tt0111161'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("imdb/title-redux-overview-query", {
  "id": "tt0111161"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "imdb/title-redux-overview-query", sandbase.Params{
	"id": "tt0111161",
})
```

Same call via the path form: `POST /v1/api/imdb/title-redux-overview-query` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string | yes | The IMDb title identifier in tt<digits> format.  |
| `languageCountry` | string |  | Language and country preferences. one of: `en_US`, `fr_CA`, `fr_FR`, `de_DE`, `hi_IN`, `it_IT`, `pt_BR`, `es_ES`, `es_US`, `es_MX`; default `"en_US"` |

## Details

Returns an overview of one IMDb title: plot text, rating, runtime, release date, certificate, Metacritic score, genre interests and production status. It needs an IMDb title ID in `tt<digits>` format and accepts an optional `languageCountry` preference.

### Use cases

- Check the IMDb rating, vote count and Metacritic score of a title in one call.
- Fill a catalog record with the title text, plot, poster image, release year and runtime.
- Show the age certificate and rating reason for a title on a content review page.
- Tag titles with the subgenre interests IMDb assigns to them.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/imdb/title-redux-overview-query" \
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
    "__typename": "Title",
    "canRate": {
      "isRatable": true
    },
    "certificate": {
      "__typename": "Certificate",
      "country": {
        "id": "US"
      },
      "id": "ce0067765",
      "rating": "R",
      "ratingReason": "Rated R for language and prison violence",
      "ratingsBody": {
        "id": "MPAA",
        "text": "MPAA"
      }
    },
    "engagementStatistics": {
      "watchlistStatistics": {
        "displayableCount": {
          "text": "Added by 5.1M users"
        }
      }
    },
    "episodes": null,
    "externalLinks": {
      "total": 152
    },
    "id": "tt0111161",
    "interests": {
      "edges": [
        {
          "node": {
            "__typename": "Interest",
            "description": {
              "value": {
                "plainText": "The epic subgenre features grand and sweeping stories often set against signific…"
              }
            },
            "id": "in0000077",
            "primaryImage": {
              "__typename": "Image",
              "caption": {
                "plainText": "Orson Welles in Citizen Kane (1941)"
              },
              "copyright": null,
              "countries": [],
              "createdBy": null,
              "height": 900,
              "id": "rm3123641601",
              "languages": []
            },
            "primaryText": {
              "__typename": "InterestText",
              "id": "Epic",
              "text": "Epic"
            },
            "secondaryText": {
              "__typename": "InterestText",
              "id": "Subgenre",
              "text": "Subgenre"
            }
          }
        }
      ]
    },
    "meta": {
      "id": "tt0111161",
      "restrictions": null
    },
    "metacritic": {
      "metascore": {
        "reviewCount": 22,
        "score": 82
      },
      "url": "https://www.metacritic.com/movie/the-shawshank-redemption?ftag=MCD-06-10aaa1c"
    },
    "originalTitleText": {
      "isOriginalTitle": true,
      "text": "The Shawshank Redemption"
    },
    "plot": {
      "plotText": {
        "plainText": "After a banker is sentenced to life in Shawshank Prison, he forms an unlikely fr…"
      }
    }
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `title.titleText.text / title.originalTitleText.text` | The title name and the original title name. `isOriginalTitle` shows whether the displayed name is the original. |
| `title.plot.plotText.plainText` | Short plain text plot summary. |
| `title.ratingsSummary.aggregateRating / title.ratingsSummary.voteCount` | The IMDb average rating and the number of votes behind it. |
| `title.metacritic.metascore.score / title.metacritic.metascore.reviewCount` | The Metacritic score and the number of reviews it is based on. `title.metacritic.url` links to the Metacritic page. |
| `title.runtime.seconds` | Running time of the title in seconds. |
| `title.releaseDate.year / title.releaseDate.month / title.releaseDate.day` | Release date parts, with the release country in `title.releaseDate.country.id`. |
| `title.certificate.rating / title.certificate.ratingReason` | The age rating (for example `R`) and the text that explains it. `title.certificate.ratingsBody.text` names the rating body. |
| `title.interests.edges[].node.primaryText.text` | Name of an interest or subgenre linked to the title, such as `Prison Drama`. `secondaryText.text` gives the interest type. |
| `title.productionStatus.currentProductionStage.text` | Current production stage, such as `Released`. `productionStatusHistory[]` lists dated status changes. |
| `title.titleType.text / title.primaryImage.url` | The title type (for example `Movie`) and the URL of the main poster image with its `width` and `height`. |

### Notes

- Use the `tt` ID from an IMDb title URL as `id`, for example `tt0111161`.
- `languageCountry` accepts `en_US`, `fr_CA`, `fr_FR`, `de_DE`, `hi_IN`, `it_IT`, `pt_BR`, `es_ES`, `es_US` and `es_MX`. The default is `en_US`.
- For cast and crew, call [IMDb Top Cast and Crew](/apis/imdb/title-top-cast-and-crew). For a longer plot, call [IMDb Plot Summary](/apis/imdb/title-plot-query).
- `episodes` and `series` are `null` for a movie.

### Pricing

$0.007143 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/imdb/title-redux-overview-query.json`](../../../catalog/models/imdb/title-redux-overview-query.json) · Store page: https://www.sandbase.ai/model/imdb/title-redux-overview-query
