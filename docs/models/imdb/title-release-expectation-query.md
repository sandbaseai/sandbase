# IMDb Release Expectation API: pricing, parameters and code examples

`imdb/title-release-expectation-query` · data API · IMDb · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.007143 per call (free daily quota) · **Modes:** sync

Get IMDb release-expectation information for a title ID using selected language and country preferences. Use it to monitor a title's release context or support release-planning research.

## Pricing

- **$0.007143 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "imdb/title-release-expectation-query", "id": "tt0111161"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('imdb/title-release-expectation-query', {'id': 'tt0111161'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("imdb/title-release-expectation-query", {
  "id": "tt0111161"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "imdb/title-release-expectation-query", sandbase.Params{
	"id": "tt0111161",
})
```

Same call via the path form: `POST /v1/api/imdb/title-release-expectation-query` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string | yes | The IMDb title identifier in tt<digits> format.  |
| `languageCountry` | string |  | Language and country preferences. one of: `en_US`, `fr_CA`, `fr_FR`, `de_DE`, `hi_IN`, `it_IT`, `pt_BR`, `es_ES`, `es_US`, `es_MX`; default `"en_US"` |

## Details

Returns release dates, production status, and basic title info for one IMDb title. It needs an IMDb title ID in `tt<digits>` format, such as `tt0111161`. An optional `languageCountry` value sets the language and country preference.

### Use cases

- Check the current production stage of a title, such as `Released`, before adding it to a tracking list.
- Compare wide release dates across countries to plan a regional launch calendar.
- List festival and premiere screenings with their cities and dates for a film history timeline.
- Pull the title name, type, and poster image to label release records in a dashboard.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/imdb/title-release-expectation-query" \
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
    "episodes": null,
    "excludeWideReleaseDates": {
      "edges": [
        {
          "node": {
            "__typename": "ReleaseDate",
            "attributes": [
              {
                "id": "Toronto International Film Festival",
                "text": "Toronto International Film Festival"
              }
            ],
            "country": {
              "id": "CA"
            },
            "day": 10,
            "displayableProperty": {
              "qualifiersInMarkdownList": [
                {
                  "expandedMarkdown": "Toronto International Film Festival"
                }
              ]
            },
            "month": 9,
            "restriction": null,
            "year": 1994
          }
        }
      ]
    },
    "id": "tt0111161",
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
    "productionStatus": {
      "__typename": "ProductionStatusDetails",
      "announcements": null,
      "currentProductionStage": {
        "id": "released",
        "text": "Released"
      },
      "productionStatusHistory": [
        {
          "comment": {
            "text": "Derived from earliest release of 1994-09-10 (CA)"
          },
          "date": "1994-09-10",
          "status": {
            "id": "released",
            "text": "Released"
          }
        }
      ]
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
    "titleText": {
      "isOriginalTitle": true,
      "text": "The Shawshank Redemption"
    },
    "titleType": {
      "__typename": "TitleType",
      "canHaveEpisodes": false,
      "categories": [
        {
          "id": "movie",
          "text": "Movie",
          "value": "movie"
        }
      ],
      "displayableProperty": {
        "value": {
          "plainText": ""
        }
      },
      "id": "movie",
      "isEpisode": false,
      "isSeries": false,
      "text": "Movie"
    },
    "wideReleaseDates": {
      "edges": [
        {
          "node": {
            "__typename": "ReleaseDate",
            "attributes": [],
            "country": {
              "id": "CA"
            },
            "day": 23,
            "displayableProperty": {
              "qualifiersInMarkdownList": null
            },
            "month": 9,
            "restriction": null,
            "year": 1994
          }
        }
      ]
    }
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `title.id` | The IMDb title ID that was requested. |
| `title.titleText.text / title.originalTitleText.text` | The display title and the original title. `isOriginalTitle` shows whether the text is the original title. |
| `title.titleType.text` | The kind of title, such as `Movie`. `isSeries` and `isEpisode` show whether it is a series or an episode. |
| `title.releaseDate.year / title.releaseDate.month / title.releaseDate.day` | The main release date for the title, split into year, month, and day. `country.id` gives the country code for that date. |
| `title.releaseYear.year` | The release year of the title. `endYear` is `null` for this movie. |
| `title.productionStatus.currentProductionStage.text` | The current production stage, such as `Released`. |
| `title.productionStatus.productionStatusHistory[].date / title.productionStatus.productionStatusHistory[].comment.text` | The date a status began and a note on how it was set. The note here says the status comes from the earliest release. |
| `title.wideReleaseDates.edges[].node.country.id` | The country code of a wide release. Read the date from `year`, `month`, and `day` in the same `node`. |
| `title.excludeWideReleaseDates.edges[].node.attributes[].text` | Details about releases outside the wide list, such as a festival name, a premiere, or a city. |
| `title.primaryImage.url` | The URL of the main poster image. `width` and `height` give its size. |

### Notes

- Pass the title ID in `id`. It looks like `tt0111161`.
- Release dates come as separate `year`, `month`, and `day` numbers, not as one date string. Only `productionStatusHistory[].date` uses the `YYYY-MM-DD` format.
- For fuller title data, call [IMDb Details](/apis/imdb/title-details-query) or [IMDb Base Info](/apis/imdb/title-base-query) next.

### Pricing

$0.007143 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/imdb/title-release-expectation-query.json`](../../../catalog/models/imdb/title-release-expectation-query.json) · Store page: https://www.sandbase.ai/model/imdb/title-release-expectation-query
