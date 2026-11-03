# Y Combinator Search Companies API: pricing, parameters and code examples

`ycombinator/search-companies` · data API · Y Combinator · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Search and filter the YC company directory via Algolia. Returns paginated results with company metadata including name, batch, industry, team size, and hiring status.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "ycombinator/search-companies"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('ycombinator/search-companies', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("ycombinator/search-companies", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "ycombinator/search-companies", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/ycombinator/search-companies` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number (0-indexed). range -9007199254740991–9007199254740991 |
| `batch` | string |  | Filter by YC batch name (e.g. 'Winter 2024', 'Summer 2023').  |
| `limit` | integer |  | Number of results per page. range -9007199254740991–9007199254740991 |
| `query` | string |  | Search keyword to match against company name, description, and tags.  |
| `industry` | string |  | Filter by industry (e.g. 'Fintech', 'B2B', 'Healthcare').  |
| `is_hiring` | string |  | Filter by hiring status. Accepts 'true' or 'false'.  |
| `top_company` | string |  | Filter for YC top companies. Accepts 'true' or 'false'.  |

## Details

Returns a page of companies from the Y Combinator directory, with name, batch, industry, tags, team size and hiring status for each. All inputs are optional. Pass `query`, `batch`, `industry`, `is_hiring` or `top_company` to narrow the list.

### Use cases

- Build a list of companies from one batch, such as `Summer 2023`, for market research.
- Find fintech companies that are hiring and have a large `team_size`.
- Search by keyword to find Y Combinator companies in a niche, such as crypto or marketplaces.
- Pull company websites and one-line descriptions to seed a lead list.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/ycombinator/search-companies" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `batch` | string | No | Filter by YC batch name (e.g. 'Winter 2024', 'Summer 2023'). |
| `industry` | string | No | Filter by industry (e.g. 'Fintech', 'B2B', 'Healthcare'). |
| `is_hiring` | string | No | Filter by hiring status. Accepts 'true' or 'false'. |
| `limit` | integer | No | Number of results per page. |
| `page` | integer | No | Page number (0-indexed). |
| `query` | string | No | Search keyword to match against company name, description, and tags. |
| `top_company` | string | No | Filter for YC top companies. Accepts 'true' or 'false'. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "exhaustive": {
      "nbHits": true,
      "typo": true
    },
    "exhaustiveNbHits": true,
    "exhaustiveTypo": true,
    "extensions": {
      "queryCategorization": {}
    },
    "hits": [
      {
        "_highlightResult": {
          "all_locations": {
            "matchLevel": "none",
            "matchedWords": [],
            "value": "San Francisco, CA, USA"
          },
          "industries": [
            {
              "matchLevel": "none",
              "matchedWords": [],
              "value": "Consumer"
            }
          ],
          "long_description": {
            "matchLevel": "none",
            "matchedWords": [],
            "value": "Founded in 2013, DoorDash is a San Francisco-based technology company passionate…"
          },
          "name": {
            "matchLevel": "none",
            "matchedWords": [],
            "value": "DoorDash"
          },
          "one_liner": {
            "matchLevel": "none",
            "matchedWords": [],
            "value": "Restaurant delivery."
          },
          "tags": [
            {
              "matchLevel": "none",
              "matchedWords": [],
              "value": "Marketplace"
            }
          ],
          "website": {
            "matchLevel": "none",
            "matchedWords": [],
            "value": "http://doordash.com"
          }
        },
        "all_locations": "San Francisco, CA, USA",
        "app_answers": null,
        "app_video_public": false,
        "batch": "Summer 2013",
        "demo_day_video_public": false,
        "former_names": [],
        "id": 531,
        "industries": [
          "Consumer"
        ],
        "industry": "Consumer",
        "isHiring": true,
        "launched_at": 1367523459
      }
    ],
    "hitsPerPage": 20,
    "nbHits": 6362,
    "nbPages": 50,
    "page": 0,
    "params": "x-algolia-application-id=45BWZJ1SGC&x-algolia-api-key=MjQwNDk2YTE0YjMzMjQ2ZGM0NG…",
    "processingTimeMS": 3,
    "processingTimingsMS": {
      "_request": {
        "roundTrip": 19
      },
      "afterFetch": {
        "format": {
          "highlighting": 1,
          "total": 2
        }
      },
      "extensions": 2,
      "total": 3
    }
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.hits[].name` | Company name. |
| `data.hits[].slug` | URL-style identifier for the company. Use it to look up the company elsewhere. |
| `data.hits[].one_liner / data.hits[].long_description` | A short tagline and a longer description of the company. The long text can be cut off. |
| `data.hits[].batch` | The Y Combinator batch the company joined, for example `Summer 2013`. |
| `data.hits[].industry / data.hits[].industries[] / data.hits[].subindustry` | Main industry, the full list of industries, and a combined `Industry -> Sub-industry` label. |
| `data.hits[].tags[]` | Topic tags for the company, such as `Marketplace` or `Crypto / Web3`. |
| `data.hits[].team_size` | Number of people on the team. |
| `data.hits[].isHiring / data.hits[].top_company` | Boolean flags. `isHiring` shows whether the company is hiring. `top_company` marks Y Combinator top companies. |
| `data.hits[].stage / data.hits[].status` | Company stage (for example `Growth`) and status (for example `Public`). |
| `data.hits[].website / data.hits[].all_locations` | Company website URL and its locations as one text string. |
| `data.nbHits / data.nbPages / data.page / data.hitsPerPage` | Total matching companies, total pages, the current 0-indexed page, and the page size. |

### Notes

- Use `page` (0-indexed) and `limit` to move through results. Compare `data.page` with `data.nbPages` to know when to stop.
- `launched_at` is a Unix timestamp in seconds. `id` and `objectID` identify the company inside the directory.
- Ignore the `_highlightResult` and `tags_highlighted` fields unless you need match highlighting for a `query`.
- For full details on one company, call [Y Combinator Company](/apis/ycombinator/company) with its `slug`. For open roles, use [Y Combinator Search Jobs](/apis/ycombinator/search-jobs).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/ycombinator/search-companies.json`](../../../catalog/models/ycombinator/search-companies.json) · Store page: https://www.sandbase.ai/model/ycombinator/search-companies
