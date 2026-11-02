# Watsons Category Listings API: pricing, parameters and code examples

`watsons/scrape/category` · data API · Watsons · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021 per call · **Modes:** async

Extract product listings from a Watsons category page URL, including names, prices and promotions.

## Pricing

- **$0.021 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "watsons/scrape/category", "url": "https://www.watsons.com.my/health-care/vitamins-minerals/c/110100"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('watsons/scrape/category', {'url': 'https://www.watsons.com.my/health-care/vitamins-minerals/c/110100'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("watsons/scrape/category", {
  "url": "https://www.watsons.com.my/health-care/vitamins-minerals/c/110100"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "watsons/scrape/category", sandbase.Params{
	"url": "https://www.watsons.com.my/health-care/vitamins-minerals/c/110100",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/watsons/scrape/category` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Full Watsons page URL, e.g. https://www.watsons.com.my/health-care/vitamins-minerals/c/110100  |

## Details

Extract product listings from a Watsons category page URL, including names, prices and promotions.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/watsons/scrape/category" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.watsons.com.my/health-care/vitamins-minerals/c/110100"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Full Watsons page URL, e.g. https://www.watsons.com.my/health-care/vitamins-minerals/c/110100 |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/watsons/scrape/category.json`](../../../../catalog/models/watsons/scrape/category.json) · Store page: https://www.sandbase.ai/model/watsons/scrape/category
