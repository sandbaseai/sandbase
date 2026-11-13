# Flightradar24 Live Flights API: pricing, parameters and code examples

`flightradar24/flights` · data API · Flightradar24 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Get live flights from Flightradar24 by airport, flight number, airline, aircraft type or map bounds, with position, altitude, speed, route and aircraft.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "flightradar24/flights"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('flightradar24/flights', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("flightradar24/flights", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "flightradar24/flights", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/flightradar24/flights` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `airline` | string |  | Parameter defines the airline to search for, as a 3-letter ICAO airline code (e.g., `BAW` for British Airways), not its 2-letter IATA code (`BA`). The ICAO code is shown after the IATA code when you search for the…  |
| `airport` | string |  | Parameter defines the airport that flights depart from or arrive at, as a 3-letter IATA airport code (e.g., `LHR` for London Heathrow). You can search for it on Flightradar24 or IATA. Multiple airports can be separated…  |
| `callsign` | string |  | Parameter defines the callsign to search for (e.g., `BAW5L`). A callsign can differ from the flight number: `BA285` flies as `BAW5L`. Flights whose callsign starts with this value are returned. Multiple callsigns can…  |
| `arrival_id` | string |  | Parameter defines the airport that flights arrive at, as a 3-letter IATA airport code (e.g., `JFK` for New York JFK). You can search for it on Flightradar24 or IATA. Multiple airports can be separated by commas (e.g.,…  |
| `map_bounds` | string |  | Parameter defines the GPS coordinates of the map area to search in, like moving the map on Flightradar24. Only flights within these bounds are returned. Its value must be 4 comma-separated numbers matching the…  |
| `departure_id` | string |  | Parameter defines the airport that flights depart from, as a 3-letter IATA airport code (e.g., `LHR` for London Heathrow). You can search for it on Flightradar24 or IATA. Multiple airports can be separated by commas…  |
| `registration` | string |  | Parameter defines the aircraft registration to search for (e.g., `G-XLEK`). Aircraft whose registration starts with this value are returned, so `G-XLE` returns the British Airways Airbus A380s, and `G-` returns every…  |
| `aircraft_type` | string |  | Parameter defines the aircraft type to search for, as an ICAO aircraft type designator (e.g., `A388` for the Airbus A380-800). It's shown in the aircraft details of a flight on Flightradar24. Aircraft whose type starts…  |
| `flight_number` | string |  | Parameter defines the flight number to search for (e.g., `BA285`). Flights whose number starts with this value are returned, so `BA28` also returns `BA285` and `BA287`. Multiple flight numbers can be separated by…  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |

## Details

Get live flights from Flightradar24 by airport, flight number, airline, aircraft type or map bounds, with position, altitude, speed, route and aircraft.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/flightradar24/flights" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"airport": "AUS"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `airport` | string | No | Parameter defines the airport that flights depart from or arrive at, as a 3-letter IATA airport code (e.g., `LHR` for London Heathrow). You can search for it on Flightradar24 or IATA. Multiple airports can be separated by commas (e.g., `LHR |
| `map_bounds` | string | No | Parameter defines the GPS coordinates of the map area to search in, like moving the map on Flightradar24. Only flights within these bounds are returned. Its value must be 4 comma-separated numbers matching the following format: `north` + `, |
| `flight_number` | string | No | Parameter defines the flight number to search for (e.g., `BA285`). Flights whose number starts with this value are returned, so `BA28` also returns `BA285` and `BA287`. Multiple flight numbers can be separated by commas (e.g., `BA285,BA287` |
| `callsign` | string | No | Parameter defines the callsign to search for (e.g., `BAW5L`). A callsign can differ from the flight number: `BA285` flies as `BAW5L`. Flights whose callsign starts with this value are returned. Multiple callsigns can be separated by commas  |
| `airline` | string | No | Parameter defines the airline to search for, as a 3-letter ICAO airline code (e.g., `BAW` for British Airways), not its 2-letter IATA code (`BA`). The ICAO code is shown after the IATA code when you search for the airline on Flightradar24.  |
| `registration` | string | No | Parameter defines the aircraft registration to search for (e.g., `G-XLEK`). Aircraft whose registration starts with this value are returned, so `G-XLE` returns the British Airways Airbus A380s, and `G-` returns every aircraft registered in  |
| `aircraft_type` | string | No | Parameter defines the aircraft type to search for, as an ICAO aircraft type designator (e.g., `A388` for the Airbus A380-800). It's shown in the aircraft details of a flight on Flightradar24. Aircraft whose type starts with this value are r |
| `departure_id` | string | No | Parameter defines the airport that flights depart from, as a 3-letter IATA airport code (e.g., `LHR` for London Heathrow). You can search for it on Flightradar24 or IATA. Multiple airports can be separated by commas (e.g., `LHR,LGW`). |
| `arrival_id` | string | No | Parameter defines the airport that flights arrive at, as a 3-letter IATA airport code (e.g., `JFK` for New York JFK). You can search for it on Flightradar24 or IATA. Multiple airports can be separated by commas (e.g., `JFK,EWR`). |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/flightradar24/flights.json`](../../../catalog/models/flightradar24/flights.json) · Store page: https://www.sandbase.ai/model/flightradar24/flights
