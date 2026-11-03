# Brave POI Descriptions API: pricing, parameters and code examples

`brave/local-descriptions` · data API · Brave · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.005 per call (free daily quota) · **Modes:** sync

POI Descriptions from Brave. Returns the official Brave API response unchanged.

## Pricing

- **$0.005 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "brave/local-descriptions", "ids": ["loc4DFZ5OEXSZVDUAEEDV6PMTFK6YDFANIHQIRRVKLA="]}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('brave/local-descriptions', {'ids': ['loc4DFZ5OEXSZVDUAEEDV6PMTFK6YDFANIHQIRRVKLA=']})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("brave/local-descriptions", {
  "ids": [
    "loc4DFZ5OEXSZVDUAEEDV6PMTFK6YDFANIHQIRRVKLA="
  ]
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "brave/local-descriptions", sandbase.Params{
	"ids": []any{"loc4DFZ5OEXSZVDUAEEDV6PMTFK6YDFANIHQIRRVKLA="},
})
```

Same call via the path form: `POST /v1/api/brave/local-descriptions` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `ids` | array | yes | A list of unique identifiers for the location. The ids are valid only for 8 hours.  |

## Details

Returns a text description for each place ID you send. The input is a required `ids` array of location IDs, and each ID returns one description object.

### Use cases

- Add a short written summary to a map listing or place card for a cafe, shop or landmark.
- Fill a travel or local guide with place descriptions after a place search.
- Give an LLM background text about a business before it answers a question about that place.
- Show a description next to POI details such as address or opening hours.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/brave/local-descriptions" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"ids": ["loc4DFZ5OEXSZVDUAEEDV6PMTFK6YDFANIHQIRRVKLA="]}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `ids` | array | Yes | A list of unique identifiers for the location. The ids are valid only for 8 hours. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "results": [
    {
      "description": "**Storyville Coffee Pike Place** is a renowned specialty coffee roaster and café…",
      "id": "loc4DFZ5OEXSZVDUAEEDV6PMTFK6YDFANIHQIRRVKLA=",
      "type": "local_description"
    }
  ],
  "type": "local_descriptions"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `results` | List of description objects. It holds one entry for each ID you sent. |
| `results[].id` | The location ID this description belongs to. Use it to match each description to the ID in your request. |
| `results[].description` | Text description of the place. It can contain Markdown, such as `**bold**` around the place name. |
| `results[].type` | Type of the item. In this response it is `local_description`. |
| `type` | Type of the whole response. In this response it is `local_descriptions`. |

### Notes

- Get the location IDs from [Brave Place Search](/apis/brave/local-place-search) or [Brave Local POIs](/apis/brave/local-pois).
- The IDs are valid for only 8 hours, so request fresh IDs if a call fails with an old one.
- Location IDs look like `loc4DFZ5OEXSZVDUAEEDV6PMTFK6YDFANIHQIRRVKLA=`.
- Send several IDs in one `ids` array to get several descriptions in one call.

### Pricing

$0.005 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/brave/local-descriptions.json`](../../../catalog/models/brave/local-descriptions.json) · Store page: https://www.sandbase.ai/model/brave/local-descriptions
