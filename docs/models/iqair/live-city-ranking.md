# IQAir Live City Ranking API: pricing, parameters and code examples

`iqair/live-city-ranking` · data API · IQAir · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Real-time global city air quality rankings sorted by AQI descending. Returns up to 122 major cities with current AQI values, geographic metadata, and follower counts.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "iqair/live-city-ranking"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('iqair/live-city-ranking', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("iqair/live-city-ranking", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "iqair/live-city-ranking", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/iqair/live-city-ranking` with the body above minus `model`.

## Details

Returns a ranked list of major cities with their current air quality index (AQI), sorted from highest AQI to lowest. The API takes no input. Each row includes the city, state, country, follower count and a page path for the city.

### Use cases

- Show a live list of the most polluted cities in a dashboard or news widget.
- Compare the current AQI of cities in different countries in one call.
- Pick the most followed cities to decide which ones to track in more detail.
- Build a list of city page paths to pass to a city-level air quality lookup.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/iqair/live-city-ranking" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "citiesData": [
      {
        "aqi": 236,
        "city": "Lahore",
        "country": "Pakistan",
        "flagURL": "https://cdn.airvisual.net/flags/pakistan.jpg",
        "followersCount": 1139595,
        "id": "Dt8HhEj6mC2eatyBr",
        "rank": 1,
        "state": "Punjab",
        "updatedAt": "2026-11-03T07:00:00.000Z",
        "url": "/pakistan/punjab/lahore"
      }
    ],
    "updatedAt": "2026-11-03T07:00:00.000Z"
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.citiesData[].rank` | Position of the city in the list. Rank 1 has the highest `aqi`. |
| `data.citiesData[].aqi` | Current air quality index value for the city. A higher number means worse air. |
| `data.citiesData[].city / data.citiesData[].state / data.citiesData[].country` | Name of the city, its state or region, and its country. |
| `data.citiesData[].id` | Identifier of the city record. |
| `data.citiesData[].url` | Path of the city page, built as `/country/state/city` in lowercase with dashes. |
| `data.citiesData[].followersCount` | Number of followers the city has. |
| `data.citiesData[].flagURL` | Link to the country flag image. |
| `data.citiesData[].updatedAt / data.updatedAt` | Timestamp of the reading for the city and for the whole list. Both are ISO 8601 strings in UTC. |
| `status` | Shows `success` when the call worked. |

### Notes

- The request body is an empty object `{}`. There is no pagination parameter.
- The `url` value gives the country, state and city slugs. Use them with [IQAir City Air Quality](/apis/iqair/city-air-quality) for a single city.
- For a map-based view of stations, see [IQAir Map Data](/apis/iqair/map-data).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/iqair/live-city-ranking.json`](../../../catalog/models/iqair/live-city-ranking.json) · Store page: https://www.sandbase.ai/model/iqair/live-city-ranking
