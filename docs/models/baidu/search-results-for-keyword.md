# Baidu Search Results For Keyword API: pricing, parameters and code examples

`baidu/search-results-for-keyword` · data API · Baidu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Construct a Baidu search URL for a specific hot search keyword to view related news and discussions. Does not fetch search results; only builds and returns the URL.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "baidu/search-results-for-keyword", "keyword": "trending topic"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('baidu/search-results-for-keyword', {'keyword': 'trending topic'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("baidu/search-results-for-keyword", {
  "keyword": "trending topic"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "baidu/search-results-for-keyword", sandbase.Params{
	"keyword": "trending topic",
})
```

Same call via the path form: `POST /v1/api/baidu/search-results-for-keyword` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | The trending keyword to generate a Baidu search URL for.  |

## Details

Construct a Baidu search URL for a specific hot search keyword to view related news and discussions. Does not fetch search results; only builds and returns the URL.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "baidu/search-results-for-keyword", "keyword": "trending topic"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | The trending keyword to generate a Baidu search URL for. |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/baidu/search-results-for-keyword.json`](../../../catalog/models/baidu/search-results-for-keyword.json) · Store page: https://www.sandbase.ai/model/baidu/search-results-for-keyword
