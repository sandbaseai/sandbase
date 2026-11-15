# Shop Search Autocomplete API: pricing, parameters and code examples

`shop-app/search-autocomplete` · data API · Shop · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Fetches search autocomplete suggestions for a query prefix. Returns both query suggestions (text completions) and matching shop suggestions (with id, name, handle, rating). Useful for discovering merchant handles and IDs for other endpoints.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "shop-app/search-autocomplete", "query": "shoes"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('shop-app/search-autocomplete', {'query': 'shoes'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("shop-app/search-autocomplete", {
  "query": "shoes"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "shop-app/search-autocomplete", sandbase.Params{
	"query": "shoes",
})
```

Same call via the path form: `POST /v1/api/shop-app/search-autocomplete` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Search query prefix to get suggestions for.  |

## Details

Fetches search autocomplete suggestions for a query prefix. Returns both query suggestions (text completions) and matching shop suggestions (with id, name, handle, rating). Useful for discovering merchant handles and IDs for other endpoints.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "shop-app/search-autocomplete", "query": "shoes"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search query prefix to get suggestions for. |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/shop-app/search-autocomplete.json`](../../../catalog/models/shop-app/search-autocomplete.json) · Store page: https://www.sandbase.ai/model/shop-app/search-autocomplete
