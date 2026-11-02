# Tripadvisor Search API: pricing, parameters and code examples

`tripadvisor/search` · data API · Tripadvisor · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00015 per call (free daily quota) · **Modes:** sync

Search Tripadvisor hotels, restaurants, attractions and places by keyword.

## Pricing

- **$0.00015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tripadvisor/search", "q": "hotels in Austin Texas"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tripadvisor/search', {'q': 'hotels in Austin Texas'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tripadvisor/search", {
  "q": "hotels in Austin Texas"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tripadvisor/search", sandbase.Params{
	"q": "hotels in Austin Texas",
})
```

Same call via the path form: `POST /v1/api/tripadvisor/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string | yes | Search text, 1 to 500 characters.  |
| `lat` | number |  | Search center latitude from -90 through 90. Requires lon.  |
| `lon` | number |  | Search center longitude from -180 through 180. Requires lat.  |
| `num` | integer |  | Maximum number of search_results, 1 through 30, including any leading exact match. default `30` |
| `start` | integer |  | Result offset from 0 through 10,000. Offsets and positions count any leading exact match. default `0` |
| `geo_id` | integer |  | Tripadvisor geography ID to search within.  |
| `locale` | string |  | Lowercase language code with an optional uppercase country, such as en or en-US. default `"en-US"` |
| `timeout` | number |  | Optional budget for the entire request in seconds, measured from gateway receipt until the response is ready to send. Includes admission, queueing and settlement. Must be greater than 0 and at most 90. On expiry, the…  |
| `place_type` | string |  | Restrict results to one entity type. one of: `all`, `accommodation`, `attraction`, `attraction_product`, `eatery`, `geo`; default `"all"` |
| `tripadvisor_domain` | string |  | Supported first-party localized Tripadvisor hostname, such as www.tripadvisor.co.uk.  |

## Details

Search Tripadvisor hotels, restaurants, attractions and places by keyword.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tripadvisor/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "hotels in Austin Texas"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | Yes | Search text, 1 to 500 characters. |
| `geo_id` | integer | No | Tripadvisor geography ID to search within. |
| `lat` | number | No | Search center latitude from -90 through 90. Requires lon. |
| `locale` | string | No | Lowercase language code with an optional uppercase country, such as en or en-US. |
| `lon` | number | No | Search center longitude from -180 through 180. Requires lat. |
| `num` | integer | No | Maximum number of search_results, 1 through 30, including any leading exact match. |
| `place_type` | string | No | Restrict results to one entity type. |
| `start` | integer | No | Result offset from 0 through 10,000. Offsets and positions count any leading exact match. |
| `timeout` | number | No | Optional budget for the entire request in seconds, measured from gateway receipt until the response is ready to send. Includes admission, queueing and settlement. Must be greater t |
| `tripadvisor_domain` | string | No | Supported first-party localized Tripadvisor hostname, such as www.tripadvisor.co.uk. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/tripadvisor/search.json`](../../../catalog/models/tripadvisor/search.json) · Store page: https://www.sandbase.ai/model/tripadvisor/search
