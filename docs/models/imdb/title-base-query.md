# IMDb Base Info API: pricing, parameters and code examples

`imdb/title-base-query` · data API · IMDb · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.007143 per call (free daily quota) · **Modes:** sync

Get base IMDb information for a title ID using selected language and country preferences. Use it to perform a lightweight title lookup or populate basic catalog context.

## Pricing

- **$0.007143 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "imdb/title-base-query", "id": "tt0111161"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('imdb/title-base-query', {'id': 'tt0111161'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("imdb/title-base-query", {
  "id": "tt0111161"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "imdb/title-base-query", sandbase.Params{
	"id": "tt0111161",
})
```

Same call via the path form: `POST /v1/api/imdb/title-base-query` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string | yes | The IMDb title identifier in tt<digits> format.  |
| `languageCountry` | string |  | Language and country preferences. one of: `en_US`, `fr_CA`, `fr_FR`, `de_DE`, `hi_IN`, `it_IT`, `pt_BR`, `es_ES`, `es_US`, `es_MX`; default `"en_US"` |

## Details

Returns basic IMDb data for one title: its name, poster image, release date, release year, and title type. It needs an IMDb title ID in `tt<digits>` format, such as `tt0111161`. An optional `languageCountry` value sets the language and country preferences.

### Use cases

- Show a title's name, poster, and release year on a catalog page from just its IMDb ID.
- Check whether an ID points to a movie or a series before you call episode or series APIs.
- Fetch a poster image URL and its pixel size to build a thumbnail grid.
- Read the US release date of a title to sort a watchlist.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/imdb/title-base-query" \
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
    }
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `title.id` | The IMDb title ID, for example `tt0111161`. |
| `title.titleText.text` | The title name shown for the selected language and country preferences. |
| `title.originalTitleText.text` | The title name in its original form. `isOriginalTitle` is `true` when it matches the displayed name. |
| `title.primaryImage.url` | URL of the main poster image. |
| `title.primaryImage.width / title.primaryImage.height` | Pixel size of the poster image. |
| `title.releaseDate.year / title.releaseDate.month / title.releaseDate.day` | Parts of the release date as numbers. In this example the date is 14 October 1994. |
| `title.releaseDate.country.id` | Country code the release date applies to, for example `US`. |
| `title.releaseYear.year / title.releaseYear.endYear` | Start year of the title and its end year. `endYear` is `null` here, as for a single movie. |
| `title.titleType.id / title.titleType.text` | Type of the title, for example `movie` and `Movie`. |
| `title.titleType.isSeries / title.titleType.isEpisode / title.titleType.canHaveEpisodes` | Flags that tell you whether the title is a series, an episode, or can have episodes. |

### Notes

- Find the title ID in an IMDb title URL. It starts with `tt` followed by digits.
- `languageCountry` accepts `en_US`, `fr_CA`, `fr_FR`, `de_DE`, `hi_IN`, `it_IT`, `pt_BR`, `es_ES`, `es_US`, and `es_MX`. The default is `en_US`.
- For more fields on the same title, call [IMDb Details](/apis/imdb/title-details-query) or [IMDb Plot Summary](/apis/imdb/title-plot-query).
- For cast and crew, call [IMDb Top Cast and Crew](/apis/imdb/title-top-cast-and-crew).

### Pricing

$0.007143 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/imdb/title-base-query.json`](../../../catalog/models/imdb/title-base-query.json) · Store page: https://www.sandbase.ai/model/imdb/title-base-query
