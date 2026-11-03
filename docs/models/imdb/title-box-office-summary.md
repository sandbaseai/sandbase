# IMDb Box Office Summary API: pricing, parameters and code examples

`imdb/title-box-office-summary` · data API · IMDb · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.007143 per call (free daily quota) · **Modes:** sync

Get the IMDb box-office summary for a title ID using selected language and country preferences. Use it to research reported theatrical performance or compare titles.

## Pricing

- **$0.007143 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "imdb/title-box-office-summary", "id": "tt0111161"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('imdb/title-box-office-summary', {'id': 'tt0111161'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("imdb/title-box-office-summary", {
  "id": "tt0111161"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "imdb/title-box-office-summary", sandbase.Params{
	"id": "tt0111161",
})
```

Same call via the path form: `POST /v1/api/imdb/title-box-office-summary` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string | yes | The IMDb title identifier in tt<digits> format.  |
| `languageCountry` | string |  | Language and country preferences. one of: `en_US`, `fr_CA`, `fr_FR`, `de_DE`, `hi_IN`, `it_IT`, `pt_BR`, `es_ES`, `es_US`, `es_MX`; default `"en_US"` |

## Details

Returns the IMDb box-office summary for one title: budget, domestic gross, worldwide gross, and opening weekend gross. It needs an IMDb title ID in `tt<digits>` format, such as `tt0111161`.

### Use cases

- Compare the budget of a film with its worldwide gross to see how it performed at the box office.
- Look up the opening weekend gross and date for a film to compare launches.
- Add domestic and worldwide gross figures to a movie database or report.
- Check the release year and title text of a film alongside its box-office numbers.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/imdb/title-box-office-summary" \
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
    "budget": {
      "totalBudget": {
        "__typename": "Money",
        "amount": 25000000,
        "currency": "USD"
      }
    },
    "domesticGross": {
      "__typename": "BoxOfficeGross",
      "total": {
        "__typename": "Money",
        "amount": 28767189,
        "currency": "USD"
      }
    },
    "id": "tt0111161",
    "openingWeekendGrosses": {
      "edges": [
        {
          "node": {
            "gross": {
              "__typename": "BoxOfficeGross",
              "total": {
                "__typename": "Money",
                "amount": 727327,
                "currency": "USD"
              }
            },
            "weekendStartDate": "1994-09-23"
          }
        }
      ],
      "total": 1
    },
    "originalTitleText": {
      "isOriginalTitle": true,
      "text": "The Shawshank Redemption"
    },
    "releaseYear": {
      "year": 1994
    },
    "titleText": {
      "isOriginalTitle": true,
      "text": "The Shawshank Redemption"
    },
    "worldwideGross": {
      "__typename": "BoxOfficeGross",
      "total": {
        "__typename": "Money",
        "amount": 29425588,
        "currency": "USD"
      }
    }
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `title.id` | The IMDb title ID that the figures belong to. |
| `title.titleText.text / title.originalTitleText.text` | The display title and the original title. `isOriginalTitle` is `true` when the title shown is the original one. |
| `title.releaseYear.year` | The year the title was released. |
| `title.budget.totalBudget.amount` | The reported production budget. `currency` gives the currency code, such as `USD`. |
| `title.domesticGross.total.amount` | The reported domestic box-office gross, with its currency in `currency`. |
| `title.worldwideGross.total.amount` | The reported worldwide box-office gross, with its currency in `currency`. |
| `title.openingWeekendGrosses.edges[].node.gross.total.amount` | The gross for an opening weekend, with its currency in `currency`. |
| `title.openingWeekendGrosses.edges[].node.weekendStartDate` | The start date of that opening weekend, in `YYYY-MM-DD` format. |
| `title.openingWeekendGrosses.total` | The number of opening weekend entries for the title. |

### Notes

- Find the title ID in the IMDb page URL for a title. It looks like `tt0111161`.
- `languageCountry` is optional and defaults to `en_US`. Other values are `fr_CA`, `fr_FR`, `de_DE`, `hi_IN`, `it_IT`, `pt_BR`, `es_ES`, `es_US`, and `es_MX`.
- For more on the same title, call [IMDb Details](/apis/imdb/title-details-query) or [IMDb Base Info](/apis/imdb/title-base-query).

### Pricing

$0.007143 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/imdb/title-box-office-summary.json`](../../../catalog/models/imdb/title-box-office-summary.json) · Store page: https://www.sandbase.ai/model/imdb/title-box-office-summary
