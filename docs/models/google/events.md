# Google Events API: pricing, parameters and code examples

`google/events` · data API · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Search events listed on Google by keyword and place, with title, date, venue, address, ticket links and thumbnails.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/events", "q": "concerts in austin"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/events', {'q': 'concerts in austin'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/events", {
  "q": "concerts in austin"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/events", sandbase.Params{
	"q": "concerts in austin",
})
```

Same call via the path form: `POST /v1/api/google/events` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string | yes | Parameter defines the query you want to search. To search for events in a specific location, just include the location inside your search query (e.g. `Events in Austin, TX`).  |
| `uule` | string |  | Parameter is the Google encoded location you want to use for the search. `uule` and `location` parameters can't be used together. Head to UULE Generator if you need to convert a location or GPS coordinates to `uule`…  |
| `location` | string |  | Parameter defines from where you want the search to originate. If several locations match the location requested, we'll pick the most popular one. Head to the /locations.json API if you need more precise control. The…  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |

## Details

Search events listed on Google by keyword and place, with title, date, venue, address, ticket links and thumbnails.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google/events" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "concerts in austin"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | Yes | Parameter defines the query you want to search. To search for events in a specific location, just include the location inside your search query (e.g. `Events in Austin, TX`). |
| `location` | string | No | Parameter defines from where you want the search to originate. If several locations match the location requested, we'll pick the most popular one. Head to the /locations.json API if you need more precise control. The `location` and `uule` p |
| `uule` | string | No | Parameter is the Google encoded location you want to use for the search. `uule` and `location` parameters can't be used together. Head to UULE Generator if you need to convert a location or GPS coordinates to `uule` parameter, and vice vers |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/google/events.json`](../../../catalog/models/google/events.json) · Store page: https://www.sandbase.ai/model/google/events
