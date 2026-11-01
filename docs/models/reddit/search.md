# Reddit Keyword Search

`reddit/search` · api · Reddit

Search Reddit posts by keyword with an optional continuation token. Use it to discover topic-related discussions or continue through additional search-result pages.

## Pricing

- **$0.013889 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/search", "keyword": "iphone"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/search', {'keyword': 'iphone'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/search", {
  "keyword": "iphone"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/search", sandbase.Params{
	"keyword": "iphone",
})
```

Same call via the path form: `POST /v1/api/reddit/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `after` | string |  | Pagination token to retrieve the next set of results.  |
| `keyword` | string | yes | Search query keywords.  |

## Details

Search Reddit posts by keyword with an optional continuation token. Use it to discover topic-related discussions or continue through additional search-result pages.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "iphone"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search query keywords. |
| `after` | string | No | Pagination token to retrieve the next set of results. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/reddit/search.json`](../../../catalog/models/reddit/search.json) · Store page: https://www.sandbase.ai/model/reddit/search
