# Tripadvisor Reviews API: pricing, parameters and code examples

`tripadvisor/reviews` · data API · Tripadvisor · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00015 per call (free daily quota) · **Modes:** sync

Public reviews of a Tripadvisor hotel, restaurant or attraction by place ID: rating, title, text, date and reviewer.

## Pricing

- **$0.00015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tripadvisor/reviews", "place_id": 18941405}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tripadvisor/reviews', {'place_id': 18941405})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tripadvisor/reviews", {
  "place_id": 18941405
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tripadvisor/reviews", sandbase.Params{
	"place_id": 18941405,
})
```

Same call via the path form: `POST /v1/api/tripadvisor/reviews` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `num` | integer |  | Number of reviews, 1 through 50. default `10` |
| `start` | integer |  | Review offset from 0 through 10,000. default `0` |
| `locale` | string |  | Lowercase language code with an optional uppercase country, such as en or en-US. default `"en-US"` |
| `sort_by` | string |  | Review order: recent (newest first) or relevance. one of: `recent`, `relevance`; default `"recent"` |
| `timeout` | number |  | Optional budget for the entire request in seconds, measured from gateway receipt until the response is ready to send. Includes admission, queueing and settlement. Must be greater than 0 and at most 90. On expiry, the…  |
| `place_id` | integer | yes | Numeric Tripadvisor place ID, up to 16 digits.  |
| `translate` | boolean |  | Request Tripadvisor's machine translation of reviews. default `false` |
| `tripadvisor_domain` | string |  | Supported first-party localized Tripadvisor hostname, such as www.tripadvisor.co.uk.  |

## Details

Public reviews of a Tripadvisor hotel, restaurant or attraction by place ID: rating, title, text, date and reviewer.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tripadvisor/reviews" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"place_id": 18941405, "num": 5}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `place_id` | integer | Yes | Numeric Tripadvisor place ID, up to 16 digits. |
| `locale` | string | No | Lowercase language code with an optional uppercase country, such as en or en-US. |
| `num` | integer | No | Number of reviews, 1 through 50. |
| `sort_by` | string | No | Review order: recent (newest first) or relevance. |
| `start` | integer | No | Review offset from 0 through 10,000. |
| `timeout` | number | No | Optional budget for the entire request in seconds, measured from gateway receipt until the response is ready to send. Includes admission, queueing and settlement. Must be greater t |
| `translate` | boolean | No | Request Tripadvisor's machine translation of reviews. |
| `tripadvisor_domain` | string | No | Supported first-party localized Tripadvisor hostname, such as www.tripadvisor.co.uk. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/tripadvisor/reviews.json`](../../../catalog/models/tripadvisor/reviews.json) · Store page: https://www.sandbase.ai/model/tripadvisor/reviews
