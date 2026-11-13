# Google Maps Reviews API: pricing, parameters and code examples

`google-maps/reviews` · data API · Google Maps · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00015 per call · **Modes:** async

Get Google Maps reviews for one place with sorting, filtering, and paging.

## Pricing

- **$0.00015 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google-maps/reviews"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google-maps/reviews', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google-maps/reviews", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google-maps/reviews", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/google-maps/reviews` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `gl` | string |  | Two-letter country code, lowercase. Default 'us'.  |
| `hl` | string |  | Language for review labels and place context. Default 'en'.  |
| `num` | integer |  | Number of reviews: 1-100 on an unfiltered first request, 1-20 on filtered or continuation requests. Default 8. range 1–100 |
| `query` | string |  | Only reviews matching this free-text query. Cannot be combined with topic_id.  |
| `data_id` | string |  | Hexadecimal Maps feature ID in the form '0x123:0x456'. Required unless place_id is supplied.  |
| `sort_by` | string |  | Review order. Default 'qualityScore'. one of: `qualityScore`, `newestFirst`, `ratingHigh`, `ratingLow` |
| `place_id` | string |  | Google place ID of the business. Required unless data_id is supplied.  |
| `topic_id` | string |  | Only reviews under this topic from the topics group. Cannot be combined with query.  |
| `next_page_token` | string |  | Continuation token from pagination.next_page_token, passed back unchanged.  |
| `source_metadata` | boolean |  | Include review-provider icon and scale metadata when available.  |

## Details

Get Google Maps reviews for one place with sorting, filtering, and paging.

---
Machine-readable: [`catalog/models/google-maps/reviews.json`](../../../catalog/models/google-maps/reviews.json) · Store page: https://www.sandbase.ai/model/google-maps/reviews
