# IMDb User Reviews Summary API: pricing, parameters and code examples

`imdb/title-user-reviews-summary-query` · data API · IMDb · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.007143 per call (free daily quota) · **Modes:** sync

Get the IMDb user-reviews summary for a title ID using selected language and country preferences. Use it to review audience reception or support title comparison and research.

## Pricing

- **$0.007143 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "imdb/title-user-reviews-summary-query", "id": "tt0111161"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('imdb/title-user-reviews-summary-query', {'id': 'tt0111161'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("imdb/title-user-reviews-summary-query", {
  "id": "tt0111161"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "imdb/title-user-reviews-summary-query", sandbase.Params{
	"id": "tt0111161",
})
```

Same call via the path form: `POST /v1/api/imdb/title-user-reviews-summary-query` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string | yes | The IMDb title identifier in tt<digits> format.  |
| `languageCountry` | string |  | Language and country preferences. one of: `en_US`, `fr_CA`, `fr_FR`, `de_DE`, `hi_IN`, `it_IT`, `pt_BR`, `es_ES`, `es_US`, `es_MX`; default `"en_US"` |

## Details

Returns the IMDb aggregate rating and a short list of featured user reviews for one title. Each review includes the author, the author's rating, helpfulness votes, language and submission date. The input is an IMDb title ID in `tt<digits>` format.

### Use cases

- Show the current IMDb rating next to a title in a catalog or watchlist.
- Compare how helpful voters rated the top reviews of two films.
- Find the most up-voted reviews of a title for audience reception research.
- Filter out spoiler reviews before displaying review snippets.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/imdb/title-user-reviews-summary-query" \
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
    "canRate": {
      "isRatable": true
    },
    "featuredReviews": {
      "edges": [
        {
          "node": {
            "__typename": "Review",
            "author": {
              "id": "ur16749093",
              "nickName": "nowego"
            },
            "authorRating": 10,
            "helpfulness": {
              "__typename": "ReviewHelpfulness",
              "downVotes": 37,
              "score": 0.8510370348456942,
              "upVotes": 297
            },
            "id": "rw4203332",
            "language": "en-US",
            "spoiler": false,
            "submissionDate": "2018-06-15"
          }
        }
      ]
    },
    "id": "tt0111161",
    "ratingsSummary": {
      "aggregateRating": 9.3
    }
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `title.id` | The IMDb title ID that the summary belongs to. |
| `title.ratingsSummary.aggregateRating` | The overall IMDb user rating for the title. The sample value is `9.3`. |
| `title.canRate.isRatable` | Shows whether users can rate this title. |
| `title.featuredReviews.edges[].node.id` | The review ID, such as `rw4203332`. |
| `title.featuredReviews.edges[].node.author.id / title.featuredReviews.edges[].node.author.nickName` | The reviewer's user ID and display name. |
| `title.featuredReviews.edges[].node.authorRating` | The rating the reviewer gave the title. It is `null` when the reviewer left no rating. |
| `title.featuredReviews.edges[].node.helpfulness.upVotes / title.featuredReviews.edges[].node.helpfulness.downVotes` | How many readers marked the review as helpful or not helpful. |
| `title.featuredReviews.edges[].node.helpfulness.score` | A helpfulness score between 0 and 1 for the review. A higher value means more positive votes. |
| `title.featuredReviews.edges[].node.spoiler` | Is `true` when the review is marked as containing spoilers. |
| `title.featuredReviews.edges[].node.language / title.featuredReviews.edges[].node.submissionDate` | The review language code, such as `en-US`, and the date it was submitted in `YYYY-MM-DD` format. |

### Notes

- Take the `id` from an IMDb title URL or from another title API. It starts with `tt` followed by digits.
- `languageCountry` accepts `en_US`, `fr_CA`, `fr_FR`, `de_DE`, `hi_IN`, `it_IT`, `pt_BR`, `es_ES`, `es_US` or `es_MX`. The default is `en_US`.
- The response holds only a few featured reviews and no review text. Use the review `id` to match entries on your side.
- For professional reviews, call [IMDb Critics Review Summary](/apis/imdb/title-critics-review-summary-query). For title metadata, call [IMDb Base Info](/apis/imdb/title-base-query).

### Pricing

$0.007143 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/imdb/title-user-reviews-summary-query.json`](../../../catalog/models/imdb/title-user-reviews-summary-query.json) · Store page: https://www.sandbase.ai/model/imdb/title-user-reviews-summary-query
