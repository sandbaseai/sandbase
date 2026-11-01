# AutoZone Category Listings

`autozone/scrape/category` · api · AutoZone

Extract product listings from an AutoZone category page URL with pagination and preferred-store pricing.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "autozone/scrape/category", "url": "https://www.autozone.com/batteries-starting-and-charging/battery"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('autozone/scrape/category', {'url': 'https://www.autozone.com/batteries-starting-and-charging/battery'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("autozone/scrape/category", {
  "url": "https://www.autozone.com/batteries-starting-and-charging/battery"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "autozone/scrape/category", sandbase.Params{
	"url": "https://www.autozone.com/batteries-starting-and-charging/battery",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/autozone/scrape/category` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Full AutoZone page URL, e.g. https://www.autozone.com/batteries-starting-and-charging/battery  |
| `page` | integer |  | Results page number (1-indexed; default 1). range 1–9007199254740991 |
| `preferedstore` | string |  | Preferred AutoZone store ID for local availability and pricing (the upstream field name is spelled this way).  |

## Details

Extract product listings from an AutoZone category page URL with pagination and preferred-store pricing.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/autozone/scrape/category" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.autozone.com/batteries-starting-and-charging/battery"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Full AutoZone page URL, e.g. https://www.autozone.com/batteries-starting-and-charging/battery |
| `page` | integer | No | Results page number (1-indexed; default 1). |
| `preferedstore` | string | No | Preferred AutoZone store ID for local availability and pricing (the upstream field name is spelled this way). |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/autozone/scrape/category.json`](../../../../catalog/models/autozone/scrape/category.json) · Store page: https://www.sandbase.ai/model/autozone/scrape/category
