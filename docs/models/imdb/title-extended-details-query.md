# IMDb Extended Details API: pricing, parameters and code examples

`imdb/title-extended-details-query` · data API · IMDb · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.007143 per call (free daily quota) · **Modes:** sync

Get extended IMDb details for a title ID using selected language and country preferences. Use it to enrich a title catalog or perform deeper research after a basic lookup.

## Pricing

- **$0.007143 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "imdb/title-extended-details-query", "id": "tt0111161"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('imdb/title-extended-details-query', {'id': 'tt0111161'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("imdb/title-extended-details-query", {
  "id": "tt0111161"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "imdb/title-extended-details-query", sandbase.Params{
	"id": "tt0111161",
})
```

Same call via the path form: `POST /v1/api/imdb/title-extended-details-query` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string | yes | The IMDb title identifier in tt<digits> format.  |
| `languageCountry` | string |  | Language and country preferences. one of: `en_US`, `fr_CA`, `fr_FR`, `de_DE`, `hi_IN`, `it_IT`, `pt_BR`, `es_ES`, `es_US`, `es_MX`; default `"en_US"` |

## Details

Returns extended IMDb details for one title: the title text, type, release date, runtime, poster image, and a list of credited people. It needs an IMDb title ID in `tt<digits>` format, and takes an optional `languageCountry` value.

### Use cases

- Add runtime, release year, and poster URL to a movie catalog that only stores IMDb IDs.
- Tell movies apart from series or episodes with `title.titleType` before you choose the next call.
- Build a director and writer list for a title, with a link to each person's IMDb name ID.
- Check the original title text against the localized title for a given `languageCountry`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/imdb/title-extended-details-query" \
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
    "credits": {
      "edges": [
        {
          "node": {
            "category": {
              "id": "director",
              "text": "Director"
            },
            "name": {
              "__typename": "Name",
              "id": "nm0001104",
              "nameText": {
                "text": "Frank Darabont"
              },
              "primaryImage": {
                "__typename": "Image",
                "height": 400,
                "id": "rm3402598144",
                "url": "https://m.media-amazon.com/images/M/MV5BNjk0MTkxNzQwOF5BMl5BanBnXkFtZTcwODM5OTMw…",
                "width": 322
              }
            }
          }
        }
      ]
    },
    "episodes": null,
    "id": "tt0111161",
    "isAdult": false,
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
    },
    "series": null,
    "titleText": {
      "isOriginalTitle": true,
      "text": "The Shawshank Redemption"
    }
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `title.id` | The IMDb title ID, for example `tt0111161`. |
| `title.titleText.text / title.originalTitleText.text` | The title as shown and the original title. `isOriginalTitle` tells you whether the shown title is the original one. |
| `title.titleType.id / title.titleType.text` | The type of title, such as `movie`. `isSeries` and `isEpisode` are booleans for quick checks. |
| `title.releaseDate.year / title.releaseDate.month / title.releaseDate.day` | The release date parts. `title.releaseDate.country.id` is the country code the date applies to, such as `US`. |
| `title.releaseYear.year / title.releaseYear.endYear` | The release year. `endYear` is `null` for a single movie. |
| `title.runtime.seconds` | The runtime as a number of seconds. A value of `8520` means 142 minutes. |
| `title.primaryImage.url` | The poster image URL. `width` and `height` give its pixel size. |
| `title.credits.edges[].node.category.text` | The credit role for the person, such as `Director` or `Writer`. |
| `title.credits.edges[].node.name.id / title.credits.edges[].node.name.nameText.text` | The IMDb name ID (`nm<digits>`) and the display name of the credited person. |
| `title.credits.edges[].node.name.primaryImage.url` | A photo URL for the credited person. |

### Notes

- The same person can appear more than once in `title.credits.edges[]` when they hold several roles. In the sample, Frank Darabont is listed as both director and writer.
- `title.episodes` and `title.series` are `null` for a movie.
- For a lighter lookup, call [IMDb Base Info](/apis/imdb/title-base-query). For the full cast and crew, call [IMDb Top Cast and Crew](/apis/imdb/title-top-cast-and-crew).
- For the story text, call [IMDb Plot Summary](/apis/imdb/title-plot-query).

### Pricing

$0.007143 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/imdb/title-extended-details-query.json`](../../../catalog/models/imdb/title-extended-details-query.json) · Store page: https://www.sandbase.ai/model/imdb/title-extended-details-query
