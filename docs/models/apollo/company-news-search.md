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

News Articles Search from Apollo. Returns the official Apollo API response unchanged.

The response is the official Apollo API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/apollo/company-news-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"organization_ids[]": ["5d0a0fbff6512580bf33a120"], "per_page": 2}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `categories[]` | array | No | Filter your search to include only certain categories or sub-categories of news. Use the News search filter for companies within Apollo to uncover all possible  |
| `organization_ids[]` | array | Yes | The Apollo IDs for the companies you want to include in your search results. Each company in the Apollo database is assigned a unique ID. To find IDs, call the  |
| `page` | integer | No | The page number of the Apollo data that you want to retrieve. Use this parameter in combination with the per_page parameter to make search results for navigable |
| `per_page` | integer | No | The number of search results that should be returned for each page. Limiting the number of results per page improves the endpoint's performance. Use the page pa |
| `published_at[max]` | string | No | Set the upper bound of the date range you want to search. Use this parameter in combination with the published_at[min] parameter. This date should fall after th |
| `published_at[min]` | string | No | Set the lower bound of the date range you want to search. Use this parameter in combination with the published_at[max] parameter. This date should fall before t |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/apollo/company-news-search.json`](../../../catalog/models/apollo/company-news-search.json) · Store page: https://www.sandbase.ai/model/apollo/company-news-search
