# Yelp Reviews API: pricing, parameters and code examples

`yelp/reviews` · data API · Yelp · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00015 per call (free daily quota) · **Modes:** sync

Public reviews of a Yelp business by place ID: rating, text, date and reviewer, with paging and sorting.

## Pricing

- **$0.00015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "yelp/reviews", "place_id": "dDz2erKJ_Z2HMur0tQ_iJA"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('yelp/reviews', {'place_id': 'dDz2erKJ_Z2HMur0tQ_iJA'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("yelp/reviews", {
  "place_id": "dDz2erKJ_Z2HMur0tQ_iJA"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "yelp/reviews", sandbase.Params{
	"place_id": "dDz2erKJ_Z2HMur0tQ_iJA",
})
```

Same call via the path form: `POST /v1/api/yelp/reviews` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string |  | Not supported: Yelp does not offer review text filtering. Any value returns 422 unsupported_parameter.  |
| `hl` | string |  | Review language: a two-letter code with an optional two-letter region, such as en or fr-FR. default `"en"` |
| `num` | integer |  | Number of reviews, 1 through 49. default `49` |
| `start` | integer |  | Review offset from 0 through 10,000. default `0` |
| `rating` | string |  | Comma-separated star ratings to include, each from 1 through 5.  |
| `sortby` | string |  | Review order. one of: `relevance_desc`, `date_desc`, `date_asc`, `rating_desc`, `rating_asc`, `elites_desc`; default `"relevance_desc"` |
| `timeout` | number |  | Optional budget for the entire request in seconds, measured from gateway receipt until the response is ready to send. Includes admission, queueing and settlement. Must be greater than 0 and at most 90. On expiry, the…  |
| `place_id` | string | yes | Encoded Yelp business ID: letters, numbers, underscores, and hyphens.  |
| `yelp_domain` | string |  | Supported first-party localized Yelp hostname, such as www.yelp.co.uk. Links in the response use this hostname.  |
| `not_recommended` | boolean |  | Not supported: Yelp does not expose its not-recommended reviews. true returns 422 unsupported_parameter. default `false` |
| `not_recommended_start` | integer |  | Not supported, because not_recommended is not supported. Any value returns 400.  |

## Details

Public reviews of a Yelp business by place ID: rating, text, date and reviewer, with paging and sorting.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/yelp/reviews" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"place_id": "dDz2erKJ_Z2HMur0tQ_iJA", "num": 10}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `place_id` | string | Yes | Encoded Yelp business ID: letters, numbers, underscores, and hyphens. |
| `hl` | string | No | Review language: a two-letter code with an optional two-letter region, such as en or fr-FR. |
| `not_recommended` | boolean | No | Not supported: Yelp does not expose its not-recommended reviews. true returns 422 unsupported_parameter. |
| `not_recommended_start` | integer | No | Not supported, because not_recommended is not supported. Any value returns 400. |
| `num` | integer | No | Number of reviews, 1 through 49. |
| `q` | string | No | Not supported: Yelp does not offer review text filtering. Any value returns 422 unsupported_parameter. |
| `rating` | string | No | Comma-separated star ratings to include, each from 1 through 5. |
| `sortby` | string | No | Review order. |
| `start` | integer | No | Review offset from 0 through 10,000. |
| `timeout` | number | No | Optional budget for the entire request in seconds, measured from gateway receipt until the response is ready to send. Includes admission, queueing and settlement. Must be greater t |
| `yelp_domain` | string | No | Supported first-party localized Yelp hostname, such as www.yelp.co.uk. Links in the response use this hostname. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/yelp/reviews.json`](../../../catalog/models/yelp/reviews.json) · Store page: https://www.sandbase.ai/model/yelp/reviews
