# App Store Reviews

`app-store/reviews` · api · App Store

Read Apple App Store reviews for an app in one storefront country, page by page.

## Pricing

- **$0.00015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "app-store/reviews", "product_id": "570060128"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('app-store/reviews', {'product_id': '570060128'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("app-store/reviews", {
  "product_id": "570060128"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "app-store/reviews", sandbase.Params{
	"product_id": "570060128",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/app-store/reviews` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | One-based page number. Exhausted pages return an empty review list. Default 1. range 1–2147483647 |
| `sort` | string |  | 'mostrecent' or 'mosthelpful'. The Mac storefront always returns newest first. Default 'mostrecent'. one of: `mostrecent`, `mosthelpful` |
| `country` | string |  | Two-letter Apple storefront country, such as 'us' or 'gb' ('uk' is accepted). Default 'us'.  |
| `product_id` | string | yes | Positive decimal Apple app identifier, such as '570060128'.  |

## Details

Read Apple App Store reviews for an app in one storefront country, page by page.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/app-store/reviews" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"product_id": "570060128"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `product_id` | string | Yes | Positive decimal Apple app identifier, such as '570060128'. |
| `country` | string | No | Two-letter Apple storefront country, such as 'us' or 'gb' ('uk' is accepted). Default 'us'. |
| `page` | integer | No | One-based page number. Exhausted pages return an empty review list. Default 1. |
| `sort` | string | No | 'mostrecent' or 'mosthelpful'. The Mac storefront always returns newest first. Default 'mostrecent'. One of: `mostrecent`, `mosthelpful`. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/app-store/reviews.json`](../../../catalog/models/app-store/reviews.json) · Store page: https://www.sandbase.ai/model/app-store/reviews
