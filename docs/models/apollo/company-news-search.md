# Apollo News Articles Search API: pricing, parameters and code examples

`apollo/company-news-search` · data API · Apollo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01975 per call · **Modes:** sync

News Articles Search from Apollo. Returns the official Apollo API response unchanged.

## Pricing

- **$0.01975 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "apollo/company-news-search", "organization_ids[]": ["5d0a0fbff6512580bf33a120"]}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('apollo/company-news-search', {'organization_ids[]': ['5d0a0fbff6512580bf33a120']})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("apollo/company-news-search", {
  "organization_ids[]": [
    "5d0a0fbff6512580bf33a120"
  ]
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "apollo/company-news-search", sandbase.Params{
	"organization_ids[]": []any{"5d0a0fbff6512580bf33a120"},
})
```

Same call via the path form: `POST /v1/api/apollo/company-news-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | The page number of the Apollo data that you want to retrieve. Use this parameter in combination with the per_page parameter to make search results for navigable and improve the performance of the endpoint. Example: 4  |
| `per_page` | integer |  | The number of search results that should be returned for each page. Limiting the number of results per page improves the endpoint's performance. Use the page parameter to search the different pages of data. Example: 10  |
| `categories[]` | array |  | Filter your search to include only certain categories or sub-categories of news. Use the News search filter for companies within Apollo to uncover all possible categories and sub-categories. Examples: hires;…  |
| `published_at[max]` | string |  | Set the upper bound of the date range you want to search. Use this parameter in combination with the published_at[min] parameter. This date should fall after the published_at[min] date. The date should be formatted as…  |
| `published_at[min]` | string |  | Set the lower bound of the date range you want to search. Use this parameter in combination with the published_at[max] parameter. This date should fall before the published_at[max] date. The date should be formatted as…  |
| `organization_ids[]` | array | yes | The Apollo IDs for the companies you want to include in your search results. Each company in the Apollo database is assigned a unique ID. To find IDs, call the Organization Search endpoint and identify the values for…  |

## Details

Returns news articles about one or more companies, with title, snippet, source domain, URL, publish date and event categories. It needs at least one Apollo organization ID in `organization_ids[]`.

### Use cases

- Track launches, hires and funding news for a list of target accounts.
- Flag accounts with a recent valuation or investment story before a sales outreach.
- Build a news feed for a company by filtering on `categories[]` and a date range.
- Pull recent coverage of a competitor and read the source links.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/apollo/company-news-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"organization_ids[]": ["5d0a0fbff6512580bf33a120"], "per_page": 2}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `organization_ids[]` | array | Yes | The Apollo IDs for the companies you want to include in your search results. Each company in the Apollo database is assigned a unique ID. To find IDs, call the Organization Search endpoint and identify the values for org |
| `categories[]` | array | No | Filter your search to include only certain categories or sub-categories of news. Use the News search filter for companies within Apollo to uncover all possible categories and sub-categories. Examples: hires; investment;  |
| `page` | integer | No | The page number of the Apollo data that you want to retrieve. Use this parameter in combination with the per_page parameter to make search results for navigable and improve the performance of the endpoint. Example: 4 |
| `per_page` | integer | No | The number of search results that should be returned for each page. Limiting the number of results per page improves the endpoint's performance. Use the page parameter to search the different pages of data. Example: 10 |
| `published_at[max]` | string | No | Set the upper bound of the date range you want to search. Use this parameter in combination with the published_at[min] parameter. This date should fall after the published_at[min] date. The date should be formatted as YY |
| `published_at[min]` | string | No | Set the lower bound of the date range you want to search. Use this parameter in combination with the published_at[max] parameter. This date should fall before the published_at[max] date. The date should be formatted as Y |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "news_articles": [
    {
      "domain": "aurav.ae",
      "event_categories": [
        "launches"
      ],
      "id": "6ae7a6f3cb0a690020c9d8b8",
      "organization_ids": [
        "5d0a0fbff6512580bf33a120"
      ],
      "published_at": "2026-11-01T00:00:00.000+00:00",
      "snippet": "Stripe announced Link Balance, a feature that adds a funded source to its existi…",
      "title": "Stripe launches Link Balance to fund autonomous AI agents.",
      "url": "https://aurav.ae/fintech/stripe-launches-link-balance-to-fund-autonomous-ai-agen…"
    }
  ],
  "pagination": {
    "page": 1,
    "per_page": 2,
    "total_entries": 976,
    "total_pages": 488
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `news_articles[].title` | Headline of the article. |
| `news_articles[].snippet` | Short text excerpt from the article. Long snippets end with an ellipsis. |
| `news_articles[].url / news_articles[].domain` | Link to the article and the website that published it. |
| `news_articles[].published_at` | Publish date and time as an ISO 8601 timestamp. |
| `news_articles[].event_categories` | List of event labels for the article, such as `launches` or `has_valuation`. Use these values in `categories[]` to filter. |
| `news_articles[].organization_ids` | Apollo IDs of the companies the article is linked to. |
| `news_articles[].id` | Apollo ID of the news article. |
| `pagination.page / pagination.per_page` | The current page number and the page size used for this response. |
| `pagination.total_entries / pagination.total_pages` | Total number of matching articles and the number of pages at the current page size. |

### Notes

- Get the organization ID from [Apollo Organization Search](/apis/apollo/company-search) and pass it in `organization_ids[]`.
- Use `page` and `per_page` to move through results. Check `pagination.total_pages` for the last page.
- Format `published_at[min]` and `published_at[max]` as `YYYY-MM-DD`.
- For firmographic details on the same company, call [Apollo Organization Enrichment](/apis/apollo/company-enrich).

### Pricing

$0.01975 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/apollo/company-news-search.json`](../../../catalog/models/apollo/company-news-search.json) · Store page: https://www.sandbase.ai/model/apollo/company-news-search
