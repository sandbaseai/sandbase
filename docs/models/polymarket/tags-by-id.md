# Polymarket Get tag by id API: pricing, parameters and code examples

`polymarket/tags-by-id` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00044 per call (free daily quota) · **Modes:** sync

Get tag by id from Polymarket. Returns the official Polymarket API response unchanged.

## Pricing

- **$0.00044 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/tags-by-id", "id": 101867}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/tags-by-id', {'id': 101867})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/tags-by-id", {
  "id": 101867
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/tags-by-id", sandbase.Params{
	"id": 101867,
})
```

Same call via the path form: `POST /v1/api/polymarket/tags-by-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | integer | yes | id  |
| `include_template` | boolean |  | include_template  |

## Details

Returns a single Polymarket tag for a numeric tag `id`. The response gives the tag label, slug, and creation and update timestamps. The request also accepts an optional boolean `include_template`.

### Use cases

- Turn a tag `id` from an event or market into a readable label for display.
- Look up the `slug` of a tag to build a tag page URL or to call a slug-based lookup.
- Check when a tag was created or last changed using `createdAt` and `updatedAt`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/tags-by-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"id": 101867}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | integer | Yes | id |
| `include_template` | boolean | No | include_template |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "$schema": "https://gamma-api.polymarket.com/schemas/Tag.json",
  "createdAt": "2025-02-18T16:58:25.464578Z",
  "id": "101867",
  "label": "product marekt fit",
  "slug": "product-marekt-fit",
  "updatedAt": "2026-04-17T17:23:11.67487Z"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `id` | The tag id as a string. It matches the `id` you sent in the request. |
| `label` | The display name of the tag, returned as stored. |
| `slug` | The URL-friendly name of the tag. Use it with the tag-by-slug lookup. |
| `createdAt` | ISO 8601 timestamp with a `Z` suffix for when the tag was created. |
| `updatedAt` | ISO 8601 timestamp with a `Z` suffix for the last update to the tag. |

### Notes

- Find tag ids by calling [Polymarket List tags](/apis/polymarket/tags) or [Polymarket Get event tags](/apis/polymarket/events-tags).
- The request takes `id` as an integer, but the response returns `id` as a string.
- To look up a tag by its slug instead, use [Polymarket Get tag by slug](/apis/polymarket/tags-slug).

### Pricing

$0.00044 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/tags-by-id.json`](../../../catalog/models/polymarket/tags-by-id.json) · Store page: https://www.sandbase.ai/model/polymarket/tags-by-id
