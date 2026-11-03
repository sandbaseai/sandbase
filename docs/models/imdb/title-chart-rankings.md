# IMDb Chart Rankings API: pricing, parameters and code examples

`imdb/title-chart-rankings` · data API · IMDb · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.007143 per call (free daily quota) · **Modes:** sync

Get the IMDb Top 250 movie or TV chart selected by ranking type using language and country preferences. Use it to monitor chart positions or compare highly ranked titles.

## Pricing

- **$0.007143 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "imdb/title-chart-rankings", "rankingsChartType": "TOP_250"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('imdb/title-chart-rankings', {'rankingsChartType': 'TOP_250'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("imdb/title-chart-rankings", {
  "rankingsChartType": "TOP_250"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "imdb/title-chart-rankings", sandbase.Params{
	"rankingsChartType": "TOP_250",
})
```

Same call via the path form: `POST /v1/api/imdb/title-chart-rankings` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `languageCountry` | string |  | Language and country preferences. one of: `en_US`, `fr_CA`, `fr_FR`, `de_DE`, `hi_IN`, `it_IT`, `pt_BR`, `es_ES`, `es_US`, `es_MX`; default `"en_US"` |
| `rankingsChartType` | string | yes | Type of rankings chart to retrieve. one of: `TOP_250`, `TOP_250_TV` |

## Details

Returns the IMDb Top 250 chart for movies or TV shows. Each entry has the title ID, original title, rating, vote count, rank, poster image and release date. The only required input is `rankingsChartType`, with an optional `languageCountry`.

### Use cases

- Track how a title's rank in the Top 250 changes from one day to the next.
- Build a list of the highest rated movies with poster images and release years.
- Compare `chartRating` and `aggregateRating` across top titles to see how votes shape the chart.
- Collect title IDs from the TV chart to feed into other title lookups.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/imdb/title-chart-rankings" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"rankingsChartType": "TOP_250"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `rankingsChartType` | string | Yes | Type of rankings chart to retrieve. |
| `languageCountry` | string | No | Language and country preferences. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "titleChartRankings": {
    "edges": [
      {
        "node": {
          "chartRating": 9.240896480966825,
          "chartVoteCount": 3260964,
          "item": {
            "__typename": "Title",
            "canRate": {
              "isRatable": true
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
            "ratingsSummary": {
              "aggregateRating": 9.3,
              "topRanking": {
                "rank": 1
              },
              "voteCount": 3260964
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
            }
          }
        }
      }
    ]
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `titleChartRankings.edges[].node.item.id` | IMDb title ID, such as `tt0111161`. Use it to look up the same title in other IMDb APIs. |
| `titleChartRankings.edges[].node.item.originalTitleText.text` | Original title of the movie or show. |
| `titleChartRankings.edges[].node.item.ratingsSummary.topRanking.rank` | Position of the title on the requested chart. `1` is the top entry. |
| `titleChartRankings.edges[].node.item.ratingsSummary.aggregateRating` | Rating of the title, shown with one decimal place, for example `9.3`. |
| `titleChartRankings.edges[].node.chartRating` | Unrounded rating value attached to the chart entry. |
| `titleChartRankings.edges[].node.chartVoteCount / titleChartRankings.edges[].node.item.ratingsSummary.voteCount` | Number of votes counted for the title. |
| `titleChartRankings.edges[].node.item.releaseYear.year` | Year the title was first released. `endYear` is `null` for single releases like films. |
| `titleChartRankings.edges[].node.item.releaseDate.year / month / day` | Full release date, with the release country in `releaseDate.country.id`. |
| `titleChartRankings.edges[].node.item.primaryImage.url` | Link to the main poster image. `width` and `height` give its size. |

### Notes

- Set `rankingsChartType` to `TOP_250` for the movie chart or `TOP_250_TV` for the TV chart.
- `languageCountry` accepts values like `en_US`, `fr_FR`, `de_DE` and `es_MX`. It defaults to `en_US`.
- Pass the title `id` to [IMDb Base Info](/apis/imdb/title-base-query) or [IMDb Details](/apis/imdb/title-details-query) to get more about a chart title.

### Pricing

$0.007143 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/imdb/title-chart-rankings.json`](../../../catalog/models/imdb/title-chart-rankings.json) · Store page: https://www.sandbase.ai/model/imdb/title-chart-rankings
