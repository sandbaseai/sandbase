# Lemon8 Search API: pricing, parameters and code examples

`lemon8/app/search` · data API · Lemon8 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Search Lemon8 posts and users by keyword: post titles, content, authors, images and engagement, with Top and other tabs, sorting and filters.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "lemon8/app/search", "query": "OpenAI"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('lemon8/app/search', {'query': 'OpenAI'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("lemon8/app/search", {
  "query": "OpenAI"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "lemon8/app/search", sandbase.Params{
	"query": "OpenAI",
})
```

Same call via the path form: `POST /v1/api/lemon8/app/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Search keyword  |
| `order_by` | string |  | Search sort type, default is an empty string, optional values are as follows: Empty string: Relevance (default using this parameter to sort); popular: Sort by popularity; recent: Sort from new to old default `""` |
| `max_cursor` | string |  | Pagination parameter, can be obtained from the return result of the last request. It is empty for the first request, and the `max_cursor` returned by the last request is used for subsequent requests. You can judge… default `""` |
| `search_tab` | string |  | Search type, default is `main`, optional values are as follows: main: Display as `Top` in the APP (comprehensive search, default using this parameter to search); user: Display as `Accounts` in the APP (search user… default `"main"` |
| `filter_type` | string |  | Search filter type, default is an empty string, optional values are as follows: Empty string: All (default using this parameter to search); video: Search only video; posts: Search only posts default `""` |

## Details

Search Lemon8 for a keyword and get matching posts and users. Choose the tab with `search_tab` and paginate with `max_cursor`.

### Use cases

- Research lifestyle and product trends on Lemon8.
- Find creators in a niche.
- Monitor brand mentions.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/lemon8/app/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "OpenAI"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search keyword |
| `order_by` | string | No | Search sort type, default is an empty string, optional values are as follows: Empty string: Relevance (default using th… |
| `max_cursor` | string | No | Pagination parameter, can be obtained from the return result of the last request. |
| `search_tab` | string | No | Search type, default is `main`, optional values are as follows: main: Display as `Top` in the APP (comprehensive search… |
| `filter_type` | string | No | Search filter type, default is an empty string, optional values are as follows: Empty string: All (default using this p… |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "has_more": true,
    "items": [
      {
        "articles": [
          {
            "group_id": "7661250232746885645",
            "article_class": "Gallery",
            "language": "en",
            "publish_time": 1783774883,
            "read_count": 16,
            "title": "ChatGPT just clocked in. 👀    OpenAI launched Cha…",
            "article_url": "https://www.lemon8-app.com/@itsdebbiedarlin/76612…",
            "author": {
              "name": "<user>"
            }
          }
        ]
      }
    ]
  }
}
```

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Get banners of discover page](/model/lemon8/app/discover-banners): Get banners of discover page.
- [Get main content of discover page](/model/lemon8/app/discover-tab): Get main content of discover page.
- [Get Editor's Picks of discover page](/model/lemon8/app/discover-tab-information-tabs): Get Editor's Picks of discover page.

---
Machine-readable: [`catalog/models/lemon8/app/search.json`](../../../../catalog/models/lemon8/app/search.json) · Store page: https://www.sandbase.ai/model/lemon8/app/search
