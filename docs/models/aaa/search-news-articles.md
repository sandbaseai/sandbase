# AAA Search News Articles API: pricing, parameters and code examples

`aaa/search-news-articles` · data API · AAA · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Searches the AAA gas price news archive (weekly national reports and state-specific releases going back years) by keyword, optionally restricted to a publication date range, and returns one page of matching articles.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "aaa/search-news-articles", "query": "gas prices"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('aaa/search-news-articles', {'query': 'gas prices'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("aaa/search-news-articles", {
  "query": "gas prices"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "aaa/search-news-articles", sandbase.Params{
	"query": "gas prices",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/aaa/search-news-articles` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | 1-based page number of the match set. range -9007199254740991–9007199254740991 |
| `limit` | integer |  | Articles per page, 1 to 100. range -9007199254740991–9007199254740991 |
| `order` | string |  | Sort direction by publication date.  |
| `query` | string | yes | Keyword or phrase to search article titles and bodies for, e.g. a state name such as Indiana.  |
| `end_date` | string |  | Latest publication date to include, ISO date YYYY-MM-DD (inclusive). Omitting places no upper bound, i.e. results run until now.  |
| `start_date` | string |  | Earliest publication date to include, ISO date YYYY-MM-DD (inclusive). Omitting places no lower bound.  |

## Details

Searches the AAA gas price news archive (weekly national reports and state-specific releases going back years) by keyword, optionally restricted to a publication date range, and returns one page of matching articles.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/aaa/search-news-articles" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "gas prices"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Keyword or phrase to search article titles and bodies for, e.g. a state name such as Indiana. |
| `end_date` | string | No | Latest publication date to include, ISO date YYYY-MM-DD (inclusive). Omitting places no upper bound, i.e. results run until now. |
| `limit` | integer | No | Articles per page, 1 to 100. |
| `order` | string | No | Sort direction by publication date. |
| `page` | integer | No | 1-based page number of the match set. |
| `start_date` | string | No | Earliest publication date to include, ISO date YYYY-MM-DD (inclusive). Omitting places no lower bound. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/aaa/search-news-articles.json`](../../../catalog/models/aaa/search-news-articles.json) · Store page: https://www.sandbase.ai/model/aaa/search-news-articles
