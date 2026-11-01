# Clutch Company Reviews

`clutch/company-reviews` · api · Clutch

Get paginated reviews for a company. Returns review titles, ratings, dates, and project information (services, project size, project length).

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "clutch/company-reviews", "slug": "simform"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('clutch/company-reviews', {'slug': 'simform'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("clutch/company-reviews", {
  "slug": "simform"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "clutch/company-reviews", sandbase.Params{
	"slug": "simform",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/clutch/company-reviews` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number, 0-based. range -9007199254740991–9007199254740991 |
| `slug` | string | yes | Company profile slug from search_companies results.  |

## Details

Get paginated reviews for a company. Returns review titles, ratings, dates, and project information (services, project size, project length).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/clutch/company-reviews" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"slug": "simform", "page": 0}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `slug` | string | Yes | Company profile slug from search_companies results. |
| `page` | integer | No | Page number, 0-based. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/clutch/company-reviews.json`](../../../catalog/models/clutch/company-reviews.json) · Store page: https://www.sandbase.ai/model/clutch/company-reviews
