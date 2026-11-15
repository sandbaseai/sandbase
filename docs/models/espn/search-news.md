# ESPN Search News API: pricing, parameters and code examples

`espn/search-news` · data API · ESPN · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Search ESPN news articles about a topic within a league using the site's article search.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "espn/search-news", "query": "trade", "league": "nba"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('espn/search-news', {'query': 'trade', 'league': 'nba'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("espn/search-news", {
  "query": "trade",
  "league": "nba"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "espn/search-news", sandbase.Params{
	"query": "trade",
	"league": "nba",
})
```

Same call via the path form: `POST /v1/api/espn/search-news` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of articles to return, 1-50. default `5` |
| `query` | string | yes | Topic to search for (e.g. trade, injury, transfer).  |
| `league` | string | yes | League identifier.  |

## Details

Search ESPN news articles about a topic within a league using the site's article search.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "espn/search-news", "query": "trade", "league": "nba"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `league` | string | Yes | League identifier. |
| `query` | string | Yes | Topic to search for (e.g. trade, injury, transfer). |
| `limit` | integer | No | Maximum number of articles to return, 1-50. |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/espn/search-news.json`](../../../catalog/models/espn/search-news.json) · Store page: https://www.sandbase.ai/model/espn/search-news
