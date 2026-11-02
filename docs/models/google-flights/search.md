# Google Flights Search API: pricing, parameters and code examples

`google-flights/search` · data API · Google Flights · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.015 per call · **Modes:** sync

Google Flights itineraries for a route and date: airlines, times, stops, durations, prices and price insights.

## Pricing

- **$0.015 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google-flights/search", "departure_id": "CDG", "arrival_id": "AUS", "outbound_date": "2026-12-15"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google-flights/search', {'departure_id': 'CDG', 'arrival_id': 'AUS', 'outbound_date': '2026-12-15'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google-flights/search", {
  "departure_id": "CDG",
  "arrival_id": "AUS",
  "outbound_date": "2026-12-15"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google-flights/search", sandbase.Params{
	"departure_id": "CDG",
	"arrival_id": "AUS",
	"outbound_date": "2026-12-15",
})
```

Same call via the path form: `POST /v1/api/google-flights/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `type` | string |  | 1 round trip (default) \| 2 one way \| 3 multi-city  |
| `currency` | string |  | currency  |
| `arrival_id` | string | yes | destination airport/location code  |
| `return_date` | string |  | YYYY-MM-DD, required when type=1  |
| `departure_id` | string | yes | origin airport/location code  |
| `outbound_date` | string | yes | YYYY-MM-DD  |

## Details

Google Flights itineraries for a route and date: airlines, times, stops, durations, prices and price insights.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google-flights/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"departure_id": "CDG", "arrival_id": "AUS", "outbound_date": "2026-12-15", "type": "2"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `arrival_id` | string | Yes | destination airport/location code |
| `departure_id` | string | Yes | origin airport/location code |
| `outbound_date` | string | Yes | YYYY-MM-DD |
| `currency` | string | No | currency |
| `return_date` | string | No | YYYY-MM-DD, required when type=1 |
| `type` | string | No | 1 round trip (default) / 2 one way / 3 multi-city |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/google-flights/search.json`](../../../catalog/models/google-flights/search.json) · Store page: https://www.sandbase.ai/model/google-flights/search
