# X (Twitter) Search Tweets Across Communities API: pricing, parameters and code examples

`twitter/community-search-tweets` · data API · X (Twitter) · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.003 per call · **Modes:** sync

Search tweets posted in all X Communities by keyword, sorted by Latest or Top.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.003**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/community-search-tweets", "query": "AI", "queryType": "Latest"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/community-search-tweets', {'query': 'AI', 'queryType': 'Latest'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/community-search-tweets", {
  "query": "AI",
  "queryType": "Latest"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/community-search-tweets", sandbase.Params{
	"query": "AI",
	"queryType": "Latest",
})
```

Same call via the path form: `POST /v1/api/twitter/community-search-tweets` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Search query (e.g., keyword)  |
| `cursor` | string |  | Cursor for pagination  |
| `queryType` | string | yes | Query type (Latest or Top) one of: `Latest`, `Top`; default `"Latest"` |

## Details

Search tweets posted in all X Communities by keyword, sorted by Latest or Top.

The result is returned in `outputs[0].data` as the official X (Twitter) API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/community-search-tweets" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "AI", "queryType": "Latest"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | string | No | Cursor for pagination |
| `query` | string | Yes | Search query (e.g., keyword) |
| `queryType` | string | Yes | Query type (Latest or Top) |

### Pricing

Billed at the actual cost of each call, about $0.003 for a typical request; the cost grows with the number of rows returned. Searches with no results are billed at their actual cost. Failed calls are not charged.

---
Machine-readable: [`catalog/models/twitter/community-search-tweets.json`](../../../catalog/models/twitter/community-search-tweets.json) · Store page: https://www.sandbase.ai/model/twitter/community-search-tweets
