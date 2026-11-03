# IMDb Top Cast and Crew API: pricing, parameters and code examples

`imdb/title-top-cast-and-crew` · data API · IMDb · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.007143 per call (free daily quota) · **Modes:** sync

Get IMDb top cast and crew information for a title ID using selected language and country preferences. Use it to research principal talent or enrich title credits.

## Pricing

- **$0.007143 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "imdb/title-top-cast-and-crew", "id": "tt0111161"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('imdb/title-top-cast-and-crew', {'id': 'tt0111161'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("imdb/title-top-cast-and-crew", {
  "id": "tt0111161"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "imdb/title-top-cast-and-crew", sandbase.Params{
	"id": "tt0111161",
})
```

Same call via the path form: `POST /v1/api/imdb/title-top-cast-and-crew` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string | yes | The IMDb title identifier in tt<digits> format.  |
| `languageCountry` | string |  | Language and country preferences. one of: `en_US`, `fr_CA`, `fr_FR`, `de_DE`, `hi_IN`, `it_IT`, `pt_BR`, `es_ES`, `es_US`, `es_MX`; default `"en_US"` |

## Details

Returns the top cast and crew credits for an IMDb title. It needs an IMDb title ID in `tt<digits>` format, such as `tt0111161`, and accepts an optional `languageCountry` value.

### Use cases

- Show the lead actors and their character names on a movie detail page.
- Collect IMDb name IDs for the cast of a title, then use them to look up the same people elsewhere.
- Pull profile photo URLs and sizes to build a cast gallery for a title.
- Check how many credits a title lists in total before you decide how deep to go into its cast.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/imdb/title-top-cast-and-crew" \
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
    "credits": {
      "__typename": "CreditConnection",
      "edges": [
        {
          "node": {
            "__typename": "Cast",
            "characters": [
              {
                "id": "Captain Hadley",
                "name": "Captain Hadley"
              }
            ],
            "name": {
              "__typename": "Name",
              "id": "nm0000317",
              "nameText": {
                "text": "Clancy Brown"
              },
              "primaryImage": {
                "__typename": "Image",
                "height": 2048,
                "id": "rm1769979648",
                "url": "https://m.media-amazon.com/images/M/MV5BMTUxODY3NjAzMF5BMl5BanBnXkFtZTcwMTQ5MjYw…",
                "width": 1418
              }
            }
          }
        }
      ],
      "total": 556
    },
    "id": "tt0111161",
    "principalCredits": [
      {
        "credits": [
          {
            "__typename": "Crew"
          }
        ]
      }
    ],
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
| `title.id` | The IMDb title ID that the credits belong to. |
| `title.titleType.text / title.titleType.id` | The type of the title, such as `Movie` and `movie`. |
| `title.titleType.isSeries / title.titleType.canHaveEpisodes / title.titleType.isEpisode` | Flags that tell you whether the title is a series, can have episodes, or is an episode. |
| `title.principalCredits[].credits[]` | The principal credits, grouped in a list of blocks. Each credit has a `__typename` of `Cast` or `Crew`. In this response the `Crew` entries hold only `__typename`, and the `Cast` entries hold the full details. |
| `title.principalCredits[].credits[].name.nameText.text` | The full name of a principal cast member. |
| `title.principalCredits[].credits[].characters[].name` | The character that the principal cast member plays. |
| `title.credits.edges[].node.name.nameText.text` | The name of a person in the wider cast list. |
| `title.credits.edges[].node.name.id` | The IMDb name ID of the person, in `nm<digits>` format. |
| `title.credits.edges[].node.characters[].name` | The character that this cast member plays. |
| `title.credits.edges[].node.name.primaryImage.url / height / width` | The URL of the person's main photo, with its height and width in pixels as given by the values. |
| `title.credits.total` | The total number of credits for the title. The `edges` list holds only part of them. |

### Notes

- Find the title ID in the IMDb page URL, for example `tt0111161` in `imdb.com/title/tt0111161/`.
- `languageCountry` accepts `en_US`, `fr_CA`, `fr_FR`, `de_DE`, `hi_IN`, `it_IT`, `pt_BR`, `es_ES`, `es_US` and `es_MX`. The default is `en_US`.
- Call [IMDb Base Info](/apis/imdb/title-base-query) or [IMDb Plot Summary](/apis/imdb/title-plot-query) with the same ID for more details on the title.

### Pricing

$0.007143 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/imdb/title-top-cast-and-crew.json`](../../../catalog/models/imdb/title-top-cast-and-crew.json) · Store page: https://www.sandbase.ai/model/imdb/title-top-cast-and-crew
