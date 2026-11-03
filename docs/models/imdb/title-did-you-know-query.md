# IMDb 'Did You Know' Insights API: pricing, parameters and code examples

`imdb/title-did-you-know-query` · data API · IMDb · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.007143 per call (free daily quota) · **Modes:** sync

Get IMDb 'Did You Know' information for a title ID using selected language and country preferences. Use it to research title trivia and add editorial context.

## Pricing

- **$0.007143 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "imdb/title-did-you-know-query", "id": "tt0111161"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('imdb/title-did-you-know-query', {'id': 'tt0111161'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("imdb/title-did-you-know-query", {
  "id": "tt0111161"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "imdb/title-did-you-know-query", sandbase.Params{
	"id": "tt0111161",
})
```

Same call via the path form: `POST /v1/api/imdb/title-did-you-know-query` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string | yes | The IMDb title identifier in tt<digits> format.  |
| `languageCountry` | string |  | Language and country preferences. one of: `en_US`, `fr_CA`, `fr_FR`, `de_DE`, `hi_IN`, `it_IT`, `pt_BR`, `es_ES`, `es_US`, `es_MX`; default `"en_US"` |

## Details

Returns IMDb trivia, goofs, quotes, crazy credits and soundtrack entries for one title. It needs an IMDb title ID in `tt<digits>` format, such as `tt0111161`, and takes an optional `languageCountry` value.

### Use cases

- Pull trivia and quotes for a film to write editorial copy or a fan page.
- Rank trivia by `usersInterested` to show the most liked facts first.
- List goofs by category to build a continuity-error section for a movie.
- Show soundtrack credits next to a title in a music discovery app.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/imdb/title-did-you-know-query" \
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
    "crazyCredits": {
      "edges": [
        {
          "node": {
            "__typename": "CrazyCredit",
            "id": "cz0007591",
            "interestScore": {
              "__typename": "InterestScore",
              "usersInterested": 221,
              "usersVoted": 226
            },
            "text": {
              "plainText": "The man who cried and was beaten when Andy first arrived is listed and credited …"
            }
          }
        }
      ]
    },
    "goofs": {
      "edges": [
        {
          "node": {
            "__typename": "Goof",
            "category": {
              "id": "anachronism",
              "text": "Anachronisms"
            },
            "id": "gf1546878",
            "interestScore": {
              "__typename": "InterestScore",
              "usersInterested": 124,
              "usersVoted": 133
            },
            "isSpoiler": false,
            "text": {
              "plainText": "Circa 1963, Heywood is shown listening to the record \"24 of Hank Williams' Great…"
            }
          }
        }
      ]
    },
    "goofsCount": {
      "total": 113
    },
    "originalTitleText": {
      "isOriginalTitle": true,
      "text": "The Shawshank Redemption"
    },
    "quotes": {
      "edges": [
        {
          "node": {
            "__typename": "TitleQuote",
            "id": "qt0470748",
            "interestScore": {
              "__typename": "InterestScore",
              "usersInterested": 1597,
              "usersVoted": 1608
            },
            "isSpoiler": false,
            "lines": [
              {
                "characters": [
                  {
                    "character": "Andy Dufresne",
                    "name": {
                      "id": "nm0000209"
                    }
                  }
                ],
                "stageDirection": "to Red",
                "text": "I guess it comes down to a simple choice, really. Get busy living, or get busy d…"
              }
            ]
          }
        }
      ]
    },
    "quotesCount": {
      "total": 119
    },
    "soundtrack": {
      "edges": [
        {
          "node": {
            "__typename": "Track",
            "comments": [
              {
                "plainText": "by Jack Lawrence"
              }
            ],
            "id": "sn0691810",
            "text": "If I Didn't Care"
          }
        }
      ]
    },
    "titleText": {
      "isOriginalTitle": true,
      "text": "The Shawshank Redemption"
    },
    "trivia": {
      "edges": [
        {
          "node": {
            "__typename": "TitleTrivia",
            "category": {
              "id": "uncategorized"
            },
            "id": "tr1008159",
            "interestScore": {
              "__typename": "InterestScore",
              "usersInterested": 4399,
              "usersVoted": 4417
            },
            "isSpoiler": false,
            "relatedNames": null,
            "text": {
              "plainText": "Andy and Red's opening chat in the prison yard, in which Red is throwing a baseb…"
            },
            "trademark": null
          }
        }
      ]
    },
    "triviaCount": {
      "total": 244
    }
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `title.trivia.edges[].node.text.plainText` | The text of one trivia entry. |
| `title.trivia.edges[].node.isSpoiler` | Whether the trivia entry is marked as a spoiler. Quotes and goofs carry the same flag. |
| `title.goofs.edges[].node.text.plainText` | The text of one goof. |
| `title.goofs.edges[].node.category.text` | The goof category label, such as `Anachronisms`. The matching `category.id` is a lowercase code. |
| `title.quotes.edges[].node.lines[]` | The lines of one quote. Each line has `text`, an optional `stageDirection`, and `characters[]` with the `character` name and the name `id`. |
| `title.crazyCredits.edges[].node.text.plainText` | The text of one crazy credit, which is an odd or notable detail in the end credits. |
| `title.soundtrack.edges[].node.text / title.soundtrack.edges[].node.comments[].plainText` | The track title and its credit notes, such as composer, performer or label. |
| `usersInterested / usersVoted` | Under each `interestScore`. `usersInterested` is the number of voters who found the entry interesting, out of `usersVoted` total voters. |
| `title.triviaCount.total / title.goofsCount.total / title.quotesCount.total` | The total number of trivia entries, goofs and quotes for the title. The `edges` lists hold only a part of them. |
| `title.titleText.text / title.originalTitleText.text` | The title in the requested language and the original title. |

### Notes

- Take the title ID from the IMDb title URL, or from another title API such as [IMDb Base Info](/apis/imdb/title-base-query).
- Each entry has its own ID, for example `tr1008159` for trivia, `gf1546878` for goofs, `qt0470748` for quotes and `cz0007591` for crazy credits.
- Quote `characters[].name.id` uses the `nm<digits>` format, which is the IMDb name ID.
- Compare the `total` counts with the number of `edges` returned to see how many entries are not in the response.

### Pricing

$0.007143 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/imdb/title-did-you-know-query.json`](../../../catalog/models/imdb/title-did-you-know-query.json) · Store page: https://www.sandbase.ai/model/imdb/title-did-you-know-query
