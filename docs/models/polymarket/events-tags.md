# Polymarket Get event tags API: pricing, parameters and code examples

`polymarket/events-tags` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00044 per call (free daily quota) · **Modes:** sync

Get event tags from Polymarket. Returns the official Polymarket API response unchanged.

## Pricing

- **$0.00044 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/events-tags", "id": 2890}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/events-tags', {'id': 2890})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/events-tags", {
  "id": 2890
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/events-tags", sandbase.Params{
	"id": 2890,
})
```

Same call via the path form: `POST /v1/api/polymarket/events-tags` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | integer | yes | id  |

## Details

Returns the list of tags attached to one Polymarket event. You send the numeric event `id` and get back an array of tag objects with an `id`, `label`, `slug` and update time.

### Use cases

- Show category labels next to an event in a market dashboard.
- Group events by tag `slug` to build topic filters.
- Check whether an event carries a given tag before you list other events under it.
- Sync Polymarket tag labels and ids into your own database.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/events-tags" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"id": 2890}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | integer | Yes | id |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
[
  {
    "forceShow": false,
    "id": "100215",
    "label": "All",
    "slug": "all",
    "updatedAt": "2026-04-17T20:23:54.340488Z"
  }
]
```

### Response fields

| Field | Meaning |
|---|---|
| `[].id` | Tag id as a string. Pass it to the tag lookup APIs to get more detail. |
| `[].label` | Display name of the tag, such as `All`. |
| `[].slug` | URL-friendly name of the tag. Use it to look up the tag by slug. |
| `[].forceShow` | Boolean flag on the tag. In this response it is `false`. |
| `[].updatedAt` | UTC timestamp in ISO 8601 format for the last update to the tag. |

### Notes

- The `id` parameter is the event id. Get event ids from [Polymarket List events](/apis/polymarket/events) or [Polymarket Get event by slug](/apis/polymarket/events-slug).
- Tag `id` values are strings, while the request `id` is an integer.
- Use [Polymarket Get tag by id](/apis/polymarket/tags-by-id) to fetch full details for a tag returned here.

### Pricing

$0.00044 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/events-tags.json`](../../../catalog/models/polymarket/events-tags.json) · Store page: https://www.sandbase.ai/model/polymarket/events-tags
