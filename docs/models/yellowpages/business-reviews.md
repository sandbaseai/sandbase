# Yellow Pages Business Reviews API: pricing, parameters and code examples

`yellowpages/business-reviews` · data API · Yellow Pages · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Retrieve customer reviews for a business from its YellowPages detail page. Returns review author, date, star rating, optional title, and review text. Returns an empty array if the business has no reviews.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "yellowpages/business-reviews", "url": "https://www.yellowpages.com/new-york-ny/mip/punch-28771538"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('yellowpages/business-reviews', {'url': 'https://www.yellowpages.com/new-york-ny/mip/punch-28771538'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("yellowpages/business-reviews", {
  "url": "https://www.yellowpages.com/new-york-ny/mip/punch-28771538"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "yellowpages/business-reviews", sandbase.Params{
	"url": "https://www.yellowpages.com/new-york-ny/mip/punch-28771538",
})
```

Same call via the path form: `POST /v1/api/yellowpages/business-reviews` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Full YellowPages business URL or path (e.g., 'https://www.yellowpages.com/new-york-ny/mip/punch-28771538')  |

## Details

Retrieve customer reviews for a business from its YellowPages detail page. Returns review author, date, star rating, optional title, and review text. Returns an empty array if the business has no reviews.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "yellowpages/business-reviews", "url": "https://www.yellowpages.com/new-york-ny/mip/punch-28771538"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Full YellowPages business URL or path (e.g., 'https://www.yellowpages.com/new-york-ny/mip/punch-28771538') |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/yellowpages/business-reviews.json`](../../../catalog/models/yellowpages/business-reviews.json) · Store page: https://www.sandbase.ai/model/yellowpages/business-reviews
