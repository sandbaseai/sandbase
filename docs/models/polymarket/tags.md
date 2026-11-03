# Polymarket List tags API: pricing, parameters and code examples

`polymarket/tags` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00044 per call (free daily quota) · **Modes:** sync

List tags from Polymarket. Returns the official Polymarket API response unchanged.

## Pricing

- **$0.00044 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/tags"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/tags', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/tags", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/tags", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/polymarket/tags` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | limit range 0– |
| `order` | string |  | Comma-separated list of fields to order by  |
| `offset` | integer |  | offset range 0– |
| `ascending` | boolean |  | ascending  |
| `is_carousel` | boolean |  | is_carousel  |
| `include_template` | boolean |  | include_template  |

## Details

Returns a list of Polymarket tags. Each tag has an `id`, a `label`, a `slug` and creation and update timestamps. All inputs are optional, so you can call it with no body or use `limit` and `offset` to page through tags.

### Use cases

- Build a full list of Polymarket tag labels and slugs to use as category filters in your own app.
- Sync tag `id` values into a database so you can map events and markets to their tags.
- Find recently updated tags by sorting on `updatedAt` and checking which categories changed.
- Page through all tags with `limit` and `offset` to audit the tag catalog.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/tags" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": 1}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `ascending` | boolean | No | ascending |
| `include_template` | boolean | No | include_template |
| `is_carousel` | boolean | No | is_carousel |
| `limit` | integer | No | limit |
| `offset` | integer | No | offset |
| `order` | string | No | Comma-separated list of fields to order by |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
[
  {
    "createdAt": "2025-02-18T16:58:25.464578Z",
    "id": "101867",
    "label": "product marekt fit",
    "slug": "product-marekt-fit",
    "updatedAt": "2026-04-17T17:23:11.67487Z"
  }
]
```

### Response fields

| Field | Meaning |
|---|---|
| `[].id` | Tag ID as a string. Pass it to the tag-by-id and related-tags APIs. |
| `[].label` | Display name of the tag, as people see it on Polymarket. |
| `[].slug` | URL-style name of the tag. Use it to look up a tag by slug. |
| `[].createdAt` | ISO 8601 UTC timestamp for when the tag was created. |
| `[].updatedAt` | ISO 8601 UTC timestamp for the last change to the tag. |

### Notes

- The response is a plain JSON array, so there is no wrapper object. Use `limit` and `offset` to page through it.
- The `order` parameter takes a comma-separated list of fields, and `ascending` sets the sort direction.
- To fetch one tag, call [Polymarket Get tag by id](/apis/polymarket/tags-by-id) with the `id`, or [Polymarket Get tag by slug](/apis/polymarket/tags-slug) with the `slug`.
- To see tags linked to a tag, call [Polymarket Get related tags (relationships) by tag id](/apis/polymarket/tags-related-tags).

### Pricing

$0.00044 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/tags.json`](../../../catalog/models/polymarket/tags.json) · Store page: https://www.sandbase.ai/model/polymarket/tags
