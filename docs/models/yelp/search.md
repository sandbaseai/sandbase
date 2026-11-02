# Yelp Business Search API: pricing, parameters and code examples

`yelp/search` · data API · Yelp · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00015 per call (free daily quota) · **Modes:** sync

Search Yelp businesses by keyword and location: name, rating, review count, price level, categories and address.

## Pricing

- **$0.00015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "yelp/search", "find_loc": "Austin, TX"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('yelp/search', {'find_loc': 'Austin, TX'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("yelp/search", {
  "find_loc": "Austin, TX"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "yelp/search", sandbase.Params{
	"find_loc": "Austin, TX",
})
```

Same call via the path form: `POST /v1/api/yelp/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `l` | string |  | Yelp map-bounds token, up to 1,024 characters.  |
| `cflt` | string |  | Yelp category identifier, such as coffee.  |
| `attrs` | string |  | Comma-separated Yelp attribute filters, such as OutdoorSeating; up to 4,096 characters.  |
| `start` | integer |  | Result offset from 0 through 10,000. default `0` |
| `sortby` | string |  | Result order. one of: `recommended`, `rating`, `review_count`; default `"recommended"` |
| `timeout` | number |  | Optional budget for the entire request in seconds, measured from gateway receipt until the response is ready to send. Includes admission, queueing and settlement. Must be greater than 0 and at most 90. On expiry, the…  |
| `find_loc` | string | yes | Search location, 1 to 500 characters.  |
| `find_desc` | string |  | Business name, category, or search terms, up to 500 characters.  |
| `yelp_domain` | string |  | Supported first-party localized Yelp hostname, such as www.yelp.co.uk. Links in the response use this hostname.  |

## Details

Search Yelp businesses by keyword and location: name, rating, review count, price level, categories and address.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/yelp/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"find_desc": "coffee", "find_loc": "Austin, TX"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `find_loc` | string | Yes | Search location, 1 to 500 characters. |
| `attrs` | string | No | Comma-separated Yelp attribute filters, such as OutdoorSeating; up to 4,096 characters. |
| `cflt` | string | No | Yelp category identifier, such as coffee. |
| `find_desc` | string | No | Business name, category, or search terms, up to 500 characters. |
| `l` | string | No | Yelp map-bounds token, up to 1,024 characters. |
| `sortby` | string | No | Result order. |
| `start` | integer | No | Result offset from 0 through 10,000. |
| `timeout` | number | No | Optional budget for the entire request in seconds, measured from gateway receipt until the response is ready to send. Includes admission, queueing and settlement. Must be greater t |
| `yelp_domain` | string | No | Supported first-party localized Yelp hostname, such as www.yelp.co.uk. Links in the response use this hostname. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/yelp/search.json`](../../../catalog/models/yelp/search.json) · Store page: https://www.sandbase.ai/model/yelp/search
