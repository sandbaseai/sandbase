# IMDb Details API: pricing, parameters and code examples

`imdb/title-details-query` · data API · IMDb · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.007143 per call (free daily quota) · **Modes:** sync

Get IMDb title details for a title ID using selected language and country preferences. Use it to support detailed title research or enrich a movie and television catalog.

## Pricing

- **$0.007143 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "imdb/title-details-query", "id": "tt0111161"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('imdb/title-details-query', {'id': 'tt0111161'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("imdb/title-details-query", {
  "id": "tt0111161"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "imdb/title-details-query", sandbase.Params{
	"id": "tt0111161",
})
```

Same call via the path form: `POST /v1/api/imdb/title-details-query` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string | yes | The IMDb title identifier in tt<digits> format.  |
| `languageCountry` | string |  | Language and country preferences. one of: `en_US`, `fr_CA`, `fr_FR`, `de_DE`, `hi_IN`, `it_IT`, `pt_BR`, `es_ES`, `es_US`, `es_MX`; default `"en_US"` |

## Details

Returns IMDb details for one title: original and alternate titles, release date, runtime, languages, countries of origin, filming locations, official links and the main poster image. It needs an IMDb title ID in `tt<digits>` format, such as `tt0111161`.

### Use cases

- Add runtime, release year and spoken languages to a movie and TV catalog.
- Build a list of localized titles for a film using the `akas` entries.
- Show filming locations with the scenes shot there on a travel or trivia page.
- Collect official websites and social pages for a title.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/imdb/title-details-query" \
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
    "akas": {
      "__typename": "AkaConnection",
      "edges": [
        {
          "node": {
            "attributes": [
              {
                "id": "alternativeTitle",
                "text": "Alternative Title"
              }
            ],
            "country": {
              "__typename": "DisplayableCountry",
              "id": "MX",
              "text": "Mexico"
            },
            "displayableProperty": {
              "__typename": "DisplayableTitleAkaProperty",
              "value": {
                "id": "Sueño de fuga",
                "plainText": "Sueño de fuga"
              }
            },
            "language": null
          }
        }
      ],
      "pageInfo": {
        "__typename": "PageInfo",
        "endCursor": "MA==",
        "hasNextPage": true,
        "hasPreviousPage": false,
        "startCursor": "MA=="
      },
      "total": 64
    },
    "alternateVersions": {
      "__typename": "AlternateVersionConnection",
      "edges": [
        {
          "node": {
            "text": {
              "plainText": "This film was produced independently by Castle Rock Entertainment, but distribut…"
            }
          }
        }
      ],
      "pageInfo": {
        "__typename": "PageInfo",
        "endCursor": "Z0xrd3FsSWRDQlNqaFJyYy9qU2UzcWlHN21OSmtsa1MxM3pwVWlpdERtdz0=",
        "hasNextPage": true,
        "hasPreviousPage": false,
        "startCursor": "Z0xrd3FsSWRDQlNqaFJyYy9qU2UzcWlHN21OSmtsa1MxM3pwVWlpdERtdz0="
      },
      "total": 5
    },
    "countriesOfOrigin": {
      "countries": [
        {
          "__typename": "CountryOfOrigin",
          "id": "US",
          "text": "United States"
        }
      ]
    },
    "filmingLocations": {
      "__typename": "FilmingLocationConnection",
      "edges": [
        {
          "node": {
            "attributes": [
              {
                "text": "Exterior"
              }
            ],
            "displayableProperty": {
              "__typename": "DisplayableTitleFilmingLocationProperty",
              "value": {
                "id": "Butler, Ohio, USA",
                "plainText": "Butler, Ohio, USA"
              }
            },
            "id": "lc0342942",
            "interestScore": {
              "__typename": "InterestScore",
              "usersInterested": 57,
              "usersVoted": 57
            }
          }
        }
      ],
      "pageInfo": {
        "__typename": "PageInfo",
        "endCursor": "bGMwMzQyOTQy",
        "hasNextPage": true,
        "hasPreviousPage": false,
        "startCursor": "bGMwMzQyOTQy"
      },
      "total": 21
    },
    "id": "tt0111161",
    "officialLinks": {
      "edges": [
        {
          "node": {
            "__typename": "ExternalLink",
            "externalLinkRegion": null,
            "label": "Official Facebook",
            "url": "https://www.facebook.com/shawshankredemptionfilm/"
          }
        }
      ]
    },
    "originalTitleText": {
      "isOriginalTitle": true,
      "text": "The Shawshank Redemption"
    },
    "primaryImage": {
      "__typename": "Image",
      "height": 1800,
      "id": "rm1690056449",
      "url": "https://m.media-amazon.com/images/M/MV5BMDAyY2FhYjctNDc5OS00MDNlLThiMGUtY2UxYWVk…",
      "width": 1200
    },
    "releaseDate": {
      "__typename": "ReleaseDate",
      "attributes": [],
      "country": {
        "id": "US"
      },
      "day": 14,
      "displayableProperty": {
        "qualifiersInMarkdownList": null
      },
      "month": 10,
      "restriction": null,
      "year": 1994
    },
    "releaseYear": {
      "__typename": "YearRange",
      "endYear": null,
      "year": 1994
    },
    "runtime": {
      "seconds": 8520
    }
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `title.id` | The IMDb title ID, in `tt<digits>` format. |
| `title.titleText.text / title.originalTitleText.text` | The title text and the original title text. `isOriginalTitle` is `true` when the text is the original title. |
| `title.titleType.id / title.titleType.text` | The type of title, such as `movie`. `isSeries` and `isEpisode` are booleans, and `canHaveEpisodes` shows whether the title can have episodes. |
| `title.releaseDate.year / title.releaseDate.month / title.releaseDate.day` | The release date for the country in `title.releaseDate.country.id`. |
| `title.releaseYear.year / title.releaseYear.endYear` | The start year and the end year of the title. `endYear` is `null` for this movie. |
| `title.runtime.seconds` | The runtime in seconds. |
| `title.spokenLanguages.spokenLanguages[].text` | The name of each spoken language. The `id` is a language code such as `en`. |
| `title.akas.edges[].node.displayableProperty.value.plainText` | An alternate title. The `country.text` field gives the country it applies to, and `total` gives the number of alternate titles. |
| `title.filmingLocations.edges[].node.displayableProperty.value.plainText` | A filming location name. The `attributes[].text` field describes the scene, and `interestScore.usersVoted` counts the votes. |
| `title.primaryImage.url` | The URL of the main poster image. `width` and `height` give its size in pixels. |

### Notes

- The list sections `akas`, `alternateVersions` and `filmingLocations` each return `total`, `pageInfo.hasNextPage` and `pageInfo.endCursor`. The response shows only the first page of each.
- Set `languageCountry` to one of `en_US`, `fr_CA`, `fr_FR`, `de_DE`, `hi_IN`, `it_IT`, `pt_BR`, `es_ES`, `es_US` or `es_MX`. The default is `en_US`.
- For plot text, call [IMDb Plot Summary](/apis/imdb/title-plot-query). For cast and crew, call [IMDb Top Cast and Crew](/apis/imdb/title-top-cast-and-crew).

### Pricing

$0.007143 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/imdb/title-details-query.json`](../../../catalog/models/imdb/title-details-query.json) · Store page: https://www.sandbase.ai/model/imdb/title-details-query
