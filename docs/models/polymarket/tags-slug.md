# Polymarket Get tag by slug API: pricing, parameters and code examples

`polymarket/tags-slug` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00044 per call (free daily quota) · **Modes:** sync

Get tag by slug from Polymarket. Returns the official Polymarket API response unchanged.

## Pricing

- **$0.00044 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/tags-slug", "slug": "product-marekt-fit"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/tags-slug', {'slug': 'product-marekt-fit'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/tags-slug", {
  "slug": "product-marekt-fit"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/tags-slug", sandbase.Params{
	"slug": "product-marekt-fit",
})
```

Same call via the path form: `POST /v1/api/polymarket/tags-slug` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `slug` | string | yes | slug  |
| `include_template` | boolean |  | include_template  |

## Details

Returns one Polymarket tag record for a given tag `slug`. The record holds the tag `id`, its display `label`, and creation and update timestamps.

### Use cases

- Convert a known tag `slug` into its numeric `id` for other Polymarket calls that filter by tag.
- Check whether a tag exists on Polymarket before you build a link or filter around it.
- Show the display `label` for a tag in your own app when you only store the `slug`.
- Track when a tag was created or last changed using `createdAt` and `updatedAt`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/tags-slug" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"slug": "product-marekt-fit"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `slug` | string | Yes | slug |
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
| `id` | Identifier of the tag, returned as a string. Use it in APIs that take a tag id. |
| `label` | Human-readable name of the tag. |
| `slug` | URL-style name of the tag. It matches the `slug` you sent in the request. |
| `createdAt / updatedAt` | ISO 8601 UTC timestamps for when the tag was created and when it was last updated. |

### Notes

- The `slug` is required. The example request uses `product-marekt-fit`.
- The `include_template` parameter is optional and has no description in the schema. The example request leaves it out, and the response shows no template fields.
- To look up a tag by its id instead, call [Polymarket Get tag by id](/apis/polymarket/tags-by-id). To browse tags, call [Polymarket List tags](/apis/polymarket/tags).
- To find tags linked to this one, pass the `id` to [Polymarket Get related tags (relationships) by tag id](/apis/polymarket/tags-related-tags).

### Pricing

$0.00044 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/tags-slug.json`](../../../catalog/models/polymarket/tags-slug.json) · Store page: https://www.sandbase.ai/model/polymarket/tags-slug
