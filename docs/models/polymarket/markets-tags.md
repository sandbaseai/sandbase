# Polymarket Get market tags by id API: pricing, parameters and code examples

`polymarket/markets-tags` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00044 per call (free daily quota) · **Modes:** sync

Get market tags by id from Polymarket. Returns the official Polymarket API response unchanged.

## Pricing

- **$0.00044 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/markets-tags", "id": 559651}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/markets-tags', {'id': 559651})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/markets-tags", {
  "id": 559651
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/markets-tags", sandbase.Params{
	"id": 559651,
})
```

Same call via the path form: `POST /v1/api/polymarket/markets-tags` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | integer | yes | id  |

## Details

Returns the list of tags attached to one Polymarket market. Each tag has an `id`, a `label`, a `slug` and timestamps. The only input is the numeric market `id`.

### Use cases

- Show topic badges such as Geopolitics next to a market in a dashboard.
- Group markets by tag `slug` to build category pages.
- Collect tag `id` values for a market, then look up all other markets or events under the same tag.
- Check which tags have `forceShow` set to true before choosing which labels to display.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/markets-tags" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"id": 559651}'
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
    "createdAt": "2026-02-10T00:17:21.422175Z",
    "forceShow": false,
    "id": "103715",
    "isCarousel": false,
    "label": "HFC",
    "slug": "hfc",
    "updatedAt": "2026-04-17T20:55:08.357992Z"
  }
]
```

### Response fields

| Field | Meaning |
|---|---|
| `id` | Tag ID as a string. Use it to look up the tag in other tag APIs. |
| `label` | Display name of the tag, for example `Geopolitics`. |
| `slug` | URL-style name of the tag, for example `world-affairs`. |
| `createdAt / updatedAt` | ISO 8601 UTC timestamps for when the tag was created and last changed. |
| `publishedAt` | Time the tag was published. Only some tags include it, and its format differs from `createdAt`. |
| `forceShow` | Boolean flag on the tag. When `true`, the tag is marked to be shown. Not present on every tag. |
| `isCarousel` | Boolean flag on the tag. Not present on every tag. |

### Notes

- The response is a JSON array with one object per tag. Optional fields such as `forceShow`, `isCarousel` and `publishedAt` appear only on some tags.
- Get the market `id` from [Polymarket List markets](/apis/polymarket/markets) or [Polymarket Get market by slug](/apis/polymarket/markets-slug).
- Call [Polymarket Get tag by id](/apis/polymarket/tags-by-id) with a tag `id` to get details for a single tag.

### Pricing

$0.00044 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/markets-tags.json`](../../../catalog/models/polymarket/markets-tags.json) · Store page: https://www.sandbase.ai/model/polymarket/markets-tags
