# IMDb Plot Summary API: pricing, parameters and code examples

`imdb/title-plot-query` · data API · IMDb · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.007143 per call (free daily quota) · **Modes:** sync

Get IMDb plot information for a title ID using selected language and country preferences. Use it to review a movie or series storyline or enrich title descriptions.

## Pricing

- **$0.007143 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "imdb/title-plot-query", "id": "tt0111161"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('imdb/title-plot-query', {'id': 'tt0111161'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("imdb/title-plot-query", {
  "id": "tt0111161"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "imdb/title-plot-query", sandbase.Params{
	"id": "tt0111161",
})
```

Same call via the path form: `POST /v1/api/imdb/title-plot-query` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string | yes | The IMDb title identifier in tt<digits> format.  |
| `languageCountry` | string |  | Language and country preferences. one of: `en_US`, `fr_CA`, `fr_FR`, `de_DE`, `hi_IN`, `it_IT`, `pt_BR`, `es_ES`, `es_US`, `es_MX`; default `"en_US"` |

## Details

Returns the plot summary for one IMDb title, plus the title type (such as movie). It needs an IMDb title ID in `tt<digits>` format, and you can pick a language and country with `languageCountry`.

### Use cases

- Show a short storyline on a movie page using the `title.plot.plotText.plainText` text.
- Fill in missing descriptions in a catalog of IMDb titles.
- Fetch plots in `fr_FR` or `es_MX` to show localized synopses.
- Check whether a title is a movie, series or episode before you decide how to display it.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/imdb/title-plot-query" \
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
    "id": "tt0111161",
    "plot": {
      "id": "po1124508",
      "plotText": {
        "plainText": "After a banker is sentenced to life in Shawshank Prison, he forms an unlikely fr…"
      }
    },
    "type": {
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
| `title.id` | The IMDb title ID that you requested, for example `tt0111161`. |
| `title.plot.id` | The ID of the plot entry that the API returned, in `po<digits>` format. |
| `title.plot.plotText.plainText` | The plot summary as plain text, with no markup. |
| `title.type.id / title.type.text` | The title type as an ID and as a display label. In the sample, both say movie. |
| `title.type.categories[].id / title.type.categories[].text / title.type.categories[].value` | The category the title belongs to, for example `movie` and `Movie`. |
| `title.type.isSeries / title.type.isEpisode / title.type.canHaveEpisodes` | Boolean flags that show whether the title is a series, is an episode, or can contain episodes. |

### Notes

- Find the title ID in the `tt<digits>` format in an IMDb title URL, or from other IMDb APIs such as [IMDb Base Info](/apis/imdb/title-base-query).
- `languageCountry` accepts `en_US`, `fr_CA`, `fr_FR`, `de_DE`, `hi_IN`, `it_IT`, `pt_BR`, `es_ES`, `es_US` and `es_MX`. The default is `en_US`.
- For cast, crew or other details of the same title, call [IMDb Top Cast and Crew](/apis/imdb/title-top-cast-and-crew) or [IMDb Details](/apis/imdb/title-details-query).

### Pricing

$0.007143 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/imdb/title-plot-query.json`](../../../catalog/models/imdb/title-plot-query.json) · Store page: https://www.sandbase.ai/model/imdb/title-plot-query
